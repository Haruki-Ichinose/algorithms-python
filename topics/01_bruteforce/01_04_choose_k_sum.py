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

    # 確認コメント:
    # combinations(a, 3) だとサンプルの K=3 に固定される。
    # 問題では K が入力で与えられるため combinations(a, k) を使う。
    # tmp = 1 は負の数だけの入力で壊れるので、十分小さい値から始める。
    tmp = 1
    for nums in combinations(a, 3):
        total = sum(nums)
        tmp = max(tmp, total)

    print(tmp)


def model_answer():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    best = -10**18

    for nums in combinations(a, k):
        total = sum(nums)
        best = max(best, total)

    print(best)


if __name__ == "__main__":
    main()
