---
date: 2026-10-12
title: "Negative Feedback Really Matters: Signed Dual-Channel Graph Contrastive Learning Framework for Recommendation"
authors: "Leqi Zheng, Chaokun Wang, Zixin Song, Cheng Wu, Shannan Yan, Jiajun Zhang, Ziyang Liu"
venue: "NeurIPS 2025"
---

# Negative Feedback Really Matters: Signed Dual-Channel Graph Contrastive Learning Framework for Recommendation

- Paper page: https://papers.nips.cc/paper_files/paper/2025/hash/9a92ea37efa0d290bd7015558166c056-Abstract-Conference.html
- PDF: https://papers.nips.cc/paper_files/paper/2025/file/9a92ea37efa0d290bd7015558166c056-Paper-Conference.pdf
- Local PDF: [../../pdfs/2026-10/2026-10-12-negative-feedback-really-matters-signed-dual-channel-graph-contrastive-learning-framework-for-recommendation.pdf](../../pdfs/2026-10/2026-10-12-negative-feedback-really-matters-signed-dual-channel-graph-contrastive-learning-framework-for-recommendation.pdf)
- Venue: NeurIPS 2025

## English Summary

This paper argues that explicit negative feedback should be modeled as a first-class structural signal rather than discarded or used only for sampling. Signed Dual-Channel Graph Contrastive Learning (SDCGCL) is a model-agnostic framework that splits user-item interactions into positive and negative graphs and propagates them in separate embedding spaces. It can wrap graph contrastive recommenders such as SGL, LightGCL, and XSimGCL, while the authors also introduce DualFuse, a purpose-built implementation designed to use both channels efficiently.

SDCGCL has three main mechanisms. Dual-channel graph embedding applies the selected GNN and augmentation independently to each signed graph. Cross-channel distribution calibration combines channel-specific contrastive objectives with an alignment loss over normalized user- and item-centric interaction patterns; the intent is to preserve distinct positive and negative semantics without letting the higher variance of negative feedback destabilize prediction. The final score adaptively adds the positive-channel affinity and subtracts a weighted negative-channel affinity. DualFuse further creates each channel's contrastive view with a normalized perturbation derived from the opposite channel, enabling structured information exchange instead of independent processing.

Training combines BPR recommendation loss, contrastive loss, distribution alignment, and L2 regularization. A full-graph warm-up first learns the complete signed structure; later epochs replace the full negative graph with a popularity-guided random-walk sample. On ML-1M, a 1% negative-graph sampling rate gives the best Recall@20/NDCG@20 of 0.3282/0.3693 and reduces total training time from 28.9 to 20.8 minutes relative to full-graph training. Sampling too aggressively at 0.1% sharply degrades accuracy and fails to converge within 50 epochs, illustrating the efficiency-quality boundary.

Experiments use ML-1M, ML-10M, Yelp, and Amazon with a 7:1:2 split and compare against 22 unsigned and sign-aware baselines. DualFuse is best on every reported Recall@20 and NDCG@20 metric, with statistically significant gains (`p < 0.01`); against the strongest sign-aware baseline, Recall improves by 6.11% on ML-1M, 28.01% on Yelp, 18.13% on Amazon, and 11.75% on ML-10M. Ablations show that cross-channel fusion is the largest architectural contributor, while supervised recommendation loss remains essential. Important caveats are that all ratings below four are treated as negative, conflating neutral and disliked items; evaluation uses explicit-rating public datasets rather than implicit production feedback; and industrial scale, temporal preference evolution, and extreme cold-start settings remain untested.

## 繁中摘要

這篇論文主張，明確的 negative feedback 應被視為第一級的結構訊號，而不是直接丟棄或只拿來 sampling。Signed Dual-Channel Graph Contrastive Learning（SDCGCL）是一個 model-agnostic framework，將 user-item interactions 分成 positive graph 與 negative graph，並在兩個獨立 embedding spaces 中傳播。它可以包裝 SGL、LightGCL、XSimGCL 等 graph contrastive recommenders；作者也提出專門搭配此 framework 的 DualFuse，以更有效率地利用兩個 channels。

SDCGCL 有三個主要機制。Dual-channel graph embedding 對兩張 signed graphs 分別套用選定的 GNN 與 augmentation。Cross-channel distribution calibration 結合各 channel 的 contrastive objective，以及針對正規化 user-centric、item-centric interaction patterns 的 alignment loss；目標是在保留正負訊號差異的同時，避免 variance 較高的 negative feedback 讓預測不穩定。最終分數會加入 positive-channel affinity，再減去加權的 negative-channel affinity。DualFuse 進一步用另一個 channel 的 normalized embedding 形成結構化 perturbation，建立 contrastive view，使兩個 channels 能交換資訊，而不是完全獨立處理。

訓練目標包含 BPR recommendation loss、contrastive loss、distribution alignment 與 L2 regularization。模型先用完整 signed graph warm-up，學習整體結構；後續 epochs 則以 popularity-guided random walk 取樣 negative graph。在 ML-1M 上，1% negative-graph sampling rate 得到最佳 Recall@20/NDCG@20 0.3282/0.3693，並把相對於 full-graph training 的總訓練時間從 28.9 分鐘降至 20.8 分鐘。若過度取樣到 0.1%，準確率會明顯下降，50 epochs 內也無法收斂，顯示效率與品質之間存在明確邊界。

實驗使用 ML-1M、ML-10M、Yelp、Amazon，採 7:1:2 split，並與 22 個 unsigned 與 sign-aware baselines 比較。DualFuse 在所有回報的 Recall@20、NDCG@20 都最佳，提升具統計顯著性（`p < 0.01`）；相較最強 sign-aware baseline，Recall 在 ML-1M、Yelp、Amazon、ML-10M 分別提升 6.11%、28.01%、18.13%、11.75%。Ablation 顯示 cross-channel fusion 是貢獻最大的架構元件，而 supervised recommendation loss 仍不可或缺。主要限制是把所有低於四分的評分都視為 negative，因而混合中立與真正不喜歡的 items；評估只使用 explicit-rating public datasets，沒有測試 production implicit feedback；工業規模、偏好隨時間演化與極端 cold-start 也尚未驗證。

## Notes

- Official code and processed data: https://github.com/LQgdwind/nips25-sdcgcl
- The four datasets contain 6,040-69,878 users, 3,706-38,121 items, and 1.0-10.0 million interactions.
- Experiments use 64-dimensional embeddings, Adam with learning rate `1e-3`, batch size 2,048, and eight RTX 3090 GPUs.
- Under 20% randomly corrupted interactions, DualFuse retains 81.3% of its MovieLens performance and 76.7% of its Amazon performance.
