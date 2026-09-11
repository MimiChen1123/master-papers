---
date: 2026-09-10
title: "User-Creator Feature Polarization in Recommender Systems with Dual Influence"
authors: "Tao Lin, Kun Jin, Andrew Estornell, Xiaoying Zhang, Yiling Chen, Yang Liu"
venue: "NeurIPS 2024"
---

# User-Creator Feature Polarization in Recommender Systems with Dual Influence

- Paper page: https://proceedings.neurips.cc/paper_files/paper/2024/hash/e3642e94ac68254419b7cdeb5e4a46f7-Abstract-Conference.html
- PDF: https://proceedings.neurips.cc/paper_files/paper/2024/file/e3642e94ac68254419b7cdeb5e4a46f7-Paper-Conference.pdf
- Local PDF: [../../pdfs/2026-09/2026-09-10-user-creator-feature-polarization-in-recommender-systems-with-dual-influence.pdf](../../pdfs/2026-09/2026-09-10-user-creator-feature-polarization-in-recommender-systems-with-dual-influence.pdf)
- Venue: NeurIPS 2024

## English Summary

This paper studies recommender systems as dynamic systems that influence both users and creators. Many diversity interventions assume that users and items are fixed, but on content platforms recommendations can shift user preferences and also incentivize creators to change what they produce. The authors call this two-sided process user-creator feature dynamics.

The paper proves that under dual influence, recommender systems can converge to consensus or bi-polarization, reducing long-term diversity among both users and creators. A striking result is that short-term diversity-promoting interventions, such as diversity-aware objectives or reranking-like ideas, may not prevent polarization and can even worsen long-term outcomes when both sides adapt. The paper then analyzes mitigation strategies such as top-k truncation and threshold truncation.

Experiments on synthetic data and MovieLens 20M support the theory. Systems with dual influence tend to polarize, and myopic recommendation diversity can increase long-term polarization. In contrast, some relevance-oriented or efficiency-oriented designs, especially small top-k truncation, can reduce polarization and improve creation diversity, though with tradeoffs in single-shot recommendation diversity. The main message is that diversity should be evaluated dynamically, not just on one recommendation list.

## 繁中摘要

這篇論文把推薦系統視為會同時影響使用者與創作者的動態系統。許多 diversity 方法假設使用者偏好與 item 內容是固定的，但在 YouTube、TikTok、Twitter 這類內容平台中，推薦會改變使用者偏好，也會讓創作者調整內容風格來吸引流量。作者把這種雙邊互相影響稱為 user-creator feature dynamics。

論文理論上證明，在 dual influence 下，推薦系統可能收斂到 consensus 或 bi-polarization，導致使用者與創作者的長期多樣性下降。特別值得注意的是，一些短期提升 recommendation diversity 的方法，例如 diversity-aware objective，放在雙邊都會適應的動態環境中，不一定能防止極化，甚至可能讓長期結果更糟。作者也分析 top-k truncation、threshold truncation 等可能緩解方式。

在 synthetic data 與 MovieLens 20M 上的實驗支持理論結果：有雙邊影響時系統容易極化，短視的 diversity optimization 可能增加長期 polarization；相反地，一些 relevance-oriented 或 efficiency-oriented 設計，尤其是較小的 top-k truncation，反而能降低 polarization 並改善 creation diversity，但會和單次推薦列表多樣性產生取捨。這篇的核心提醒是：推薦系統的 diversity 不能只看某一次推薦列表，而要看長期動態。

## Notes

- Important for creator platforms where recommendations change both demand and supply.
- The paper challenges the assumption that short-term recommendation diversity always improves long-term ecosystem diversity.
- It suggests evaluating diversity with dynamic simulations or longitudinal metrics.
