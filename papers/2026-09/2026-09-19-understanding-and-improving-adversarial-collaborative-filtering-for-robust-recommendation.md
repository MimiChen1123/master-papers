---
date: 2026-09-19
title: "Understanding and Improving Adversarial Collaborative Filtering for Robust Recommendation"
authors: "Kaike Zhang, Qi Cao, Yunfan Wu, Fei Sun, Huawei Shen, Xueqi Cheng"
venue: "NeurIPS 2024"
---

# Understanding and Improving Adversarial Collaborative Filtering for Robust Recommendation

- Paper page: https://proceedings.neurips.cc/paper_files/paper/2024/hash/da07cfa60cc883c5ee94ba899383bb6d-Abstract-Conference.html
- PDF: https://proceedings.neurips.cc/paper_files/paper/2024/file/da07cfa60cc883c5ee94ba899383bb6d-Paper-Conference.pdf
- Local PDF: [../../pdfs/2026-09/2026-09-19-understanding-and-improving-adversarial-collaborative-filtering-for-robust-recommendation.pdf](../../pdfs/2026-09/2026-09-19-understanding-and-improving-adversarial-collaborative-filtering-for-robust-recommendation.pdf)
- Venue: NeurIPS 2024

## English Summary

This paper investigates why adversarial collaborative filtering (ACF) can improve both recommendation quality and resistance to poisoning attacks, unlike the familiar clean-accuracy tradeoff often observed in adversarial training for computer vision. ACF trains a collaborative-filtering model against worst-case perturbations to learned user and item embeddings. Using a simplified Gaussian single-item recommender, the authors prove that, under stated constraints on perturbation size and embedding distributions, one adversarial-training step produces lower recommendation error than a standard CF step after the same pretraining, in both clean and poisoned settings.

The theoretical error-reduction bounds reveal that users should not all receive the same perturbation magnitude. Each user has a maximum useful magnitude, and that limit is positively related to the scale of the user's embedding. Increasing perturbation strength within the valid range improves the bounds, whereas exceeding it can hurt recommendation quality. Based on this result, the paper proposes Personalized Magnitude Adversarial Collaborative Filtering (PamaCF). It computes a bounded user-specific coefficient from the user's embedding norm relative to the population average and scales the adversarial perturbation accordingly, allowing users with larger embeddings to receive stronger perturbations while retaining a shared global magnitude parameter.

Experiments cover Gowalla, Yelp2018, and MIND; Matrix Factorization is the main backbone, with supplementary LightGCN and NeuMF results. The evaluation includes Random and Bandwagon heuristic attacks plus DP and Rev optimization-based black-box attacks, using a 1% attack budget. Across clean and poisoned settings, PamaCF improves average Recall@20 and NDCG@20 over the backbone by 13.84% and 22.04%. Against target-item promotion, it reduces average T-HR@50 and T-NDCG@50 by 49.92% and 43.73% relative to the best baseline, indicating lower attack success. The method is broadly stable across attack types, while detection-based defenses can degrade when attacks differ from their supervised training pattern. The main caveat is that the formal guarantees rely on a Gaussian single-item model; extending the analysis beyond collaborative filtering, including sequential recommendation, remains open.

## 繁中摘要

這篇論文研究為什麼對抗式協同過濾（ACF）能同時提升推薦品質與抵抗資料 poisoning attack 的能力，這與電腦視覺對抗訓練常見的乾淨資料準確率取捨不同。ACF 會針對學到的使用者與物品 embedding 加入最壞情況擾動，再進行協同過濾模型訓練。作者先在簡化的 Gaussian 單物品推薦模型上證明：當擾動大小與 embedding 分布符合特定條件時，在相同預訓練進度後，對抗訓練的一步更新會比標準 CF 更新得到更低的推薦錯誤，而且這個結論同時適用於乾淨與被污染的資料。

推薦錯誤下降的理論界限顯示，不應對所有使用者採用相同擾動強度。每位使用者都有一個有效的最大擾動範圍，而這個上限與其 embedding 尺度正相關；在有效範圍內提高擾動可改善理論界限，但超過上限反而會傷害推薦品質。據此，作者提出 Personalized Magnitude Adversarial Collaborative Filtering（PamaCF）。它根據使用者 embedding norm 相對於全體平均的大小，計算有界的個人化係數，再縮放對抗擾動，使 embedding 較大的使用者可接受較強擾動，同時保留一個全域強度參數。

實驗使用 Gowalla、Yelp2018 與 MIND，主要骨幹是 Matrix Factorization，附錄也驗證 LightGCN 與 NeuMF。攻擊包含 Random、Bandwagon 兩種啟發式方法，以及 DP、Rev 兩種最佳化式黑箱攻擊，攻擊預算為 1%。在乾淨與污染資料情境中，PamaCF 相較原始骨幹模型，平均 Recall@20 與 NDCG@20 分別提升 13.84% 與 22.04%。針對目標物品推廣攻擊，相較最佳基準防禦，平均 T-HR@50 與 T-NDCG@50 分別下降 49.92% 與 43.73%，表示攻擊成功率降低。PamaCF 在不同攻擊類型間維持較穩定的防禦效果；相對地，依賴監督資料的偵測式防禦，在攻擊模式偏離訓練資料時可能退化。主要限制是正式理論建立在 Gaussian 單物品模型上，未來仍需推廣到更一般的 CF 與序列推薦場景。

## Notes

- Dataset sizes after preprocessing: Gowalla has 29,858 users and 40,981 items; Yelp2018 has 31,668 users and 38,048 items; MIND has 141,920 users and 36,214 items.
- Lower T-HR and T-NDCG indicate a stronger defense because they measure how often the attacker's target items enter genuine users' recommendation lists.
- The paper reports that excessively large adversarial-training weight can reduce recommendation performance even after defense performance has stabilized, so both perturbation magnitude and adversarial weight require validation.
