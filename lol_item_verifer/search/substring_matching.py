"""Matches search terms by if it contains a substring of the item names

"""

from util import load_data


def match_substring():
    data_set = load_data()
    print(data_set.keys())


if __name__ == "__main__":
    match_substring()