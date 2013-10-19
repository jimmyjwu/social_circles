"""
constants.py contains constant values used throughout the 'friends' app.
"""

# Graph API Options
DEVELOPER_ACCESS_TOKEN = 'CAACEdEose0cBALixChwGYtX8V0IKG0sZCYCgzBZA5I8fve3eWyvR2p1CcgrXtqt0AcngjBHaZCpac1Wpv4fsii9r4JUZAIIl1r2MQBVlM6pcAMFnW5JwSy2XYqi7ZBg1wB4Hxd7SZBWQvJJ7LwEALRyMMmenOzytrGfqfeu8ZBQQ18sRZAb7aZCuHrtTDSHVNZBbgZD'

# FQL Queries
USER_ID_AND_NAME_QUERY = 'SELECT uid, name FROM user WHERE uid=me()'
FRIENDS_ID_AND_NAME_QUERY = 'SELECT uid, name FROM user WHERE uid IN (SELECT uid2 FROM friend WHERE uid1 = me())'

FRIENDSHIPS_BETWEEN_FRIENDS_AND_PEOPLE_QUERY = lambda friend_IDs: 'SELECT uid1, uid2 FROM friend WHERE uid1 IN (' + ','.join(friend_IDs) + ') AND uid2 in (SELECT uid2 FROM friend WHERE uid1=me())'
NUMBER_OF_FRIENDS_PER_FRIENDSHIP_REQUEST = 60