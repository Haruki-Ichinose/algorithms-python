"""
例題 00-2: 頻度カウント

入力:
N
A1 A2 ... AN

整数列 A の中で、値 1, 2, 3 がそれぞれ何回出てくるかを、この順に出力する。

例:
入力
7
1 3 2 1 3 1 5

出力
3
1
2

模範解答:
- 数えたい値だけを辞書に用意する
- A を1つずつ見て、辞書にある値だけカウントする

別解:
- 長さ4以上のリストを使って、counts[x] に個数を入れる
- collections.Counter を使う
"""

from collections import Counter


def solve_with_dict(a):
    counts = {1: 0, 2: 0, 3: 0}

    for x in a:
        if x in counts:
            counts[x] += 1

    print(counts[1])
    print(counts[2])
    print(counts[3])


def solve_with_list(a):
    counts = [0] * 4

    for x in a:
        if 1 <= x <= 3:
            counts[x] += 1

    print(counts[1])
    print(counts[2])
    print(counts[3])


def solve_with_counter(a):
    counts = Counter(a)

    print(counts[1])
    print(counts[2])
    print(counts[3])


def main():
    n = int(input())
    a = list(map(int, input().split()))

    solve_with_dict(a)


if __name__ == "__main__":
    main()
