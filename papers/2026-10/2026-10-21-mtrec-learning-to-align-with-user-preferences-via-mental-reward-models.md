---
date: 2026-10-21
title: "MTRec: Learning to Align with User Preferences via Mental Reward Models"
authors: "Mengchen Zhao, Yifan Gao, Yaqing Hou, Xiangyang Li, Pengjie Gu, Zhenhua Dong, Ruiming Tang, Yi Cai"
venue: "NeurIPS 2025"
---

# MTRec: Learning to Align with User Preferences via Mental Reward Models

- Paper page: https://proceedings.neurips.cc/paper_files/paper/2025/hash/e530ae20f6433b2a24672fd443d3bd14-Abstract-Conference.html
- PDF: https://proceedings.neurips.cc/paper_files/paper/2025/file/e530ae20f6433b2a24672fd443d3bd14-Paper-Conference.pdf
- Local PDF: [../../pdfs/2026-10/2026-10-21-mtrec-learning-to-align-with-user-preferences-via-mental-reward-models.pdf](../../pdfs/2026-10/2026-10-21-mtrec-learning-to-align-with-user-preferences-via-mental-reward-models.pdf)
- Venue: NeurIPS 2025

## English Summary

Recommenders are commonly trained on implicit feedback such as clicks, but a click does not necessarily mean that the user was satisfied after consuming the item. MTRec addresses this mismatch by introducing a latent "mental reward": the user's internal satisfaction after taking an action. The paper assumes that mental rewards affect subsequent short-term interests and that users tend to maximize their accumulated mental rewards. It models the user, rather than the recommender, as an agent in a Markov decision process and learns the hidden reward function from behavioral trajectories through inverse reinforcement learning.

Because satisfaction can vary even for the same state-action pair, MTRec represents mental reward as a distribution instead of a deterministic scalar. Its Quantile Regression Inverse Q-Learning (QR-IQL) algorithm learns a distributional Q-function through quantile regression, then recovers the reward distribution from the learned Q-values and next-state values. The expected mental rewards become complementary supervision for downstream recommenders. For classification models, an alignment loss rewards predictions associated with higher inferred satisfaction and is added to the usual cross-entropy objective. For RL recommenders, the inferred mental reward is added to the environment reward. This design can wrap multiple architectures without changing their core inference structure.

Offline experiments on Amazon Electronics and Books show broadly consistent AUC and NCIS gains across Wide&Deep, PNN, DeepFM, SASRec, DIN, DIEN, LinRec, and SIGMA, with larger improvements in the long-term-oriented NCIS metric. In Virtual Taobao, adding MTRec raises average simulated CTR from 0.5435 to 0.678 for PPO and from 0.7055 to 0.909 for SAC. An online A/B test on an industrial short-video platform with tens of millions of daily active users reports about a 7% increase in average viewing time over a DCN baseline. The central limitation is identifiability and evaluation: no ground-truth mental-reward labels exist, so the inferred reward is validated only indirectly through behavior correlations and downstream outcomes. Results also depend on the assumption that observed trajectories approximately reflect reward-maximizing user behavior, and the paper does not provide public code or a systematic human-study benchmark.

## 繁中摘要

推薦系統通常以 click 等 implicit feedback 訓練，但 click 不代表使用者看完內容後真的滿意。MTRec 以潛在的「mental reward」描述使用者採取行動後的內在滿意度，藉此處理觀測行為與真實偏好之間的落差。論文假設 mental reward 會影響後續的短期興趣，且使用者傾向最大化累積 mental rewards。方法把使用者而非 recommender 視為 Markov decision process 中的 agent，再利用 inverse reinforcement learning 從 behavioral trajectories 推回隱藏的 reward function。

由於相同 state-action pair 的滿意度仍可能隨環境或偏好變化而不同，MTRec 將 mental reward 建模為 distribution，而不是固定 scalar。其 Quantile Regression Inverse Q-Learning（QR-IQL）透過 quantile regression 學習 distributional Q-function，再由 Q-values 與 next-state values 還原 reward distribution。推論出的 expected mental rewards 會成為下游 recommender 的補充 supervision。對 classification models，方法把偏向高滿意度預測的 alignment loss 加到原本的 cross-entropy objective；對 RL recommenders，則把 mental reward 加到 environment reward。因此它能套用到多種架構，而不需改變核心 inference 流程。

Amazon Electronics 與 Books 的 offline experiments 顯示，Wide&Deep、PNN、DeepFM、SASRec、DIN、DIEN、LinRec、SIGMA 大多能同時改善 AUC 與 NCIS，且偏向長期效益的 NCIS 提升更明顯。在 Virtual Taobao 中，加入 MTRec 後，PPO 的 average simulated CTR 從 0.5435 提升至 0.678，SAC 則從 0.7055 提升至 0.909。於擁有數千萬 daily active users 的工業短影音平台進行 online A/B test 時，相較 DCN baseline，average viewing time 約增加 7%。主要限制在於 identifiability 與 evaluation：mental reward 沒有 ground-truth labels，只能透過行為相關性與下游成效間接驗證；結果也依賴觀測 trajectories 大致反映 reward-maximizing user behavior 的假設，且論文未提供公開程式碼或系統性 human-study benchmark。

## Notes

- The public offline datasets are Amazon Electronics and Books; the interactive simulator is Virtual Taobao.
- The online experiment uses average viewing time as its engagement metric and reports an approximately 7% lift.
- The paper states that code was not publicly available at submission time.
