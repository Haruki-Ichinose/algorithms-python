"""
例題 01-2: 3つの和

入力:
N X
A1 A2 ... AN

A から異なる3つの要素を選び、和が X になる組が存在するなら Yes、
存在しないなら No を出力する。

例:
入力
5 9
1 4 6 2 8

出力
Yes
"""


def main():
    n, x = map(int, input().split())
    a = list(map(int, input().split()))

    # break は一番内側の k ループしか抜けない。
    # 存在判定では、見つかった時点で探索全体を終え、
    # 最後まで見つからなければ No を出力する必要がある。
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if a[i] + a[j] + a[k] == x:
                    print("Yes")
                    break


def model_answer():
    n, x = map(int, input().split())
    a = list(map(int, input().split()))

    # i < j < k にすることで、異なる3要素の組を重複なく調べる。
    # 見つかった場合は return で関数を終了する。
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if a[i] + a[j] + a[k] == x:
                    print("Yes")
                    return

    print("No")


if __name__ == "__main__":
    main()
