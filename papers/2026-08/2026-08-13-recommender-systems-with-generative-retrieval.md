---
date: 2026-08-13
title: "Recommender Systems with Generative Retrieval"
authors: "Shashank Rajput, Nikhil Mehta, Anima Singh, Raghunandan Hulikal Keshavan, Trung Vu, Lukasz Heldt, Lichan Hong, Yi Tay, Vinh Q. Tran, Jonah Samost, Maciej Kula, Ed H. Chi, Maheswaran Sathiamoorthy"
venue: "NeurIPS 2023"
---

# Recommender Systems with Generative Retrieval

- Paper page: https://proceedings.neurips.cc/paper/2023/hash/20dcab0f14046a5c6b02b61da9f13229-Abstract.html
- PDF: ../../pdfs/2026-08/2026-08-13-recommender-systems-with-generative-retrieval.pdf
- Venue: NeurIPS 2023

## English Summary

This paper proposes TIGER, a generative retrieval framework for sequential recommendation. Instead of representing every item with an arbitrary atomic ID and retrieving candidates through embedding similarity plus approximate nearest-neighbor search, TIGER converts each item into a sequence of semantic codewords called a Semantic ID. A Transformer encoder-decoder then treats recommendation as a sequence generation task: given a user's interaction history, it autoregressively predicts the Semantic ID of the next item.

The key idea is that Semantic IDs are derived from item content embeddings, then quantized with an RQ-VAE-style residual quantization process. This gives similar items partially shared token structure, so the model can transfer information across related items and avoid depending only on memorized item IDs. In experiments on Amazon Beauty, Sports and Outdoors, and Toys and Games sequential recommendation benchmarks, TIGER improves Recall and NDCG over strong baselines such as SASRec, S3-Rec, BERT4Rec, and P5. The paper is especially interesting because generative retrieval naturally supports cold-start and long-tail recommendation: newly added or infrequent items can still be represented by meaningful Semantic IDs instead of requiring a well-trained standalone item embedding.

## 繁中摘要

這篇論文提出 TIGER，把推薦系統中的 retrieval 階段改寫成生成式任務。傳統做法通常會為使用者和 item 學 embedding，接著用近似最近鄰搜尋取回候選 item；TIGER 則先把每個 item 的內容特徵轉成一串具有語意的離散 token，也就是 Semantic ID，再讓 Transformer encoder-decoder 根據使用者互動序列逐 token 生成下一個可能互動 item 的 Semantic ID。

這個方法的核心價值在於 item ID 不再只是隨機或任意編號，而是帶有內容語意與階層結構。相似 item 會共享部分 Semantic ID token，因此模型可以在相似 item 之間共享知識，對冷啟動 item、低互動量 item 和長尾推薦更友善。實驗使用 Amazon Product Reviews 的 Beauty、Sports and Outdoors、Toys and Games 三個序列推薦資料集，並以 Recall@K 和 NDCG@K 評估；結果顯示 TIGER 相對 SASRec、S3-Rec、BERT4Rec、P5 等 baseline 有穩定提升。對研究推薦系統的人來說，這篇值得讀，因為它把「生成式檢索」和「語意化 item 表示」結合起來，提供了一條不同於 embedding retrieval 的推薦系統設計路線。

## Notes

- TIGER uses content features such as title, price, brand, and category to build item semantic embeddings before quantization.
- The learned Semantic IDs form a hierarchy: earlier codewords capture coarser item categories, while later codewords refine item distinctions.
- Compared with random IDs and LSH-based Semantic IDs, the RQ-VAE Semantic ID variant performs best in the paper's ablation study.
- The paper reports additional capabilities for cold-start retrieval and diversity control, which follow from generating semantic item codes rather than selecting only from memorized dense item vectors.
