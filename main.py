from modules.countChars import countChars
from modules.queueOperations import createQueue
from modules.fileOperations import *
from modules.createBinaryTree import binaryTree
from modules.encodeChars import *

if __name__ == '__main__':
    text = readFile("data/text.txt")

    dictionary = countChars(text)
    print("Dictionary: ", dictionary)

    priorityQueue = createQueue(dictionary)
    print("Priority queue: ", priorityQueue)

    binaryTree = binaryTree(priorityQueue)
    print("Binary tree: ", binaryTree)

    encode(binaryTree, "", "")
    print("Encoded dictionary:", encodedDictionary)

    saveEncodedDictionary("data/encodedDictionary.txt", encodedDictionary)
    saveTextAsBinary("data/encodedText.txt", encodedDictionary, text)
