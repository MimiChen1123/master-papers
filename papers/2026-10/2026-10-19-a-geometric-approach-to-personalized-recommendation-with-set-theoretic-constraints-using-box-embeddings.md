---
date: 2026-10-19
title: "A Geometric Approach to Personalized Recommendation with Set-Theoretic Constraints Using Box Embeddings"
authors: "Shib Dasgupta, Michael Boratko, Andrew McCallum"
venue: "ICML 2025"
---

# A Geometric Approach to Personalized Recommendation with Set-Theoretic Constraints Using Box Embeddings

- Paper page: https://proceedings.mlr.press/v267/dasgupta25a.html
- PDF: https://raw.githubusercontent.com/mlresearch/v267/main/assets/dasgupta25a/dasgupta25a.pdf
- Local PDF: [../../pdfs/2026-10/2026-10-19-a-geometric-approach-to-personalized-recommendation-with-set-theoretic-constraints-using-box-embeddings.pdf](../../pdfs/2026-10/2026-10-19-a-geometric-approach-to-personalized-recommendation-with-set-theoretic-constraints-using-box-embeddings.pdf)
- Venue: ICML 2025

## English Summary

This paper studies personalized recommendation under explicit set-theoretic constraints, such as finding movies a user would like that are both comedy and action but not romance. Conventional matrix factorization and neural vector recommenders work well for ordinary collaborative filtering, but their linear representations are poorly aligned with intersection and negation. Filtering separately predicted attribute sets also ignores user-attribute interactions and compounds errors as a query adds constraints. The authors therefore formulate the problem as set-theoretic matrix completion, in which user and attribute rows denote sets of items and test queries are Boolean combinations of those rows.

The proposed model represents every user, attribute, and item as an axis-aligned hyperrectangle, or box, in a latent space. Boxes behave like trainable Venn diagrams: overlap measures compatibility, intersections are computed geometrically, and differences are scored through inclusion-exclusion. User-item and attribute-item observations are learned jointly, while query scores can be evaluated directly from the composed boxes without materializing the exponentially large space of possible user-attribute queries. The method compares three inference strategies: threshold-based filtering, multiplication of individual scores, and direct geometric composition. Box models use 64 dimensions versus 128 for vector models so that each entity has the same number of parameters.

Experiments cover MovieLens-1M, MovieLens-20M, Last-FM, and NYC restaurant data, spanning 1,872 to 138,493 users and three domains. The benchmark includes simple queries of the form user AND attribute and complex queries with two positive attributes or one positive and one negated attribute. Models are selected using ordinary held-out user-item NDCG, then evaluated by ranking the target item against the full item vocabulary. Baselines include matrix factorization, NeuMF, and LightGCN combined with filtering, score products, or vector arithmetic.

Across Last-FM, MovieLens-1M, and NYC-R, the paper reports an average 30% improvement in aggregate HR@50 for the best box-geometric method over the best vector alternative. The advantage is especially strong for the difficult three-way intersection: on MovieLens-1M, Box-Geometric reaches HR@50 of 46.1%, versus 27.5% for MF-Filter and 43.5% for NeuMF-Product; on MovieLens-20M it reaches 42.4%, versus 22.1% for the best reported vector baseline. It also has the smallest generalization-spectrum gap on all query types, indicating less degradation when every component of a composed query is unseen during training. Important limitations are that the complex-query benchmark is generated with statistical heuristics and manual filtering rather than natural user-issued queries, the method assumes an upstream system has already converted free text into structured attributes, and evaluation is offline on binarized implicit feedback rather than an online recommender.

## 繁中摘要

這篇論文研究帶有明確集合限制的個人化推薦，例如找出某位使用者會喜歡、同時屬於喜劇與動作、但不屬於愛情類的電影。傳統 matrix factorization 與 neural vector recommenders 適合一般 collaborative filtering，但其線性表示方式不符合 intersection 與 negation 的運算結構。若先分別預測各 attribute set 再過濾，不但無法利用 user-attribute interaction，限制條件增加時還會累積誤差。因此作者把問題定義為 set-theoretic matrix completion：user 與 attribute 的每一列都代表一個 item set，而測試查詢則是這些集合列的 Boolean 組合。

模型將每個 user、attribute 與 item 表示成 latent space 中的 axis-aligned hyperrectangle，也就是 box。Boxes 可視為可訓練的 Venn diagrams：以重疊程度衡量 compatibility，以幾何運算求 intersection，並透過 inclusion-exclusion 計算 difference。模型共同學習 user-item 與 attribute-item observations，推論時直接組合 boxes 即可計算查詢分數，不必實體化數量呈指數成長的所有 user-attribute queries。論文比較三種推論方式：threshold filtering、個別分數相乘，以及直接 geometric composition。為公平控制參數量，box models 使用 64 維，而 vector models 使用 128 維。

實驗使用 MovieLens-1M、MovieLens-20M、Last-FM 與 NYC restaurant datasets，涵蓋電影、音樂、餐廳三個領域，users 數量從 1,872 到 138,493。Benchmark 包含 user AND attribute 的 simple queries，以及兩個正向 attributes 或一正一負 attributes 的 complex queries。各模型先依一般 held-out user-item NDCG 選擇 checkpoint，再讓 target item 與完整 item vocabulary 排名。Baselines 包括 matrix factorization、NeuMF、LightGCN，並分別搭配 filtering、score product 或 vector arithmetic。

在 Last-FM、MovieLens-1M 與 NYC-R 上，最佳 Box-Geometric 相對最佳 vector method 的 aggregate HR@50 平均提升 30%。優勢在三重 intersection 特別明顯：MovieLens-1M 的 Box-Geometric HR@50 為 46.1%，高於 MF-Filter 的 27.5% 與 NeuMF-Product 的 43.5%；MovieLens-20M 則達 42.4%，最佳 vector baseline 為 22.1%。Box-Geometric 在所有 query types 也有最小的 generalization-spectrum gap，表示 composed query 的每個部分都未在訓練中出現時，效能下降較少。主要限制是 complex-query benchmark 由統計 heuristics 與人工篩選產生，而非真實使用者提出的 queries；模型也假設上游系統已將 free text 解析成 structured attributes，且實驗僅使用 binarized implicit feedback 做離線評估，尚未驗證線上推薦成效。

## Notes

- Official code and processed query data: https://github.com/ssdasgupta/set-based-collaborative-filtering
- Query types are `u intersect a`, `u intersect a1 intersect a2`, and `u intersect a1 intersect not a2`.
- MovieLens-20M is the largest dataset, with 138,493 users, 26,744 items, 95 attributes, and 19,722,646 training user-item interactions.
- At batch size 1024 on MovieLens-1M, one Box epoch takes 1:12, compared with 0:40 for MF, 1:20 for NeuMF, and 5:24 for LightGCN on a GTX 1080 Ti.
