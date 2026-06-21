"""
例題 02-3: 長さ K の連続部分列の最大和

入力:
N K
A1 A2 ... AN

長さ N の整数列 A がある。
連続する K 個の要素を選んだとき、その要素の和としてあり得る最大値を出力する。

制約:
- 1 <= K <= N <= 200000
- -1000000000 <= Ai <= 1000000000

例:
入力
7 3
2 -1 4 5 -2 3 1

出力
8
"""


def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    # 最初の K 個を、最初の区間の和として計算する。
    # 最大値をこの区間和で初期化することで、負の数だけの場合にも対応できる。
    current_sum = sum(a[:k])
    max_sum = current_sum

    # 区間を右へ1つずらすたびに、区間から外れる値を引き、
    # 新しく区間に入る値を足す。各区間の和を O(1) で更新できる。
    for i in range(k, n):
        current_sum += a[i] - a[i - k]
        max_sum = max(max_sum, current_sum)

    print(max_sum)


def another_answer_with_prefix_sum():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    # prefix_sum[i] は、A の先頭から i 個分の合計。
    # 累積和を使うと、任意の長さ K の区間和を O(1) で求められる。
    prefix_sum = [0] * (n + 1)
    for i in range(1, n + 1):
        prefix_sum[i] = prefix_sum[i - 1] + a[i - 1]

    # 最初の区間和で初期化し、全ての長さ K の区間を比較する。
    max_sum = prefix_sum[k] - prefix_sum[0]

    for left in range(1, n - k + 1):
        right = left + k
        current_sum = prefix_sum[right] - prefix_sum[left]
        max_sum = max(max_sum, current_sum)

    print(max_sum)


if __name__ == "__main__":
    main()
