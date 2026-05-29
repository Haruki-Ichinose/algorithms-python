"""
例題 00-3: 値の出現位置

入力:
N
A1 A2 ... AN
Q
X1
X2
...
XQ

整数列 A について、各質問 X に対して、X が A の何番目に出てくるかを
すべて出力する。

位置は 0-indexed とする。存在しない場合は空行を出力する。

例:
入力
7
3 1 3 2 1 3 5
4
1
3
5
9

出力
1 4
0 2 5
6


模範解答:
- 値ごとに、出現した位置のリストを持つ
- 通常の dict を使い、初めて出る値なら空リストを作る

別解:
- collections.defaultdict(list) を使うと、空リストを作る処理を省ける
"""

from collections import defaultdict


def build_positions_with_dict(a):
    positions = {}

    for i, x in enumerate(a):
        if x not in positions:
            positions[x] = []
        positions[x].append(i)

    return positions


def build_positions_with_defaultdict(a):
    positions = defaultdict(list)

    for i, x in enumerate(a):
        positions[x].append(i)

    return positions


def main():
    n = int(input())
    a = list(map(int, input().split()))

    positions = build_positions_with_dict(a)

    q = int(input())
    for _ in range(q):
        x = int(input())
        if x in positions:
            print(*positions[x])
        else:
            print()


if __name__ == "__main__":
    main()
