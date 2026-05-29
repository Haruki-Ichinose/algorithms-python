import heapq


def main():
    heap = []
    for x in [5, 1, 3]:
        heapq.heappush(heap, x)
    while heap:
        print(heapq.heappop(heap))


if __name__ == "__main__":
    main()
