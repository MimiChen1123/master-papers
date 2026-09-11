---
date: 2026-09-11
title: "Graph-enhanced Optimizers for Structure-aware Recommendation Embedding Evolution"
authors: "Cong Xu, Jun Wang, Jianyong Wang, Wei Zhang"
venue: "NeurIPS 2024"
---

# Graph-enhanced Optimizers for Structure-aware Recommendation Embedding Evolution

- Paper page: https://proceedings.neurips.cc/paper_files/paper/2024/hash/938ac7bb9a997b60b6be0348c486aaef-Abstract-Conference.html
- PDF: https://proceedings.neurips.cc/paper_files/paper/2024/file/938ac7bb9a997b60b6be0348c486aaef-Paper-Conference.pdf
- Local PDF: [../../pdfs/2026-09/2026-09-11-graph-enhanced-optimizers-for-structure-aware-recommendation-embedding-evolution.pdf](../../pdfs/2026-09/2026-09-11-graph-enhanced-optimizers-for-structure-aware-recommendation-embedding-evolution.pdf)
- Venue: NeurIPS 2024

## English Summary

This paper proposes Structure-aware Embedding Evolution (SEvo), a graph-enhanced embedding update mechanism for recommender systems. Modern recommenders depend heavily on entity embeddings, and related items or users should evolve similarly during training. Graph neural networks can inject structural information, but they often add model-specific architecture, training cost, and inference overhead. SEvo instead modifies the optimizer update itself.

SEvo applies graph regularization to the embedding variation at each update step, encouraging related nodes to move in similar directions while preserving convergence. Because the method transforms the update rather than adding a GNN inference module, it can be integrated into optimizers such as SGD, Adam, and especially AdamW. The paper further corrects moment estimates for SEvo-enhanced AdamW to handle sparse recommendation gradients more robustly.

Experiments across six public datasets and multiple recommendation backbones show consistent gains. The paper reports average relative improvements of 9% to 23% across models, and larger gains on large-scale datasets with millions of nodes. A key systems advantage is that SEvo does not change inference logic, so inference time remains the same while training overhead is small. The broader lesson is that graph structure can be used at the optimizer level, not only through explicit GNN layers.

## 繁中摘要

這篇論文提出 Structure-aware Embedding Evolution (SEvo)，一種推薦系統用的 graph-enhanced embedding 更新機制。現代推薦模型高度依賴 user/item embedding，而有關聯的節點在訓練過程中應該有相似的演化方向。GNN 可以引入圖結構資訊，但通常需要額外架構設計，也會增加訓練與 inference 成本。SEvo 的做法不同：它直接改 optimizer 的 embedding update。

SEvo 在每次更新 embedding variation 時加入 graph regularization，鼓勵相關節點往相似方向移動，同時保留收斂性。因為它改的是 update step，而不是新增 GNN inference module，所以可以整合到 SGD、Adam、AdamW 等 optimizer，尤其和 AdamW 相容。作者也針對推薦任務常見的 sparse gradient，對 SEvo-enhanced AdamW 的 moment estimate 做修正，讓訓練更穩健。

實驗涵蓋六個公開資料集與多個推薦 backbone，結果顯示 SEvo 帶來穩定提升。論文報告在不同模型上有 9% 到 23% 的平均相對提升，在百萬節點級別資料集上提升更明顯。系統面最大的好處是 SEvo 不改 inference logic，因此 inference time 維持不變，訓練額外成本也很小。這篇的重點是：圖結構資訊不一定只能透過 GNN layer 使用，也可以放進 optimizer update。

## Notes

- Useful for recommender systems that need graph structure without adding GNN inference latency.
- SEvo is an optimizer-level technique, so it may compose with existing model architectures.
- The method is particularly interesting for large-scale systems where inference overhead matters.
