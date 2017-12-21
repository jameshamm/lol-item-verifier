"""config.py contains all the configuration data necessary for other script to work.

This should probably be in a different format so that it can be updated programmatically.
"""

# Data sets and where to find them
LATEST_VERSION = "7_17_1"

LOCAL_DATA_SET_DIRECTORY = "data_set"

## data set urls
KNOWN_VERSIONS_URL = "https://ddragon.leagueoflegends.com/api/versions.json"

## For now the region is uninteresting, and is left as en_US.
## See LATEST_ITEM_DATA_SET_URL for an example of filling in the version.
ITEM_DATA_SET_URL = "http://ddragon.leagueoflegends.com/cdn/{}/data/en_US/item.json"
LATEST_ITEM_DATA_SET_URL = ITEM_DATA_SET_URL.format(LATEST_VERSION)
