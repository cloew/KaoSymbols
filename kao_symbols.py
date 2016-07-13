
def convert(text, mappings):
    """ Convert the text using the mapping given """
    for key, value in mappings.items():
        text = text.replace(key, value)
    return text