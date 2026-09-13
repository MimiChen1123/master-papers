---
date: 2026-09-13
title: "Unveiling User Satisfaction and Creator Productivity Trade-Offs in Recommendation Platforms"
authors: "Fan Yao, Yiming Liao, Jingzhou Liu, Shaoliang Nie, Qifan Wang, Haifeng Xu, Hongning Wang"
venue: "NeurIPS 2024"
---

# Unveiling User Satisfaction and Creator Productivity Trade-Offs in Recommendation Platforms

- Paper page: https://proceedings.neurips.cc/paper_files/paper/2024/hash/9e2b548fd8d6c555fb79fa34a27592f9-Abstract-Conference.html
- PDF: https://proceedings.neurips.cc/paper_files/paper/2024/file/9e2b548fd8d6c555fb79fa34a27592f9-Paper-Conference.pdf
- Local PDF: [../../pdfs/2026-09/2026-09-13-unveiling-user-satisfaction-and-creator-productivity-trade-offs-in-recommendation-platforms.pdf](../../pdfs/2026-09/2026-09-13-unveiling-user-satisfaction-and-creator-productivity-trade-offs-in-recommendation-platforms.pdf)
- Venue: NeurIPS 2024

## English Summary

This paper studies user-generated content recommendation platforms where algorithms influence not only user satisfaction, but also creators' willingness to produce content. A purely relevance-driven recommender can maximize short-term user satisfaction by showing the most relevant creators or items, but this traffic allocation may reduce incentives for creators outside the winning group and weaken long-term content supply.

The authors introduce Cournot Content Creation Competition (C4), a game-theoretic model where creators strategically choose production frequency while competing for recommendation traffic. The platform controls exploration strength in the recommendation policy. The theoretical analysis shows an intrinsic trade-off: higher recommendation accuracy increases immediate user satisfaction, while stronger exploration can increase total creator productivity and content volume.

The paper then formulates the problem of choosing exploration strengths as a bilevel optimization problem and solves it with projected gradient descent plus efficient gradient approximation. Experiments and simulations validate the trade-off and show that per-user exploration control can produce better balances than fixed policies. The practical takeaway is that UGC recommenders should be audited before deployment for both user-side and creator-side outcomes, because optimizing only short-term relevance can harm long-term platform sustainability.

## 繁中摘要

這篇論文研究 user-generated content 平台中的推薦系統，重點是推薦演算法不只影響使用者滿意度，也會影響創作者是否願意持續產出內容。純粹 relevance-driven 的推薦策略可以在短期內提升使用者滿意度，因為它把流量集中給最相關的 creator 或內容；但這種流量分配可能降低其他創作者的生產誘因，進而傷害長期內容供給。

作者提出 Cournot Content Creation Competition (C4)，一個 game-theoretical model，讓創作者在競爭推薦流量時策略性決定內容生產頻率。平台則透過 recommendation policy 的 exploration strength 控制流量分配。理論分析顯示一個基本取捨：推薦越精準，短期 user satisfaction 越高；但更強的 exploration 可能提升 creator productivity 與總內容產量。

接著，論文把選擇 exploration strength 的問題建成 bilevel optimization，並用 projected gradient descent 搭配 efficient gradient approximation 求解。實驗與模擬驗證了 user satisfaction 和 creator productivity 之間的 trade-off，也顯示 per-user exploration control 比固定策略更能取得平衡。實務上的重點是：UGC 推薦系統上線前應同時審計使用者端與創作者端結果，因為只最佳化短期 relevance 可能傷害平台長期永續性。

## Notes

- Relevant for YouTube/TikTok/Instagram-like platforms where creators react to traffic allocation.
- The paper frames exploration as a tool for balancing user satisfaction and creator productivity.
- Useful as a pre-deployment audit perspective for recommender systems, not only as a ranking model paper.
