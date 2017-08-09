from main import load_items
from util import TEST_STATUS, set_status


TESTS = dict()


@set_status(TEST_STATUS.in_development, TESTS)
def test_items_dependencies_and_upgrades(data_set):
    """ Test every item to make sure all items it builds into also lists it as a dependency"""

    items = data_set["data"]
    bad_links = dict()
    for item, data in items.items():
        try:
            upgrades = data["into"]
        except KeyError:
            # The item doesn't build into anything
            pass
        else:
            for upgrade in upgrades:
                if upgrade not in items:
                    # Error case; The upgrade doesn't exist
                    if item not in bad_links:
                        bad_links[item] = list()
                    bad_links[item].append(upgrade)
                else:
                    upgraded_item = items[upgrade]
                    if "from" not in upgraded_item or item not in upgraded_item["from"]:
                        # Error case; The item hasn't been linked correctly
                        if item not in bad_links:
                            bad_links[item] = list()
                        bad_links[item].append(upgrade)

        try:
            dependencies = data["from"]
        except KeyError:
            # The item isn't built from anything
            continue
        else:
            for dependency in dependencies:
                if dependency not in items:
                    # Error case; The dependency doesn't exist
                    if dependency not in bad_links:
                        bad_links[dependency] = list()
                    bad_links[dependency].append(item)
                else:
                    dependent_item = items[dependency]
                    if "into" not in dependent_item or item not in dependent_item["into"]:
                        # Error case; The item hasn't been linked correctly
                        if dependency not in bad_links:
                            bad_links[dependency] = list()
                        bad_links[dependency].append(item)

    if bad_links:
        message = "The following items are not linked correctly: " + str(bad_links)
        return False, message
    return True, None


@set_status(TEST_STATUS.in_development, TESTS)
def test_item_depth(data_set):
    """Check the depth for each item"""
    bad_depth_items = list()
    default_depth = data_set["basic"]["depth"]
    items = data_set["data"]

    for item, data in items.items():
        if "depth" in data:
            if "from" in data:
                largest_depth = default_depth
                for dependency in data["from"]:
                    dependent_item = items[dependency]
                    depth = dependent_item["depth"] if "depth" in dependent_item else default_depth
                    largest_depth = max(largest_depth, depth)

                if data["depth"] != largest_depth + 1:
                    # The item and/or one of it's components does not have the correct depth
                    bad_depth_items.append(item)

            elif data["depth"] > default_depth:
                # Item is missing component info or the depth is too high
                bad_depth_items.append(item)

        elif "from" in data and data["from"]:
            # The item has components and therefore is missing depth info
            bad_depth_items.append(item)

    if bad_depth_items:
        message = "The following items are not listing their depth correctly: " + str(bad_depth_items)
        return False, message

    return True, None


def run_dev_tests():
    """Run the tests in this file that are marked as ready"""
    data_set = load_items()

    for test in TESTS[TEST_STATUS.in_development]:
        result, log = test(data_set)
        message = test.__name__ + ": " + ("PASSED" if result else "FAILED")
        if log:
            message += " - " + log
        print(message)


if __name__ == "__main__":
    run_dev_tests()