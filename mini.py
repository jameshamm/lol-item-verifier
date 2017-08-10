import json

from util import load_data


FILE_AMMENDMENT = "mini"


def minify(filepath):
    """Minifis the file by removing unnecessary whitespace
    Also remove properties which are the same as the default properties of an item"""
    data_set = load_data(filepath)

    basic_data = data_set["basic"]
    items = data_set["data"]

    smaller_items = dict()

    for item, data in items.items():
        smaller_item = dict()
        for k, v in data.items():
            if k in basic_data and v == basic_data[k]:
                # This property is the same as the default
                # It doesn't need to be re-specified
                continue
            smaller_item[k] = v

        smaller_items[item] = smaller_item

    data_set["data"] = smaller_items

    filename, extension = filepath.rsplit(".", 1)
    new_filepath = filename + "_" + FILE_AMMENDMENT + "." + extension

    with open(new_filepath, "w") as file:
        # Write the json minified and with a deterministic key order
        file.write(json.dumps(data_set, separators=(',',':'), sort_keys=True))

if __name__ == "__main__":
    minify("items-7_16_1-en_US.json")
