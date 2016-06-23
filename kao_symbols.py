
def convert(text, mappings):
    """ Convert the text using the mapping given """
    pieces = []
    needToRunAgain = False
    for c in text:
        if c in mappings:
            pieces.append(mappings[c])
            needToRunAgain = True
        else:
            pieces.append(c)
    if needToRunAgain:
        pieces = convert(pieces, mappings)
    return "".join(pieces)