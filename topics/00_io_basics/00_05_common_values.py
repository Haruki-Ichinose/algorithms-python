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

学び:
- set で重複を消せる
- `set_a & set_b` で共通部分を求められる
- 出力順が必要なら sorted を使う

計算量:
- set 作成: O(N + M)
- 共通部分の計算: O(min(N, M)) 程度
- ソート: O(K log K), K は共通する値の種類数

模範解答:
- A と B を set に変換する
- `set_a & set_b` で共通する値を求める
- sorted で小さい順にして出力する

別解:
- A を set にして、B の各値が A に含まれるか調べる
- 見つかった値を set に入れて重複を消す
"""


def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    set_a = set(a)
    set_b = set(b)

    print(*sorted(set_a & set_b))


def model_answer():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    common = set(a) & set(b)
    print(*sorted(common))


def another_answer_with_membership():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    values = set(a)
    common = set()

    for x in b:
        if x in values:
            common.add(x)

    print(*sorted(common))

if __name__ == "__main__":
    main()
