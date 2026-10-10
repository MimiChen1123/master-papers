---
date: 2026-10-10
title: "Unbiased Recommender Learning from Implicit Feedback via Weakly Supervised Learning"
authors: "Hao Wang, Zhichao Chen, Haotian Wang, Yanchao Tan, Licheng Pan, Tianqiao Liu, Xu Chen, Haoxuan Li, Zhouchen Lin"
venue: "ICML 2025"
---

# Unbiased Recommender Learning from Implicit Feedback via Weakly Supervised Learning

- Paper page: https://proceedings.mlr.press/v267/wang25p.html
- PDF: https://raw.githubusercontent.com/mlresearch/v267/main/assets/wang25p/wang25p.pdf
- Local PDF: [../../pdfs/2026-10/2026-10-10-unbiased-recommender-learning-from-implicit-feedback-via-weakly-supervised-learning.pdf](../../pdfs/2026-10/2026-10-10-unbiased-recommender-learning-from-implicit-feedback-via-weakly-supervised-learning.pdf)
- Venue: ICML 2025

## English Summary

Implicit-feedback recommenders observe positive actions such as clicks or views but usually lack reliable negative labels. Treating every unobserved user-item pair as negative can misclassify items that the user would like but has never seen. This paper proposes WeaklyRec, a model-agnostic framework that reframes implicit recommendation as positive-unlabeled learning. Instead of negative sampling or inverse-propensity weighting, it constructs a surrogate risk from observed positives and unlabeled pairs. A correction term subtracts the risk of incorrectly treating positives as negatives, making the estimator unbiased with respect to the ideal positive-negative risk when the positive class prior is known.

The unknown class prior is estimated with Progressive Proximal Transport (PPT). PPT compares positive and unlabeled embeddings through a sequence of partial optimal-transport problems with different mass weights. Large weights allow the labeled positives to match only a small, nearby subset of the unlabeled distribution; as the weight decreases, matching eventually includes negative samples and sharply raises transport cost. The weight minimizing an augmented transport cost determines the estimated positive proportion. During each mini-batch, WeaklyRec estimates this prior, evaluates a non-negative version of the weakly supervised risk, and updates the underlying recommender. The paper proves unbiasedness and consistency properties, derives estimation-error bounds, and shows that more unlabeled data can reduce variance under stated assumptions.

Experiments use matrix factorization on Yahoo! R3, Coat, and KuaiRec, with chronological 80/10/10 splits and unbiased or explicit-negative test data. Across NDCG@1/3/5 and Recall@1/3/5, WeaklyRec achieves the best result on most dataset-metric combinations; all results are averaged over five runs, and many gains over the strongest baseline are statistically significant. On Yahoo! R3, for example, NDCG@5 increases from 0.829 for UPL to 0.843, while Recall@5 rises from 0.346 to 0.354. Ablations show that accurate class-prior estimation is important and that performance generally improves as more unlabeled data is used. The main caveats are the repeated optimal-transport computation during training, sensitivity to candidate mass weights and mini-batch representations, and evaluation centered on ID-based matrix factorization rather than content-rich or modern deep recommenders.

## 繁中摘要

Implicit-feedback recommender 通常只能觀察到 click、view 等正向行為，卻沒有可靠的負標籤。若把所有未互動的 user-item pair 都當成負樣本，便會誤判使用者其實喜歡、但從未看過的物品。本文提出 model-agnostic framework WeaklyRec，把 implicit recommendation 改寫成 positive-unlabeled learning 問題。它不使用 negative sampling 或 inverse-propensity weighting，而是直接從觀測到的 positives 與 unlabeled pairs 建立 surrogate risk；其中的修正項會扣除「把正樣本誤當負樣本」造成的風險，因此在已知 positive class prior 時，可對理想的正負樣本風險提供 unbiased estimator。

未知的 class prior 由 Progressive Proximal Transport（PPT）估計。PPT 以多個不同 mass weight 的 partial optimal-transport problems，比對正樣本與 unlabeled embeddings。較大的 weight 只允許正樣本匹配 unlabeled distribution 中距離較近的小部分；weight 逐步下降後，matching 最終會被迫納入負樣本，使 transport cost 明顯上升。方法以 augmented transport cost 最小的 weight 推算 unlabeled data 中的正樣本比例。每個 mini-batch 中，WeaklyRec 都會估計 prior、計算加上 non-negative constraint 的 weakly supervised risk，再更新底層 recommender。論文也提供 unbiasedness、consistency、estimation-error bound 等理論分析，並指出在其假設下，增加 unlabeled data 可降低估計變異。

實驗以 matrix factorization 為主要模型，在 Yahoo! R3、Coat、KuaiRec 上採 chronological 80/10/10 split，並使用 unbiased 或含明確負回饋的 test data。以 NDCG@1/3/5 與 Recall@1/3/5 評估時，WeaklyRec 在大多數資料集與指標組合中取得最佳結果；所有數字為五次實驗平均，且許多相對最強 baseline 的提升具有統計顯著性。例如 Yahoo! R3 的 NDCG@5 從 UPL 的 0.829 提升到 0.843，Recall@5 則從 0.346 提升到 0.354。分析也顯示 class-prior estimation 的準確度很重要，且使用更多 unlabeled data 通常能改善結果。主要限制包括訓練期間需反覆求解 optimal transport、結果可能受 candidate mass weights 與 mini-batch representations 影響，以及實驗集中在 ID-based matrix factorization，尚未充分驗證 content-rich 或現代 deep recommender。

## Notes

- Code: https://github.com/HowardZJU/weakrec
- The paper reports mean and standard deviation over five runs and uses paired-sample significance tests.
- WeaklyRec avoids requiring observed negatives, but its unbiasedness still depends on estimating the positive class prior accurately.
