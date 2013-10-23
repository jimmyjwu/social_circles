"""
constants.py contains constant values used throughout the 'friends' app.
"""
from access_token import *

# Graph API Options

# FQL Queries
USER_ID_AND_NAME_QUERY = 'SELECT uid, name FROM user WHERE uid=me()'
FRIENDS_ID_AND_NAME_QUERY = 'SELECT uid, name FROM user WHERE uid IN (SELECT uid2 FROM friend WHERE uid1 = me())'

FRIENDSHIPS_BETWEEN_FRIENDS_AND_PEOPLE_QUERY = lambda friend_IDs: 'SELECT uid1, uid2 FROM friend WHERE uid1 IN (' + ','.join(friend_IDs) + ') AND uid2 in (SELECT uid2 FROM friend WHERE uid1=me())'
NUMBER_OF_FRIENDS_PER_FRIENDSHIP_QUERY = 60