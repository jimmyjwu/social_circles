"""
constants.py contains constant values used throughout the 'friends' app.
"""

# Graph API Options
REQUEST_TIMEOUT_IN_SECONDS = 15
DEVELOPER_ACCESS_TOKEN = 'CAACEdEose0cBABHqoiBAUZBSZBwnP1UqYbWhbmmbndyAir8IH4N1pG1FeGATiI5cJOprR0EFQkZCpidpSpFQg14e0VvUkoiX5tGT6TGbLsG2mNg1eplfdktXDEX4tJPpHKzjsvBskKGeZB9EVTlhgZA1vp8TO62rhSHQJ7XSjC3infHzP9LZCB95ib4lsGng0ZD'

# FQL Queries
FRIENDS_ID_AND_NAME_QUERY = 'SELECT uid, name FROM user WHERE uid IN (SELECT uid2 FROM friend WHERE uid1 = me())'
FRIENDSHIPS_BETWEEN_FRIENDS_QUERY = 'SELECT uid1, uid2 FROM friend WHERE uid1 IN (SELECT uid2 FROM friend WHERE uid1=me()) AND uid2 IN (SELECT uid2 FROM friend WHERE uid1=me())'

FRIENDSHIPS_BETWEEN_FRIENDS_AND_PEOPLE_QUERY = lambda people: 'SELECT uid1, uid2 FROM friend WHERE uid1 IN (' + ','.join(people) + ') AND uid2 in (SELECT uid2 FROM friend WHERE uid1=me())'
NUMBER_OF_FRIENDS_PER_FRIENDSHIP_REQUEST = 60