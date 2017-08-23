from enum import Enum
from util import load_data


TEST_STATUS = Enum('Test_Status', 'ready in_development unused')

TESTS = dict()
# Contains all the tests indexed by their current status.
# Useful for running all tests of a particular status


def run_dev_tests():
    """Run the currently known developing tests from the imports below"""
    from . import test_item_paths
    from . import test_item_sanity

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
    """Run the tests that are marked with any of the passed statuses"""
    data_set = load_data()

    if not statuses:
        # Default to running tests marked as ready
        statuses = [TEST_STATUS.ready]

    for status in statuses:
        if status in TESTS:
            for test in TESTS[status]:
                # Expect either a pass, or a fail along with a description of what went wrong and the offending items
                success, *log = test(data_set)
                message = test.__name__ + ": " + ("PASSED" if success else "FAILED")
                if not success:
                    error_log, bad_items = log
                    message += " - " + error_log + ": " + str(bad_items)
                print(message)
