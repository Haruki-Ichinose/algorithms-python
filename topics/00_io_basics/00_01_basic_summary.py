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

n = int(input())
a = list(map(int, input().split()))

print(sum(a))
print(max(a))
print(len(set(a)))
