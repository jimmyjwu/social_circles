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

	# Use FQL multi-query to get friendships among friends
	start = time.time()
	friends_sublists = chunks(friend_IDs, NUMBER_OF_FRIENDS_PER_FRIENDSHIP_REQUEST)
	friendships_multiquery = {'query_' + str(sublist_index): FRIENDSHIPS_BETWEEN_FRIENDS_AND_PEOPLE_QUERY(friends_sublists[sublist_index]) for sublist_index in range(len(friends_sublists))}
	friendship_multiquery_results = facebook_graph.fql(friendships_multiquery)['data']
	friendships_between_friends = [friendship for query_results in friendship_multiquery_results for friendship in query_results['fql_result_set']]
	end = time.time()
	print_execution_time('Getting friendships between friends', start, end)

	# Construct graph of local region
	start = time.time()
	friends_graph = networkx.Graph()
	[friends_graph.add_edge(me['id'], friend_ID) for friend_ID in friend_IDs]
	[friends_graph.add_edge(friendship['uid1'], friendship['uid2']) for friendship in friendships_between_friends]
	end = time.time()
	print_execution_time('Constructing graph of local region', start, end)

	# Render page with friend information
	return render(request, 'friends/index.html', {'friends': friends, 'number_of_friendships': len(friends_graph.edges())})








