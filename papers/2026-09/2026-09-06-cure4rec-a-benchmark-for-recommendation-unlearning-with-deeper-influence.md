---
date: 2026-09-06
title: "CURE4Rec: A Benchmark for Recommendation Unlearning with Deeper Influence"
authors: "Chaochao Chen, Jiaming Zhang, Yizhao Zhang, Li Zhang, Lingjuan Lyu, Yuyuan Li, Biao Gong, Chenggang Yan"
venue: "NeurIPS 2024 Datasets and Benchmarks Track"
---

# CURE4Rec: A Benchmark for Recommendation Unlearning with Deeper Influence

- Paper page: https://proceedings.neurips.cc/paper_files/paper/2024/hash/b364953e402d7d92e13830383677efb5-Abstract-Datasets_and_Benchmarks_Track.html
- PDF: https://proceedings.neurips.cc/paper_files/paper/2024/file/b364953e402d7d92e13830383677efb5-Paper-Datasets_and_Benchmarks_Track.pdf
- Local PDF: [../../pdfs/2026-09/2026-09-06-cure4rec-a-benchmark-for-recommendation-unlearning-with-deeper-influence.pdf](../../pdfs/2026-09/2026-09-06-cure4rec-a-benchmark-for-recommendation-unlearning-with-deeper-influence.pdf)
- Venue: NeurIPS 2024 Datasets and Benchmarks Track

## English Summary

This paper introduces CURE4Rec, a benchmark for evaluating machine unlearning methods in recommender systems. The motivation is that recommendation models are trained on sensitive user interaction histories, so privacy regulations such as the right to be forgotten require systems to remove the influence of selected user data. Existing recommendation unlearning work often reports utility or runtime, but lacks a unified evaluation framework and largely ignores deeper model effects such as fairness.

CURE4Rec evaluates recommendation unlearning along four dimensions: unlearning completeness, recommendation utility, unlearning efficiency, and recommendation fairness. It also varies the unlearning set through three selection strategies: core data, edge data, and random data. This design tests not only whether a method can forget the requested records, but also whether it remains robust when the removed data has different influence levels on the recommender.

The experiments compare exact unlearning and approximate unlearning methods across multiple recommendation datasets and models. The paper finds a clear tradeoff: exact unlearning methods based on division and aggregation can better satisfy completeness, but they often hurt utility, efficiency, and fairness. Approximate methods that directly manipulate model parameters usually perform better on most practical dimensions except strict completeness. A useful takeaway is that recommendation unlearning should not be judged only by forgetting accuracy; fairness and robustness can change substantially after unlearning.

## 繁中摘要

這篇論文提出 CURE4Rec，一個用來評估推薦系統 machine unlearning 的 benchmark。問題背景是推薦模型通常依賴使用者歷史互動資料，這些資料可能包含敏感資訊；當使用者要求刪除資料時，系統不只要刪掉資料庫紀錄，也需要讓模型忘掉該資料造成的影響。作者指出，現有 recommendation unlearning 研究缺少統一評估框架，而且常忽略 fairness 這類更深層的模型影響。

CURE4Rec 從四個面向評估 unlearning：unlearning completeness、recommendation utility、unlearning efficiency、recommendation fairness。同時，它用 core data、edge data、random data 三種方式選擇要被 unlearn 的資料，觀察不同影響力資料被移除後，方法是否仍然穩健。

實驗比較 exact unlearning 與 approximate unlearning。結果顯示，division-aggregation 類型的 exact unlearning 較能保證 completeness，但常犧牲推薦效果、效率與公平性；直接操作模型參數的 approximate unlearning 則在 completeness 以外的面向通常較好。這篇對實務的提醒是：推薦系統做資料刪除或忘卻時，不能只看是否忘乾淨，也要檢查推薦品質、公平性與對不同 unlearning set 的穩健性。

## Notes

- This is most relevant for privacy-sensitive recommender systems that must support user deletion requests.
- The benchmark explicitly brings fairness into recommendation unlearning evaluation.
- The paper is useful if you need a checklist for evaluating unlearning beyond accuracy and runtime.
