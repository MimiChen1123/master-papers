---
date: 2026-08-21
title: "Understanding and Improving Adversarial Collaborative Filtering for Robust Recommendation"
authors: "Kaike Zhang, Qi Cao, Yunfan Wu, Fei Sun, Huawei Shen, Xueqi Cheng"
venue: "NeurIPS 2024"
---

# Understanding and Improving Adversarial Collaborative Filtering for Robust Recommendation

- Paper page: https://proceedings.neurips.cc/paper_files/paper/2024/hash/da07cfa60cc883c5ee94ba899383bb6d-Abstract-Conference.html
- PDF: ../../pdfs/2026-08/2026-08-21-understanding-and-improving-adversarial-collaborative-filtering.pdf
- Venue: NeurIPS 2024
- Code: https://github.com/Kaike-Zhang/PamaCF

## English Summary

This paper studies adversarial collaborative filtering (ACF), a family of methods that add adversarial perturbations to user and item embeddings during training to make collaborative filtering recommenders more robust against poisoning attacks. Prior work has shown empirically that ACF can both improve robustness and improve normal recommendation performance, which is unusual compared with adversarial training in computer vision, where robustness often hurts clean accuracy. The paper's main contribution is a theoretical explanation for this phenomenon: under a simplified Gaussian recommender setting, ACF can obtain lower recommendation error than standard CF under both clean and poisoned data.

Building on this analysis, the authors argue that a single global perturbation magnitude is not ideal because users have different embedding scales and therefore different tolerances to perturbation. They propose Personalized Magnitude Adversarial Collaborative Filtering (PamaCF), which assigns perturbation magnitudes dynamically based on each user's embedding scale. This makes adversarial training more user-specific and better aligned with the theoretical error-reduction bounds. Experiments show that PamaCF improves both recommendation performance and robustness against multiple poisoning attacks; the paper reports a 13.84% average performance improvement over the backbone model and a 44.92% reduction in attack success ratio compared with the strongest baseline defense.

## 繁中摘要

這篇論文研究 adversarial collaborative filtering (ACF)，也就是在 collaborative filtering 的 user/item embedding 上加入 adversarial perturbation 進行訓練，以提升推薦系統面對 poisoning attack 時的穩健性。過去實驗已經觀察到 ACF 不只可以提升抗攻擊能力，也常常能提升一般推薦表現；這和 computer vision 裡 adversarial training 經常犧牲 clean accuracy 的現象不同。作者的核心貢獻是提供理論解釋：在簡化的 Gaussian recommender setting 下，ACF 相比傳統 CF 可以在 clean data 和 poisoned data 中都達到更低的 recommendation error。

基於理論分析，作者進一步指出固定的全域 perturbation magnitude 並不理想，因為不同 user 的 embedding scale 不同，能承受的擾動強度也不同。因此他們提出 PamaCF，根據每個 user 的 embedding scale 動態設定個人化的 perturbation magnitude。這讓 adversarial training 更符合不同使用者的表示尺度，也更貼近理論推導出的 error reduction bounds。實驗結果顯示，PamaCF 在推薦表現和抗 poisoning attack 兩方面都優於既有 defense 方法；論文報告相對 backbone model 平均提升 13.84% 推薦表現，並相對最佳 baseline defense 降低 44.92% attack success ratio。

## Notes

- Main question: why ACF can improve both clean recommendation performance and robustness against poisoning attacks.
- Main theory: ACF can reduce recommendation error more than standard CF under both clean and poisoned data settings.
- Main method: PamaCF personalizes adversarial perturbation magnitudes according to user embedding scales.
- Practical relevance: useful for recommender systems exposed to fake-user injection or other poisoning attacks.
- This paper is a good robustness-focused complement to the previous CF and sequential recommendation papers in this repo.
