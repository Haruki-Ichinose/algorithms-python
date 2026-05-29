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

学び:
- 二重ループで全ペアを試せる
- set で和の重複を消せる
- itertools.combinations を使う別解もある

計算量:
- 全ペアの列挙: O(N^2)
- 和のソート: O(K log K), K は作れる和の種類数

模範解答:
- 添字 i, j を使い、i < j のペアだけを試す
- set に和を入れて重複を消す
- sorted で小さい順にして出力する

別解:
- itertools.combinations(a, 2) で異なる2要素の組を作る
"""

from itertools import combinations


def my_answer():
    n = int(input())
    a = list(map(int, input().split()))

    sums = set()
    for i in range(n):
        for j in range(i + 1, n):
            sums.add(a[i] + a[j])

    print(*sorted(sums))


def model_answer():
    n = int(input())
    a = list(map(int, input().split()))

    sums = set()

    for i in range(n):
        for j in range(i + 1, n):
            sums.add(a[i] + a[j])

    print(*sorted(sums))


def another_answer_with_combinations():
    n = int(input())
    a = list(map(int, input().split()))

    sums = set()

    for x, y in combinations(a, 2):
        sums.add(x + y)

    print(*sorted(sums))


def main():
    my_answer()


if __name__ == "__main__":
    main()
