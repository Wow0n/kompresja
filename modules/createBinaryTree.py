from modules.queueOperations import *


def binaryTree(queue):
    while len(queue) > 1:
        x = dequeue(queue)
        y = dequeue(queue)

        if x[0] == y[0] and not x[1] == "":
            x, y = y, x

        enqueue(queue, (x[0] + y[0], "", x, y))

    return dequeue(queue)