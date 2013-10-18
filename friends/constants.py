"""
constants.py contains constant values used throughout the 'friends' app.
"""

# Graph API Options
REQUEST_TIMEOUT_IN_SECONDS = 15
DEVELOPER_ACCESS_TOKEN = 'CAACEdEose0cBAJAnIUlLH6kX01j0qdlcZCOSLDT3qRlsUBDzxq5bt5gVsR9ZAgxHaZBxBA8gCCYM50gMNKVGe7OsseKeax8lZBQv3jxCyXSNcft5Fb7OgvtJ7ZA9YLzLCUuElnjKhg4qQxZADc2RinnIivJpaQiqBt5ZCkGlnaU0KqBT6jp0vOLlWREYcRkrJkZD'

# FQL Queries
FRIENDS_ID_AND_NAME_QUERY = 'SELECT uid, name FROM user WHERE uid IN (SELECT uid2 FROM friend WHERE uid1 = me())'
FRIENDSHIPS_BETWEEN_FRIENDS_QUERY = 'SELECT uid1, uid2 FROM friend WHERE uid1 IN (SELECT uid2 FROM friend WHERE uid1=me()) AND uid2 IN (SELECT uid2 FROM friend WHERE uid1=me())'