
def convert(text, mappings):
    """ Convert the text using the mapping given """
    if hasattr(mappings, 'items'):
        return _convert(text, mappings)
    else:        
        for mapping in mappings:
            text = _convert(text, mapping)
        return text
    

def _convert(text, mapping):
    """ Convert the text using the mapping given """
    for key, value in mapping.items():
        text = text.replace(key, value)
    return text