"""Use show.py to display the (desired) information about an item"""
from data import load_data

def naive_display(item_number, full_detail=False):
    """Take the number for an item.
    Output the item data using the latest data_set.

    Example:
    >>> naive_display(1001)
    FILL THIS IN"""
    if isinstance(item_number, int):
        item_number = str(item_number)

    data_set = load_data()

    all_items = data_set["data"]

    if item_number not in all_items:
        message = "The item number ({}) does not correspond to an item "\
        "in the data set.".format(item_number)
        raise ValueError(message)

    item_data = all_items[item_number]

    if full_detail:
        for k, v in item_data.items():
            print("{}: {}".format(k, v))
    else:
        interesting_keys = ('name', 'plaintext', 'description')

        print("--- {} ---".format(item_number))
        for k in interesting_keys:
            if k in item_data:
                print("{}: {}".format(k, item_data[k]))

if __name__ == "__main__":
    naive_display(1001, full_detail=True)
