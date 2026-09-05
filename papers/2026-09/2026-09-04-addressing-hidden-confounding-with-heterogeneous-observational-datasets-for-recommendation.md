---
date: 2026-09-04
title: "Addressing Hidden Confounding with Heterogeneous Observational Datasets for Recommendation"
authors: "Yanghao Xiao, Haoxuan Li, Yongqiang Tang, Wensheng Zhang"
venue: "NeurIPS 2024"
---

# Addressing Hidden Confounding with Heterogeneous Observational Datasets for Recommendation

- Paper page: https://proceedings.neurips.cc/paper_files/paper/2024/hash/eb5254c4ee813d05af9c098f2d9c5708-Abstract-Conference.html
- PDF: https://proceedings.neurips.cc/paper_files/paper/2024/file/eb5254c4ee813d05af9c098f2d9c5708-Paper-Conference.pdf
- Local PDF: [../../pdfs/2026-09/2026-09-04-addressing-hidden-confounding-with-heterogeneous-observational-datasets-for-recommendation.pdf](../../pdfs/2026-09/2026-09-04-addressing-hidden-confounding-with-heterogeneous-observational-datasets-for-recommendation.pdf)
- Venue: NeurIPS 2024

## English Summary

This paper studies debiased recommendation under hidden confounding. Standard selection-bias correction methods assume that all variables affecting both exposure and feedback are observed. In real systems, that assumption often fails: optional user or item attributes such as age, salary, or richer item metadata may be missing for part of the data, and the unobserved variables can influence both what users see and how they respond. Existing hidden-confounding approaches either require strong assumptions about confounding strength or depend on expensive randomized controlled trial data.

The authors propose using heterogeneous observational data instead. The key setup is that some user-item pairs have sufficiently complete features and are treated as data without hidden confounding, while other pairs have incomplete features and may contain hidden confounders. Their method, MetaDebias, explicitly models identifiable propensity scores, naive error imputation, an oracle error imputation target, and an additional residual term for hidden-confounding bias. It then trains the prediction model with a bi-level optimization procedure so the recommender can learn from observational data while correcting for the missingness mechanism.

Experiments on COAT, Yahoo! R3, and KuaiRec show that MetaDebias outperforms IPS, DR, RCT-based calibration methods, and recent hidden-confounding baselines across AUC, Recall, and NDCG. The analysis shows that MetaDebias remains robust as hidden-confounding strength increases, works under different ratios of complete and incomplete observational data, and still performs well when the training set is small. The main limitation is that the approach assumes the complete-feature group can include all confounders; this may be reasonable in some industrial settings but is still a strong practical assumption.

## 繁中摘要

這篇論文處理推薦系統中的 hidden confounding 問題。許多 selection bias correction 方法假設所有同時影響曝光與回饋的變數都已被觀測到，但真實系統常常不是這樣。例如有些使用者填了完整年齡、收入或偏好資訊，有些人只填必要欄位；這些缺失的 optional features 可能同時影響系統推薦給他的內容，以及他是否互動。既有方法通常需要對 hidden confounding strength 做強假設，或依賴昂貴的 RCT/A/B test 資料。

作者提出使用 heterogeneous observational data：資料中一部分 user-item pair 有完整特徵，可以視為沒有 hidden confounding；另一部分特徵不完整，可能存在 hidden confounder。MetaDebias 會同時建模 propensity score、naive error imputation、oracle error imputation，以及 hidden confounding 帶來的 residual bias，最後用 bi-level optimization 訓練推薦模型。核心想法是利用比較容易取得的異質觀測資料，而不是要求額外的隨機實驗資料。

實驗使用 COAT、Yahoo! R3 和 KuaiRec，結果顯示 MetaDebias 在 AUC、Recall、NDCG 上優於 IPS、DR、RCT-based calibration 以及其他 hidden-confounding baseline。進一步分析也顯示，當 hidden confounding 更強、完整與不完整資料比例改變、或訓練資料變少時，MetaDebias 仍維持較穩定的表現。主要限制是它假設「特徵完整的那群資料」真的包含所有 confounders，這在某些工業場景可能可行，但仍是一個需要小心檢查的假設。

## Notes

- This is relevant for recommendation systems trained from observational logs with missing optional user or item features.
- The practical value is reducing reliance on RCT data while still addressing hidden confounding.
- The method depends heavily on correctly identifying which data has sufficiently complete features.
