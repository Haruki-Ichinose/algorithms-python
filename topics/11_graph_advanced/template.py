from collections import deque


def topological_sort(graph):
    n = len(graph)
    indegree = [0] * n
    for edges in graph:
        for to in edges:
            indegree[to] += 1

    queue = deque([i for i in range(n) if indegree[i] == 0])
    order = []
    while queue:
        v = queue.popleft()
        order.append(v)
        for to in graph[v]:
            indegree[to] -= 1
            if indegree[to] == 0:
                queue.append(to)
    return order


def main():
    graph = [[1, 2], [3], [3], []]
    print(topological_sort(graph))


if __name__ == "__main__":
    main()
