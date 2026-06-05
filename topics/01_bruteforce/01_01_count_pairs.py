"""
例題 01-1: 条件を満たすペア数

入力:
N K
A1 A2 ... AN

A から異なる2つの要素を選び、和が K 以下になるペアの個数を出力する。

例:
入力
5 7
1 4 3 2 5

出力
8
"""


def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    count = 0
    for i in range(n):
        for j in range(i + 1, n):
            if a[i] + a[j] <= k:
                count += 1

    print(count)

if __name__ == "__main__":
    main()
