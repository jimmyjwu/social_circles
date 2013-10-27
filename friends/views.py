# Django modules
from django.shortcuts import render

# Python and system-wide modules
import time
import facepy
import networkx
import networkx.algorithms as algorithms
import networkx.algorithms.approximation as approximation

# Local modules
from utilities import *
from constants import *
import community


access_token = DEVELOPER_ACCESS_TOKEN


def index(request):
	view_start = time.time()

	# Create Facebook Graph API object
	facebook_graph = facepy.GraphAPI(oauth_token=access_token)

	# Get user and friends
	start = time.time()
	user_and_friends_multiquery = {
		'user': USER_QUERY,
		'friends': FRIENDS_QUERY,
	}
	user_and_friends_multiquery_results = facebook_graph.fql(user_and_friends_multiquery)
	user_and_friends_results_dictionary = parse_multiquery_results(user_and_friends_multiquery_results)
	user = [{'uid': unicode(user['uid']), 'name': user['name']} for user in user_and_friends_results_dictionary['user']][0]
	friends = [{'uid': unicode(friend['uid']), 'name': friend['name'], 'mutual_friend_count': friend['mutual_friend_count']} for friend in user_and_friends_results_dictionary['friends']]
	end = time.time()
	print_execution_time('getting user, friends, and mutual friend counts', start, end)

	# Calculate graph density from mutual friend counts
	friendships_count = sum([friend['mutual_friend_count'] for friend in friends]) / 2
	print_graph_density(len(friends), friendships_count)

	# Use FQL multiquery to get friendships among friends
	start = time.time()
	friend_UID_strings = [str(friend['uid']) for friend in friends]	# Friend UIDs must be strings (not unicode) to use in FQL multiqueries
	friend_chunks = random_chunks(friend_UID_strings, FRIEND_COUNT_PER_FRIENDSHIP_QUERY(len(friends), graph_density(len(friends), friendships_count)))
	print_friend_chunks_information(friend_chunks)
	friendships_multiquery = {'friendships_' + str(sublist_index): FRIENDSHIPS_BETWEEN_FRIENDS_AND_PEOPLE_QUERY(friend_chunks[sublist_index]) for sublist_index in range(len(friend_chunks))}
	friendships_multiquery_results = facebook_graph.fql(friendships_multiquery)
	friendships = parse_and_combine_multiquery_results(friendships_multiquery_results)
	end = time.time()
	print_execution_time('getting local friendships', start, end)

	# Build graph of local region
	start = time.time()
	friends_graph = networkx.Graph()
	[friends_graph.add_node(friend['uid'], name=friend['name']) for friend in friends]
	[friends_graph.add_edge(friendship['uid1'], friendship['uid2']) for friendship in friendships]
	end = time.time()
	print_execution_time('building local graph', start, end)

	# Find clusters of friends
	start = time.time()

	# Assign each friend to a cluster in the partition
	friends_partition = community.best_partition(friends_graph)

	# Convert partition assignments into a list of clusters (lists) of people
	friends_by_cluster = {cluster_number: [] for cluster_number in friends_partition.values()}
	[friends_by_cluster[cluster_number].append(friend_ID) for friend_ID, cluster_number in friends_partition.iteritems()]
	clusters = friends_by_cluster.values()

	# Convert friends' IDs into names
	named_clusters = [ [friends_graph.node[friend_ID]['name'] for friend_ID in cluster] for cluster in clusters ]

	end = time.time()
	print_execution_time('finding clusters', start, end)

	view_end = time.time()
	print_execution_time('rendering complete index view', view_start, view_end)

	# Render page with friend information
	return render(request, 'friends/index.html', {'friends': friends, 'clusters': named_clusters})








