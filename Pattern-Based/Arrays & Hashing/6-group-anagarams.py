def groupAnagarams(strs):
    result = []
    groups = {}

    for word in strs:
        key = ''.join(sorted(word))

        if key in groups:
            groups[key].append(word)
        else:
            groups[key] = [word]

    for key,value in groups.items():
        result.append(value)

    return result

strs = ["eat", "tea", "tan", "ate", "nat", "bat"]

print(groupAnagarams(strs))