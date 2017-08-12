"""
Contains logic to reduce the size and possibly the complexity of the data set

Currently minifying the data set outputs it with all unnecessary whitespace removed and
removes item data that is identical to the default values

TODO: Change some colloqs to tags
TODO: Investigate some effects. Some are 0 which seems unusual, and others seem unused.
"""
import json

from util import load_data


FILE_AMMENDMENT = "mini"


def minify(filepath):
    """Minifies the file by removing unnecessary whitespace
    Also remove properties which are the same as the default properties of an item"""
    data_set = load_data(filepath)

    basic_data = data_set["basic"]
    items = data_set["data"]

    smaller_items = dict()

    for item, data in items.items():
        smaller_item = dict()
        for key, value in data.items():
            if key in basic_data and value == basic_data[key]:
                # This property is the same as the default
                # It doesn't need to be re-specified
                continue
            smaller_item[key] = value

        smaller_items[item] = smaller_item

    data_set["data"] = smaller_items

    filename, extension = filepath.rsplit(".", 1)
    new_filepath = filename + "_" + FILE_AMMENDMENT + "." + extension

    with open(new_filepath, "w") as file:
        # Write the json minified and with a deterministic(?) key order
        file.write(json.dumps(data_set, separators=(',', ':'), sort_keys=True))


if __name__ == "__main__":
    minify("data_set/items-7_16_1-en_US.json")
