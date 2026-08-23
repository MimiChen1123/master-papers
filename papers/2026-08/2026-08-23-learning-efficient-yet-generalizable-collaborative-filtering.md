---
date: 2026-08-23
title: "Learning-Efficient Yet Generalizable Collaborative Filtering for Item Recommendation"
authors: "Yuanhao Pu, Xiaolong Chen, Xu Huang, Jin Chen, Defu Lian, Enhong Chen"
venue: "ICML 2024"
---

# Learning-Efficient Yet Generalizable Collaborative Filtering for Item Recommendation

- Paper page: https://proceedings.mlr.press/v235/pu24a.html
- PDF: https://raw.githubusercontent.com/mlresearch/v235/main/assets/pu24a/pu24a.pdf
- Local PDF: [../../pdfs/2026-08/2026-08-23-learning-efficient-yet-generalizable-collaborative-filtering.pdf](../../pdfs/2026-08/2026-08-23-learning-efficient-yet-generalizable-collaborative-filtering.pdf)
- Venue: ICML 2024

## English Summary

This paper revisits why weighted squared-loss collaborative filtering methods, especially implicit ALS and WRMF-style matrix factorization, can perform surprisingly well on ranking metrics even though their objectives look like regression losses rather than ranking losses. The authors connect squared loss to ranking-oriented objectives by starting from softmax loss, a known DCG-consistent surrogate, and applying a Taylor expansion. This derivation motivates a new squared-form surrogate called Ranking-Generalizable Squared loss, or RG2.

The key idea is that RG2 keeps the optimization advantages of squared losses while giving the loss a clearer theoretical relationship to ranking quality. The paper proves that RG2 is DCG-consistent and also provides a generalization upper bound when RG2 is instantiated with matrix factorization. Practically, RG2 can be optimized with an ALS-style closed-form update over all items, avoiding both negative sampling variance and the expensive nonlinear normalization in full softmax training.

Experiments on MovieLens-10M, Amazon Electronics, and Steam show that RG2 is competitive with or better than softmax loss on ranking metrics such as MRR@10 and NDCG@10, while converging faster. Compared with WRMF, RG2 uses the same broad ALS optimization advantage but better aligns the objective with ranking metrics, which helps explain its stronger recommendation performance.

## 繁中 Summary

這篇論文重新檢視一個推薦系統中常見但理論上不夠清楚的現象：像 implicit ALS、WRMF 這類使用加權平方損失的 collaborative filtering 方法，明明看起來是在做回歸式目標，卻常常在 NDCG、MRR 這類排序指標上表現很好。作者從已知和 DCG 一致的 softmax loss 出發，透過 Taylor expansion 推導出平方形式的近似與上界，進而提出 Ranking-Generalizable Squared loss，也就是 RG2。

RG2 的重點是保留平方損失容易最佳化的優點，同時讓目標函數和排序品質之間有更明確的理論關係。論文證明 RG2 具有 DCG-consistency，並在 matrix factorization 場景下給出 generalization upper bound。實作上，RG2 可以用 ALS 類型的 closed-form update 在所有 items 上進行最佳化，因此不需要依賴 negative sampling，也避開 full softmax 訓練中昂貴的非線性 normalization。

實驗使用 MovieLens-10M、Amazon Electronics、Steam 三個資料集，評估 MRR@10 與 NDCG@10。結果顯示 RG2 的排序表現可與 softmax loss 相當，部分情況更好，而且收斂速度更快。相較 WRMF，RG2 同樣享有 ALS 的效率，但因為目標函數更貼近排序指標，所以在推薦品質上更有優勢。

## Notes

- The paper is useful if you care about the gap between efficient implicit-feedback CF objectives and ranking metrics.
- RG2 can be read as a theoretically motivated replacement for WRMF-style squared loss.
- The contribution is strongest for non-sampling recommendation training, where all unobserved items are considered rather than sampled as negatives.
