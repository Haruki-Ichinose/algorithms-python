"""
例題 01-4: K個選ぶ

入力:
N K
A1 A2 ... AN

A から異なる K 個の要素を選ぶとき、作れる和の最大値を出力する。

例:
入力
5 3
1 4 6 2 8

出力
18
"""
from itertools import combinations


def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    # combinations(a, 3) では、選ぶ個数がサンプルの K=3 に固定される。
    # また、最大値の初期値を 1 にすると、全ての和が負の場合に正しく更新されない。
    tmp = 1
    for nums in combinations(a, 3):
        total = sum(nums)
        tmp = max(tmp, total)

    print(tmp)


def model_answer():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    # combinations(a, k) で、A から異なる K 個を選ぶ全組合せを列挙する。
    # 負の数だけの場合にも対応できるよう、最大値は十分小さい値で初期化する。
    best = -10**18

    for nums in combinations(a, k):
        total = sum(nums)
        best = max(best, total)

    print(best)


if __name__ == "__main__":
    main()
