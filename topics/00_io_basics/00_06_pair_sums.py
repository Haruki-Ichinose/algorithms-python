"""
例題 00-6: ペアの和

入力:
N
A1 A2 ... AN

A から異なる2つの要素を選んで作れる和を、重複なしで小さい順に出力する。

例:
入力
4
1 3 3 5

出力
4 6 8

説明:
- 1 + 3 = 4
- 1 + 5 = 6
- 3 + 3 = 6
- 3 + 5 = 8
"""

from itertools import combinations


def main():
    n = int(input())
    a = list(map(int, input().split()))

    sums = set()

    # i < j にすると、同じ位置を2回選ばず、同じペアを順番違いで数えない。
    for i in range(n):
        for j in range(i + 1, n):
            sums.add(a[i] + a[j])

    print(*sorted(sums))


def another_answer_with_combinations():
    n = int(input())
    a = list(map(int, input().split()))

    # itertools.combinations で異なる2要素の組を作る方法。
    sums = set()

    # combinations(a, 2) は、A から異なる2要素を選ぶ全ての組を作る。
    for x, y in combinations(a, 2):
        sums.add(x + y)

    print(*sorted(sums))


if __name__ == "__main__":
    main()
