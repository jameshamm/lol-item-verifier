"""Provide a method of accessing data from the data sets

This should deal with issues such as relative file paths breaking and
define the most up to date data set to run tests on

"""
import json

from os import path

DNAME = path.dirname(path.abspath(__file__))
DATA_SET_DIRECTORY_ABSPATH = path.join(DNAME, "data_set")

LATEST = "items-7_17_1-en_US_pretty.json"
LATEST_DATA_SET_PATH = path.join(DATA_SET_DIRECTORY_ABSPATH, LATEST)


def load_data(filepath=None):
    """Load the items from a json file into a dict"""
    if filepath is None:
        filepath = LATEST_DATA_SET_PATH

    with open(filepath) as file:
        return json.load(file)


def save_data(data_set, filepath, pretty=False):
    with open(filepath, "w") as file:
        if pretty:
            file.write(json.dumps(data_set, indent=4, sort_keys=True))
        else:
            file.write(json.dumps(data_set, separators=(',', ':'), sort_keys=True))


