import json


DEFAULT_PATH = "items-7_15_1-en_US_pretty.json"

def run():
    items = load_items()

    print(json.dumps(items["data"], indent=4))


def load_items(filepath=DEFAULT_PATH):
    """ filepath: The path to the item set
        Returns a dict
    """
    with open(filepath) as f:
        return json.load(f)

if __name__ == "__main__":
    run()
