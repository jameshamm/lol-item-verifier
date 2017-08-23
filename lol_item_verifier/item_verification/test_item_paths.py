"""
Check that items build into one another correctly

All tests here validate the links between items
"""
from . import TEST_STATUS, set_status, run_tests


@set_status(TEST_STATUS.in_development)
def test_item_components_and_upgrades(data_set):
    """ Test every item to make sure all items it builds into also lists it as a dependency"""
    all_items = data_set["data"]
    bad_links = dict()

    for item, data in all_items.items():
        # Check the upgrades all list the item as a component
        try:
            upgrades = data["into"]
        except KeyError:
            # The item doesn't build into anything
            pass
        else:
            for upgrade in upgrades:
                if upgrade not in all_items:
                    # Error case; The upgrade doesn't exist
                    if item not in bad_links:
                        bad_links[item] = list()
                    bad_links[item].append(upgrade)
                else:
                    upgraded_item = all_items[upgrade]
                    if "from" not in upgraded_item or item not in upgraded_item["from"]:
                        # Error case; The item hasn't been linked correctly
                        if item not in bad_links:
                            bad_links[item] = list()
                        bad_links[item].append(upgrade)

        # Check that all components list this item as an upgrade
        try:
            components = data["from"]
        except KeyError:
            # The item has no components
            continue
        else:
            for component in components:
                if component not in all_items:
                    # Error case; The component doesn't exist
                    if component not in bad_links:
                        bad_links[component] = list()
                    bad_links[component].append(item)
                else:
                    dependent_item = all_items[component]
                    if "into" not in dependent_item or item not in dependent_item["into"]:
                        # Error case; The item hasn't been linked correctly
                        if component not in bad_links:
                            bad_links[component] = list()
                        bad_links[component].append(item)

    if bad_links:
        message = "Some items do not link their dependencies or upgrades correctly"
        return False, message, bad_links
    return True, None


@set_status(TEST_STATUS.in_development)
def test_item_depth(data_set):
    """Check the depth for each item is correct relative to the item's components"""
    bad_depth_items = list()
    default_depth = data_set["basic"]["depth"]  # Assume this is the smallest depth
    all_items = data_set["data"]

    for item, data in all_items.items():
        if "depth" in data:
            if "from" in data:
                largest_depth = default_depth
                for dependency in data["from"]:
                    dependent_item = all_items[dependency]
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
        message = "Some items do not list their depth correctly"
        return False, message, bad_depth_items
    return True, None


@set_status(TEST_STATUS.in_development)
def test_item_components_available(data_set):
    """Check the depth for each item is correct relative to the item's components"""
    all_items = data_set["data"]

    unavailable_components = dict()
    for item, data in all_items.items():
        if "from" in data:
            for depedency in data["from"]:
                component = all_items[depedency]
                for map_id, available in data["maps"].items():
                    if available and not component["maps"][map_id]:
                        # The item is available, but it's component isn't on this map
                        if item not in unavailable_components:
                            unavailable_components[item] = list()
                        unavailable_components[item].append(depedency)
                        break

    if unavailable_components:
        message = "Some items have components which are not available on all the same maps"
        return False, message, unavailable_components
    return True, None


if __name__ == "__main__":
    run_tests(TEST_STATUS.in_development)
