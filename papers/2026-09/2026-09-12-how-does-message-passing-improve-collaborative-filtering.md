---
date: 2026-09-12
title: "How Does Message Passing Improve Collaborative Filtering?"
authors: "Clark Mingxuan Ju, William Shiao, Zhichun Guo, Yanfang Ye, Yozen Liu, Neil Shah, Tong Zhao"
venue: "NeurIPS 2024"
---

# How Does Message Passing Improve Collaborative Filtering?

- Paper page: https://proceedings.neurips.cc/paper_files/paper/2024/hash/10a3b1c30b8cceb507b9e8ddcc9a1a6a-Abstract-Conference.html
- PDF: https://proceedings.neurips.cc/paper_files/paper/2024/file/10a3b1c30b8cceb507b9e8ddcc9a1a6a-Paper-Conference.pdf
- Local PDF: [../../pdfs/2026-09/2026-09-12-how-does-message-passing-improve-collaborative-filtering.pdf](../../pdfs/2026-09/2026-09-12-how-does-message-passing-improve-collaborative-filtering.pdf)
- Venue: NeurIPS 2024

## English Summary

This paper investigates why message passing improves collaborative filtering. Graph-based recommender models such as LightGCN are often explained by analogy to general graph learning, where node representations are refined through repeated neighbor aggregation. The authors show that this explanation is incomplete for collaborative filtering, because user-item supervision already creates graph-like effects during optimization, especially for high-degree users and items.

Through ablation studies and theoretical analysis, the paper finds two main mechanisms. First, most of the benefit of message passing comes from additional neighbor representations used in the forward pass, rather than from extra gradient updates to neighboring embeddings during backpropagation. Second, message passing helps low-degree users more than high-degree users, because high-degree nodes already receive many training signals from the collaborative filtering objective.

Based on these findings, the authors propose Test-time Aggregation for Collaborative Filtering (TAG-CF). TAG-CF trains a standard non-graph collaborative filtering model, then performs message passing only once at inference time. This keeps the useful neighbor aggregation effect while avoiding the repeated training-time cost of graph CF. Across six datasets, TAG-CF improves non-graph CF methods by up to 39.2% on cold users and 31.7% overall, while using less than 1% of the total training time of graph-enhanced CF methods in the reported comparisons.

## 繁中摘要

這篇論文分析為什麼 message passing 會提升 collaborative filtering。像 LightGCN 這類 graph-based recommender 常被解釋為和一般 graph learning 類似，也就是透過鄰居聚合逐步改善 node representation。但作者指出，這個解釋放在 collaborative filtering 不完全正確，因為 user-item interaction 的訓練目標本身就已經在 optimization 過程中產生類似圖傳遞的效果，尤其是對 high-degree users/items。

透過消融實驗與理論分析，論文得到兩個重點。第一，message passing 的主要收益來自 forward pass 中使用額外鄰居 representation，而不是 backpropagation 時對鄰居 embedding 產生額外 gradient update。第二，message passing 對 low-degree users 的幫助通常比 high-degree users 更大，因為 high-degree nodes 已經從 CF objective 收到大量訓練訊號。

基於這些觀察，作者提出 Test-time Aggregation for Collaborative Filtering (TAG-CF)。TAG-CF 先訓練一般 non-graph collaborative filtering 模型，然後只在 inference time 做一次 message passing。這樣保留鄰居聚合的好處，同時避免 graph CF 在訓練期間反覆 message passing 的成本。六個資料集上的結果顯示，TAG-CF 對 non-graph CF 在 cold users 上最多提升 39.2%，overall 最多提升 31.7%，且相較 graph-enhanced CF 方法只需不到 1% 的總訓練時間。

## Notes

- Useful for understanding why LightGCN-style message passing helps recommendation.
- The key systems idea is to move aggregation from training time to test time.
- Particularly relevant for cold-start or low-degree users where graph information is most valuable.
