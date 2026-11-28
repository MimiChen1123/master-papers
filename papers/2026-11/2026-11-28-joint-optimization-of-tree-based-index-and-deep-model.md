---
date: 2026-11-28
title: "Joint Optimization of Tree-based Index and Deep Model for Recommender Systems"
authors: "Han Zhu, Daqing Chang, Ziru Xu, Pengye Zhang, Xiang Li, Jie He, Han Li, Jian Xu, Kun Gai"
venue: "NeurIPS 2019"
---

# Joint Optimization of Tree-based Index and Deep Model for Recommender Systems

- [Official paper page](https://proceedings.neurips.cc/paper/2019/hash/1c6a0198177bfcc9bd93f6aab94aad3c-Abstract.html)
- [Official PDF](https://proceedings.neurips.cc/paper_files/paper/2019/file/1c6a0198177bfcc9bd93f6aab94aad3c-Paper.pdf)
- [Local PDF](../../pdfs/2026-11/2026-11-28-joint-optimization-of-tree-based-index-and-deep-model.pdf)

## English Summary

JTM jointly learns where items sit in a retrieval tree and how a neural model scores its nodes. Training alternates between updating the scorer and reassigning items to leaves under a shared loss that rewards high scores along paths to observed items. To make reassignment tractable, the algorithm divides it into smaller problems across tree levels. The scorer represents each past interaction by its ancestor node at the current search depth, so broad categories guide early decisions and more specific behavior guides later ones. At inference, beam search expands only the highest-scoring branches, avoiding a full catalog scan. A relevant item can still be missed if its branch is pruned early.

With 200 candidates, JTM raises offline recall from 8.57% to 12.45% on Amazon Books and from 13.45% to 14.71% on Taobao UserBehavior versus a full-scan DNN. In a one-week Taobao homepage advertising A/B test, replacing one Item-CF candidate source with JTM increased click-through rate by 11.3% and revenue per thousand impressions by 12.9% relative to the production baseline. Those online gains apply to the tested advertising setup.

## 繁中摘要

JTM 同時學習物品在檢索樹中的位置，以及神經網路如何為樹節點評分。訓練交替更新評分模型與物品的葉節點分配，兩者共用同一個損失函數，讓通往已觀測互動物品的路徑獲得較高分。為降低重新分配的成本，演算法將問題依樹的層級拆成較小的子問題。評分時，使用者的歷史互動會映射到當前深度的祖先節點，讓上層根據較粗略的興趣篩選，下層再用更細的資訊判斷。推論以束搜尋只展開高分分支，不必掃描整個目錄，但相關物品所在分支若被提早剪去，仍可能漏掉。

候選數為 200 時，相較於全量掃描的 DNN，JTM 在 Amazon Books 的離線召回率由 8.57% 升至 12.45%，在淘寶 UserBehavior 則由 13.45% 升至 14.71%。為期一週的淘寶首頁廣告 A/B 測試中，以 JTM 替換其中一個 Item-CF 候選來源，相較於原線上系統，點擊率與每千次曝光收入分別相對提升 11.3% 與 12.9%。這兩項線上增幅僅反映該廣告場景的測試結果。
