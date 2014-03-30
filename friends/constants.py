"""
constants.py contains constant values used throughout the 'friends' app.
"""
from access_token import *

# Constants
MAXIMUM_RESULTS_PER_QUERY = 5000
SAFE_RESULTS_PER_QUERY = 1000

# FQL Queries
USER_QUERY = 'SELECT uid, name FROM user WHERE uid=me()'
FRIENDS_QUERY = 'SELECT uid, name, mutual_friend_count FROM user WHERE uid IN (SELECT uid2 FROM friend WHERE uid1 = me())'

FRIENDSHIPS_BETWEEN_FRIENDS_AND_PEOPLE_QUERY = lambda friend_IDs: 'SELECT uid1, uid2 FROM friend WHERE uid1 IN (' + ','.join(friend_IDs) + ') AND uid2 in (SELECT uid2 FROM friend WHERE uid1=me())'
FRIEND_COUNT_PER_FRIENDSHIP_QUERY = lambda number_of_friends, graph_density: int(SAFE_RESULTS_PER_QUERY / graph_density / number_of_friends)