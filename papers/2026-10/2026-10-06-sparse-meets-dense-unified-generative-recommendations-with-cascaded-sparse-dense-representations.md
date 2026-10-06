---
date: 2026-10-06
title: "Sparse Meets Dense: Unified Generative Recommendations with Cascaded Sparse-Dense Representations"
authors: "Yuhao Yang, Zhi Ji, Zhaopeng Li, Yi Li, Zhonglin Mo, Yue Ding, Kai Chen, Zijian Zhang, Jie Li, Shuanglong Li, Lin Liu"
venue: "NeurIPS 2025"
---

# Sparse Meets Dense: Unified Generative Recommendations with Cascaded Sparse-Dense Representations

- Paper page: https://proceedings.neurips.cc/paper_files/paper/2025/hash/86ba836d4c5dd859d795a172911745e2-Abstract-Conference.html
- PDF: https://proceedings.neurips.cc/paper_files/paper/2025/file/86ba836d4c5dd859d795a172911745e2-Paper-Conference.pdf
- Local PDF: [../../pdfs/2026-10/2026-10-06-sparse-meets-dense-unified-generative-recommendations-with-cascaded-sparse-dense-representations.pdf](../../pdfs/2026-10/2026-10-06-sparse-meets-dense-unified-generative-recommendations-with-cascaded-sparse-dense-representations.pdf)
- Venue: NeurIPS 2025

## English Summary

This paper addresses an information bottleneck in generative recommendation. Systems such as TIGER represent each item with a short sequence of discrete semantic IDs and autoregressively generate the next item's IDs. These IDs make retrieval efficient and preserve coarse semantic structure, but quantization discards fine-grained item information. COBRA instead assigns every item a cascaded representation consisting of a sparse semantic ID followed by a trainable dense vector, so the model can first identify a semantic region and then refine the prediction within that region.

The sparse IDs are produced by a residual-quantization VAE over item text, while a Transformer text encoder generates dense item vectors. A unified Transformer decoder models the joint probability as `P(ID | history) P(vector | ID, history)`: it generates the hierarchical sparse ID first and then predicts the dense vector conditioned on that ID. Training combines cross-entropy loss for sparse-ID generation with an in-batch contrastive cosine loss for dense-vector prediction. Because the dense encoder is trained end to end with the sequential objective, its representation can adapt to recommendation behavior instead of remaining fixed after a separate quantization stage.

At inference time, beam search produces multiple candidate sparse IDs. For each beam, the predicted dense vector retrieves nearest neighbors restricted to the corresponding sparse-ID region. BeamFusion then combines the autoregressive beam score with dense-vector similarity and selects the final top-K items. This coarse-to-fine procedure uses the sparse branch for structured search and the dense branch for item-level discrimination, while its fusion weight provides an explicit accuracy-diversity control.

On three 5-core Amazon subsets, COBRA outperforms all reported baselines, including TIGER. Its Recall@10 is 0.0725 on Beauty, 0.0434 on Sports, and 0.0781 on Toys, compared with TIGER's 0.0648, 0.0400, and 0.0712. Ablations consistently degrade when sparse IDs, dense vectors, or BeamFusion are removed. On a private dataset with 5 million users and 2 million advertisements, COBRA reaches Recall@800 of 0.4466; an online A/B test covering 10% of traffic reports a 3.60% conversion lift and a 4.15% ARPU lift. The strongest practical evidence is therefore proprietary, limiting independent verification, and the paper identifies generative inference efficiency and scalability as remaining work. The extra dense prediction, approximate-nearest-neighbor retrieval, and beam fusion also add serving complexity beyond sparse-only generation.

## 繁中摘要

這篇論文處理 generative recommendation 的資訊瓶頸。TIGER 等系統會用一小段離散 semantic IDs 表示每個 item，再 autoregressively 產生下一個 item 的 IDs。這種表示有利於高效率 retrieval，也能保留粗粒度的語意結構，但 quantization 會丟失細緻的 item 資訊。COBRA 改為替每個 item 建立 cascaded representation：先放 sparse semantic ID，再接 trainable dense vector，讓模型先定位語意區域，再於區域內細化預測。

Sparse IDs 由針對 item text 訓練的 residual-quantization VAE 產生，dense item vectors 則來自 Transformer text encoder。統一的 Transformer decoder 將聯合機率分解為 `P(ID | history) P(vector | ID, history)`，先產生階層式 sparse ID，再以該 ID 為條件預測 dense vector。訓練時，sparse-ID generation 使用 cross-entropy loss，dense-vector prediction 使用 in-batch contrastive cosine loss。由於 dense encoder 會跟 sequential objective 一起 end-to-end 訓練，其表示能根據推薦行為調整，而不是在獨立量化階段完成後就固定不變。

Inference 時，beam search 先產生多個候選 sparse IDs；每個 beam 再使用預測的 dense vector，在對應 sparse-ID 區域內找 nearest neighbors。BeamFusion 將 autoregressive beam score 與 dense-vector similarity 結合，選出最終 top-K items。這套 coarse-to-fine 流程利用 sparse branch 進行結構化搜尋、dense branch 區分細粒度 items，並可透過 fusion weight 明確調整 accuracy 與 diversity 的取捨。

在三個經過 5-core filtering 的 Amazon 子資料集上，COBRA 全面優於論文列出的 baselines，包括 TIGER。Beauty、Sports、Toys 的 Recall@10 分別為 0.0725、0.0434、0.0781，TIGER 則為 0.0648、0.0400、0.0712；移除 sparse IDs、dense vectors 或 BeamFusion 的 ablation 也都會退步。在包含 500 萬使用者與 200 萬則廣告的私有資料上，COBRA 的 Recall@800 達 0.4466；涵蓋 10% 流量的線上 A/B test 回報 conversion 提升 3.60%、ARPU 提升 4.15%。不過最有力的實務證據來自 proprietary data，外界難以獨立驗證；論文也把 generative inference 的效率與 scalability 列為後續工作。此外，dense prediction、approximate-nearest-neighbor retrieval 與 beam fusion 會比 sparse-only generation 增加 serving complexity。

## Notes

- Public evaluation uses Amazon Beauty, Sports and Outdoors, and Toys and Games with leave-one-out chronological evaluation.
- The industrial training split covers 60 days, and the immediately following day is used for testing.
- At the reported operating point, changing the BeamFusion weight from `1.0` to `0.9` improves recall by 0.12% and diversity by 18.80% relative to the reference setting.
- The implementation uses sequence packing, FlashAttention, and encoder caching; the paper reports deployment to a platform serving more than 200 million daily users.
