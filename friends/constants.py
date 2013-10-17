"""
constants.py contains constant values used throughout the 'friends' app.
"""

# Graph API Options
REQUEST_TIMEOUT_IN_SECONDS = 15
DEVELOPER_ACCESS_TOKEN = 'CAACEdEose0cBANvKjZASP8qU7j3uUx51gF6a2bZAWZAZC8oJjWuJwF726dhM0eJpeiZBIKR69zuZBF4nSPiDIMGA9qfP7JGARsjNzJz8HmevUrn6ZBRt2aYxhCrMi0z5G6oDC4sdk9Q73tjmb98ZCf8JZCoMdTZCufvg22FhtoCtE72ZAaDCZBs98P8ssghjN1IvoDAZD'

# FQL Queries
FRIENDS_ID_AND_NAME_QUERY = 'SELECT uid, name FROM user WHERE uid IN (SELECT uid2 FROM friend WHERE uid1 = me())'
FRIENDSHIPS_BETWEEN_FRIENDS_QUERY = 'SELECT uid1, uid2 FROM friend WHERE uid1 IN (SELECT uid2 FROM friend WHERE uid1=me()) AND uid2 IN (SELECT uid2 FROM friend WHERE uid1=me())'