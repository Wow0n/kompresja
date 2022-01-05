def countChars(text):
    dictionary = {}

    for i in text:
        if i not in dictionary:
            dictionary[i] = 1
        else:
            dictionary[i] += 1

    return dictionary
