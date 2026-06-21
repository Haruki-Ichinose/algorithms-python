"""
例題 00-5: 共通する値

入力:
N M
A1 A2 ... AN
B1 B2 ... BM

整数列 A と B の両方に含まれる値を、小さい順に空白区切りで出力する。
共通する値がない場合は空行を出力する。

例:
入力
5 6
3 1 4 1 5
5 9 2 6 3 5

出力
3 5
"""


def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    # set 同士の & は共通部分を表す。
    # 最後に sorted することで、小さい順のリストとして出力できる。
    common = set(a) & set(b)
    print(*sorted(common))


def another_answer_with_membership():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    # A を set にして、B の各値が A に含まれるか調べる方法。
    values = set(a)
    common = set()

    for x in b:
        if x in values:
            common.add(x)

    print(*sorted(common))


def another_answer_with_loop_over_set():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    # ループで両方の set を見比べる方法。
    set_a = set(a)
    set_b = set(b)
    common = set()

    # set_a の各値が set_b に含まれるか確認する。
    # `set_a & set_b` を自分で書くとこの形になる。
    for x in set_a:
        if x in set_b:
            common.add(x)

    print(*sorted(common))


if __name__ == "__main__":
    main()
