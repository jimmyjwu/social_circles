# Django modules
from django.shortcuts import render

# Python and system-wide modules
import time
import facebook
import networkx

# Local modules
from utilities import *
from constants import *


access_token = DEVELOPER_ACCESS_TOKEN


def index(request):
	facebook_graph = facebook.GraphAPI(access_token=access_token, timeout=REQUEST_TIMEOUT_IN_SECONDS)
	profile = facebook_graph.get_object('me')

	friends = facebook_graph.fql(FRIENDS_ID_AND_NAME_QUERY)
	friendships_between_friends = facebook_graph.fql(FRIENDSHIPS_BETWEEN_FRIENDS_QUERY)

	# Render page with friend information
	return render(request, 'friends/index.html', {'friends': friends, 'number_of_connections_between_friends': len(friendships_between_friends)})








