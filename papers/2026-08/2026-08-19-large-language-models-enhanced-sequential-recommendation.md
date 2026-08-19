---
date: 2026-08-19
title: "LLM-ESR: Large Language Models Enhancement for Long-tailed Sequential Recommendation"
authors: "Qidong Liu, Xian Wu, Yejing Wang, Zijian Zhang, Feng Tian, Yefeng Zheng, Xiangyu Zhao"
venue: "NeurIPS 2024"
---

# LLM-ESR: Large Language Models Enhancement for Long-tailed Sequential Recommendation

- Paper page: https://proceedings.neurips.cc/paper_files/paper/2024/hash/2f07231386c732725834bafb99035aa8-Abstract-Conference.html
- arXiv: https://arxiv.org/abs/2405.20646
- PDF: ../../pdfs/2026-08/2026-08-19-large-language-models-enhanced-sequential-recommendation.pdf
- Venue: NeurIPS 2024
- Code: https://github.com/Applied-Machine-Learning-Lab/LLM-ESR

## English Summary

This paper addresses long-tail problems in sequential recommender systems, where many users have very short interaction histories and many items receive very few interactions. Standard sequential models such as SASRec, GRU4Rec, and BERT4Rec rely heavily on collaborative signals, so they tend to perform better for active users and popular items. LLM-ESR introduces semantic information from large language models to improve these weakly observed users and items without requiring expensive LLM calls during online recommendation.

The framework first uses LLMs to encode item attributes and user history prompts into semantic embeddings, then caches those embeddings. For long-tail items, LLM-ESR uses dual-view modeling: one view keeps frozen LLM-derived semantic item embeddings, while another learns conventional collaborative embeddings from interaction data. Cross-attention and a shared sequence encoder combine the semantic and collaborative views. For long-tail users, the method retrieves semantically similar users using cached LLM user embeddings and applies retrieval augmented self-distillation, letting richer similar-user representations guide the target user's representation. Experiments on Yelp, Amazon Fashion, and Amazon Beauty with GRU4Rec, BERT4Rec, and SASRec show consistent gains over long-tail SRS baselines and LLM-enhanced baselines, especially on tail users and tail items.

## 繁中摘要

這篇論文處理 sequential recommendation 中常見的長尾問題：大部分使用者互動紀錄很短，很多 item 也只有少量互動。傳統序列推薦模型主要依賴 collaborative signal，因此對活躍使用者和熱門 item 表現較好，但對長尾使用者和長尾 item 容易失準。LLM-ESR 的想法是把大型語言模型的語意能力引入推薦系統，但不在推論時直接呼叫 LLM，避免線上推薦的延遲和成本問題。

方法上，LLM-ESR 先用 LLM 將 item 屬性和 user history prompt 編碼成 semantic embeddings，並預先快取。針對長尾 item，它設計 dual-view modeling：一邊保留 frozen 的 LLM semantic embedding，另一邊學習傳統 collaborative embedding，再透過 cross-attention 和 sequence encoder 融合兩種訊號。針對長尾 user，它用 LLM user embedding 找出語意相近的使用者，並用 retrieval augmented self-distillation 讓相似使用者的表示輔助訓練目標使用者。實驗在 Yelp、Amazon Fashion、Amazon Beauty 三個資料集上，搭配 GRU4Rec、BERT4Rec、SASRec 三種 backbone，結果顯示 LLM-ESR 對整體表現、長尾使用者、長尾 item 都有穩定提升。

## Notes

- The method avoids online LLM inference by caching LLM-derived semantic embeddings.
- Dual-view modeling is used for long-tail items: semantic view plus collaborative view.
- Retrieval augmented self-distillation is used for long-tail users by retrieving semantically similar users.
- The framework is model-agnostic and is evaluated with GRU4Rec, BERT4Rec, and SASRec.
- The paper is useful if you care about practical LLM-enhanced recommendation systems where latency matters.
