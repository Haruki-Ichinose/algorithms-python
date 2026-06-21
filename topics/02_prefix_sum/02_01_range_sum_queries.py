"""
例題 02-1: 複数の区間和クエリ

入力:
N Q
A1 A2 ... AN
L1 R1
L2 R2
...
LQ RQ

長さ N の整数列 A がある。
各クエリについて、A の L 番目から R 番目までの要素の和を出力する。

制約:
- 1 <= N, Q <= 200000
- 1 <= Ai <= 10000
- 1 <= Li <= Ri <= N

例:
入力
5 3
1 4 3 2 5
1 3
2 5
4 4

出力
8
14
2
"""

def main():
    n, q = map(int, input().split())
    a = list(map(int, input().split()))

    # 各クエリで区間を直接合計する方法。
    # 区間の長さ分の計算が必要なので、最悪計算量は O(NQ)。
    for _ in range(q):
        l, r = map(int, input().split())
        print(sum(a[l - 1 : r]))


def model_answer():
    n, q = map(int, input().split())
    a = list(map(int, input().split()))

    # prefix_sum[i] は、A の先頭から i 個分の合計。
    # 先頭に 0 を置くことで、先頭を含む区間も同じ式で求められる。
    prefix_sum = [0] * (n + 1)
    for i in range(1, n + 1):
        prefix_sum[i] = prefix_sum[i - 1] + a[i - 1]

    for _ in range(q):
        l, r = map(int, input().split())

        # 右端までの合計から、左端より前の合計を引く。
        # 1-indexed の閉区間 [l, r] の和を O(1) で求められる。
        result = prefix_sum[r] - prefix_sum[l - 1]
        print(result)


if __name__ == "__main__":
    main()
