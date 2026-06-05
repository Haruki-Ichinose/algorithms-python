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
"""

from collections import defaultdict


def main():
    n = int(input())
    a = list(map(int, input().split()))

    positions = defaultdict(list)

    # enumerate(a) は (index, value) を順番に取り出せる。
    # positions[x] に、値 x が出てきた位置 i を追加していく。
    for i, x in enumerate(a):
        positions[x].append(i)

    q = int(input())
    for _ in range(q):
        x = int(input())
        print(*positions[x])


def another_answer_with_dict():
    n = int(input())
    a = list(map(int, input().split()))

    # 別解:
    # 通常の dict を使う場合は、初めて出る値なら空リストを作る。
    positions = {}

    for i, x in enumerate(a):
        if x not in positions:
            positions[x] = []
        positions[x].append(i)

    q = int(input())
    for _ in range(q):
        x = int(input())
        if x in positions:
            print(*positions[x])
        else:
            print()


def another_answer_by_scanning_each_query():
    n = int(input())
    a = list(map(int, input().split()))

    # 別解:
    # 事前計算せず、質問ごとに A 全体を走査する。
    q = int(input())
    for _ in range(q):
        x = int(input())
        result = []

        # 事前計算せず、質問ごとに A 全体を見る。
        # 書き方は単純だが、毎回 O(N) かかる。
        for i, value in enumerate(a):
            if value == x:
                result.append(i)

        print(*result)


if __name__ == "__main__":
    main()
