---
date: 2026-09-08
title: "Identify Then Recommend: Towards Unsupervised Group Recommendation"
authors: "Yue Liu, Shihao Zhu, Tianyuan Yang, Jian Ma, Wenliang Zhong"
venue: "NeurIPS 2024"
---

# Identify Then Recommend: Towards Unsupervised Group Recommendation

- Paper page: https://proceedings.neurips.cc/paper_files/paper/2024/hash/ae485c4579564ca17b643d45eb598930-Abstract-Conference.html
- PDF: https://proceedings.neurips.cc/paper_files/paper/2024/file/ae485c4579564ca17b643d45eb598930-Paper-Conference.pdf
- Local PDF: [../../pdfs/2026-09/2026-09-08-identify-then-recommend-towards-unsupervised-group-recommendation.pdf](../../pdfs/2026-09/2026-09-08-identify-then-recommend-towards-unsupervised-group-recommendation.pdf)
- Venue: NeurIPS 2024

## English Summary

This paper targets group recommendation, where the system recommends items to a group of users rather than to a single individual. Existing deep group recommendation models usually assume a predefined fixed number of groups and require supervised labels such as user-group membership and group-item interactions. The authors argue that these assumptions are weak for industrial systems, where group distributions shift dynamically and annotation is expensive.

The proposed framework, Identify Then Recommend (ITR), separates the problem into unsupervised group identification and self-supervised group recommendation. In the identification stage, it estimates adaptive density over user representations to find likely group centers and decision boundaries, then applies a heuristic merge-and-split strategy to discover groups without knowing the number of groups in advance. In the recommendation stage, it uses two pretext tasks: pull-and-repulsion to refine user-group structure, and pseudo group recommendation to construct learning signals from estimated group-item relations.

Experiments compare ITR with twelve group recommendation baselines on open datasets for both group and user recommendation. ITR achieves the best or strongest results despite not using group annotations, with reported gains such as 22.95% NDCG@5 improvement for group recommendation and 22.22% NDCG@5 improvement for user recommendation in key settings. The paper also reports deployment in a large-scale industrial livestream recommendation scenario, where online A/B testing shows average performance improvement.

## 繁中摘要

這篇論文研究 group recommendation，也就是推薦 item 給一群使用者，而不是單一使用者。現有 deep group recommendation 方法通常假設 group 數量事先固定，而且需要 user-group 與 group-item 標註。作者指出，這在工業場景不實用，因為 group 分布會動態變化，標註成本也很高。

作者提出 Identify Then Recommend (ITR)，把任務拆成兩階段：先無監督辨識 group，再做 self-supervised group recommendation。group identification 階段會根據 user representation 估計 adaptive density，找出可能的 group center 與 decision boundary，接著用 merge-and-split 策略在不知道 group 數量的情況下發現群體。recommendation 階段則設計兩個 pretext task：pull-and-repulsion 用來調整 user-group 分布，pseudo group recommendation 用估計出的 group-item 關係提供訓練訊號。

實驗把 ITR 和十二個 group recommendation baseline 比較，涵蓋 group recommendation 與 user recommendation。ITR 在不使用 group annotation 的情況下仍取得最好或很強的結果，論文中特別提到在某些設定下 group recommendation NDCG@5 提升 22.95%，user recommendation NDCG@5 提升 22.22%。此外，ITR 也部署到大型直播推薦場景，線上 A/B test 顯示平均效果提升。

## Notes

- Best fit for dynamic group recommendation where group labels are unavailable or costly.
- The method is interesting because it avoids requiring the number of groups as an input.
- The industrial deployment makes it more practically grounded than a purely offline clustering paper.
