"""
例題 01-3: 部分和

入力:
N X
A1 A2 ... AN

A の各要素を「選ぶ/選ばない」で決めたとき、和が X になる選び方が存在するなら
Yes、存在しないなら No を出力する。

例:
入力
4 10
2 3 5 8

出力
Yes
"""


def main():
    n, x = map(int, input().split())
    a = list(map(int, input().split()))

    # この方法で作れるのは、0 個、1 個、2 個を選んだ和だけ。
    # 各要素を「選ぶ/選ばない」で決める問題では、3 個以上を選ぶ場合も含めて
    # 2^N 通りを調べる必要がある。
    # また、存在判定では最後まで見つからなかった場合に No を出力する。
    s = {0}
    for i in range(n):
        for j in range(i + 1, n):
            s.add(a[i])
            s.add(a[j])
            s.add(a[i] + a[j])

    if x in s:
        print("Yes")


def model_answer():
    n, x = map(int, input().split())
    a = list(map(int, input().split()))

    # mask の i bit 目で、A[i] を選ぶかどうかを表す。
    # 0 から 2^N - 1 まで調べることで、全ての部分集合を列挙できる。
    for mask in range(1 << n):
        total = 0

        for i in range(n):
            if mask >> i & 1:
                total += a[i]

        if total == x:
            print("Yes")
            return

    print("No")


if __name__ == "__main__":
    main()
