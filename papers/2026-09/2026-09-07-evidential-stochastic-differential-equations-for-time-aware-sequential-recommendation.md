---
date: 2026-09-07
title: "Evidential Stochastic Differential Equations for Time-Aware Sequential Recommendation"
authors: "Krishna Prasad Neupane, Ervine Zheng, Qi Yu"
venue: "NeurIPS 2024"
---

# Evidential Stochastic Differential Equations for Time-Aware Sequential Recommendation

- Paper page: https://proceedings.neurips.cc/paper_files/paper/2024/hash/7cdbd53dfbcf9a5263227555aac5b9cd-Abstract-Conference.html
- PDF: https://proceedings.neurips.cc/paper_files/paper/2024/file/7cdbd53dfbcf9a5263227555aac5b9cd-Paper-Conference.pdf
- Local PDF: [../../pdfs/2026-09/2026-09-07-evidential-stochastic-differential-equations-for-time-aware-sequential-recommendation.pdf](../../pdfs/2026-09/2026-09-07-evidential-stochastic-differential-equations-for-time-aware-sequential-recommendation.pdf)
- Venue: NeurIPS 2024

## English Summary

This paper studies sequential recommendation when the time gaps between user interactions are irregular. Many sequential recommenders treat adjacent interactions as if they were evenly spaced, but real user behavior can have gaps ranging from seconds to days or longer. The authors argue that a longer inactive interval should increase uncertainty about the user's current preference, and that a recommender should use this uncertainty to guide exploration and ranking.

The proposed model, E-NSDE, combines Neural Stochastic Differential Equations with evidential deep learning. The NSDE component represents user and item states as continuously evolving stochastic processes, which lets the model handle non-uniform interaction intervals. The evidential component estimates predictive uncertainty from user-item interactions. The paper also derives a monotonic relationship between interaction time gap and uncertainty, so longer gaps explicitly push the model toward higher uncertainty.

Experiments on real-world sequential recommendation datasets show that E-NSDE improves top-N recommendation performance compared with strong sequential baselines, and ablation studies support the contribution of its uncertainty-aware components. The model also produces more diverse recommendations when uncertainty is high. The main practical idea is that elapsed time is not just another feature; it should change how confident the recommender is and how much it explores.

## 繁中摘要

這篇論文處理 sequential recommendation 中「互動時間間隔不固定」的問題。許多序列推薦模型把相鄰互動視為等間隔事件，但實際上使用者可能幾秒後又互動，也可能隔了很久才回來。作者的核心觀點是：距離上次互動越久，模型對使用者目前偏好的不確定性應該越高，而推薦策略也應該利用這個不確定性做更好的探索與排序。

作者提出 E-NSDE，把 Neural Stochastic Differential Equations 和 evidential deep learning 結合。NSDE 負責建模使用者與 item representation 隨時間連續演化，適合處理不規則時間間隔；evidential learning 則估計 user-item prediction 的不確定性。論文還推導出互動時間間隔與 epistemic uncertainty 之間的單調關係，讓較長的 inactive interval 對應到較高的不確定性。

在真實資料上的實驗顯示，E-NSDE 相比多個 sequential recommendation baseline 有更好的 top-N 指標，消融實驗也證明 uncertainty-aware 模組有幫助。模型在高不確定性時會推薦更多元的 item。實務上，這篇的重點是：時間間隔不應只是普通特徵，而應該影響推薦模型的信心與探索程度。

## Notes

- Useful for products where user sessions have highly irregular gaps.
- The model links elapsed time and uncertainty instead of treating time only as a timestamp feature.
- The uncertainty estimate can support more exploratory recommendations after long inactivity.
