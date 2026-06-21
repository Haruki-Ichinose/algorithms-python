"""
例題 02-4: 長方形領域の和

入力:
H W
A11 A12 ... A1W
A21 A22 ... A2W
...
AH1 AH2 ... AHW
Q
R1_1 C1_1 R2_1 C2_1
R1_2 C1_2 R2_2 C2_2
...
R1_Q C1_Q R2_Q C2_Q

H 行 W 列の整数グリッド A がある。
各クエリについて、左上が (R1, C1)、右下が (R2, C2) の
長方形領域に含まれる値の合計を出力する。

行番号と列番号は 1-indexed とし、長方形の境界上のマスも含む。

制約:
- 1 <= H, W <= 1000
- 1 <= Q <= 200000
- -1000000000 <= Aij <= 1000000000
- 1 <= R1 <= R2 <= H
- 1 <= C1 <= C2 <= W

例:
入力
3 4
1 2 3 4
5 6 7 8
9 10 11 12
4
1 1 2 2
2 2 3 4
1 3 3 3
3 4 3 4

出力
14
54
21
12
"""


def main():
    # 二次元累積和の作り方と、長方形領域の和を求める式を
    # 自力で組み立てられなかった。
    pass


def model_answer():
    h, w = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(h)]

    # prefix_sum[r][c] は、左上 (1, 1) から右下 (r, c) までの合計。
    # 上と左の領域を足すと左上の領域を2回数えるため、1回分を引く。
    prefix_sum = [[0] * (w + 1) for _ in range(h + 1)]

    for r in range(1, h + 1):
        for c in range(1, w + 1):
            prefix_sum[r][c] = (
                a[r - 1][c - 1]
                + prefix_sum[r - 1][c]
                + prefix_sum[r][c - 1]
                - prefix_sum[r - 1][c - 1]
            )

    q = int(input())
    for _ in range(q):
        r1, c1, r2, c2 = map(int, input().split())

        # 右下までの合計から、長方形より上と左の領域を引く。
        # 左上の領域は2回引かれるため、最後に1回足し戻す。
        result = (
            prefix_sum[r2][c2]
            - prefix_sum[r1 - 1][c2]
            - prefix_sum[r2][c1 - 1]
            + prefix_sum[r1 - 1][c1 - 1]
        )
        print(result)


if __name__ == "__main__":
    main()
