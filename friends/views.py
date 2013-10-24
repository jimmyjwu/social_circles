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


access_token = DEVELOPER_ACCESS_TOKEN


def index(request):
	# Create Facebook Graph API object
	facebook_graph = facepy.GraphAPI(oauth_token=access_token)

	# Query for user and friends
	start = time.time()
	user_and_friends_multiquery = {
		'user': USER_ID_AND_NAME_QUERY,
		'friends': FRIENDS_ID_AND_NAME_QUERY,
	}
	user_and_friends_multiquery_results = facebook_graph.fql(user_and_friends_multiquery)
	user_and_friends_results_dictionary = parse_multiquery_results(user_and_friends_multiquery_results)
	user = [{'uid': unicode(user['uid']), 'name': user['name']} for user in user_and_friends_results_dictionary['user']][0]
	friends = [{'uid': unicode(friend['uid']), 'name': friend['name']} for friend in user_and_friends_results_dictionary['friends']]
	end = time.time()
	print_execution_time('getting user and friends', start, end)

	# User FQL to calculate graph density
	start = time.time()
	mutual_friend_counts_results = facebook_graph.fql(MUTUAL_FRIEND_COUNTS_QUERY)['data']
	mutual_friend_counts = [result['mutual_friend_count'] for result in mutual_friend_counts_results]
	friendships_count = sum(mutual_friend_counts) / 2
	print_graph_density(len(friends), friendships_count)
	end = time.time()
	print_execution_time('calculating graph density', start, end)

	# Use FQL multi-query to get friendships among friends
	start = time.time()
	friend_UID_strings = [str(friend['uid']) for friend in friends]	# Friend UIDs must be strings (not unicode) to use in FQL multiqueries
	friend_chunks = shuffled_chunks(friend_UID_strings, FRIEND_COUNT_PER_FRIENDSHIP_QUERY(len(friends)))
	print_friend_chunks_information(friend_chunks)
	friendships_multiquery = {'friendships_' + str(sublist_index): FRIENDSHIPS_BETWEEN_FRIENDS_AND_PEOPLE_QUERY(friend_chunks[sublist_index]) for sublist_index in range(len(friend_chunks))}
	friendships_multiquery_results = facebook_graph.fql(friendships_multiquery)
	friendships_between_friends = parse_and_combine_multiquery_results(friendships_multiquery_results)
	end = time.time()
	print_execution_time('getting local friendships', start, end)

	# Construct graph of local region
	start = time.time()
	friends_graph = networkx.Graph()
	[friends_graph.add_edge(user['uid'], friend['uid']) for friend in friends]
	[friends_graph.add_edge(friendship['uid1'], friendship['uid2']) for friendship in friendships_between_friends]
	end = time.time()
	print_execution_time('building local graph', start, end)

	# Render page with friend information
	return render(request, 'friends/index.html', {'friends': friends, 'number_of_friendships': len(friends_graph.edges())})








