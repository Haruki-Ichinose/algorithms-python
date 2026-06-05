"""
例題 01-5: 最短経路

入力:
N
D11 D12 ... D1N
D21 D22 ... D2N
...
DN1 DN2 ... DNN

地点 0 から出発し、残りの地点をすべて1回ずつ訪れる。
移動コスト D[i][j] が与えられるとき、最小コストを出力する。
地点 0 に戻る必要はない。

例:
入力
4
0 3 4 7
3 0 2 5
4 2 0 6
7 5 6 0

出力
11
"""
from itertools import permutations


def main():
    n = int(input())
    d = [list(map(int, input().split())) for _ in range(n)]

    best = float("inf")

    for order in permutations(range(1, n)):
        route = (0,) + order

        cost = 0
        for i in range(n - 1):
            # 確認コメント:
            # 入力した距離表は d という変数名なので、ここも d を使う。
            # dist は定義されていないため NameError になる。
            cost += dist[route[i]][route[i + 1]]

        best = min(best, cost)

    print(best)


def model_answer():
    n = int(input())
    dist = [list(map(int, input().split())) for _ in range(n)]

    # 最小値を求めるので、最初は十分大きい値にしておく。
    best = 10**18

    # 地点 0 は始点として固定されている。
    # そのため、並べ替える必要があるのは地点 1 から n - 1 まで。
    # permutations(range(1, n)) は、残りの地点を訪れる順番を全て列挙する。
    for order in permutations(range(1, n)):
        # order は例として (2, 1, 3) のような形になる。
        # 実際の移動ルートは地点 0 から始まるので、先頭に 0 を足す。
        route = (0,) + order
        cost = 0

        # route の隣り合う地点同士を順番に見て、移動コストを足す。
        # 例: route = (0, 2, 1, 3) なら
        # dist[0][2] + dist[2][1] + dist[1][3] を計算する。
        for i in range(n - 1):
            current_city = route[i]
            next_city = route[i + 1]
            cost += dist[current_city][next_city]

        # 今まで見たルートの中で、一番小さいコストを残す。
        best = min(best, cost)

    print(best)


if __name__ == "__main__":
    main()
