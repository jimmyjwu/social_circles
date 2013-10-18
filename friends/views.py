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

	# Query for local region (friends and friendships among them)
	me = facebook_graph.get_object('me')
	friends = facebook_graph.fql(FRIENDS_ID_AND_NAME_QUERY)
	friendships_between_friends = facebook_graph.fql(FRIENDSHIPS_BETWEEN_FRIENDS_QUERY)

	# Construct graph of local region
	friends_graph = networkx.Graph()
	for friend in friends:
		friends_graph.add_edge(me['id'], friend['uid'])
	for friendship in friendships_between_friends:
		friends_graph.add_edge(friendship['uid1'], friendship['uid2'])

	print "me['id'] is a " + str(type(me['id']))
	print "friend['uid'] is a " + str(type(friends[0]['uid']))
	print "friendship['uid1'] is a " + str(type(friendships_between_friends[0]['uid1']))
	print "friendship['uid2'] is a " + str(type(friendships_between_friends[0]['uid2']))

	# Render page with friend information
	return render(request, 'friends/index.html', {'friends': friends, 'number_of_friendships': len(friends_graph.edges())})








