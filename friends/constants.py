"""
constants.py contains constant values used throughout the 'friends' app.
"""

# Graph API Options
REQUEST_TIMEOUT_IN_SECONDS = 15
DEVELOPER_ACCESS_TOKEN = 'CAACEdEose0cBAPscLnx3mPS7g9TSO18ho3d5Yjl3WBM1FQyj0dXGcbj69Ok2zQcAhYN4Cv2PqZA0d3PvMvlGlHmzL4oututX6AAzG7gdYJ4G0N7tIQHz3puwVMhw3dvo6jy7mwZBVQC4Oz83lwKEN3f1ZC8RwAsIZBMCMDXwTYWi8FJkIMf4GJmNZC82RfswZD'

# FQL Queries
FRIENDS_ID_AND_NAME_QUERY = 'SELECT uid, name FROM user WHERE uid IN (SELECT uid2 FROM friend WHERE uid1 = me())'
FRIENDSHIPS_BETWEEN_FRIENDS_QUERY = 'SELECT uid1, uid2 FROM friend WHERE uid1 IN (SELECT uid2 FROM friend WHERE uid1=me()) AND uid2 IN (SELECT uid2 FROM friend WHERE uid1=me())'

FRIENDSHIPS_BETWEEN_FRIENDS_AND_PEOPLE_QUERY = lambda people: 'SELECT uid1, uid2 FROM friend WHERE uid1 IN (' + ','.join(people) + ') AND uid2 in (SELECT uid2 FROM friend WHERE uid1=me())'
NUMBER_OF_FRIENDS_PER_FRIENDSHIP_REQUEST = 100