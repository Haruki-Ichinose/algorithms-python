"""
例題 00-4: 存在判定

入力:
N
A1 A2 ... AN
Q
X1
X2
...
XQ

整数列 A について、各質問 X が A に含まれるなら Yes、含まれないなら No を出力する。

例:
入力
5
3 1 4 1 5
4
1
2
5
9

出力
Yes
No
Yes
No
"""


def main():
    n = int(input())
    a = list(map(int, input().split()))

    # 存在判定を何度もするなら set にしておく。
    # 同じ値が複数あっても「含まれるか」だけなら重複情報は不要。
    values = set(a)

    q = int(input())
    for _ in range(q):
        x = int(input())

        if x in values:
            print("Yes")
        else:
            print("No")


def another_answer_with_list():
    n = int(input())
    a = list(map(int, input().split()))

    # A を list のまま `x in a` で判定する方法。
    # ただし、list の存在判定は毎回 O(N) なので、質問が多いと遅い。
    q = int(input())
    for _ in range(q):
        x = int(input())

        # list のままでも書けるが、毎回先頭から探す。
        if x in a:
            print("Yes")
        else:
            print("No")


if __name__ == "__main__":
    main()
