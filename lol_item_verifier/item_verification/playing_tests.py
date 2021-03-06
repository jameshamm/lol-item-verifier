from . import TEST_STATUS, set_status, run_tests


@set_status(TEST_STATUS.in_development)
def test_colloq_is_useful(data_set):
    """Check the colloq contains some actual content"""
    default_colloq = data_set["basic"]["colloq"]
    items = data_set["data"]

    bad_colloqs = list()

    for item, data in items.items():
        if "colloq" in data:
            colloq = data["colloq"]
            if colloq == "" or colloq == default_colloq:
                # The colloq is empty or isn't needed
                bad_colloqs.append(item)

    if bad_colloqs:
        message = "Some items have an unnecessary colloq property"
        return False, message, bad_colloqs

    return True, None


@set_status(TEST_STATUS.unused)
def test_stats_work(data_set):
    listed_stats = data_set["basic"]["stats"]
    listed_stats = set(listed_stats.keys())

    used_stats = set()

    for data in data_set["data"].values():
        stats = data["stats"]
        for stat in stats.keys():
            used_stats.add(stat)

    # print(listed_stats)
    # print(used_stats)
    print("Unused stats")
    print(listed_stats - used_stats)

    return True, None


@set_status(TEST_STATUS.unused)
def test_available(data_set):
    items = data_set["data"]

    not_available = list()
    for item, data in items.items():
        if not any(v for v in data["maps"].values()):
            # Cannot buy this item on any map
            not_available.append(item)

    if not_available:
        message = "Some items cannot be bought on any map"
        return False, message, not_available

    return True, None


@set_status(TEST_STATUS.in_development)
def test_sprites_are_unique(data_set):
    """Check that no two items share the same sprite"""
    items = data_set["data"]

    seen = dict()
    for item, data in items.items():
        image = data["image"]
        image_data = image["sprite"], image["x"], image["y"]
        if image_data not in seen:
            seen[image_data] = []
        seen[image_data].append(item)

    repeats = dict()
    for image, items_seen in seen.items():
        if len(items_seen) > 1:
            repeats[image] = items_seen

    if repeats:
        message = "Some items share the same sprite"
        return False, message, repeats

    return True, None


if __name__ == "__main__":
    run_tests(TEST_STATUS.in_development)
