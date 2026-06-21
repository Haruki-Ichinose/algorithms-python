"""
例題 00-1: 配列の基本集計

入力:
N
A1 A2 ... AN

整数列 A について、次の3つを順番に出力する。

- 合計
- 最大値
- 異なる値の個数

例:
入力
5
3 1 4 1 5

出力
14
5
4
"""


def main():
    n = int(input())
    a = list(map(int, input().split()))

    # Python の組み込み関数を使うのが一番読みやすい。
    # set は重複を消すデータ構造なので、len(set(a)) で異なる値の個数になる。
    print(sum(a))
    print(max(a))
    print(len(set(a)))


def another_answer_with_loop():
    n = int(input())
    a = list(map(int, input().split()))

    # 1 回のループで合計、最大値、出現済み集合をまとめて更新する方法。
    total = 0
    maximum = a[0]
    seen = set()

    for x in a:
        total += x
        maximum = max(maximum, x)
        seen.add(x)

    print(total)
    print(maximum)
    print(len(seen))


if __name__ == "__main__":
    main()
