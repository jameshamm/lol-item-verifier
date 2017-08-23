"""
Contains logic to reduce the size and possibly the complexity of the data set

Currently minifying the data set outputs it with all unnecessary whitespace removed and
removes item data that is identical to the default values

TODO: Change some colloqs to tags
TODO: Investigate some effects. Some are 0 which seems unusual, and others seem unused.
"""
from util import load_data, save_data, LATEST_DATA_SET_PATH


FILE_AMMENDMENT = "pretty"


def prettify(filepath=None):
    """Minifies the file by removing unnecessary whitespace
    Also remove properties which are the same as the default properties of an item"""
    if filepath is None:
        filepath = LATEST_DATA_SET_PATH
    data_set = load_data(filepath)

    filename, extension = filepath.rsplit(".", 1)
    new_filepath = filename + "_" + FILE_AMMENDMENT + "." + extension

    save_data(data_set, new_filepath, pretty=True)


if __name__ == "__main__":
    prettify()
