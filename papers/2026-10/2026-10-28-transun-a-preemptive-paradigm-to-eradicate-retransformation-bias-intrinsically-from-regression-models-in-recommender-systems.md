---
date: 2026-10-28
title: "TranSUN: A Preemptive Paradigm to Eradicate Retransformation Bias Intrinsically from Regression Models in Recommender Systems"
authors: "Jiahao Yu, Haozhuang Liu, Yeqiu Yang, Lu Chen, Jian Wu, Yuning Jiang, Bo Zheng"
venue: "NeurIPS 2025"
---

# TranSUN: A Preemptive Paradigm to Eradicate Retransformation Bias Intrinsically from Regression Models in Recommender Systems

- Paper page: https://proceedings.neurips.cc/paper_files/paper/2025/hash/ce3e23a212815cc1f9b7cf2b3490d715-Abstract-Conference.html
- PDF: https://proceedings.neurips.cc/paper_files/paper/2025/file/ce3e23a212815cc1f9b7cf2b3490d715-Paper-Conference.pdf
- Local PDF: [../../pdfs/2026-10/2026-10-28-transun-a-preemptive-paradigm-to-eradicate-retransformation-bias-intrinsically-from-regression-models-in-recommender-systems.pdf](../../pdfs/2026-10/2026-10-28-transun-a-preemptive-paradigm-to-eradicate-retransformation-bias-intrinsically-from-regression-models-in-recommender-systems.pdf)
- Venue: NeurIPS 2025

## English Summary

This paper identifies retransformation bias in regression-based recommender systems. Highly skewed targets such as watch time, transaction value, and lifetime value are often transformed before mean-squared-error training so that optimization converges more smoothly. The model then estimates the conditional mean in the transformed space, but applying the inverse transform does not generally recover the conditional mean of the original target. For convex inverse transforms such as those induced by log or square-root transforms, Jensen's inequality implies systematic underestimation. Existing corrections are usually post-hoc, adding calibration or processing after model scoring.

TranSUN makes the correction part of the model. Alongside the transformed-MSE branch, it trains an auxiliary branch to predict the ratio between the original target and the back-transformed prediction. A stop-gradient operation prevents this auxiliary loss from changing the main branch, allowing the two objectives to be optimized independently; multiplying the back-transformed prediction by the learned ratio yields an estimator of the original conditional mean. The paper further generalizes this idea into Generalized TranSUN (GTS), a family that combines a conditional point loss with a dynamically generated linear correction. Under the stated formulation, conditional linearity rather than merely adding a bias branch is the mechanism that provides the unbiasedness guarantee. GTS can also be attached to existing regression models as a debiasing module.

On synthetic distributions, TranSUN keeps signed relative error below roughly 0.7% across linear, logarithmic, square, and arctangent transformations, while nonlinear transformed-MSE baselines can show substantial under- or overestimation. On CIKM16, LogSUN reduces total ratio error from 0.3451 for LogMSE to 0.0123 and improves NRMSE from 0.6189 to 0.5625; on DTMart it reaches the best reported NRMSE and NMAE among the compared regression methods. Adding GTS to WLR, ZILN, MDME, and OptDist reduces their TRE and MRE by more than 70% in the reported CIKM16 tests. Results on a proprietary GMV dataset show similar improvements, particularly for high-value samples.

The method is deployed in Taobao's product and short-video recommendation scenarios. In product recommendation, LogSUN improves GMV by 1.06% over LogMAE and 1.02% over LogMSE; in short video, it improves GMV by 1.83% and GMV per impression by 1.57% over LogMAE, with all reported confidence intervals excluding zero. The online model adds modest cost: training speed falls 2.7%, mean latency changes from 27.8 ms to 28.1 ms, and GPU resources increase 5%. Limitations are that experiments focus on right-skewed targets and debiasing can slightly reduce overall XAUC, exposing a trade-off between value calibration and ranking order.

## 繁中摘要

這篇論文指出 regression-based recommender systems 中長期被忽略的 retransformation bias。Watch time、transaction value、lifetime value 等 targets 通常高度偏斜，因此常先做 transformation，再用 mean squared error 訓練，使最佳化更平滑。然而，模型學到的是 transformed space 中的 conditional mean，直接套用 inverse transform 通常無法還原原始 target 的 conditional mean。對 log 或 square-root transform 所對應的 convex inverse transform，Jensen's inequality 會導致系統性低估。既有方法多半是 post-hoc correction，需要在 model scoring 後再加 calibration 或額外處理。

TranSUN 把修正機制直接放進模型。除了 transformed-MSE 主分支，它新增 auxiliary branch，學習原始 target 與 back-transformed prediction 之間的比例。`stop_gradient` 阻止 auxiliary loss 回傳到主分支，讓兩個 objectives 可獨立最佳化；推論時把 back-transformed prediction 乘上學到的比例，即可估計原始 conditional mean。作者進一步提出 Generalized TranSUN（GTS），以 conditional point loss 搭配動態生成的 linear correction。依論文推導，提供 unbiasedness guarantee 的核心是 conditional linearity，而不是單純增加 bias branch；GTS 也能作為 debiasing module 接到既有 regression models。

在 synthetic distributions 上，TranSUN 對 linear、logarithmic、square、arctangent transformations 的 signed relative error 都維持在約 0.7% 以內，而 nonlinear transformed-MSE baselines 可能出現明顯低估或高估。在 CIKM16 上，LogSUN 將 LogMSE 的 total ratio error 從 0.3451 降到 0.0123，NRMSE 由 0.6189 改善為 0.5625；在 DTMart 上，其 NRMSE 與 NMAE 也是比較方法中最佳。將 GTS 套用到 WLR、ZILN、MDME、OptDist 後，CIKM16 測試中的 TRE 與 MRE 都降低超過 70%。專有 GMV dataset 也呈現類似改善，尤其是高價值 samples。

這個方法已部署於 Taobao 的商品與短影音推薦場景。商品推薦中，LogSUN 相較 LogMAE 讓 GMV 提升 1.06%，相較 LogMSE 提升 1.02%；短影音場景中，相較 LogMAE，GMV 提升 1.83%、GMV per impression 提升 1.57%，而且所有報告的 confidence intervals 都不跨過零。線上成本相對有限：training speed 降低 2.7%，mean latency 從 27.8 ms 變為 28.1 ms，GPU resources 增加 5%。主要限制是目前實驗集中在 right-skewed targets，且 debiasing 可能讓整體 XAUC 小幅下降，顯示 value calibration 與 ranking order 之間存在 trade-off。

## Notes

- Public evaluation uses CIKM16 for dwell-time prediction and DTMart for market-mix regression, plus a proprietary e-commerce GMV dataset.
- TRE and MRE measure aggregate and sample-level relative bias; NRMSE, NMAE, XAUC, and NDCG provide complementary accuracy and ranking views.
- Product A/B tests run for one week with LogSUN serving 15% traffic; the short-video test runs for one month with 6% traffic per arm.
- The paper provides TensorFlow-style reference code in its appendix but does not link a separate public implementation repository.
