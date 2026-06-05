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

    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                if a[i] + a[j] + a[k] == x:
                    print("Yes")
                    break


def model_answer():
    n, x = map(int, input().split())
    a = list(map(int, input().split()))

    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if a[i] + a[j] + a[k] == x:
                    print("Yes")
                    return

    print("No")

if __name__ == "__main__":
    main()
