---
date: 2026-10-15
title: "Improving LLMs for Recommendation with Out-Of-Vocabulary Tokens"
authors: "Ting-Ji Huang, Jia-Qi Yang, Chunxu Shen, Kai-Qi Liu, De-Chuan Zhan, Han-Jia Ye"
venue: "ICML 2025"
---

# Improving LLMs for Recommendation with Out-Of-Vocabulary Tokens

- Paper page: https://proceedings.mlr.press/v267/huang25ar.html
- PDF: https://raw.githubusercontent.com/mlresearch/v267/main/assets/huang25ar/huang25ar.pdf
- Local PDF: [../../pdfs/2026-10/2026-10-15-improving-llms-for-recommendation-with-out-of-vocabulary-tokens.pdf](../../pdfs/2026-10/2026-10-15-improving-llms-for-recommendation-with-out-of-vocabulary-tokens.pdf)
- Venue: ICML 2025

## English Summary

This paper studies how large language models should represent users and items for recommendation. Existing instruction-based recommenders often encode an item identifier such as 2024 with ordinary vocabulary tokens such as "20" and "24." Those tokens already carry meanings learned from natural-language pretraining, so unrelated identifiers can acquire similar representations and conflict with the collaborative structure in interaction data. Assigning a unique new token to every entity avoids that collision but scales poorly and leaves every embedding to be learned from scratch.

The proposed META ID framework constructs compact identifiers from out-of-vocabulary (OOV) tokens while preserving both memorization of user-item relationships and diversity among entities. It samples rating-aware user-item meta-paths from the interaction graph, trains a skip-gram model so users and items share one collaborative embedding space, and clusters those representations with K-Means. Each entity receives a coarse token for its cluster and a fine token based on its position within the cluster, plus a user/item type token. Similar users and items can therefore share coarse structure without losing unique identities.

To use META IDs in an LLM, the method expands the vocabulary and token-embedding table. A learned linear transformation, initialized from cluster centroids, augments the new token embeddings before normal language-model fine-tuning. The authors also define memorization and diversity scores for assessing identifier representations. Their analyses show that the sum of these two scores correlates positively with NDCG@10, while heatmaps, t-SNE plots, and attention visualizations indicate that META IDs better preserve collaborative similarity and entity distinctions than random, sequential, or collaborative ID baselines.

Experiments use the 2019 Amazon Sports, Beauty, and Toys subsets and evaluate sequential recommendation, direct recommendation, rating prediction, explanation generation, and review-title generation. With T5, META ID reaches HR@10/NDCG@10 of 0.0487/0.0277 on Sports, 0.0753/0.0429 on Beauty, and 0.0761/0.0441 on Toys; it leads the compared ID strategies and is competitive with or better than specialized sequential models. Results also improve across the other four task families, and ablations favor meta-path embeddings and K-Means over MF, GCN, DBSCAN, spectral clustering, and RQ-VAE alternatives. However, performance depends on the chosen OOV vocabulary size, evaluation is limited to three Amazon categories and two LLM backbones, and META ID assumes a fixed user-item catalog with sufficient interaction history. New users and items remain a cold-start problem, while scaling the current two-level identifiers to very large catalogs is left for future work.

## 繁中摘要

這篇論文探討大型語言模型在推薦任務中應如何表示使用者與項目。既有 instruction-based recommenders 常把 2024 這類 item identifier 拆成「20」、「24」等一般 vocabulary tokens；但這些 token 已從自然語言預訓練中帶有語意，使不相關的 identifiers 可能得到相似表示，並與互動資料中的 collaborative structure 衝突。若為每個 entity 分配一個全新的獨立 token，雖能避免碰撞，卻難以擴展，且每個 embedding 都必須從零學習。

META ID 以 out-of-vocabulary（OOV）tokens 建立精簡 identifiers，同時保留 user-item relationships 的 memorization 與 entities 之間的 diversity。方法先從 interaction graph 取樣考慮 rating 的 user-item meta-paths，再以 skip-gram model 將 users 與 items 學到同一個 collaborative embedding space，最後用 K-Means 分群。每個 entity 會取得代表 cluster 的 coarse token、依 cluster 內位置指定的 fine token，以及 user/item type token。如此一來，相似 users 與 items 可以共享粗粒度結構，又不會失去各自的唯一識別。

為了將 META IDs 整合進 LLM，方法會擴充 vocabulary 與 token-embedding table，並使用以 cluster centroids 初始化的 learned linear transformation，在一般 language-model fine-tuning 前增強新 tokens 的 embeddings。作者另外提出 memorization score 與 diversity score 來評估 identifier representations。分析顯示兩者總和與 NDCG@10 呈正相關；heatmaps、t-SNE 與 attention visualizations 也顯示，META IDs 比 random、sequential 或 collaborative ID baselines 更能同時保存 collaborative similarity 與 entity distinctions。

實驗使用 2019 年 Amazon Sports、Beauty、Toys 三個子集，評估 sequential recommendation、direct recommendation、rating prediction、explanation generation 與 review-title generation。搭配 T5 時，META ID 在 Sports、Beauty、Toys 的 HR@10/NDCG@10 分別達 0.0487/0.0277、0.0753/0.0429、0.0761/0.0441；它領先其他 ID strategies，並能與專用 sequential models 競爭或超越它們。其餘四類任務也普遍改善，而 ablations 顯示 meta-path embeddings 與 K-Means 優於 MF、GCN、DBSCAN、spectral clustering、RQ-VAE alternatives。不過，成效會受 OOV vocabulary size 選擇影響，評估僅涵蓋三個 Amazon categories 與兩種 LLM backbones；META ID 也假設固定 user-item catalog 且已有足夠 interaction history。新 users/items 仍有 cold-start 問題，如何把目前的 two-level identifiers 擴展到超大型 catalog 則留待後續研究。

## Notes

- Official code: https://github.com/Tingji2419/META-ID
- Dataset sizes are 35,598 users/18,357 items for Sports, 22,363/12,101 for Beauty, and 19,412/11,924 for Toys.
- Sequential and direct recommendation use all-item evaluation with HR@5/10 and NDCG@5/10; the remaining tasks use RMSE or BLEU metrics.
- The reported OOV vocabulary sizes for META ID are 1,600 on Sports, 1,319 on Beauty, and 727 on Toys, much smaller than assigning one independent token per item.
