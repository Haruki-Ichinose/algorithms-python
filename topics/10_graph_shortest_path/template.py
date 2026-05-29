import heapq


def dijkstra(graph, start):
    inf = 10**30
    dist = [inf] * len(graph)
    dist[start] = 0
    heap = [(0, start)]
    while heap:
        cost, v = heapq.heappop(heap)
        if cost != dist[v]:
            continue
        for to, weight in graph[v]:
            next_cost = cost + weight
            if next_cost < dist[to]:
                dist[to] = next_cost
                heapq.heappush(heap, (next_cost, to))
    return dist


def main():
    graph = [[(1, 2), (2, 5)], [(2, 1)], []]
    print(dijkstra(graph, 0))


if __name__ == "__main__":
    main()
