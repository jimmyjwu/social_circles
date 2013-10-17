# Django modules
from django.shortcuts import render

# Python and system-wide modules
import time
import facebook

# Local modules
from utilities import *
from constants import *


access_token = DEVELOPER_ACCESS_TOKEN


def index(request):
	graph = facebook.GraphAPI(access_token=access_token, timeout=REQUEST_TIMEOUT_IN_SECONDS)
	profile = graph.get_object('me')

	start_time = time.time()
	friends = graph.fql(FRIENDS_ID_AND_NAME_QUERY)
	end_time = time.time()
	print_execution_time('FQL query for friends', start_time, end_time)

	start_time = time.time()
	friendships_between_friends = graph.fql(FRIENDSHIPS_BETWEEN_FRIENDS_QUERY)
	end_time = time.time()
	print_execution_time('FQL query for friendships between friends', start_time, end_time)

	# Render page with friend information
	return render(request, 'friends/index.html', {'friends': friends, 'number_of_connections_between_friends': len(friendships_between_friends)})








