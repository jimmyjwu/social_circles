"""
constants.py contains constant values used throughout the 'friends' app.
"""

# Graph API Options
REQUEST_TIMEOUT_IN_SECONDS = 15
DEVELOPER_ACCESS_TOKEN = 'CAACEdEose0cBAC0ZBZBHVXgGskvCbDkV0xxlViOZCZBGoc0pTpmZBbRUPvhuBvpva7vF1JpIwF7U7rycEotXQqRkLBQR6DLmwILfQZATQI11LYZCm6Eeol7srhR9c1lZCd0Tq0BUObzTlBxQDx2IktM0CaVIKXRHZCyZBw3St21Y5e5VxCuZAImd8SVIawwsJa06TUZD'

# FQL Queries
FRIENDS_ID_AND_NAME_QUERY = 'SELECT uid, name FROM user WHERE uid IN (SELECT uid2 FROM friend WHERE uid1 = me())'
FRIENDSHIPS_BETWEEN_FRIENDS_QUERY = 'SELECT uid1, uid2 FROM friend WHERE uid1 IN (SELECT uid2 FROM friend WHERE uid1=me()) AND uid2 IN (SELECT uid2 FROM friend WHERE uid1=me())'

FRIENDSHIPS_BETWEEN_FRIENDS_AND_PEOPLE_QUERY = lambda friend_IDs: 'SELECT uid1, uid2 FROM friend WHERE uid1 IN (' + ','.join(friend_IDs) + ') AND uid2 in (SELECT uid2 FROM friend WHERE uid1=me())'
NUMBER_OF_FRIENDS_PER_FRIENDSHIP_REQUEST = 60