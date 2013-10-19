"""
constants.py contains constant values used throughout the 'friends' app.
"""

# Graph API Options
REQUEST_TIMEOUT_IN_SECONDS = 15
DEVELOPER_ACCESS_TOKEN = 'CAACEdEose0cBAO4FU7f7VBuZA8MslGKyAsu9dtR4CZBRsWZAHa6QOs7msU8H1WMTNkYgKYEndVLCnZAv2ZCCITMZBY8LQ3yk33jZC9u5fmmfswEdzBZAhaRDaXZCJhZBpyaaZCEQpPvV8Brv9aLBpy59D39zhSVVWxffsdb5rrscuRoyLaltWvs1y2Os8QArCfeA3wZD'

# FQL Queries
FRIENDS_ID_AND_NAME_QUERY = 'SELECT uid, name FROM user WHERE uid IN (SELECT uid2 FROM friend WHERE uid1 = me())'
FRIENDSHIPS_BETWEEN_FRIENDS_QUERY = 'SELECT uid1, uid2 FROM friend WHERE uid1 IN (SELECT uid2 FROM friend WHERE uid1=me()) AND uid2 IN (SELECT uid2 FROM friend WHERE uid1=me())'

FRIENDSHIPS_BETWEEN_FRIENDS_AND_PEOPLE_QUERY = lambda friend_IDs: 'SELECT uid1, uid2 FROM friend WHERE uid1 IN (' + ','.join(friend_IDs) + ') AND uid2 in (SELECT uid2 FROM friend WHERE uid1=me())'
NUMBER_OF_FRIENDS_PER_FRIENDSHIP_REQUEST = 60