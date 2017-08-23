from enum import Enum
from data import load_data


TEST_STATUS = Enum('Test_Status', 'ready in_development unused informative')
"""The test status describes the current 'readiness' of the
function it is decorating

Ready: The test has been tested on multiple data sets and
is a useful reliable test.

In Development: The test is still being written, and is not yet ready.

Unused: The test might contain a useful idea or implementation,
but is not useful as a test right now.

Informative: The test is not intended to be a real test,
it only serves to pull some information from the data set.
"""

TESTS = dict()
# Contains all the tests indexed by their current status.
# Useful for running all tests of a particular status


def run_dev_tests():
    """Run the currently known developing tests from the imports below"""

    # TODO: Iterate over all files in this subdirectory and
    # run any tests marked appropiately
    from . import test_item_paths
    from . import test_item_sanity
    from . import playing_tests

    print("--- Running developing tests ---")
    run_tests(TEST_STATUS.in_development)


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
    """Run the tests that are marked with one of the statuses"""
    data_set = load_data()

    if not statuses:
        # Default to running tests marked as ready
        statuses = [TEST_STATUS.ready]

    for status in statuses:
        if status in TESTS:
            for test in TESTS[status]:
                # Expect either a pass, or a fail
                # A fail comes with a description of what went wrong
                # and the offending items.
                success, *log = test(data_set)
                message = test.__name__ + ": " + ("PASSED" if success else "FAILED")
                if not success:
                    error_log, bad_items = log
                    message += " - " + error_log + ": " + str(bad_items)
                print(message)
