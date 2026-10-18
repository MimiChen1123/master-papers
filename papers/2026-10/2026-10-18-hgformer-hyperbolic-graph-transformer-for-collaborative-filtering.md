---
date: 2026-10-18
title: "Hgformer: Hyperbolic Graph Transformer for Collaborative Filtering"
authors: "Xin Yang, Xingrun Li, Heng Chang, Jinze Yang, Xihong Yang, Shengyu Tao, Maiko Shigeno, Ningkang Chang, Junfeng Wang, Dawei Yin, Erxue Min"
venue: "ICML 2025"
---

# Hgformer: Hyperbolic Graph Transformer for Collaborative Filtering

- Paper page: https://proceedings.mlr.press/v267/yang25o.html
- PDF: https://raw.githubusercontent.com/mlresearch/v267/main/assets/yang25o/yang25o.pdf
- Local PDF: [../../pdfs/2026-10/2026-10-18-hgformer-hyperbolic-graph-transformer-for-collaborative-filtering.pdf](../../pdfs/2026-10/2026-10-18-hgformer-hyperbolic-graph-transformer-for-collaborative-filtering.pdf)
- Venue: ICML 2025

## English Summary

This paper targets long-tail collaborative filtering, where a small set of popular items receives many interactions while most items remain sparsely connected. Standard graph neural recommenders face two related problems: neighborhood aggregation gives head items richer representations than tail items, and Euclidean embeddings distort the hierarchical, power-law structure of the user-item graph. Hgformer moves both local message passing and global attention into a hyperbolic manifold, whose volume grows exponentially with radius and is therefore better suited to hierarchical structures.

The local component, Light Hyperbolic Graph Convolutional Network (LHGCN), is a parameter-free analogue of LightGCN. It aggregates neighboring users and items through hyperbolic centroids without repeatedly projecting embeddings to a tangent Euclidean space, avoiding the local-approximation distortion used by earlier hyperbolic CF models. A separate Hyperbolic Transformer performs cross-attention only between users and items, respecting the graph's bipartite structure and allowing every node to obtain global information beyond its observed neighborhood. Local and global representations are combined with a tunable weight and trained with a hyperbolic margin-ranking loss.

Naive all-user/all-item cross-attention costs O(MN). Hgformer introduces positive random features that provide an unbiased estimator of its hyperbolic softmax kernel, reorders the matrix products, and reduces time to O((M + N)md), where m and d are much smaller than the user and item counts. The paper also bounds the approximation error in terms of embedding norm, curvature, random-feature count, and the requested failure probability. Increasing the number of random features improves accuracy of the approximation, while hyperbolic normalization supports numerical stability.

Experiments use six Amazon and Douban datasets with up to 211,170 users, 163,789 items, and 5.07 million interactions. Hgformer is best on all reported Recall@10/20 and NDCG@10/20 metrics. On Amazon Book, it reaches Recall@10 of 0.0901 and NDCG@10 of 0.0573, improving 17.6% and 18.1% over the second-best model; on Amazon CD the corresponding gains are 18.3% and 15.9%. Ablations show that LHGCN contributes most, while hyperbolic cross-attention still provides sizable gains. With the least-popular 80% defined as tail items, Hgformer improves tail Recall@10 over the stronger compared hyperbolic baseline by 55.7% on Amazon CD, 17.5% on Amazon Movie, 29.8% on Douban Movie, and 26.7% on Douban Music. Limitations include the transductive ID-only setup, random negative sampling, offline 8:1:1 splits, and popularity-defined tail metrics that do not directly establish user or provider fairness. The paper proves asymptotic complexity but does not report end-to-end runtime or memory comparisons, and it does not test cold-start users/items, side information, temporal drift, or online serving.

## 繁中摘要

這篇論文處理 long-tail collaborative filtering：少數熱門 items 擁有大量 interactions，而大多數 items 只有稀疏連結。標準 graph neural recommenders 有兩個相關問題：neighborhood aggregation 讓 head items 得到比 tail items 更充分的 representations；Euclidean embeddings 也會扭曲 user-item graph 的 hierarchical、power-law structure。Hgformer 將 local message passing 與 global attention 都移到 hyperbolic manifold，其空間體積會隨半徑呈指數成長，因此更適合表示階層結構。

Local component Light Hyperbolic Graph Convolutional Network（LHGCN）是 parameter-free 的 LightGCN 對應版本。它直接以 hyperbolic centroids 聚合相鄰 users/items，不必反覆投影到 tangent Euclidean space，避免早期 hyperbolic CF models 因 local approximation 造成的 distortion。另一個 Hyperbolic Transformer 僅在 users 與 items 之間進行 cross-attention，符合 bipartite graph 結構，也讓每個 node 能取得 observed neighborhood 之外的 global information。Local/global representations 以可調權重合併，並用 hyperbolic margin-ranking loss 訓練。

Naive all-user/all-item cross-attention 的成本為 O(MN)。Hgformer 以 positive random features 建立 hyperbolic softmax kernel 的 unbiased estimator，再調整 matrix multiplication 次序，把時間複雜度降至 O((M + N)md)，其中 m、d 遠小於 users/items 數量。論文也根據 embedding norm、curvature、random-feature count 與 failure probability 推導 approximation error bound；增加 random features 可提高 approximation accuracy，而 hyperbolic normalization 用於維持 numerical stability。

實驗涵蓋六個 Amazon 與 Douban datasets，最大規模為 211,170 users、163,789 items、507 萬 interactions。Hgformer 在所有回報的 Recall@10/20、NDCG@10/20 都最佳；Amazon Book 的 Recall@10 為 0.0901、NDCG@10 為 0.0573，分別比 second-best model 高 17.6% 與 18.1%，Amazon CD 則提高 18.3% 與 15.9%。Ablations 顯示 LHGCN 貢獻最大，但 hyperbolic cross-attention 仍帶來顯著增益。把人氣最低 80% 定義為 tail items 時，Hgformer 相對較強的比較 hyperbolic baseline，在 Amazon CD、Amazon Movie、Douban Movie、Douban Music 的 tail Recall@10 分別提升 55.7%、17.5%、29.8%、26.7%。限制包括 transductive ID-only setting、random negative sampling、離線 8:1:1 split，以及以 popularity 定義的 tail metrics 無法直接證明 user/provider fairness。論文只證明 asymptotic complexity，未提供 end-to-end runtime 或 memory comparisons，也未測試 cold-start users/items、side information、temporal drift 或線上服務。

## Notes

- Official code: https://github.com/EnkiXin/Hgformer
- The six datasets are Amazon Book, Amazon CD, Amazon Movie, Douban Book, Douban Movie, and Douban Music.
- The largest dataset, Amazon Book, has 5,069,747 interactions but a density of only 0.015%.
- Tail items are operationally defined as the bottom 80% of items ranked by popularity.
