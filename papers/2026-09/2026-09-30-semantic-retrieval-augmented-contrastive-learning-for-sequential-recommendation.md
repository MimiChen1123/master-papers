---
date: 2026-09-30
title: "Semantic Retrieval Augmented Contrastive Learning for Sequential Recommendation"
authors: "Ziqiang Cui, Yunpeng Weng, Xing Tang, Xiaokun Zhang, Shiwei Li, Peiyang Liu, Bowei He, Dugang Liu, Weihong Luo, Xiuqiang He, Chen Ma"
venue: "NeurIPS 2025"
---

# Semantic Retrieval Augmented Contrastive Learning for Sequential Recommendation

- Paper page: https://proceedings.neurips.cc/paper_files/paper/2025/hash/ee2841db84cd09a5f6e3e313ce3d79d9-Abstract-Conference.html
- PDF: https://proceedings.neurips.cc/paper_files/paper/2025/file/ee2841db84cd09a5f6e3e313ce3d79d9-Paper-Conference.pdf
- Local PDF: [../../pdfs/2026-09/2026-09-30-semantic-retrieval-augmented-contrastive-learning-for-sequential-recommendation.pdf](../../pdfs/2026-09/2026-09-30-semantic-retrieval-augmented-contrastive-learning-for-sequential-recommendation.pdf)
- Venue: NeurIPS 2025

## English Summary

This paper targets a central weakness of contrastive learning for sequential recommendation: the positive pairs used for supervision are often unreliable. Random masking or dropout can change a sequence's underlying preference, while pairs built from sparse collaborative signals or fixed heuristics may be semantically unrelated and cannot adapt during training. Semantic Retrieval Augmented Contrastive Learning (SRA-CL) uses LLM-derived semantic representations to construct better candidate pools, then combines inter-user and intra-user contrastive objectives with the ordinary next-item prediction loss.

For inter-user contrastive learning, an LLM summarizes each user's chronologically ordered item history, including names, brands, categories, and descriptions. SimCSE-RoBERTa converts the summaries into fixed semantic embeddings, and cosine similarity retrieves the top-k related users. A trainable attention-based synthesizer uses the target user as a query and forms a weighted combination of candidate users' recommendation representations as the positive sample. Other synthesized samples in the batch act as negatives, allowing positive construction to be optimized jointly with the recommender rather than fixed by a hard rule.

For intra-user contrastive learning, the LLM summarizes each item from its attributes and up to ten interaction contexts. The method retrieves semantically similar items, randomly selects 20% of positions in a sequence, and substitutes each selected item with a neighbor from its candidate pool. Two independently augmented views form the positive pair. The authors found that a learnable item synthesizer did not improve this branch, so only inter-user synthesis is learned. During deployment, neither the LLM nor the semantic contrastive modules are used: embeddings are generated and cached once before training, and inference runs only the recommendation backbone.

Experiments use Yelp, Amazon Sports, Beauty, and Office after five-core filtering, with full-item ranking under leave-one-out evaluation. Across HR@20 and NDCG@20, SRA-CL is best in all eight dataset-metric combinations, improving over the strongest baseline by 3.59%-11.82%; all main comparisons use five runs and paired t-tests at the 0.01 level. Adding SRA-CL to GRU4Rec, SASRec, and DuoRec improves HR@20 by 8.3%-27.3% and NDCG@20 by 9.7%-25.5%. Ablations support contributions from both contrastive branches, semantic retrieval, LLM processing, and learnable inter-user synthesis. The main limitations are the up-front LLM API cost, dependence on item text quality, and evaluation with only DeepSeek and Qwen; the offline benchmarks also do not establish online impact or recommendation diversity.

## 繁中摘要

這篇論文處理 sequential recommendation 中 contrastive learning 的核心弱點：用來監督模型的 positive pairs 經常不可靠。Random masking 或 dropout 可能改變序列原本的偏好語意；依賴稀疏 collaborative signals 或固定 heuristic 建立的 pair，也可能語意不一致，而且無法在訓練中自行調整。Semantic Retrieval Augmented Contrastive Learning（SRA-CL）使用 LLM 產生的 semantic representations 建立更可靠的 candidate pools，再把 inter-user、intra-user contrastive objectives 與一般 next-item prediction loss 一起訓練。

Inter-user contrastive learning 先讓 LLM 摘要每位使用者依時間排列的物品歷史，其中包含名稱、品牌、類別與描述；接著以 SimCSE-RoBERTa 轉成固定 semantic embeddings，透過 cosine similarity 取回 top-k 相似使用者。可訓練的 attention-based synthesizer 以目標使用者為 query，對候選使用者的 recommendation representations 加權組合，形成 positive sample；同一 batch 的其他合成表示則作為 negatives。這使 positive pair 的建立能和 recommender 共同最佳化，而不是完全依賴固定規則。

Intra-user contrastive learning 則讓 LLM 根據物品屬性及最多十個互動情境產生摘要，再取回語意相似物品。方法隨機選擇序列中 20% 的位置，以 candidate pool 中的相似物品替換，獨立產生兩個 augmented views 作為 positive pair。作者發現可學習的 item synthesizer 沒有改善此分支，因此只學習 inter-user synthesis。部署時不需要 LLM 或 semantic contrastive modules：semantic embeddings 在訓練前一次產生並快取，inference 僅執行 recommendation backbone。

實驗使用經 five-core filtering 的 Yelp、Amazon Sports、Beauty、Office，採 leave-one-out 並對完整 item set 排序。SRA-CL 在 HR@20 與 NDCG@20 的八個資料集與指標組合全部最佳，相對最強 baseline 提升 3.59%-11.82%；主要比較皆重複五次，並通過顯著水準 0.01 的 paired t-test。把 SRA-CL 加入 GRU4Rec、SASRec、DuoRec 後，HR@20 提升 8.3%-27.3%，NDCG@20 提升 9.7%-25.5%。Ablation 顯示兩種 contrastive branches、semantic retrieval、LLM processing 與 learnable inter-user synthesis 都有貢獻。主要限制是前置 LLM API 成本、對 item text 品質的依賴，以及只分析 DeepSeek 與 Qwen；離線 benchmark 也不能直接證明線上效果或推薦多樣性。

## Notes

- The official implementation is available at https://github.com/ziqiangcui/SRA-CL.
- The four datasets contain 4,905-35,598 users, 2,420-18,357 items, and 53,258-296,337 actions; their reported densities range from 0.05% to 0.45%.
- The authors report that asynchronous LLM preprocessing completes within a few hours and is performed once, but no API token count or monetary cost is provided.
