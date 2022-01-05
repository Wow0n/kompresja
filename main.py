from modules.countChars import countChars
from modules.queueOperations import createQueue
from modules.readFile import readFile
from modules.createBinaryTree import binaryTree


if __name__ == '__main__':
    text = readFile("data/text.txt")

    dictionary = countChars(text)
    print("Dictionary: ", dictionary)

    priorityQueue = createQueue(dictionary)
    print("Priority queue: ", priorityQueue)

    binaryTree = binaryTree(priorityQueue)
    print("Binary tree: ", binaryTree)
