---
date: 2026-11-27
title: "An Empirical Study Towards Prompt-Tuning for Graph Contrastive Pre-Training in Recommendations"
authors: "Haoran Yang, Xiangyu Zhao, Yicong Li, Hongxu Chen, Guandong Xu"
venue: "NeurIPS 2023 Main Conference"
---

# An Empirical Study Towards Prompt-Tuning for Graph Contrastive Pre-Training in Recommendations

- [Official paper page](https://proceedings.neurips.cc/paper_files/paper/2023/hash/c6af791af7ef0f3e02bccef011211ca5-Abstract-Conference.html)
- [Official PDF](https://proceedings.neurips.cc/paper_files/paper/2023/file/c6af791af7ef0f3e02bccef011211ca5-Paper-Conference.pdf)
- [Local PDF](../../pdfs/2026-11/2026-11-27-prompt-tuning-for-graph-contrastive-pre-training-in-recommendations.pdf)

## English Summary

CPTPP separates graph contrastive pre-training from downstream ranking instead of optimizing both losses jointly. It first learns user and item embeddings from the interaction graph. A two-layer network then turns each user's interaction history, matrix-factorization features, or higher-order graph connections into a personalized prompt vector. The model concatenates this vector with the pre-trained user embedding, fuses the two with an MLP, and adapts the embeddings using Bayesian Personalized Ranking. These prompts are learned vectors, not natural-language instructions.

The paper evaluates full-catalog ranking on random 80/20 interaction splits of Douban, MovieLens-1M, and Gowalla. In Table 2, the best CPTPP variant raises MovieLens-1M NDCG@20 from 0.2683 to 0.2782. On Gowalla, it improves Hit Ratio@20 from 0.1065 to 0.1120, but its best NDCG@20 is 0.1092 versus SimGCL's 0.1126. The results support the approach for offline ranking on these datasets, but a random interaction split does not establish performance on new users or future interactions.

## 繁中摘要

CPTPP 將圖對比預訓練與下游排序分成兩個階段，不再同時最佳化兩種損失。模型先從使用者與物品的互動圖學習嵌入，再以兩層網路將使用者的歷史互動、矩陣分解特徵或高階圖鄰接關係轉為個人化提示向量。接著將提示與預訓練的使用者嵌入串接，以多層感知器融合，並用貝氏個人化排序微調嵌入。這裡的提示是可學習的向量，不是自然語言指令。

實驗在 Douban、MovieLens-1M 與 Gowalla 將互動隨機分為 80% 訓練與 20% 測試，並對完整物品目錄排序。表 2 顯示，MovieLens-1M 的 NDCG@20 從最佳基準的 0.2683 提升至 0.2782。Gowalla 的 Hit Ratio@20 從 0.1065 提升至 0.1120，但 CPTPP 最好的 NDCG@20 為 0.1092，低於 SimGCL 的 0.1126。這些是離線排序結果；隨機切分不能證明模型對新使用者或未來互動同樣有效。
