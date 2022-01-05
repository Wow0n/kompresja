encodedDictionary = {}


def encode(tree, code, temp):
    if tree[1] != "":
        encodedDictionary[tree[1]] = code
        return temp

    temp = encode(tree[2], code + "0", temp)
    temp = encode(tree[3], code + "1", temp)

    return temp
