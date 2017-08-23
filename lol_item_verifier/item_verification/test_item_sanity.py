"""
Contains tests that check the stand alone validity of an item

All tests here should only check one item at a time and not compare it to other items
"""
from . import TEST_STATUS, set_status, run_tests


@set_status(TEST_STATUS.unused)
def test_tags_in_stats(data_set):
    """Check that any stats mentioned are tagged
    TODO: Finish this test"""
    all_items = data_set["data"]

    for item, data in all_items.items():
        print(item, data["name"], data["tags"])

        # print(data["stats"])
        # if "effect" in data:
        #     print(data["effect"])
        # print(data["description"])
        # print("---")

    return True, None


@set_status(TEST_STATUS.in_development)
def test_sells_well(data_set):
    """Make sure no item can be sold for more than it costs.
    If such an item exists, it could be repeatedly bought and sold for (fast) infinite gold"""
    all_items = data_set["data"]

    bad_prices = list()
    for item, data in all_items.items():
        prices = data["gold"]
        if prices["sell"] > prices["total"]:
            # You can sell this for more than it costs to buy
            bad_prices.append(item)

    if bad_prices:
        message = "Some items can be sold for more than they cost"
        return False, message, bad_prices
    return True, None


@set_status(TEST_STATUS.in_development)
def test_cannot_build_itself(data_set):
    """Test an item isn't listed as a component or an upgrade for itself
    This could cause loops in dependency checking tests"""
    all_items = data_set["data"]

    can_build_into_itself = list()
    for item, data in all_items.items():
        if "into" in data and item in data["into"]:
            # Can build into itself
            can_build_into_itself.append(item)

        if "from" in data and item in data["from"]:
            # Can build from itself
            can_build_into_itself.append(item)

    if can_build_into_itself:
        message = "Some items can build into themselves"
        return False, message, can_build_into_itself
    return True, None


if __name__ == "__main__":
    run_tests(TEST_STATUS.in_development)
