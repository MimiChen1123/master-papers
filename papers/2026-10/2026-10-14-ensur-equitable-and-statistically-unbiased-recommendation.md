---
date: 2026-10-14
title: "ENSUR: Equitable and Statistically Unbiased Recommendation"
authors: "Nitin Bisht, Xiuwen Gong, Guandong Xu"
venue: "ICML 2025"
---

# ENSUR: Equitable and Statistically Unbiased Recommendation

- Paper page: https://proceedings.mlr.press/v267/bisht25a.html
- PDF: https://raw.githubusercontent.com/mlresearch/v267/main/assets/bisht25a/bisht25a.pdf
- Local PDF: [../../pdfs/2026-10/2026-10-14-ensur-equitable-and-statistically-unbiased-recommendation.pdf](../../pdfs/2026-10/2026-10-14-ensur-equitable-and-statistically-unbiased-recommendation.pdf)
- Venue: ICML 2025

## English Summary

This paper addresses two credibility problems in recommender systems at once: whether a recommendation set contains the user's truly relevant item with a specified level of confidence, and whether recommendation quality is equitable across user groups. Rather than returning a fixed top-k list, ENSUR wraps an arbitrary black-box relevance model with group-specific, nested prediction sets. It controls the expected miss risk below a user-chosen threshold and bounds group disparity, measured through differences such as Hit Rate or DCG, with separately specified confidence levels.

The formulation extends risk-controlling prediction sets with a fairness-controlling constraint. For each of two known user groups, ENSUR chooses a threshold that minimizes average prediction-set size while requiring both group-wise coverage and bounded cross-group metric disparity. Smaller sets matter because they reduce uncertainty, cognitive load, and serving cost. The framework is model-agnostic: it only needs relevance scores from the underlying recommender and a calibration split, so it can be applied after training without refitting the base model.

Directly searching all pairs of group thresholds is expensive. The Guaranteed User Fairness Algorithm (GUFA) instead derives concentration-based upper confidence bounds for both risk and fairness, then greedily seeks the largest feasible thresholds, which correspond to the smallest nested sets. The paper proves that the selected predictors satisfy the requested risk and fairness controls with their prescribed confidence levels. It also proves a minimum-set-size result relative to alternative predictors whose risk and fairness are no worse under the paper's assumptions.

Experiments apply ENSUR to DeepFM, GMF, MLP, NeuMF, and LightGCN on AmazonOffice, Last.fm, MovieLens, and Book-Crossing, with groups defined by interaction count, region, gender, and age. At the main setting of risk and fairness thresholds 0.20 with error probabilities 0.10, every ENSUR-enhanced model meets both controls across the reported datasets, while base and fairness baselines frequently exceed at least one threshold. ENSUR also produces the smallest average sets and is faster than four compared fairness methods: calibration takes 8, 12, 8, and 15 minutes on the four datasets, respectively, versus 22-135 minutes for the baselines. Parameter studies show the expected trade-off: relaxing risk, fairness, or confidence constraints yields smaller sets. Important limitations are that the analysis assumes known group membership and two disjoint groups, the evaluation is offline with sampled negatives and hand-selected main thresholds, and optimization efficiency depends on the tightness of the derived upper bounds; tighter bounds are left for future work.

## 繁中摘要

這篇論文同時處理推薦系統的兩個可信度問題：推薦集合是否能以指定信心水準包含使用者真正相關的項目，以及不同使用者群組是否獲得公平的推薦品質。ENSUR 不回傳固定大小的 top-k list，而是在任意 black-box relevance model 之外，加上一層依群組調整的 nested prediction sets。它分別以使用者指定的信心水準，將預期遺漏風險控制在門檻以下，並限制群組間 Hit Rate、DCG 等推薦指標的差距。

方法把 risk-controlling prediction sets 延伸為同時含有 fairness-controlling constraint 的最佳化問題。對兩個已知使用者群組，ENSUR 選擇各自的 threshold，在滿足 group-wise coverage 與跨群組差異上限的前提下，最小化平均 prediction-set size。較小的集合可降低推薦不確定性、使用者認知負擔與平台服務成本。此框架與底層模型無關，只需要既有 recommender 的 relevance scores 和 calibration split，因此能在模型訓練完成後套用，不必重新訓練 base model。

直接搜尋所有群組 threshold 組合的成本很高，因此 Guaranteed User Fairness Algorithm（GUFA）先用 concentration inequalities 推導 risk 與 fairness 的 upper confidence bounds，再以 greedy search 尋找最大的可行 thresholds；因 prediction sets 具有 nested 性質，這也對應到最小集合。論文證明所選 predictors 能以預設信心水準滿足 risk 與 fairness controls，並在論文假設下，相對於 risk 與 fairness 不優於它的其他 predictors，具有 minimum-set-size guarantee。

實驗將 ENSUR 套用於 DeepFM、GMF、MLP、NeuMF、LightGCN，使用 AmazonOffice、Last.fm、MovieLens、Book-Crossing 四個資料集，並分別依 interaction count、region、gender、age 分群。在主要設定中，risk 與 fairness thresholds 均為 0.20、error probabilities 均為 0.10；所有 ENSUR-enhanced models 在回報資料集上都符合兩項限制，而 base models 與 fairness baselines 經常至少有一項超標。ENSUR 也產生最小的平均集合，且比四個 fairness methods 更省時間：四個資料集的 calibration 分別需 8、12、8、15 分鐘，baselines 則為 22 至 135 分鐘。Parameter studies 顯示符合預期的取捨：放寬 risk、fairness 或 confidence constraints 會縮小集合。主要限制是分析假設 group membership 已知且只有兩個互斥群組，實驗採離線資料、sampled negatives 與手動選定的主要 thresholds；此外，最佳化效率取決於 upper bounds 是否夠緊，而更緊的 bounds 仍留待後續研究。

## Notes

- Official code: https://github.com/kalpiree/ENSUR
- The four datasets are evaluated over 20 independently sampled trials; training, calibration, and test data use a leave-one-out protocol with 50 sampled non-interacted items per user.
- Group definitions are interaction count (AmazonOffice), region (Last.fm), binary gender (MovieLens), and age above or below 60 (Book-Crossing).
- ENSUR is a post-training calibration layer and does not require access to or modification of the base recommender's training procedure.
