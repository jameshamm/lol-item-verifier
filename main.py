def run_dev_tests():
    """Runs the currently known developing tests from the imports below"""
    import test_item_paths
    import test_item_sanity

    from util import TEST_STATUS, run_tests

    print("--- Running developing tests ---")
    run_tests(TEST_STATUS.in_development)


if __name__ == "__main__":
    run_dev_tests()
