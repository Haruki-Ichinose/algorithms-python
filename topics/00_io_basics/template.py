from collections import Counter, defaultdict, deque
from itertools import combinations, permutations, product


def main():
    n = int(input())
    a = list(map(int, input().split()))

    counts = Counter(a)
    positions = defaultdict(list)
    for i, x in enumerate(a):
        positions[x].append(i)

    print(n)
    print(counts)


if __name__ == "__main__":
    main()
