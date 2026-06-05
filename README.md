# Algorithms Python Playground

Pythonでコーディングテスト・競技プログラミング対策を進めるための学習用リポジトリです。

目的は2つです。

- 基本アルゴリズムを自分で実装できるようにする
- 試験中・練習中にすぐ参照できるコードとメモを残す

## 進め方

各テーマは次の流れで進めます。

1. 中心概念を理解する
2. 例題を自力で解く
3. 問題ファイルに自分の解答を残す
4. 模範解答・別解・学びを追記する
5. 繰り返しそうなミスを記録する

演習時の詳しい運用ルールは `notes/study_workflow.md` にまとめています。

## テーマ一覧

優先度順に進めます。
未着手テーマのディレクトリは先に作らず、着手時に `topics/` 配下へ追加します。

1. `00_io_basics` - 入出力、配列、辞書、集合、標準ライブラリ
2. `01_bruteforce` - 全探索、bit全探索、順列・組合せ
3. `02_prefix_sum` - 累積和、二次元累積和、差分配列
4. `03_two_pointers` - 尺取り法、スライディングウィンドウ
5. `04_binary_search` - 二分探索、答えで二分探索
6. `05_sort_greedy` - ソート、区間、貪欲法
7. `06_bfs_dfs` - BFS、DFS、グリッド探索、連結成分
8. `07_union_find` - Union-Find、連結性、グループ管理
9. `08_heap` - 優先度付きキュー、上位K個、イベント処理
10. `09_dp` - 動的計画法、ナップサック、区間DP、bit DP
11. `10_graph_shortest_path` - Dijkstra、Bellman-Ford、Warshall-Floyd
12. `11_graph_advanced` - トポロジカルソート、木、最小全域木
13. `12_string` - 文字列、頻度、ハッシュ、KMP/Z algorithm
14. `13_math` - gcd、素数、約数、mod、組合せ
15. `14_advanced` - セグメント木、Fenwick Tree、座標圧縮

## ロードマップ

Phase 1: Python基礎と探索の土台

- `00_io_basics`
- `01_bruteforce`
- `02_prefix_sum`
- `03_two_pointers`
- `04_binary_search`

Phase 2: 頻出データ構造とグラフ

- `05_sort_greedy`
- `06_bfs_dfs`
- `07_union_find`
- `08_heap`

Phase 3: DPとグラフ発展

- `09_dp`
- `10_graph_shortest_path`
- `11_graph_advanced`

Phase 4: 文字列・数学・高度データ構造

- `12_string`
- `13_math`
- `14_advanced`

各テーマの完了条件:

- 概念を自分の言葉で説明できる
- 最小実装を自分で書ける
- 典型問題を1問以上解き、問題ファイルに自分の解答・模範解答・別解を残す
- `notes/mistakes.md` に詰まった点を書く

## ディレクトリ構成

```text
playground/algorithms-python/
  README.md
  notes/
    mistakes.md
    study_workflow.md
  topics/
    00_io_basics/
    01_bruteforce/
```

- `topics/`: テーマごとの学習メモ、問題ファイル
- `notes/`: 復習メモ、ミス集、判断基準

## 実行方針

基本はPython標準ライブラリだけで進めます。
