# Django modules
from django.shortcuts import render

# Python and system-wide modules
import time
import facebook
import networkx
import networkx.algorithms as algorithms
import networkx.algorithms.approximation as approximation

# Local modules
from utilities import *
from constants import *


access_token = DEVELOPER_ACCESS_TOKEN


def index(request):
	# Create Facebook Graph API object
	facebook_graph = facebook.GraphAPI(access_token=access_token, timeout=REQUEST_TIMEOUT_IN_SECONDS)

	# Query for user and friends
	me = facebook_graph.get_object('me')
	friends = facebook_graph.fql(FRIENDS_ID_AND_NAME_QUERY)
	friend_IDs = [unicode(friend['uid']) for friend in friends]

	# Query, in chunks, for friendships among friends
	# TO-DO: determine experimentally what chunk size to use
	# (find one such that the number of friendships (u,v) returned is safely fewer than 5,000)
	# TO-DO: use FQL multi-query (switch to facepy library)
	start = time.time()
	friends_partition = chunks(friend_IDs, NUMBER_OF_FRIENDS_PER_FRIENDSHIP_REQUEST)
	friendships_between_friends = []
	for friends_sublist in friends_partition:
		friendships_in_sublist = facebook_graph.fql(FRIENDSHIPS_BETWEEN_FRIENDS_AND_PEOPLE_QUERY(friends_sublist))
		friendships_between_friends += friendships_in_sublist
	end = time.time()
	print_execution_time('Getting friendships between friends', start, end)

	# Construct graph of local region
	friends_graph = networkx.Graph()
	for friend_ID in friend_IDs:
		friends_graph.add_edge(me['id'], friend_ID)
	for friendship in friendships_between_friends:
		friends_graph.add_edge(friendship['uid1'], friendship['uid2'])

	"""
	# DEBUG
	print "me['id'] is a " + str(type(me['id']))
	print "friendship['uid1'] is a " + str(type(friendships_between_friends[0]['uid1']))
	print "friendship['uid2'] is a " + str(type(friendships_between_friends[0]['uid2']))
	"""

	"""
	# DEBUG
	# Result: found that 10,197 edges are indeed unique; if (u,v) exists, (v,u) doesn't.
	edges = friends_graph.edges()
	edge_set = set(edges)
	for u, v in edges:
		if (v, u) in edge_set:
			print('DUPLICATE DETECTED')
	print(edge_set)
	"""


	# Render page with friend information
	return render(request, 'friends/index.html', {'friends': friends, 'number_of_friendships': len(friends_graph.edges())})








