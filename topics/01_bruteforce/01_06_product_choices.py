"""
例題 01-6: 各グループから1つずつ選ぶ

入力:
A1 A2 A3
B1 B2 B3
C1 C2 C3
X

3つのグループ A, B, C からそれぞれ1つずつ整数を選ぶ。
合計が X になる選び方の個数を出力する。

例:
入力
1 2 3
2 4 6
3 6 9
10

出力
3
"""

from itertools import product


def main():
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))
    x = int(input())

    count = 0
    for i in range(len(a)):
        for j in range(len(b)):
            for k in range(len(c)):
                if a[i] + b[j] + c[k] == x:
                    # 確認コメント:
                    # 正しく数えられている。細かい点として、`count += 1` のように
                    # 演算子の前後に空白を入れると読みやすい。
                    count +=1

    print(count)


def model_answer():
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))
    x = int(input())

    count = 0

    # 添字 i, j, k は使わないので、リストから値を直接取り出す。
    # A から1つ、B から1つ、C から1つ選ぶ全パターンを三重ループで試す。
    for value_a in a:
        for value_b in b:
            for value_c in c:
                if value_a + value_b + value_c == x:
                    count += 1

    print(count)


def another_answer_with_product():
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))
    x = int(input())

    count = 0

    # product(a, b, c) は、a, b, c からそれぞれ1つずつ選ぶ全組合せを作る。
    # 三重ループを標準ライブラリで書いた形。
    for value_a, value_b, value_c in product(a, b, c):
        if value_a + value_b + value_c == x:
            count += 1

    print(count)


if __name__ == "__main__":
    main()
