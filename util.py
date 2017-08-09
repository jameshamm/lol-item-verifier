import json

from enum import Enum

DEFAULT_PATH = "items-7_16_1-en_US_pretty.json"

TEST_STATUS = Enum('Test_Status', 'ready in_development unused')

TESTS = dict()
# Contains all the tests indexed by their current status.
# Useful for running all tests of a particular status


def set_status(status, tests=None):
    """Decorator to add the readiness to the function
    If a dict is passed, store the function"""
    if tests is None:
        tests = TESTS

    def decorator(func):
        func.status = status
        if status not in tests:
            tests[status] = list()
        tests[status].append(func)
        return func
    return decorator


def run_tests(*statuses):
    """Run the tests that are marked with any of the passed statuses"""
    data_set = load_items()

    if not statuses:
        # Default to running tests marked as ready
        statuses = [TEST_STATUS.ready]

    for status in statuses:
        if status in TESTS:
            for test in TESTS[status]:
                result, log = test(data_set)
                message = test.__name__ + ": " + ("PASSED" if result else "FAILED")
                if log:
                    message += " - " + log
                print(message)


def load_items(filepath=DEFAULT_PATH):
    """Load the items from a json file into a dict"""
    with open(filepath) as file:
        return json.load(file)
