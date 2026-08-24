---
date: 2026-08-24
title: "On the Embedding Collapse when Scaling up Recommendation Models"
authors: "Xingzhuo Guo, Junwei Pan, Ximei Wang, Baixu Chen, Jie Jiang, Mingsheng Long"
venue: "ICML 2024"
---

# On the Embedding Collapse when Scaling up Recommendation Models

- Paper page: https://proceedings.mlr.press/v235/guo24e.html
- PDF: https://raw.githubusercontent.com/mlresearch/v235/main/assets/guo24e/guo24e.pdf
- Local PDF: [../../pdfs/2026-08/2026-08-24-on-the-embedding-collapse-when-scaling-up-recommendation-models.pdf](../../pdfs/2026-08/2026-08-24-on-the-embedding-collapse-when-scaling-up-recommendation-models.pdf)
- Venue: ICML 2024

## English Summary

This paper studies why simply making recommendation models larger often fails to improve performance. The authors identify embedding collapse as a key scalability bottleneck: learned embedding tables tend to occupy a low-dimensional subspace, so increasing embedding size does not translate into richer representations. They quantify this with spectral analysis and an information-abundance measure based on singular values.

The main technical insight is that feature interaction has a two-sided effect. Interacting with already-collapsed embeddings can further constrain other embeddings and worsen collapse, but feature interaction is also necessary because it encodes higher-order recommendation signals and helps reduce overfitting. This means that removing or heavily suppressing interaction can make embeddings less collapsed but still fail to scale because the model loses useful inductive bias.

Based on this analysis, the paper proposes multi-embedding: instead of only increasing one embedding table's dimension, the model uses multiple independent embedding sets, each with its own interaction module, and combines their outputs. This lets different embedding sets learn more diverse interaction patterns while preserving the recommendation-specific feature interaction structure. Experiments on Criteo and Avazu across several models, including DNN, IPNN, NFwFM, xDeepFM, DCNv2, and FinalMLP, show more consistent gains when scaling to larger models and stronger mitigation of embedding collapse.

## 繁中 Summary

這篇論文討論推薦模型為什麼不能像 foundation model 一樣，單純放大參數就穩定提升效果。作者指出主要瓶頸之一是 embedding collapse：推薦模型學到的 embedding table 往往只佔據低維子空間，因此把 embedding size 加大，並不一定會學到更豐富的表示。論文用 singular value 的光譜分析，並提出 information abundance 來量化 collapse 程度。

核心觀察是 feature interaction 對 scalability 有雙面效果。一方面，當某些 field 的 embedding 已經 collapse，和它互動會限制其他 embedding 的學習，進一步造成 collapse；另一方面，feature interaction 本身又是推薦模型捕捉高階特徵關係的重要 inductive bias，也能降低放大模型後的 overfitting。因此，直接移除或過度限制 interaction 雖然可能讓 embedding 看起來比較不 collapse，但模型仍然不一定能 scale。

基於這個分析，作者提出 multi-embedding 設計：不要只把單一 embedding table 的維度加大，而是建立多組獨立 embedding，每組搭配自己的 interaction module，最後再整合輸出。這樣可以讓不同 embedding set 學到更多樣的 interaction pattern，同時保留推薦模型需要的 feature interaction 結構。在 Criteo 和 Avazu 上，針對 DNN、IPNN、NFwFM、xDeepFM、DCNv2、FinalMLP 等模型的實驗顯示，multi-embedding 在放大模型時有更穩定的 AUC 提升，也更有效緩解 embedding collapse。

## Notes

- This paper is relevant for large-scale recommendation model design, especially when increasing embedding dimension gives weak or negative returns.
- The paper's diagnosis is architectural: scalability is blocked by how feature embeddings interact, not only by data size or optimization.
- Multi-embedding is attractive because it can be applied to multiple existing recommendation architectures without replacing the whole model.
