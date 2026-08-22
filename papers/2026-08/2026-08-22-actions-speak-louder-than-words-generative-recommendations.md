---
date: 2026-08-22
title: "Actions Speak Louder than Words: Trillion-Parameter Sequential Transducers for Generative Recommendations"
authors: "Jiaqi Zhai, Lucy Liao, Xing Liu, Yueming Wang, Rui Li, Xuan Cao, Leon Gao, Zhaojie Gong, Fangda Gu, Jiayuan He, Yinghai Lu, Yu Shi"
venue: "ICML 2024"
---

# Actions Speak Louder than Words: Trillion-Parameter Sequential Transducers for Generative Recommendations

- Paper page: https://proceedings.mlr.press/v235/zhai24a.html
- PDF: ../../pdfs/2026-08/2026-08-22-actions-speak-louder-than-words-generative-recommendations.pdf
- Venue: ICML 2024
- Code: https://github.com/facebookresearch/generative-recommenders

## English Summary

This paper proposes Generative Recommenders (GRs), a large-scale recommendation paradigm that treats user actions as a sequential modality and reformulates ranking and retrieval as sequential transduction tasks. Instead of relying on conventional Deep Learning Recommendation Models (DLRMs) with many handcrafted heterogeneous features, the paper sequentializes categorical features, removes many dense aggregate features when they can be recovered from action history, and trains models generatively over user behavior sequences. The motivation is that industrial recommenders process enormous volumes of user actions, yet traditional DLRMs often fail to scale with additional compute the way language or vision foundation models do.

The central architecture is HSTU, or Hierarchical Sequential Transduction Units, designed for high-cardinality, non-stationary recommendation data. HSTU modifies the attention stack to reduce training and inference cost while preserving quality, and the paper further introduces serving techniques such as M-FALCON to amortize inference computation. Across synthetic, public, and industrial datasets, HSTU improves recommendation quality and scales better than Transformer or DLRM baselines. The paper reports up to 65.8% improvement in NDCG on public datasets, 5.3x to 15.2x speedups over FlashAttention2-based Transformers on long sequences, and 12.4% online A/B test gains from deployed HSTU-based GR models with up to 1.5 trillion parameters. The most important takeaway is that recommendation quality can follow a power-law scaling trend with training compute when the system is formulated as a generative sequential model.

## 繁中摘要

這篇論文提出 Generative Recommenders (GRs)，把推薦系統中的 ranking 和 retrieval 重新表述成 sequential transduction，也就是根據使用者過去的行為序列來生成或預測後續推薦目標。傳統工業推薦模型 DLRM 通常依賴大量人工設計的 heterogeneous features，例如各種 categorical IDs、counter、ratio 和 cross features；但作者認為這些設計在大規模資料和算力增加時不容易展現類似語言模型的 scaling law。因此他們將使用者行為視為一種新的序列模態，盡量把推薦問題統一到序列生成框架中。

方法上，論文提出 HSTU，也就是 Hierarchical Sequential Transduction Units，專門針對高基數、動態 vocabulary、非平穩 streaming recommendation data 設計。HSTU 透過調整 attention 和計算結構降低長序列建模成本，同時保留推薦品質；搭配 M-FALCON 等推論服務方法，可以在相同 serving budget 下支援遠比傳統 DLRM 複雜的模型。實驗顯示 HSTU 在公開資料集上最高提升 NDCG 65.8%，在 8192 長度序列上比 FlashAttention2-based Transformer 快 5.3x 到 15.2x；在工業線上 A/B 測試中，最高 1.5 兆參數的 GR 模型帶來 12.4% 指標提升。這篇的重點不只是提出新架構，而是展示推薦系統也可能像 LLM 一樣，透過合適的建模方式和架構設計隨訓練算力呈現 scaling law。

## Notes

- Main framing: recommendation is treated as a sequential transduction and generative modeling problem over user actions.
- Main architecture: HSTU replaces many DLRM feature interaction modules with a scalable sequential block.
- Efficiency: HSTU is designed to handle long sequences and high-cardinality streaming recommendation data.
- Industrial relevance: the paper reports deployed GR models with up to 1.5 trillion parameters and online A/B gains.
- Research relevance: this is a strong example of foundation-model-style scaling ideas moving into recommender systems.
