---
date: 2026-10-07
title: "Path-Enhanced Contrastive Learning for Recommendation"
authors: "Haoran Sun, Fei Xiong, Yuanzhe Hu, Liang Wang"
venue: "NeurIPS 2025"
---

# Path-Enhanced Contrastive Learning for Recommendation

- Paper page: https://proceedings.neurips.cc/paper_files/paper/2025/hash/7cb33a355bbe68305e02a080ad4eb86a-Abstract-Conference.html
- PDF: https://proceedings.neurips.cc/paper_files/paper/2025/file/7cb33a355bbe68305e02a080ad4eb86a-Paper-Conference.pdf
- Local PDF: [../../pdfs/2026-10/2026-10-07-path-enhanced-contrastive-learning-for-recommendation.pdf](../../pdfs/2026-10/2026-10-07-path-enhanced-contrastive-learning-for-recommendation.pdf)
- Venue: NeurIPS 2025

## English Summary

This paper argues that graph contrastive learning for collaborative filtering underuses the information carried by multi-hop interaction paths. Common graph augmentations align a node across perturbed graph views, but their contrastive objectives may treat other nodes on a meaningful user-item path as negatives and push their representations apart. Path-Enhanced Contrastive Learning (PECL) instead treats both nodes within sampled paths and entire related paths as positive evidence, aiming to extract stronger self-supervision from sparse interaction graphs.

PECL uses LightGCN as its recommendation backbone and adds two complementary objectives. The intra-path loss selects as positives the nodes that occur frequently in restart-based random walks from a target node, then applies an InfoNCE-style objective to attract those nodes and repel sampled negatives. The inter-path loss first constructs a timestamp-ordered center path, follows it deterministically for a configurable number of steps, and completes a positive path with a time-biased conditional random walk. Paths are encoded by combining node and temporal edge embeddings through Hermitian products, after which contrastive learning aligns the center path with related paths and separates unrelated ones.

The total objective combines BPR recommendation loss, intra-path contrast, inter-path contrast, and L2 regularization. The two contrastive losses serve different roles: intra-path learning reinforces local node coherence, while inter-path learning captures broader structural and temporal consistency. The appendix proposes gradient-norm balancing for the loss weights. Sampling bounds the additional cost, but inter-path learning remains the more expensive component because every sampled path must be encoded and contrasted; its stated complexity scales with the number and length of sampled paths, average node degree, and embedding dimension.

Experiments randomly split interactions 80/20 on ML-1M, Ciao, and an Amazon dataset and compare against nine baselines. PECL is best on every reported Recall@10/20 and NDCG@10/20 metric. For example, its ML-1M Recall@10/NDCG@10 are 0.1676/0.4206, versus 0.1601/0.4148 for the strongest competing entries; on Amazon, Recall@20 improves from 0.1764 to 0.1820. Removing inter-path contrast causes the largest ablation loss, reducing ML-1M Recall@10 by 27.4%, while removing intra-path contrast or replacing the proposed sampler with a standard random walk also hurts performance. The evidence should still be read cautiously: random interaction splits do not test strictly future-facing recommendation, the main table reports only five-run averages without variance or the p-values claimed in the checklist, and the study does not report wall-clock training or inference overhead against the baselines.

## 繁中摘要

這篇論文認為，現有用於 collaborative filtering 的 graph contrastive learning 沒有充分利用 multi-hop interaction paths 所包含的資訊。常見 graph augmentation 會讓同一節點在不同 perturbed graph views 中保持一致，但其 contrastive objective 可能把有意義 user-item path 上的其他節點當成 negatives，反而把表示推遠。Path-Enhanced Contrastive Learning（PECL）同時把 sampled path 內的節點與彼此相關的完整 paths 視為 positive evidence，希望從稀疏 interaction graph 中取得更強的 self-supervised signals。

PECL 以 LightGCN 作為推薦 backbone，再加入兩個互補 objectives。Intra-path loss 從 target node 執行 restart-based random walks，把多次出現在 paths 中的節點選為 positives，並以 InfoNCE-style objective 拉近這些節點、推離 sampled negatives。Inter-path loss 先根據 timestamp 建立依序排列的 center path，沿著它確定性地走若干步，再以具時間偏好的 conditional random walk 完成 positive path。模型透過 Hermitian products 結合 node embeddings 與 temporal edge embeddings 來編碼 paths，最後讓 center path 接近相關 paths、遠離不相關 paths。

總目標函數結合 BPR recommendation loss、intra-path contrast、inter-path contrast 與 L2 regularization。兩個 contrastive losses 的作用不同：intra-path learning 強化局部節點的一致性，inter-path learning 則捕捉較完整的結構與時間關係；附錄另提出以 gradient norm 平衡 loss weights。Sampling 能限制額外成本，但 inter-path learning 仍較昂貴，因為每條 sampled path 都必須被編碼與比較；論文所列 complexity 會隨 sampled paths 的數量與長度、平均 node degree 及 embedding dimension 增加。

實驗在 ML-1M、Ciao 與一個 Amazon dataset 上隨機切分 80% interactions 訓練、20% 測試，並與九個 baselines 比較。PECL 在所有回報的 Recall@10/20 與 NDCG@10/20 上都是最佳；例如 ML-1M 的 Recall@10/NDCG@10 為 0.1676/0.4206，各 baseline 最強值為 0.1601/0.4148；Amazon 的 Recall@20 則從 0.1764 提升至 0.1820。移除 inter-path contrast 的影響最大，使 ML-1M Recall@10 下降 27.4%；移除 intra-path contrast 或把 proposed sampler 換成 standard random walk 也會退步。不過這些證據仍需審慎解讀：random interaction split 沒有嚴格測試面向未來的推薦情境，主表只提供五次實驗平均值，未呈現 variance 或 checklist 所稱的 p-values，也沒有比較各 baseline 的實際訓練與推論時間成本。

## Notes

- Dataset sizes are 6,040 users/3,706 items for ML-1M, 101,998 users/5,441 items for Ciao, and 6,170 users/2,753 items for Amazon.
- The reported sparsity is 95.53% for ML-1M, 99.95% for Ciao, and 98.85% for Amazon.
- Experiments use an Intel Xeon Bronze 3204 CPU, one Tesla A100 GPU, and 256 GB of memory.
- Hyperparameter analysis reports the best ML-1M setting at positive-node threshold `alpha = 2`, deterministic traversal length `beta = 4`, and contrastive temperature `tau = 0.05`.
