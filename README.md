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
5. テンプレートと使いどころを整理する

## テーマ一覧

優先度順に進めます。

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

## ディレクトリ構成

```text
playground/algorithms-python/
  README.md
  roadmap.md
  topics/
  cli/
  notes/
```

- `topics/`: テーマごとの学習メモ、問題ファイル、テンプレート
- `cli/`: 将来、CLIから問題作成・実行・提出を行うための置き場
- `notes/`: 復習メモ、ミス集、判断基準

## 実行方針

基本はPython標準ライブラリだけで進めます。
競プロCLI化を始める段階で、必要なら `online-judge-tools` や自作ランナーを追加します。
