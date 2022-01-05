heapSize = 0


def minHeapify(a, i):
    global heapSize
    l = 2 * i + 1
    r = 2 * i + 2
    if l <= heapSize and a[l] < a[i]:
        smallest = l
    else:
        smallest = i
    if r <= heapSize and a[r] < a[smallest]:
        smallest = r
    if smallest != i:
        a[i], a[smallest] = a[smallest], a[i]
        minHeapify(a, smallest)


def buildMinHeap(a):
    global heapSize
    heapSize = len(a) - 1
    n = (len(a) - 1) // 2
    for i in range(n, -1, -1):
        minHeapify(a, i)
