from util import TEST_STATUS, set_status, run_tests


@set_status(TEST_STATUS.in_development)
def test_stats_work(data_set):
    listed_stats = data_set["basic"]["stats"]
    listed_stats = set(listed_stats.keys())

    known_stats = set()

    for data in data_set["data"].values():
        stats = data["stats"]
        for stat in stats.keys():
            known_stats.add(stat)

    # print(listed_stats)
    # print(known_stats)
    print("Unused stats")
    print(listed_stats - known_stats)

    return True, None


@set_status(TEST_STATUS.in_development)
def test_available_on_a_map(data_set):
    items = data_set["data"]

    not_available = list()
    for item, data in items.items():
        if not any(v for v in data["maps"].values()):
            # Cannot buy this item on any map
            not_available.append(item)

    if not_available:
        message = "The following items cannot be bought: " + str(not_available)
        return False, message

    return True, None



@set_status(TEST_STATUS.in_development)
def test_sprites_are_unique(data_set):
    items = data_set["data"]

    seen = dict()
    for item, data in items.items():
        image = data["image"]
        pic, x, y = image["sprite"], image["x"], image["y"]
        if (pic, x, y) not in seen:
            seen[pic, x, y] = []
        seen[pic, x, y].append(item)
    
    repeats = dict()
    for image, items_seen in seen.items():
        if len(items_seen) > 1:
            repeats[image] = items_seen

    if repeats:
        message = "The following items share a sprite: " + str(repeats)
        return False, message

    return True, None


if __name__ == "__main__":
    run_tests(TEST_STATUS.in_development)
