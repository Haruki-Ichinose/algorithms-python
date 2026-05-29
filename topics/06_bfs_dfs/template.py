from collections import deque


def bfs(graph, start):
    dist = [-1] * len(graph)
    dist[start] = 0
    queue = deque([start])
    while queue:
        v = queue.popleft()
        for to in graph[v]:
            if dist[to] != -1:
                continue
            dist[to] = dist[v] + 1
            queue.append(to)
    return dist


def main():
    graph = [[1, 2], [0, 3], [0], [1]]
    print(bfs(graph, 0))


if __name__ == "__main__":
    main()
