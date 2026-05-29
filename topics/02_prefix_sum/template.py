def build_prefix_sum(a):
    s = [0]
    for x in a:
        s.append(s[-1] + x)
    return s


def range_sum(prefix, left, right):
    return prefix[right] - prefix[left]


def main():
    a = [1, 2, 3, 4]
    prefix = build_prefix_sum(a)
    print(range_sum(prefix, 1, 3))


if __name__ == "__main__":
    main()
