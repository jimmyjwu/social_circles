from django.http import HttpResponse
from django.shortcuts import render
import facebook

def index(request):
	# Temporary access access_token generated by Facebook's Graph API Explorer
	access_token = 'CAACEdEose0cBAM3VoDKu50jgyHErRbMYINuiSa0SZCgbPSgocEKdH5bim1pD1uwP6G1B4WU5B7OPuRlCKGdKjjs4Hd2QCI4M8ZByCZBBVHmfPL9APnlaXcNZAWKaJwjg4ygjYhaWqo5yhrN2ewt2Kygh7fu2ZAB6Va0arL8OOkcuYHHurs077gWQYHpj2tXAZD'

	graph = facebook.GraphAPI(access_token)
	profile = graph.get_object("me")
	friends_data = graph.get_connections("me", "friends")['data']

	# Assemble a list of friend dictionaries with names and IDs
	friends = []
	for friend_data in friends_data:
		friends += [
			{
				'name': friend_data['name'],
				'ID': friend_data['id'],
			}
		]

	# WARNING: The code below runs extremely slowly due to large number of requests over network.
	"""
	# Add, to each friend dictionary, a list of mutual friends with the user
	for friend in friends:
		print(counter)
		friend['mutual_friends'] = graph.get_connections(friend['ID'], "mutualfriends")['data']
	"""

	# Render page with friend information
	return render(request, 'friends/index.html', {'friends': friends})