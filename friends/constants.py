"""
constants.py contains constant values used throughout the 'friends' app.
"""

# Graph API Options
REQUEST_TIMEOUT_IN_SECONDS = 15
DEVELOPER_ACCESS_TOKEN = 'CAACEdEose0cBAPDHaZBLSXSTo9fOlesNV8CZCAUq3NOThTiYO7t2p8GzVlmIwZBfEOFdSqZChRltGMU51W9ry6zqfZBYZChJ0ZCvKITUPxZAIb4QSbmMGxsWg1HSXYwZCZBQGRrPn9lsRZBJlgX8nqEacKmjZBiOf95UyVx4pXVXXWQahzV8PLLjPdC8M1F2rcDjhIYZD'

# FQL Queries
FRIENDS_ID_AND_NAME_QUERY = 'SELECT uid, name FROM user WHERE uid IN (SELECT uid2 FROM friend WHERE uid1 = me())'
FRIENDSHIPS_BETWEEN_FRIENDS_QUERY = 'SELECT uid1, uid2 FROM friend WHERE uid1 IN (SELECT uid2 FROM friend WHERE uid1=me()) AND uid2 IN (SELECT uid2 FROM friend WHERE uid1=me())'