---
date: 2026-11-09
title: "Efficient Knowledge Transfer in Federated Recommendation for Joint Venture Ecosystem"
authors: "Yichen Li, Yijing Shan, Yi Liu, Haozhao Wang, Cheng Wang, Wei Wang, Yi Wang, Ruixuan Li"
venue: "NeurIPS 2025"
---

# Efficient Knowledge Transfer in Federated Recommendation for Joint Venture Ecosystem

- Paper page: https://proceedings.neurips.cc/paper_files/paper/2025/hash/b4f9b809750373d111728b8a5f649ece-Abstract-Conference.html
- PDF: https://proceedings.neurips.cc/paper_files/paper/2025/file/b4f9b809750373d111728b8a5f649ece-Paper-Conference.pdf
- Local PDF: [../../pdfs/2026-11/2026-11-09-efficient-knowledge-transfer-in-federated-recommendation-for-joint-venture-ecosystem.pdf](../../pdfs/2026-11/2026-11-09-efficient-knowledge-transfer-in-federated-recommendation-for-joint-venture-ecosystem.pdf)
- Venue: NeurIPS 2025

## English Summary

This paper studies federated recommendation in a joint-venture ecosystem, where each client is a subsidiary or business group rather than an individual device. Clients own large, partially overlapping user and item sets, so communicating only item embeddings may leave useful cross-client user knowledge unused. Directly sharing user embeddings, however, exposes private information. The proposed FR-JVE framework targets this cross-silo setting and aims to transfer user-related knowledge without uploading raw user data or user embeddings.

Before federated training, every client transforms one-hot user and item identifiers with random initialization and softmax, then applies model inversion locally to distill a per-user rating preference while freezing user gradients. This rating preference is a weighted combination of local item embeddings and acts as a privacy-oriented matching signal. The fixed preferences are aggregated once by the server. During regular federated training, clients communicate only item embeddings through FedAvg, while a local bridge function maps other clients' aggregated preferences into the local preference space. At inference, each client searches for top-k users with similar transferred preferences and averages their embedding-based predictions.

Experiments cover rating prediction on MovieLens-100K and MovieLens-1M and top-k recommendation on LastFM-2K and QB-article. FR-JVE achieves the best reported results across the main tables. On MovieLens-100K, it obtains MAE 1.1765 and RMSE 1.4725, compared with 1.2503 and 1.6465 for PFedRec. On LastFM-2K, it reaches HR@10 0.6578 and NDCG@10 0.4684, versus 0.6010 and 0.4358 for FedRAP. Removing rating preferences degrades MovieLens-100K MAE to 2.9596 and LastFM-2K HR@10 to 0.5416. The model also reaches its strongest results in fewer than 20 communication rounds and incurs only a small additional top-k search cost.

The paper contrasts FR-JVE with local differential privacy on user embeddings, showing a steep utility loss under strict privacy budgets. Its formal privacy argument relies on frozen gradients and randomly transformed user representations making reconstruction difficult. This is narrower than a standard end-to-end differential privacy guarantee, and the paper does not empirically evaluate adaptive attacks against released rating preferences. The NeurIPS checklist explicitly states that limitations are not discussed. Other practical constraints include experiments on simulated client partitions of public datasets, a focus on few-client cross-silo settings, and the need for natural overlap among users or items. The linear bridge may also be insufficient for more complex real-world distributions.

## 繁中摘要

這篇論文研究 joint-venture ecosystem 中的 federated recommendation。此處每個 client 不是個人裝置，而是擁有大量資料的子公司或 business group，彼此的 user set 與 item set 只有部分重疊。若只交換 item embeddings，可能無法充分利用跨 client 的 user knowledge；但直接分享 user embeddings 又會暴露隱私。作者提出 FR-JVE，針對這類 cross-silo 場景，在不上傳 raw user data 或 user embeddings 的前提下轉移與使用者相關的知識。

在 federated training 前，每個 client 先以隨機初始化與 softmax 轉換 one-hot user/item identifiers，再於本地使用 model inversion 蒸餾每位使用者的 rating preference，同時凍結 user gradients。Rating preference 是 local item embeddings 的加權組合，作為較隱私友善的 user-matching signal；固定後只需由 server 聚合一次。正式訓練期間，client 僅透過 FedAvg 傳遞 item embeddings，並在本地訓練 bridge function，把其他 clients 的 aggregated preferences 對齊到自己的 preference space。推論時，系統依 transferred preferences 找出 top-k 相似使用者，再平均其 embedding-based predictions。

實驗涵蓋 MovieLens-100K、MovieLens-1M 的 rating prediction，以及 LastFM-2K、QB-article 的 top-k recommendation。FR-JVE 在主要表格中全面取得最佳結果。MovieLens-100K 的 MAE/RMSE 為 1.1765/1.4725，優於 PFedRec 的 1.2503/1.6465；LastFM-2K 的 HR@10/NDCG@10 為 0.6578/0.4684，優於 FedRAP 的 0.6010/0.4358。移除 rating preference 後，MovieLens-100K MAE 惡化至 2.9596，LastFM-2K HR@10 降至 0.5416。模型也在不到 20 個 communication rounds 達到最佳表現，top-k 搜尋只增加少量推論成本。

論文將 FR-JVE 與套用在 user embeddings 的 local differential privacy 比較，顯示嚴格 privacy budget 會明顯損害效用。其 formal privacy argument 主要依賴 frozen gradients 與隨機轉換的 user representations，使 reconstruction 變得困難；這比標準 end-to-end differential privacy guarantee 更窄，且未實驗評估針對 released rating preferences 的 adaptive attacks。NeurIPS checklist 也明確註記作者未討論方法限制。其他實務限制包括：只在公開資料集的 simulated client partitions 上測試、主要適用於少量 clients 的 cross-silo 場景，以及需要 user/item 之間存在自然重疊；簡單 linear bridge 在更複雜的真實分布中也可能不足。

## Notes

- The evaluation simulates partial overlap and heterogeneous client data with a Dirichlet distribution.
- FR-JVE is designed as a lightweight add-on and is also evaluated with FedNCF and PFedRec backbones.
- Adding differential privacy to rating preferences slightly lowers utility in the reported settings, but no attack-based privacy benchmark is provided.
- The paper releases no new dataset, model, or code asset.
