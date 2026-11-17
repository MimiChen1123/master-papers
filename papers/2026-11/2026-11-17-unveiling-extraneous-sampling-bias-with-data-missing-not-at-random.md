---
date: 2026-11-17
title: "Unveiling Extraneous Sampling Bias with Data Missing-Not-At-Random"
authors: "Chunyuan Zheng, Haocheng Yang, Haoxuan Li, Mengyue Yang"
venue: "NeurIPS 2025"
---

# Unveiling Extraneous Sampling Bias with Data Missing-Not-At-Random

- Paper page: https://proceedings.neurips.cc/paper_files/paper/2025/hash/1ca17a149e75431e20d5d9878c4f17de-Abstract-Conference.html
- PDF: https://proceedings.neurips.cc/paper_files/paper/2025/file/1ca17a149e75431e20d5d9878c4f17de-Paper-Conference.pdf
- Local PDF: [../../pdfs/2026-11/2026-11-17-unveiling-extraneous-sampling-bias-with-data-missing-not-at-random.pdf](../../pdfs/2026-11/2026-11-17-unveiling-extraneous-sampling-bias-with-data-missing-not-at-random.pdf)
- Code: https://github.com/ChunyuanZheng/neurips-25-SuperDR
- Venue: NeurIPS 2025

## English Summary

This paper revisits selection-bias correction for recommendation under missing-not-at-random feedback. Conventional doubly robust (DR) estimators assume exact matching: the user-item units in the target population and evaluation set are fixed and identical, with randomness arising only from whether a rating is observed. In deployed systems, offline training and online evaluation can contain different users and items. The authors therefore study a super-population setting in which units are sampled independently but the joint feature-rating distribution remains the same across train and test. This differs from cold start, where the underlying hot- and cold-unit distributions themselves differ.

The theoretical analysis shows that the usual DR estimator has an additional covariance bias under this sampling process. Besides the familiar product of propensity and imputation errors, unbiasedness now also requires the residual imputation error to be uncorrelated with the propensity-weighted observation residual. Consequently, even exactly learned propensities or imputed errors are not, by themselves, sufficient under super-population sampling. This identifies a source of bias that prior exact-matching analyses hide.

SuperDR addresses the extra term with a targeted correction to the imputation model. It adds a learned scalar times the difference between the observation indicator and estimated propensity to each imputed error. Optimizing the corrected propensity-weighted imputation loss makes the observed empirical covariance vanish and bounds the missing-part covariance through concentration arguments. The correction enlarges the imputation hypothesis space, degenerates to the original model when no correction is needed, and yields stated bias- and variance-reduction properties under the paper's conditions. A joint-learning algorithm alternates between this corrected imputation model and the SuperDR prediction loss, adding only one scalar parameter to the conventional procedure.

Experiments simulate partial train-test unit overlap on Coat, Yahoo! R3, and KuaiRec and compare SuperDR with propensity, information-bottleneck, and numerous DR baselines. SuperDR is best on all nine reported main metrics. On Coat it reaches AUC 0.757, NDCG@5 0.667, and Recall@5 0.637; on Yahoo! R3 the corresponding values are 0.686, 0.667, and 0.463; on KuaiRec it reaches AUC 0.828, NDCG@50 0.640, and Recall@50 0.680. Gains are largest when only 5%-10% of users and items are sampled for training, where overlap is lowest. Several, though not all, improvements over the strongest baseline are statistically significant under paired t-tests.

The work assumes that train and test share the same joint feature-rating distribution and that distribution shift can be handled separately through reweighting. Real systems may violate this assumption through temporal drift, changing exposure policies, or genuinely new user populations. Experiments use matrix-factorization features with an MLP backbone, so evidence for modern deep ranking architectures is limited. The authors also identify the looseness of the empirical-covariance bound and the cost of alternating prediction, imputation, and targeting updates as open problems. KuaiRec is large relative to the academic datasets but still an offline benchmark, not an online intervention.

## 繁中摘要

這篇論文重新檢視 missing-not-at-random feedback 下的推薦 selection-bias correction。傳統 doubly robust（DR）estimator 假設 exact matching：target population 與 evaluation set 的 user-item units 固定且完全相同，隨機性只來自 rating 是否被觀測。但在實際系統中，offline training 與 online evaluation 可能包含不同 users/items。作者因此研究 super-population setting：train/test 的 units 分別抽樣，但 joint feature-rating distribution 保持一致。這不同於 cold start，因為後者的 hot/cold unit distributions 本身就不同。

理論分析顯示，在這種 sampling process 下，傳統 DR estimator 會多出 covariance bias。除了熟悉的 propensity error 與 imputation error 乘積之外，要達到 unbiasedness，還必須使 residual imputation error 與 propensity-weighted observation residual 不相關。因此在 super-population sampling 中，即使 propensity 或 imputed error 本身完全正確，也不一定足以消除偏差；這揭露了 exact-matching 分析無法呈現的額外 bias source。

SuperDR 透過 targeted correction 處理此項額外偏差。它在每個 imputed error 中加入一個 learned scalar，乘上 observation indicator 與 estimated propensity 的差。最佳化修正後的 propensity-weighted imputation loss，可讓 observed empirical covariance 變成零，並以 concentration argument 限制 missing-part covariance。此 correction 擴大 imputation hypothesis space；不需要修正時會退化回原模型，並在論文條件下具有 bias/variance reduction 性質。Joint-learning algorithm 交替更新 corrected imputation model 與 SuperDR prediction loss，相較傳統流程只多一個 scalar parameter。

實驗在 Coat、Yahoo! R3、KuaiRec 模擬 train/test units 部分重疊，並與 propensity、information-bottleneck 及多種 DR baselines 比較。SuperDR 在主要表格的九個 metrics 都是最佳。Coat 的 AUC、NDCG@5、Recall@5 為 0.757、0.667、0.637；Yahoo! R3 為 0.686、0.667、0.463；KuaiRec 的 AUC、NDCG@50、Recall@50 為 0.828、0.640、0.680。當 training 只抽樣 5%-10% users/items、train-test overlap 最低時，優勢最大。相較最強 baseline 的多項改善通過 paired t-test，但不是所有 metrics 都達到統計顯著。

此研究假設 train/test 共享相同 joint feature-rating distribution，並假定其他 distribution shift 可另外透過 reweighting 處理；真實系統的 temporal drift、exposure-policy change 或全新 user population 可能違反這些假設。實驗使用 matrix-factorization features 與 MLP backbone，對現代 deep ranking architectures 的證據仍有限。作者也把 empirical-covariance bound 較鬆，以及交替更新 prediction、imputation、targeting components 的效率列為未解問題。KuaiRec 雖比學術資料集大，仍屬 offline benchmark，而非線上 intervention。

## Notes

- Coat contains 6,960 biased and 4,640 unbiased ratings from 290 users and 300 items.
- Yahoo! R3 contains 311,704 biased and 54,000 unbiased ratings from 15,400 users and 1,000 items.
- KuaiRec contains 4,676,570 watch-ratio records from 1,411 users and 3,327 videos; the experiment selects 201,171 biased training samples and 117,113 unbiased test samples.
- The default super-population simulation samples 50% of training users and items, while the sensitivity analysis varies this ratio from 5% to 90%.
- Experiments use 32-dimensional fixed matrix-factorization features, an MLP prediction backbone, Adam, and an RTX 3090 GPU.
