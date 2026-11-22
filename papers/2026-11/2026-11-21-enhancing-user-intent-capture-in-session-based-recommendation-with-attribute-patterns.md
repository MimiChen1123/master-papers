---
date: 2026-11-21
title: "Enhancing User Intent Capture in Session-Based Recommendation with Attribute Patterns"
authors: "Xin Liu, Zheng Li, Yifan Gao, Jingfeng Yang, Tianyu Cao, Zhengyang Wang, Bing Yin, Yangqiu Song"
venue: "NeurIPS 2023"
---

# Enhancing User Intent Capture in Session-Based Recommendation with Attribute Patterns

- Paper page: https://proceedings.neurips.cc/paper_files/paper/2023/hash/621d0fd41c720ab252e178b77c200d90-Abstract-Conference.html
- PDF: https://proceedings.neurips.cc/paper_files/paper/2023/file/621d0fd41c720ab252e178b77c200d90-Paper-Conference.pdf
- Local PDF: [../../pdfs/2026-11/2026-11-21-enhancing-user-intent-capture-in-session-based-recommendation-with-attribute-patterns.pdf](../../pdfs/2026-11/2026-11-21-enhancing-user-intent-capture-in-session-based-recommendation-with-attribute-patterns.pdf)
- Venue: NeurIPS 2023

## English Summary

This paper studies session-based recommendation for anonymous users, where only a short sequence of current-session clicks or purchases is available. Sequence models preserve temporal order but can miss non-adjacent item relations, while global transition graphs add collaborative structure at the cost of noisy correlations, over-smoothing, and loss of temporal intent. FAPAT, the Frequent Attribute Pattern Augmented Transformer, combines temporal session encoding with compact graph patterns mined from item attributes.

Each item sequence is converted into a multiplex graph with a channel for every attribute type, such as category, brand, color, author, or publisher. FAPAT mines graphlets of at most four nodes using gSpan, restricts them to selected cyclic or triangular structures, and removes loose subgraphs with VF2 isomorphism checks. For a new session, it retrieves the most similar patterns by Jaccard overlap, encodes pattern nodes with relation-aware graph attention, and uses the pattern representations as external memory. Unidirectional memory attention with relative-position bias preserves the order of observed actions; a learned gate combines attribute channels, and a final Transformer captures long-range session information before next-item ranking.

Experiments cover diginetica and Tmall plus two months of industrial beauty, books, and electronics logs. Against thirteen sequence- and graph-based baselines, FAPAT is best on every reported next-item metric. On diginetica it reaches Hits@20 50.41, NDCG@20 24.59, and MRR@20 17.29; on Tmall it reaches 36.18, 22.97, and 18.99. Relative gains are larger on Tmall, reaching 19.64% for Hits@20. Industrial Hits@20 reaches 94.10 for beauty, 85.12 for books, and 82.81 for electronics. Public results average five seeds and use t-tests; industrial results use one fixed seed. Attribute-estimation and multi-step period-recommendation analyses provide additional evidence that the model captures intent beyond immediate item accuracy.

The evaluation relies on cleaned attribute data: products with missing or invalid values are removed, although real catalogs are often sparse and noisy. This preprocessing may favor an attribute-centric method and creates a deployment gap. FAPAT handles each attribute type separately rather than modeling cross-attribute patterns, and mining/retrieval complexity may grow in catalogs with hundreds of attribute types even though individual graphlets are small. The paper also notes that identical products may have different item identifiers, which makes rank metrics, especially MRR, understate semantically correct recommendations. The industrial data are proprietary, and no online A/B test is reported.

## 繁中摘要

這篇論文研究 anonymous users 的 session-based recommendation，此時模型只能看到目前 session 中一小段 clicks 或 purchases。Sequence models 能保留時間順序，卻可能忽略不相鄰 items 的關係；global transition graphs 雖加入 collaborative structure，也容易引入 noisy correlations、over-smoothing，並在 graph conversion 中遺失 temporal intent。作者提出 Frequent Attribute Pattern Augmented Transformer（FAPAT），把 temporal session encoding 與從 item attributes 挖掘出的精簡 graph patterns 結合。

系統將每個 item sequence 轉成 multiplex graph，每個 attribute type，例如 category、brand、color、author 或 publisher，都有獨立 channel。FAPAT 使用 gSpan 挖掘最多四個 nodes 的 graphlets，只保留指定的 cycle 或 triangle structures，再以 VF2 isomorphism checks 移除資訊量較低的 loose subgraphs。對新 session，模型依 Jaccard overlap 找出最相關 patterns，以 relation-aware graph attention 編碼 pattern nodes，並把 pattern representations 當成 external memory。具有 relative-position bias 的 unidirectional memory attention 保留 observed actions 的順序；learned gate 合併不同 attribute channels，最後由 Transformer 捕捉長距離 session information，再進行 next-item ranking。

實驗包含 diginetica、Tmall，以及兩個月的 beauty、books、electronics 工業紀錄。相較十三個 sequence- 與 graph-based baselines，FAPAT 在所有報告的 next-item metrics 都是最佳。Diginetica 的 Hits@20、NDCG@20、MRR@20 分別為 50.41、24.59、17.29；Tmall 為 36.18、22.97、18.99。Tmall 的相對提升較大，Hits@20 達 19.64%。工業資料 Hits@20 在 beauty、books、electronics 分別達 94.10、85.12、82.81。公開資料結果平均五個 seeds 並進行 t-test；工業結果只使用單一固定 seed。Attribute estimation 與 multi-step period recommendation 也提供模型不只改善單步 item accuracy 的額外證據。

評估依賴清洗後的 attribute data：缺少或具有無效 values 的 products 會被移除，但真實 catalog 往往稀疏且充滿雜訊。這項 preprocessing 可能有利於 attribute-centric method，也造成 deployment gap。FAPAT 分別處理每種 attribute，沒有建模 cross-attribute patterns；即使單一 graphlet 很小，面對數百種 attributes 時，mining 與 retrieval 成本仍可能增加。論文也指出，同一商品可能具有不同 item identifiers，使 ranking metrics，特別是 MRR，低估語意上正確的推薦。工業資料未公開，且沒有 online A/B test。

## Notes

- Diginetica contains 57,623 users, 43,074 items, and 993,163 clicks; Tmall contains 7,576 users, 39,768 items, and 438,315 clicks after preprocessing.
- The industrial electronics split is the largest, with 10.2 million users, 244.7 thousand items, and 115.6 million clicks.
- Attribute-pattern graph density is close to 1 across datasets, substantially below the global-transition graph density.
- Public metrics are averaged across seeds 2020-2024; the main-table significance threshold is p < 0.0001.
