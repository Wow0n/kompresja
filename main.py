from modules.countChars import countChars
from modules.readFile import readFile

if __name__ == '__main__':
    text = readFile("data/text.txt")
    dictionary = countChars(text)
    print(dictionary)
