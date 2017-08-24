"""Matches search terms by if it contains a substring of the item names

"""


def match(data_set, search_term):
    """Looks for the items in which the search term is
    a substring of the name or one of the colloqs."""
    all_items = data_set["data"]
    search_term = search_term.lower()

    matches = list()
    for item, data in all_items.items():
        if search_term in data["name"].lower():
            matches.append((item, data["name"]))
        elif "colloq" in data:
            for colloq in data["colloq"].split(";"):
                if search_term in colloq.lower():
                    matches.append((item, data["name"], colloq))

    return matches
