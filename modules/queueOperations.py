import modules.heapMin as Import
from modules.heapMin import *


def createQueue(dictionary):
    queue = []

    for char in dictionary.keys():
        enqueue(queue, (dictionary[char], char))

    return queue


def enqueue(queue, key):
    queue.append(key)
    buildMinHeap(queue)
    return queue


def dequeue(queue):
    if Import.heapSize < 1:
        return queue.pop()

    smallest, queue[0] = queue[0], queue.pop()
    Import.heapSize -= 1
    minHeapify(queue, 0)

    return smallest
