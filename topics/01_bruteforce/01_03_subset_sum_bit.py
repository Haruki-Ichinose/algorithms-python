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

    s = {0}
    for i in range(n):
        for j in range(i+1, n):
            s.add(a[i])
            s.add(a[j])
            s.add(a[i]+a[j])

    if x in s:
        print("Yes")


def model_answer():
    n, x = map(int, input().split())
    a = list(map(int, input().split()))

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
