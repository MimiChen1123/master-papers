---
date: 2026-08-27
title: "Relaxing the Accurate Imputation Assumption in Doubly Robust Learning for Debiased Collaborative Filtering"
authors: "Haoxuan Li, Chunyuan Zheng, Shuyi Wang, Kunhan Wu, Hao Wang, Peng Wu, Zhi Geng, Xu Chen, Xiao-Hua Zhou"
venue: "ICML 2024"
---

# Relaxing the Accurate Imputation Assumption in Doubly Robust Learning for Debiased Collaborative Filtering

- Paper page: https://proceedings.mlr.press/v235/li24cq.html
- PDF: https://raw.githubusercontent.com/mlresearch/v235/main/assets/li24cq/li24cq.pdf
- Local PDF: [../../pdfs/2026-08/2026-08-27-relaxing-the-accurate-imputation-assumption-in-doubly-robust-learning-for-debiased-collaborative-filtering.pdf](../../pdfs/2026-08/2026-08-27-relaxing-the-accurate-imputation-assumption-in-doubly-robust-learning-for-debiased-collaborative-filtering.pdf)
- Venue: ICML 2024

## English Summary

This paper studies debiased collaborative filtering under sample-selection bias, where observed user-item ratings are not representative of the full target population. Existing error-imputation, inverse-propensity-scoring, and doubly robust methods try to correct this bias, but standard doubly robust estimators still rely on a strong assumption: either the propensity model is accurate or the imputed pseudo-labels are accurate. In practice, pseudo-labels for missing ratings are often systematically wrong.

The authors propose new doubly robust estimators called User-DR, Item-DR, and User-Item-DR. Instead of requiring pseudo-labels to exactly match true labels, these estimators remain unbiased when the pseudo-labels deviate from true labels by arbitrary user-specific bias, item-specific bias, or both. This relaxes the accurate imputation assumption and better matches common recommender-system failure modes, such as user-level rating tendencies or item-level exposure and popularity effects.

The paper also introduces a propensity reconstruction learning approach that alternates updates for the propensity model, imputation model, and prediction model. It uses adaptive constraint weights through an attention mechanism to control variance while preserving the relaxed unbiasedness guarantees. Experiments on one semi-synthetic setting and three real-world datasets, COAT, MUSIC, and KUAIREC, show that the proposed methods outperform prior debiasing baselines on AUC, NDCG, and F1.

## 繁中 Summary

這篇論文處理 collaborative filtering 中的 sample-selection bias 問題，也就是觀察到的 user-item ratings 並不能代表完整的目標族群。既有的 error-imputation、inverse-propensity-scoring 和 doubly robust 方法都試圖修正這個偏差，但標準 doubly robust estimator 仍然依賴很強的假設：propensity model 要準，或 imputed pseudo-labels 要準。實務上，missing ratings 的 pseudo-labels 常常會有系統性誤差。

作者提出新的 doubly robust estimators：User-DR、Item-DR 和 User-Item-DR。這些方法不要求 pseudo-labels 必須完全等於 true labels；只要 pseudo-labels 和 true labels 的差異可以表示為任意 user-specific bias、item-specific bias，或兩者組合，estimator 仍可保持 unbiased。這比傳統 accurate imputation assumption 更貼近推薦系統常見情境，例如使用者本身的評分習慣，或 item 曝光、流行度造成的系統性偏差。

論文也提出 propensity reconstruction learning，交替更新 propensity model、imputation model 和 prediction model，並用 attention mechanism 自適應調整 constraint weights，以控制 variance 並維持較寬鬆的 unbiasedness 保證。實驗包含 semi-synthetic setting 以及 COAT、MUSIC、KUAIREC 三個真實資料集；結果顯示提出的方法在 AUC、NDCG 和 F1 上都優於既有 debiasing baselines。

## Notes

- This paper is useful for recommender-system debiasing when missing labels are imputed but not reliably accurate.
- The main contribution is a weaker and more realistic unbiasedness condition for doubly robust collaborative filtering.
- User-Item-DR is the most general estimator because it handles both user-specific and item-specific inductive bias.
