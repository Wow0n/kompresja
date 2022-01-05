def readFile(path):
    with open(path, "r") as f:
        return f.read()


def saveEncodedDictionary(path, dictionary):
    with open(path, "w") as f:
        for k, v in dictionary.items():
            f.write(str(k) + ' : ' + str(v) + '\n')


def saveTextAsBinary(path, dictionary, text):
    with open(path, "w") as f:
        for char in dictionary.keys():
            text = text.replace(char, dictionary[char])

        f.write(text)
