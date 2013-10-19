"""
constants.py contains constant values used throughout the 'friends' app.
"""

# Graph API Options
DEVELOPER_ACCESS_TOKEN = 'CAACEdEose0cBALNCbK6rfRNW5MRrLM9zrWMqu0FXT5HR7gZAZAcAGlOjhHR6xtpX4W7XOArFEjboVrSZAWs1Dibxt6WdO09SY1JetNF6lzgreggXrGHfLUnWHtoMtGLWXNxYJUyXstOBOxuWk1HiZAZA8GntfkF8mZBq3yOvZCu3JKZCfX5SOTggV3qZCXB9D9M4ZD'

# FQL Queries
USER_ID_AND_NAME_QUERY = 'SELECT uid, name FROM user WHERE uid=me()'
FRIENDS_ID_AND_NAME_QUERY = 'SELECT uid, name FROM user WHERE uid IN (SELECT uid2 FROM friend WHERE uid1 = me())'
FRIENDSHIPS_BETWEEN_FRIENDS_QUERY = 'SELECT uid1, uid2 FROM friend WHERE uid1 IN (SELECT uid2 FROM friend WHERE uid1=me()) AND uid2 IN (SELECT uid2 FROM friend WHERE uid1=me())'

FRIENDSHIPS_BETWEEN_FRIENDS_AND_PEOPLE_QUERY = lambda friend_IDs: 'SELECT uid1, uid2 FROM friend WHERE uid1 IN (' + ','.join(friend_IDs) + ') AND uid2 in (SELECT uid2 FROM friend WHERE uid1=me())'
NUMBER_OF_FRIENDS_PER_FRIENDSHIP_REQUEST = 60