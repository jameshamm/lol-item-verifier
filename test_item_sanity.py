from util import TEST_STATUS, set_status, run_tests


@set_status(TEST_STATUS.in_development)
def test_sells_well(data_set):
    items = data_set["data"]

    bad_prices = list()
    for item, data in items.items():
        prices = data["gold"]
        if prices["sell"] > prices["total"]:
            # You can sell this for more than it costs to buy
            bad_prices.append(item)

    if bad_prices:
        message = "The following items can be sold for more than they cost: " + str(bad_prices)
        return False, message

    return True, None


@set_status(TEST_STATUS.in_development)
def test_cannot_build_itself(data_set):
    items = data_set["data"]

    can_build_into_itself = list()
    for item, data in items.items():
        if "into" in data and item in data["into"]:
            # Can build into itself
            can_build_into_itself.append(item)

        if "from" in data and item in data["from"]:
            # Can build from itself
            can_build_into_itself.append(item)

    if can_build_into_itself:
        message = "The following items can build into themselves: " + str(bad_prices)
        return False, message

    return True, None


if __name__ == "__main__":
    run_tests(TEST_STATUS.in_development)
