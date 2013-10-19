"""
constants.py contains constant values used throughout the 'friends' app.
"""

# Graph API Options
REQUEST_TIMEOUT_IN_SECONDS = 15
DEVELOPER_ACCESS_TOKEN = 'CAACEdEose0cBAJ9pFZBopdFgCeQP5U49CZB8goad623qbWLO4j0ZBnPjresrpBoIKvkXeJDZA5NZBUySRPXqrvlYTUQBZAai1cYbkZCyEMuq09TRswNvuvlTHVUzcAlt69n55R90EdnpxrA69N8oqEnApMRvMWlejRKjSQEUH6BjH0zSHWFd1zJF1PBzDWHRRAZD'

# FQL Queries
FRIENDS_ID_AND_NAME_QUERY = 'SELECT uid, name FROM user WHERE uid IN (SELECT uid2 FROM friend WHERE uid1 = me())'
FRIENDSHIPS_BETWEEN_FRIENDS_QUERY = 'SELECT uid1, uid2 FROM friend WHERE uid1 IN (SELECT uid2 FROM friend WHERE uid1=me()) AND uid2 IN (SELECT uid2 FROM friend WHERE uid1=me())'

FRIENDSHIPS_BETWEEN_FRIENDS_AND_PEOPLE_QUERY = lambda people: 'SELECT uid1, uid2 FROM friend WHERE uid1 IN (' + ','.join(people) + ') AND uid2 in (SELECT uid2 FROM friend WHERE uid1=me())'
NUMBER_OF_FRIENDS_PER_FRIENDSHIP_REQUEST = 100