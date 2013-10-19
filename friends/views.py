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
	me = facebook_graph.get('me')
	friends = facebook_graph.fql(FRIENDS_ID_AND_NAME_QUERY)['data']
	friend_IDs = [str(friend['uid']) for friend in friends]
	end = time.time()
	print_execution_time('Getting user and friends', start, end)

	"""
	# Query, in chunks, for friendships among friends
	# TO-DO: use FQL multi-query (switch to facepy library)
	start = time.time()
	friends_partition = chunks(friend_IDs, NUMBER_OF_FRIENDS_PER_FRIENDSHIP_REQUEST)
	friendships_between_friends = []
	for friends_sublist in friends_partition:
		friendships_in_sublist = facebook_graph.fql(FRIENDSHIPS_BETWEEN_FRIENDS_AND_PEOPLE_QUERY(friends_sublist))['data']
		friendships_between_friends += friendships_in_sublist
		print('Current friends sublist has ' + str(len(friendships_in_sublist)) + ' total mutual friends.')
	end = time.time()
	print_execution_time('Getting friendships between friends', start, end)
	"""

	# Use FQL multi-query to get friendships among friends
	start = time.time()

	friends_sublists = chunks(friend_IDs, NUMBER_OF_FRIENDS_PER_FRIENDSHIP_REQUEST)
	friendships_multiquery = {}
	for sublist_index in range(len(friends_sublists)):
		friendships_multiquery['query_' + str(sublist_index)] = FRIENDSHIPS_BETWEEN_FRIENDS_AND_PEOPLE_QUERY(friends_sublists[sublist_index])
	friendship_multiquery_results = facebook_graph.fql(friendships_multiquery)['data']

	friendships_between_friends = [friendship for query_results in friendship_multiquery_results for friendship in query_results['fql_result_set']]

	end = time.time()
	print_execution_time('Getting friendships between friends using FQL multiquery', start, end)

	# Construct graph of local region
	start = time.time()
	friends_graph = networkx.Graph()
	for friend_ID in friend_IDs:
		friends_graph.add_edge(me['id'], friend_ID)
	for friendship in friendships_between_friends:
		friends_graph.add_edge(friendship['uid1'], friendship['uid2'])
	end = time.time()
	print_execution_time('Constructing graph of local region', start, end)

	# Print data types returned by Facebook
	print_object_type("me['id']", me['id'])
	print_object_type("friendships_between_friends[0]['uid1']", friendships_between_friends[0]['uid1'])
	print_object_type("friendships_between_friends[0]['uid2']", friendships_between_friends[0]['uid2'])

	# Test if edges are unique: if (u,v) exists, (v,u) doesn't
	edges = friends_graph.edges()
	edge_set = set(edges)
	number_of_duplicate_edges = 0
	for u, v in edges:
		if (v, u) in edge_set:
			number_of_duplicate_edges += 1
	print(str(number_of_duplicate_edges) + ' DUPLICATE EDGES DETECTED.' if number_of_duplicate_edges > 0 else 'NO DUPLICATE EDGES DETECTED.')

	# Render page with friend information
	return render(request, 'friends/index.html', {'friends': friends, 'number_of_friendships': len(friends_graph.edges())})








