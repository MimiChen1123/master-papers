---
date: 2026-09-09
title: "PSL: Rethinking and Improving Softmax Loss from Pairwise Perspective for Recommendation"
authors: "Weiqin Yang, Jiawei Chen, Xin Xin, Sheng Zhou, Binbin Hu, Yan Feng, Chun Chen, Can Wang"
venue: "NeurIPS 2024"
---

# PSL: Rethinking and Improving Softmax Loss from Pairwise Perspective for Recommendation

- Paper page: https://proceedings.neurips.cc/paper_files/paper/2024/hash/db1d5c63576587fc1d40d33a75190c71-Abstract-Conference.html
- PDF: https://proceedings.neurips.cc/paper_files/paper/2024/file/db1d5c63576587fc1d40d33a75190c71-Paper-Conference.pdf
- Local PDF: [../../pdfs/2026-09/2026-09-09-psl-rethinking-and-improving-softmax-loss-from-pairwise-perspective-for-recommendation.pdf](../../pdfs/2026-09/2026-09-09-psl-rethinking-and-improving-softmax-loss-from-pairwise-perspective-for-recommendation.pdf)
- Venue: NeurIPS 2024

## English Summary

This paper revisits Softmax Loss for recommender systems from a pairwise ranking perspective. Softmax Loss is effective and widely used, but the authors identify two weaknesses: its connection to ranking metrics such as DCG is not tight enough, and its exponential weighting makes it overly sensitive to false negatives. In implicit-feedback recommendation, many unobserved items are not truly negative, so giving very high weight to hard negatives can destabilize training.

The paper proposes Pairwise Softmax Loss (PSL), a family of losses that reformulates Softmax Loss over positive-negative score gaps and replaces the exponential function with alternative activation functions such as Tanh, Atan, or ReLU. This small mathematical change gives PSL three advantages: it can be a tighter surrogate for DCG, it offers better control over the weight distribution of training pairs, and it can be interpreted as a Distributionally Robust Optimization enhancement of BPR.

Experiments cover IID, out-of-distribution, and false-negative noise settings across real recommendation datasets. PSL variants consistently outperform Softmax Loss and other baseline losses in recommendation accuracy, OOD robustness, and noise resistance. The key practical takeaway is that the activation inside a softmax-style recommendation loss is not a minor implementation detail; it controls how aggressively the model emphasizes hard negatives and therefore affects robustness.

## 繁中摘要

這篇論文從 pairwise ranking 的角度重新分析推薦系統常用的 Softmax Loss。Softmax Loss 雖然有效，但作者指出兩個問題：第一，它和 DCG 等 ranking metric 的關係不夠緊；第二，exponential weighting 會讓模型對 false negative 過度敏感。在 implicit feedback 推薦中，未互動 item 不一定代表使用者不喜歡，因此如果 hard negative 被給太大權重，訓練方向可能被噪音帶偏。

作者提出 Pairwise Softmax Loss (PSL)，把 Softmax Loss 改寫成 positive-negative score gap 上的 pairwise loss，並用 Tanh、Atan、ReLU 等 activation 取代 exponential function。這個改動不大，但帶來三個理論優點：可以更貼近 DCG surrogate、可以控制 training pair 的權重分布、也可以解釋成 BPR loss 上的 Distributionally Robust Optimization。

實驗涵蓋 IID、out-of-distribution 與 false-negative noise 三種設定。結果顯示 PSL variants 在推薦準確率、OOD robustness、noise resistance 上都優於 Softmax Loss 與其他 baseline loss。實務上的重點是：softmax-style loss 裡的 activation 不是小細節，它決定模型多大程度強調 hard negative，進而影響推薦模型的穩健性。

## Notes

- Useful for training implicit-feedback recommenders with many unobserved-but-possibly-positive items.
- PSL is attractive because it changes the loss without requiring a new model architecture.
- The paper is especially relevant if Softmax Loss is unstable under popularity shift or noisy negatives.
