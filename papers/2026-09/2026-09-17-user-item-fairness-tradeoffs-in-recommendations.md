---
date: 2026-09-17
title: "User-item fairness tradeoffs in recommendations"
authors: "Sophie Greenwood, Sudalakshmee Chiniah, Nikhil Garg"
venue: "NeurIPS 2024"
---

# User-item fairness tradeoffs in recommendations

- Paper page: https://proceedings.neurips.cc/paper_files/paper/2024/hash/cf836efd32fd53493e02d26670f04d46-Abstract-Conference.html
- PDF: https://proceedings.neurips.cc/paper_files/paper/2024/file/cf836efd32fd53493e02d26670f04d46-Paper-Conference.pdf
- Local PDF: [../../pdfs/2026-09/2026-09-17-user-item-fairness-tradeoffs-in-recommendations.pdf](../../pdfs/2026-09/2026-09-17-user-item-fairness-tradeoffs-in-recommendations.pdf)
- Venue: NeurIPS 2024

## English Summary

This paper studies the tension between user fairness, item fairness, and recommendation quality. It formulates recommendation as a constrained optimization problem: the system maximizes the minimum normalized utility received by any user while requiring every item to receive at least a specified fraction of the best achievable minimum item utility. This framework makes the "price of item fairness" explicit and permits the authors to characterize the structure of optimal recommendation policies.

The main theoretical result is that preference diversity can produce "free fairness." When different groups prefer different items, exposure can be distributed more evenly without substantially reducing user utility. In contrast, homogeneous users create a sharper tradeoff because exposing less-preferred items directly harms nearly everyone. The paper also analyzes preference uncertainty. For cold-start users whose preferences are estimated from population averages, item-fairness constraints can, in the worst case, route unpopular items toward those users and make the loss caused by misestimation arbitrarily large, even when the objective includes user fairness.

The empirical study prototypes an arXiv paper recommender using pre-2020 author histories and 14,307 computer-science papers posted in 2020. TF-IDF and SPECTER representations generate user-paper utilities, while later citations validate that the similarity scores contain useful preference signals. Across sampled markets, moderate item-fairness guarantees have little average cost to user fairness, but the tradeoff becomes steep as the constraint approaches maximal item fairness. Homogeneous user groups experience larger costs than diverse groups, matching the theory. Preference misestimation already causes substantial harm in the experiment, but item-fairness constraints do not further increase that harm on average. The practical conclusion is that fairness effects are context dependent: platforms should evaluate subgroup diversity and individual cold-start outcomes rather than deploy a fairness constraint as a context-free guarantee.

## 繁中摘要

這篇論文研究推薦系統中使用者公平、物品公平與推薦品質三者之間的衝突。作者把推薦建模成受限制的最佳化問題：系統在確保每個物品至少獲得一定比例之最佳最低效用的前提下，最大化所有使用者中最低的正規化效用。這個框架明確定義了「物品公平的代價」，也讓作者能分析最佳推薦策略的結構。

核心理論結果是，偏好多樣性可能帶來「免費的公平」。當不同使用者群偏好不同物品時，系統可以更平均地分配曝光，同時幾乎不降低使用者效用；若使用者偏好高度同質，讓較不受歡迎的物品獲得曝光便會直接傷害大多數使用者，因此公平取捨更尖銳。論文也分析偏好估計不準確的情況。對於只能以群體平均偏好估計的冷啟動使用者，物品公平限制在最壞情況下可能把其他人不喜歡的物品分配給他們，使估計誤差造成的效用損失任意放大，即使目標函數同時考慮使用者公平也無法完全避免。

實驗部分建立了一個 arXiv 論文推薦器，以 2020 年以前的作者發表紀錄建模偏好，候選物品則是 2020 年發布的 14,307 篇電腦科學論文。作者使用 TF-IDF 與 SPECTER 表示產生使用者與論文之間的效用，並以後續引用驗證相似度分數確實包含有效的偏好訊號。結果顯示，中等程度的物品公平保證，平均而言對使用者公平的成本很小；但當限制接近最大物品公平時，取捨會快速惡化。偏好同質的使用者群所付出的成本也比多樣化群體高，與理論一致。實驗中，偏好誤估本身已造成明顯傷害，但物品公平限制平均而言沒有再進一步放大這項傷害。實務上的重點是：公平限制的效果高度依賴情境，平台應個別評估使用者群的偏好多樣性與冷啟動使用者的結果，而不能把加入公平限制視為不需驗證的通用保證。

## Notes

- In the arXiv prototype, more than 47% of candidate papers have less than a 0.0001% probability of being recommended to any user under the unconstrained baseline, illustrating the item-exposure problem.
- The empirical user-fairness cost remains relatively small for item-fairness levels up to about 0.9, then rises sharply near the maximal constraint.
- The model assumes one recommendation per user and shared user-item utility; the authors identify these as limitations and call for extensions to ranked lists, alternative fairness definitions, and total-platform-utility constraints.
