"""
constants.py contains constant values used throughout the 'friends' app.
"""

# Graph API Options
REQUEST_TIMEOUT_IN_SECONDS = 15
DEVELOPER_ACCESS_TOKEN = 'CAACEdEose0cBAMBlwqbUQl1DU8LwwDcuA5qEzoSVS8gbPZCP5c4aoOkjj1x5NEfSNkdiHvWtKumvtb1EbZC89BjHA6pliE6xLLCjPj9HC2wsRAihzhoUi534bOtekzrsmdIPXMzW6GwtOdGHRc3qRqk0NFp00mmnXmjIVEHZBMYLozEU5ZCZAH2OCHmLpVugZD'

# FQL Queries
FRIENDS_ID_AND_NAME_QUERY = 'SELECT uid, name FROM user WHERE uid IN (SELECT uid2 FROM friend WHERE uid1 = me())'
FRIENDSHIPS_BETWEEN_FRIENDS_QUERY = 'SELECT uid1, uid2 FROM friend WHERE uid1 IN (SELECT uid2 FROM friend WHERE uid1=me()) AND uid2 IN (SELECT uid2 FROM friend WHERE uid1=me())'