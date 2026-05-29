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

学び:
- set を使うと、存在判定を高速に書ける
- `x in values` の形に慣れる

計算量:
- set 作成: O(N)
- 各質問の判定: 平均 O(1)
- 全体: O(N + Q)

模範解答:
- A を set に変換してから、各 X について存在判定する

別解:
- A を list のまま `x in a` で判定する
- ただし list の存在判定は毎回 O(N) なので、質問が多いと遅い
"""


def my_answer():
    n = int(input())
    a = list(map(int, input().split()))
    q = int(input())
    queries = [int(input()) for _ in range(q)]

    values = set(a)
    for x in queries:
        if x in values:
            print("Yes")
        else:
            print("No")


def model_answer():
    n = int(input())
    a = list(map(int, input().split()))

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

    q = int(input())
    for _ in range(q):
        x = int(input())
        if x in a:
            print("Yes")
        else:
            print("No")


def main():
    my_answer()


if __name__ == "__main__":
    main()
