from bisect import bisect_left, bisect_right


def first_true(ok, ng, can):
    while abs(ok - ng) > 1:
        mid = (ok + ng) // 2
        if can(mid):
            ok = mid
        else:
            ng = mid
    return ok


def main():
    a = [1, 3, 3, 7]
    print(bisect_left(a, 3), bisect_right(a, 3))


if __name__ == "__main__":
    main()
