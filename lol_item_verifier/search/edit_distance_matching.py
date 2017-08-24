"""Matches search terms based on how many characters need to be
modifed to change from one word to another

"""

def lev(a, b):
    if len(a) < len(b):
        return lev(b, a)

    # len(a) >= len(b)
    if len(b) == 0:
        return len(a)

    previous_row = range(len(b) + 1)
    for i, c1 in enumerate(a):
        current_row = [i + 1]
        for j, c2 in enumerate(b):
            insertions = previous_row[j + 1] + 1 # j+1 instead of j since previous_row and current_row are one character longer
            deletions = current_row[j] + 1       # than b
            substitutions = previous_row[j] + (c1 != c2)
            current_row.append(min(insertions, deletions, substitutions))
        previous_row = current_row
    
    return previous_row[-1]


def match(data_set, search_term):
    """Look at the edit distance for betwen the search term and the name.
    Also look at the distance between each colloq and the term"""
    all_items = data_set["data"]
    search_term = search_term.lower()

    matches = dict()
    for item, data in all_items.items():
        distance = lev(search_term, data["name"].lower())
        best = (item, data["name"])
        if "colloq" in data:
            for colloq in data["colloq"].split(";"):
                if not colloq:
                    continue
                dist = lev(search_term, colloq.lower())
                if dist < distance:
                    distance = dist
                    best = (item, data["name"], colloq)

        if distance not in matches:
            matches[distance] = list()
        matches[distance].append(best)

    return matches
