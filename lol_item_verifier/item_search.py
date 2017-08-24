import argparse

from data import load_data
from search import substring_matching

def take_input():
    """Take the input from the cmdline"""
    parser = argparse.ArgumentParser(description="Searches through items")

    parser.add_argument('search_term')

    args = parser.parse_args()

    # Verify the args are ok

    # Make sure search term is not empty

    return args


def run():
    """The main function that takes args from the command line

    """
    args = take_input()

    data_set = load_data()

    matches = substring_matching.match(data_set, args.search_term)
    print(matches)


if __name__ == "__main__":
    run()




