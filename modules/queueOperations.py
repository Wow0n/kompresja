from modules.heapMin import buildMinHeap


def createQueue(dictionary):
    queue = []

    for char in dictionary.keys():
        enqueue(queue, (dictionary[char], char))

    return queue


def enqueue(queue, key):
    queue.append(key)
    buildMinHeap(queue)

    return queue
