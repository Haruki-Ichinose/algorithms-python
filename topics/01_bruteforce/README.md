# 01_bruteforce

## 目的

まず全部試す発想を身につけ、制約から間に合う探索範囲を判断できるようにする。

## 扱う内容

- 単純な全探索
- 二重ループ、三重ループ
- bit全探索
- 順列・組合せ
- `itertools.product`

## 判断基準

- `N <= 20`: bit全探索を疑う
- `N <= 8`: 順列全探索を疑う
- `N <= 2,000`: O(N^2) が通る可能性を見る
- `N <= 2 * 10^5`: O(N log N) か O(N) を考える

## 例題

1. `01_01_count_pairs.py` - 条件を満たすペア数
2. `01_02_three_sum.py` - 3つの和
3. `01_03_subset_sum_bit.py` - bit全探索で部分和
4. `01_04_choose_k_sum.py` - K個選ぶ組合せ
5. `01_05_permutation_route.py` - 順列全探索で最短経路
6. `01_06_product_choices.py` - 各グループから1つずつ選ぶ

## 完了条件

- まず全探索で書き切れる
- `i < j < k` のように重複を避けるループを書ける
- bit全探索で「選ぶ/選ばない」を表現できる
- `combinations`, `permutations`, `product` の使いどころを説明できる
