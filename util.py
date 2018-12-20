def capitalize_keys(d, toLower=False):
    result = {}
    for key, value in d.items():
        upper_key = key.lower() if toLower else key.upper()
        result[upper_key] = value
    return result