---
date: 2026-09-14
title: "LLM-ESR: Large Language Models Enhancement for Long-tailed Sequential Recommendation"
authors: "Qidong Liu, Xian Wu, Yejing Wang, Zijian Zhang, Feng Tian, Yefeng Zheng, Xiangyu Zhao"
venue: "NeurIPS 2024"
---

# LLM-ESR: Large Language Models Enhancement for Long-tailed Sequential Recommendation

- Paper page: https://proceedings.neurips.cc/paper_files/paper/2024/hash/2f0728449cb3150189d765fc87afc913-Abstract-Conference.html
- PDF: https://proceedings.neurips.cc/paper_files/paper/2024/file/2f0728449cb3150189d765fc87afc913-Paper-Conference.pdf
- Local PDF: [../../pdfs/2026-09/2026-09-14-llm-esr-large-language-models-enhancement-for-long-tailed-sequential-recommendation.pdf](../../pdfs/2026-09/2026-09-14-llm-esr-large-language-models-enhancement-for-long-tailed-sequential-recommendation.pdf)
- Venue: NeurIPS 2024

## English Summary

This paper addresses long-tailed sequential recommendation, where many users have very short interaction histories and many items receive very few interactions. These long-tail user and item groups are exactly where collaborative signals are sparse, so conventional sequential recommenders often underperform. The authors argue that large language models can help by injecting semantic information about users and items, but direct LLM inference is too expensive for low-latency recommendation serving.

LLM-ESR uses LLM-derived semantic embeddings as a cached enhancement rather than running an LLM online. For long-tail items, it builds a dual-view modeling framework that combines frozen semantic embeddings from LLMs with collaborative embeddings from a standard sequential recommender. The semantic view preserves textual meaning, while the collaborative view preserves interaction patterns. For long-tail users, the paper proposes retrieval augmented self-distillation: it retrieves semantically similar users and distills more informative preference signals into the target user's representation.

Experiments on three real-world datasets with three backbone sequential recommenders show that LLM-ESR consistently outperforms long-tail and LLM-based baselines. The gains are especially visible for long-tail users and long-tail items, and ablations show that both dual-view modeling and retrieval augmented self-distillation contribute to the final performance. The practical takeaway is that LLM semantics can be useful in recommender systems without paying online LLM inference cost, as long as the semantic embeddings are cached and integrated carefully.

## 繁中摘要

這篇論文處理 long-tailed sequential recommendation：許多使用者只有很短的互動序列，許多 item 也只有少量互動。這些長尾 user 與長尾 item 的 collaborative signal 都很稀疏，因此傳統 sequential recommender 在這些群體上表現較差。作者認為 LLM 可以用語意資訊補足稀疏互動，但直接在線上 serving 時呼叫 LLM 成本太高，不適合低延遲推薦系統。

LLM-ESR 的做法是先用 LLM 產生並快取 semantic embeddings，而不是在線上推論時跑 LLM。針對長尾 item，它設計 dual-view modeling，把凍結的 LLM semantic embedding 和傳統 sequential recommender 的 collaborative embedding 結合；semantic view 保留文字語意，collaborative view 保留互動模式。針對長尾 user，作者提出 retrieval augmented self-distillation，利用 LLM user representation 找到語意相似的使用者，再把更豐富的偏好訊號 distill 到目標使用者表示中。

在三個真實資料集與三種 sequential recommendation backbone 上，LLM-ESR 都穩定優於 long-tail 與 LLM-based baseline，尤其對長尾使用者和長尾 item 的提升更明顯。消融實驗也顯示 dual-view modeling 與 retrieval augmented self-distillation 都是關鍵。實務上的重點是：LLM 語意資訊可以幫助推薦系統，但不一定要在線上呼叫 LLM；只要先快取 embedding 並妥善整合，就能兼顧效果與 serving 成本。

## Notes

- Useful for platforms with sparse users/items and available item text metadata.
- The method is model-agnostic and can enhance multiple sequential recommender backbones.
- The production-friendly idea is to cache LLM embeddings offline and avoid online LLM latency.
