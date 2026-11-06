---
date: 2026-11-06
title: "Semantic Retrieval Augmented Contrastive Learning for Sequential Recommendation"
authors: "Ziqiang Cui, Yunpeng Weng, Xing Tang, Xiaokun Zhang, Shiwei Li, Peiyang Liu, Bowei He, Dugang Liu, Weihong Luo, Xiuqiang He, Chen Ma"
venue: "NeurIPS 2025"
---

# Semantic Retrieval Augmented Contrastive Learning for Sequential Recommendation

- Paper page: https://proceedings.neurips.cc/paper_files/paper/2025/hash/ee2841db84cd09a5f6e3e313ce3d79d9-Abstract-Conference.html
- PDF: https://proceedings.neurips.cc/paper_files/paper/2025/file/ee2841db84cd09a5f6e3e313ce3d79d9-Paper-Conference.pdf
- Local PDF: [../../pdfs/2026-11/2026-11-06-semantic-retrieval-augmented-contrastive-learning-for-sequential-recommendation.pdf](../../pdfs/2026-11/2026-11-06-semantic-retrieval-augmented-contrastive-learning-for-sequential-recommendation.pdf)
- Code: https://github.com/ziqiangcui/SRA-CL
- Venue: NeurIPS 2025

## English Summary

Contrastive learning can improve sequential recommenders, but its supervision depends on the quality of positive pairs. Random masking, cropping, or substitution may change the meaning of a user's sequence, while collaborative signals can be too sparse to identify genuinely similar users. SRA-CL addresses this problem by using LLM-derived semantics to retrieve candidate users and items, then constructs more reliable inter-user and intra-user contrastive views. The framework is designed as a training-time extension that can be attached to different sequential recommendation backbones.

For inter-user contrastive learning, an LLM summarizes each user's ordered item attributes into a preference profile, which SimCSE-RoBERTa converts into a fixed semantic embedding. Cosine retrieval forms a top-k pool of semantically similar users. Instead of choosing one candidate with a fixed rule, a learnable attention-based synthesizer combines their current sequence representations into a positive sample. For intra-user contrastive learning, the LLM summarizes each item from its category, brand, description, and up to ten interaction contexts. The method retrieves semantically similar items and creates two views by replacing 20% of each sequence with candidates from these pools. Training combines next-item cross-entropy with both contrastive losses; inference uses only the original backbone, so the LLM and semantic embeddings add no online latency.

Experiments cover Yelp, Amazon Sports, Beauty, and Office with full-catalog leave-one-out ranking. Across HR@20 and NDCG@20, SRA-CL is best on all four datasets and improves over the strongest baseline by 3.59% to 11.82% for HR and 5.07% to 9.12% for NDCG; paired tests report significance at 0.01. Adding SRA-CL to GRU4Rec, SASRec, and DuoRec improves HR@20 by 8.3% to 27.3% and NDCG@20 by 9.7% to 25.5%, supporting the plug-and-play claim. Ablations show losses from removing either contrastive objective, semantic retrieval, LLM processing, or the inter-user learnable synthesizer. The paper also reports that a learnable synthesizer does not measurably help intra-user item substitution, so that component uses direct semantic retrieval instead.

The approach moves most semantic cost offline, but does not eliminate it: DeepSeek-V3 API calls are required to summarize all users and items before embeddings and retrieval indices can be cached. The authors state that asynchronous processing finishes within a few hours, while subsequent training adds only a lightweight synthesizer, but no detailed API cost or large-scale production study is reported. Evaluation uses public sparse datasets, histories capped at 20, and only DeepSeek and Qwen in the LLM comparison. Sending behavioral histories or item contexts to an external model also requires appropriate privacy controls, and the authors note that personalized recommendation may reduce content diversity.

## 繁中摘要

Contrastive learning 能改善 sequential recommender，但 supervision 品質取決於 positive pairs 是否可靠。隨機 masking、cropping 或 substitution 可能改變使用者 sequence 的原始語意，而稀疏 collaborative signals 也不一定能找出真正相似的 users。SRA-CL 使用 LLM-derived semantics 檢索候選 users 和 items，再建立較可靠的 inter-user 與 intra-user contrastive views。整體 framework 是 training-time extension，可接到不同 sequential recommendation backbones。

在 inter-user contrastive learning 中，LLM 先依照時間順序閱讀 item attributes，為每位使用者產生 preference profile，再由 SimCSE-RoBERTa 轉成固定 semantic embedding。模型以 cosine similarity 取回 top-k 相似 users；不同於固定挑選一個 candidate，可學習的 attention-based synthesizer 會加權組合候選者目前的 sequence representations，形成 positive sample。在 intra-user contrastive learning 中，LLM 根據 category、brand、description 與最多十段 interaction contexts 摘要每個 item，再檢索語意相近 items，將 sequence 中 20% 的 items 替換成候選項目以產生兩個 views。訓練同時使用 next-item cross-entropy 和兩種 contrastive losses；inference 只保留原始 backbone，因此 LLM 與 semantic embeddings 不會增加 online latency。

實驗涵蓋 Yelp、Amazon Sports、Beauty 與 Office，採用 full-catalog leave-one-out ranking。SRA-CL 在四個資料集的 HR@20 與 NDCG@20 都是最佳；相對最強 baseline，HR 提升 3.59% 至 11.82%，NDCG 提升 5.07% 至 9.12%，paired tests 在 0.01 significance level 下成立。將 SRA-CL 接到 GRU4Rec、SASRec 與 DuoRec 後，HR@20 提升 8.3% 至 27.3%，NDCG@20 提升 9.7% 至 25.5%，支持 plug-and-play 的主張。Ablation 顯示，移除任一 contrastive objective、semantic retrieval、LLM processing 或 inter-user learnable synthesizer 都會降低表現。論文也發現 learnable synthesizer 對 intra-user item substitution 沒有可量測的幫助，因此該部分直接使用 semantic retrieval。

這個方法把大部分 semantic cost 移到 offline，但成本並未消失：建立 embeddings 與 retrieval indices 前，必須透過 DeepSeek-V3 API 摘要所有 users 和 items。作者表示 asynchronous processing 可在數小時內完成，後續訓練只增加輕量 synthesizer，但沒有提供詳細 API 成本或大規模 production study。評估僅使用公開稀疏資料集、history 上限為 20，LLM 比較也只涵蓋 DeepSeek 與 Qwen。若將 behavioral histories 或 item contexts 傳給 external model，部署時仍需適當的 privacy controls；作者也指出 personalized recommendation 可能降低 content diversity。

## Notes

- Evaluation ranks against the full item catalog and reports five-run averages for HR/NDCG at 10 and 20.
- The four datasets contain 19,936 Yelp users, 35,598 Sports users, 22,363 Beauty users, and 4,905 Office users after filtering.
- Main experiments use DeepSeek-V3, SimCSE-RoBERTa embeddings, a maximum sequence length of 20, and one 32 GB V100 GPU.
- Cached semantic embeddings remain frozen during recommendation training and are not used during inference.
