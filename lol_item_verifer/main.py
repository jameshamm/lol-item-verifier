"""
The main file to run all the implemented tests

Run this file with python3 main.py to run all (developing) tests

TODO: Take input on what tests to run and change the data set to use
"""


def run_dev_tests():
    """Run the currently known developing tests from the imports below"""
    import test_item_paths
    import test_item_sanity

    from util import TEST_STATUS, run_tests

    print("--- Running developing tests ---")
    run_tests(TEST_STATUS.in_development)


if __name__ == "__main__":
    run_dev_tests()
