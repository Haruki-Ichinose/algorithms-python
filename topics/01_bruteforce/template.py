from itertools import combinations, permutations, product


def bit_subsets(items):
    n = len(items)
    result = []
    for mask in range(1 << n):
        subset = []
        for i in range(n):
            if mask >> i & 1:
                subset.append(items[i])
        result.append(subset)
    return result


def main():
    items = [1, 2, 3]
    print(bit_subsets(items))
    print(list(combinations(items, 2)))
    print(list(permutations(items)))
    print(list(product([0, 1], repeat=3)))


if __name__ == "__main__":
    main()
