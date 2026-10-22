---
date: 2026-10-22
title: "Counterfactual Implicit Feedback Modeling"
authors: "Chuan Zhou, Lina Yao, Haoxuan Li, Mingming Gong"
venue: "NeurIPS 2025"
---

# Counterfactual Implicit Feedback Modeling

- Paper page: https://proceedings.neurips.cc/paper_files/paper/2025/hash/1436e87a58b3e6ac177450bd10721726-Abstract-Conference.html
- PDF: https://proceedings.neurips.cc/paper_files/paper/2025/file/1436e87a58b3e6ac177450bd10721726-Paper-Conference.pdf
- Local PDF: [../../pdfs/2026-10/2026-10-22-counterfactual-implicit-feedback-modeling.pdf](../../pdfs/2026-10/2026-10-22-counterfactual-implicit-feedback-modeling.pdf)
- Venue: NeurIPS 2025

## English Summary

Implicit feedback creates two coupled problems. First, an unclicked item is positive-unlabeled: the user may dislike it, or may simply never have seen it. Second, exposure is missing not at random because popular or frequently recommended items are more likely to receive clicks regardless of their true relevance. Counter-IF reframes relevance prediction as the counterfactual question, "Would this user click this item if exposed to it?" Exposure is treated as a partially missing treatment, observed clicks as outcomes, and the target relevance as the potential outcome under forced exposure.

The method separates user-item pairs into four principal strata. Definitely Positive (DP) pairs are observed clicks; Highly Exposed (HE) pairs are unclicked but inferred to have been exposed; Highly Unexposed (HU) pairs are inferred not to have been exposed; and Unknown (UN) pairs have insufficient confidence for exposure imputation. To produce these groups, Counter-IF encloses most positive pairs in a kernel-based hypersphere, assigns nearby negative pairs to HE, faraway negatives to HU, and the remainder to UN. A representation network then combines pointwise cross-entropy on DP and HE, pairwise ordering constraints across the four groups, and integral probability metric regularization that aligns their representation distributions. The paper derives a generalization bound whose controllable terms correspond to these factual, ranking, and distribution-balancing losses.

Experiments on Yahoo! R3 and Coat compare Counter-IF with exposure, propensity, PU, and pairwise-learning baselines using NDCG, Recall, and MAP at 3, 5, and 8. Counter-IF is best on almost every reported metric; for example, Yahoo NDCG@5 rises from the strongest baseline's 0.611 to 0.625, while Coat Recall@5 rises from 0.462 to 0.478. Five-run means and standard deviations are reported, with many gains statistically significant. Ablations show that pointwise loss, pairwise loss, and Wasserstein/IPM balancing each contribute. Important caveats are that the implicit data are simulated from explicit ratings rather than collected exposure logs, evaluation uses only two relatively small benchmarks, and group assignments depend on manually selected HE/HU proportions and feature-space distance. The kernel hypersphere also has quadratic cost in positive samples, although the appendix evaluates random Fourier feature and Nyström approximations.

## 繁中摘要

Implicit feedback 同時帶來兩個彼此相關的問題。第一，未點擊 item 屬於 positive-unlabeled：使用者可能不喜歡，也可能根本沒看過。第二，exposure 是 missing not at random，因為熱門或經常被推薦的 items 即使與使用者真實興趣不強，也更容易得到 clicks。Counter-IF 把 relevance prediction 改寫成 counterfactual question：「如果讓這位使用者看到某個 item，他會不會點擊？」方法將 exposure 視為部分缺失的 treatment、觀測 click 視為 outcome，而目標 relevance 則是強制 exposure 下的 potential outcome。

方法把 user-item pairs 分成四個 principal strata。Definitely Positive（DP）是已觀測 click；Highly Exposed（HE）是未點擊但推測已曝光；Highly Unexposed（HU）是推測未曝光；Unknown（UN）則是 exposure imputation 信心不足。Counter-IF 先用 kernel-based hypersphere 包住大部分 positive pairs，把鄰近的 negative pairs 分到 HE、最遠的一部分分到 HU，其餘歸入 UN。接著 representation network 在 DP 與 HE 上使用 pointwise cross-entropy，以四群之間的相對關係建立 pairwise ordering constraints，並加入 integral probability metric regularization 對齊不同群組的 representation distributions。論文推導的 generalization bound 中，可控制項正好對應 factual、ranking 與 distribution-balancing losses。

實驗在 Yahoo! R3 與 Coat 上，以 NDCG、Recall、MAP 的 @3、@5、@8 指標，比較 exposure、propensity、PU 與 pairwise-learning baselines。Counter-IF 幾乎在所有指標上最佳；例如 Yahoo NDCG@5 從最強 baseline 的 0.611 提升至 0.625，Coat Recall@5 從 0.462 提升至 0.478。結果回報五次實驗的 mean 與 standard deviation，許多提升具有統計顯著性。Ablation 顯示 pointwise loss、pairwise loss 與 Wasserstein/IPM balancing 都有貢獻。主要限制是 implicit data 由 explicit ratings 模擬，而非真實 exposure logs；只在兩個較小 benchmark 上評估；分群依賴手動設定的 HE/HU proportions 與 feature-space distance。Kernel hypersphere 對 positive samples 也有 quadratic cost，雖然 appendix 另外測試了 random Fourier feature 與 Nyström approximations。

## Notes

- Code: https://github.com/zhouchuanCN/NeurIPS25-Counter-IF
- The training data simulate clicks from explicit ratings, while the provided unbiased test sets support debiased evaluation.
- The authors identify end-to-end learning of the exposure thresholds as a future direction.
