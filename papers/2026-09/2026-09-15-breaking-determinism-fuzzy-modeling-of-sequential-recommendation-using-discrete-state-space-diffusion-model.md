---
date: 2026-09-15
title: "Breaking Determinism: Fuzzy Modeling of Sequential Recommendation Using Discrete State Space Diffusion Model"
authors: "Wenjia Xie, Hao Wang, Luankang Zhang, Rui Zhou, Defu Lian, Enhong Chen"
venue: "NeurIPS 2024"
---

# Breaking Determinism: Fuzzy Modeling of Sequential Recommendation Using Discrete State Space Diffusion Model

- Paper page: https://proceedings.neurips.cc/paper_files/paper/2024/hash/286d67ff96f99c614f75dbcfb72a3e5f-Abstract-Conference.html
- PDF: https://proceedings.neurips.cc/paper_files/paper/2024/file/286d67ff96f99c614f75dbcfb72a3e5f-Paper-Conference.pdf
- Local PDF: [../../pdfs/2026-09/2026-09-15-breaking-determinism-fuzzy-modeling-of-sequential-recommendation-using-discrete-state-space-diffusion-model.pdf](../../pdfs/2026-09/2026-09-15-breaking-determinism-fuzzy-modeling-of-sequential-recommendation-using-discrete-state-space-diffusion-model.pdf)
- Venue: NeurIPS 2024

## English Summary

This paper argues that many sequential recommendation models are overly deterministic. They try to map a user's historical sequence to a next item as if user behavior followed a fixed rule, while real decisions are noisy, unstable, and affected by context. To capture this fuzziness, the authors propose DDSR, a Discrete Diffusion Sequential Recommendation model that constructs fuzzy sets over interaction sequences.

DDSR applies diffusion in a discrete state space rather than adding Gaussian noise to continuous item embeddings. User interaction sequences are treated as directed graphs, and diffusion transitions produce structured fuzzy alternatives around observed items. This avoids some semantic distortion that can happen when discrete recommendation data is relaxed into continuous space. To make discrete diffusion tractable over large item spaces, DDSR replaces raw item IDs with semantic IDs generated through quantization or RQ-VAE from item descriptions, which also helps cold-start recommendation.

Experiments on three public sequential recommendation datasets compare DDSR with conventional, semantic, and generative baselines. DDSR outperforms the baselines in Recall and NDCG across settings, and ablations show that both semantic IDs and discrete diffusion matter. The paper also reports stronger performance on cold-start or long-tail items. The main insight is that modeling uncertainty directly over discrete interaction sequences can be more suitable for recommendation than importing continuous diffusion machinery unchanged.

## 繁中摘要

這篇論文指出，許多 sequential recommendation 模型過度 deterministic：它們把使用者歷史序列映射到下一個 item，彷彿使用者行為遵循固定規則。但真實決策通常有隨機性、不穩定性，也會被情境影響。為了捕捉這種模糊性，作者提出 DDSR，也就是 Discrete Diffusion Sequential Recommendation model，透過 interaction sequence 的 fuzzy sets 來建模使用者興趣演化。

DDSR 不像一般 diffusion recommender 把 Gaussian noise 加到連續 item embedding 上，而是在 discrete state space 中做 diffusion。它把使用者互動序列視為 directed graph，透過 diffusion transition 在觀測 item 周圍產生結構化的 fuzzy alternatives。這樣能避免把離散推薦資料硬轉成連續空間時造成語意扭曲。為了讓大量 item 的離散 diffusion 可行，DDSR 用 quantization 或 RQ-VAE 從 item descriptions 產生 semantic IDs 取代原始 item IDs，這也有助於 cold-start recommendation。

在三個公開 sequential recommendation 資料集上，DDSR 與傳統方法、semantic 方法、generative 方法比較，在 Recall 和 NDCG 上都取得更好結果。消融實驗顯示 semantic IDs 與 discrete diffusion 都有貢獻，論文也展示 DDSR 對 cold-start 或長尾 item 有更明顯幫助。這篇的核心觀點是：推薦資料本質上是離散序列，直接在離散 interaction sequence 上建模不確定性，可能比照搬連續 diffusion 更合適。

## Notes

- Useful if you are interested in diffusion models for sequential recommendation.
- The key distinction is discrete diffusion over semantic IDs, not Gaussian diffusion over continuous embeddings.
- The method is relevant to cold-start recommendation because semantic IDs inject item-side prior knowledge.
