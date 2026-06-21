"""
例題 02-2: 区間内の偶数の個数

入力:
N Q
A1 A2 ... AN
L1 R1
L2 R2
...
LQ RQ

長さ N の整数列 A がある。
各クエリについて、A の L 番目から R 番目までに含まれる偶数の個数を出力する。

制約:
- 1 <= N, Q <= 200000
- 1 <= Ai <= 1000000000
- 1 <= Li <= Ri <= N

例:
入力
7 4
3 8 2 5 10 7 4
1 3
2 6
4 4
5 7

出力
2
3
0
2
"""


def main():
    n, q = map(int, input().split())
    a = list(map(int, input().split()))

    # 偶数を 1、奇数を 0 に変換することで、区間内の偶数の個数を
    # 0/1 配列の区間和として求められる。
    is_even = [0] * n
    for i in range(n):
        if a[i] % 2 == 0:
            is_even[i] = 1

    # prefix_sum[i] は、先頭から i 個に含まれる偶数の個数。
    prefix_sum = [0] * (n + 1)
    for i in range(1, n + 1):
        prefix_sum[i] = prefix_sum[i - 1] + is_even[i - 1]

    for _ in range(q):
        l, r = map(int, input().split())

        # 1-indexed の閉区間 [l, r] に含まれる偶数の個数を O(1) で求める。
        print(prefix_sum[r] - prefix_sum[l - 1])


if __name__ == "__main__":
    main()
