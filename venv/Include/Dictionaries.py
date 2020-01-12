def flip_dict(s):
    flipDict = {}
    for k, v in s.items():
        flipDict.setdefault(v, []).append(k)
    return flipDict

print(flip_dict({"CA": "US", "NY": "US", "ON": "CA"}))