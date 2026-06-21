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
"""

from collections import Counter


def main():
    n = int(input())
    a = list(map(int, input().split()))

    # Counter は「値 -> 出現回数」の辞書のように使える。
    # 今回は 1, 2, 3 の回数だけ知りたいので、この順に取り出す。
    counts = Counter(a)

    print(counts[1])
    print(counts[2])
    print(counts[3])


def another_answer_with_dict():
    n = int(input())
    a = list(map(int, input().split()))

    # 数える値が決まっている場合は、dict で対象だけを管理できる。
    counts = {1: 0, 2: 0, 3: 0}

    for x in a:
        # 今回数えたいのは 1, 2, 3 だけ。
        # それ以外の値をそのまま counts[x] すると KeyError になる。
        if x in counts:
            counts[x] += 1

    print(counts[1])
    print(counts[2])
    print(counts[3])


def another_answer_with_list():
    n = int(input())
    a = list(map(int, input().split()))

    # 値の範囲が小さい場合は、list をカウント配列として使える。
    # 値が 1, 2, 3 のように小さい整数なら、counts[x] に個数を入れられる。
    # index 3 まで使うので長さ 4 にする。
    counts = [0] * 4

    for x in a:
        if 1 <= x <= 3:
            counts[x] += 1

    print(counts[1])
    print(counts[2])
    print(counts[3])


if __name__ == "__main__":
    main()
