---
date: 2026-10-05
title: "Fading to Grow: Growing Preference Ratios via Preference Fading Discrete Diffusion for Recommendation"
authors: "Guoqing Hu, An Zhang, Shuchang Liu, Wenyu Mao, Jiancan Wu, Xun Yang, Xiang Li, Lantao Hu, Han Li, Kun Gai, Xiang Wang"
venue: "NeurIPS 2025"
---

# Fading to Grow: Growing Preference Ratios via Preference Fading Discrete Diffusion for Recommendation

- Paper page: https://proceedings.neurips.cc/paper_files/paper/2025/hash/c5c12c9f344276b8a98fdf60ac88f5f5-Abstract-Conference.html
- PDF: https://proceedings.neurips.cc/paper_files/paper/2025/file/c5c12c9f344276b8a98fdf60ac88f5f5-Paper-Conference.pdf
- Local PDF: [../../pdfs/2026-10/2026-10-05-fading-to-grow-growing-preference-ratios-via-preference-fading-discrete-diffusion-for-recommendation.pdf](../../pdfs/2026-10/2026-10-05-fading-to-grow-growing-preference-ratios-via-preference-fading-discrete-diffusion-for-recommendation.pdf)
- Venue: NeurIPS 2025

## English Summary

This paper argues that common diffusion recommenders are mismatched with the discrete, ranking-oriented structure of recommendation data. Item-level methods add continuous Gaussian noise to dense embeddings and may overlook explicit negative signals, while score-level methods diffuse one-hot vectors under restrictive probability-simplex constraints. PreferGrow instead operates directly on the discrete item corpus and learns log preference ratios between items, connecting diffusion modeling to pairwise ranking and negative sampling.

In the forward preference-fading process, the observed positive item is retained with a time-dependent probability or replaced according to a fading matrix. A replacement acts like a sampled negative item, so perturbation does not require a Gaussian, Bernoulli, or other assumed noise prior. The paper shows that an idempotent fading matrix makes the process Markovian and reversible, and derives a rank-one closed form when fading converges to a common non-preference state. Different parameterizations yield point-wise, pair-wise, and hybrid objectives corresponding to interpretable negative-sampling schemes.

PreferGrow uses a SASRec encoder for the user history and trains a network with score-entropy loss to estimate user-conditioned preference ratios at each timestep. The authors show that the score-entropy gradient has the same descent direction and optimum as a soft-label binary cross-entropy objective, supporting its use for ranking. During reverse generation, the model starts from a non-preference item and iteratively grows the preference signal using the estimated ratios. Training also drops the user condition with some probability to learn a non-preference-user embedding; at inference, contrasting conditional and unconditional ratios strengthens personalization without retraining.

Experiments use MovieLens, Steam, Amazon Beauty, Toys, and Sports with chronological 80/10/10 user splits and full-item ranking. Hybrid PreferGrow is best across every reported HR and NDCG setting; for example, on Steam its HR@20/NDCG@20 are 0.1413/0.0628, versus 0.1159/0.0394 for the strongest competing values. Re-evaluation over five seeds reports significant NDCG@5 gains with `p < 0.001`. Ablations support pair-wise ratios and non-preference-user guidance. The trade-off is cost: on Steam, PreferGrow trains for 480 epochs and performs 20 inference steps, versus 61 epochs and one step for SASRec. Its optimized loss and inference are `O(N)` in corpus size, which is still impractical for billions of items; the authors propose Semantic IDs and higher-rank fading matrices as future remedies.

## 繁中摘要

這篇論文認為，常見 diffusion recommender 與推薦資料的離散、排序導向本質並不匹配。Item-level 方法對 dense embeddings 加入 continuous Gaussian noise，可能忽略明確的 negative signals；score-level 方法則在 probability simplex 的限制下擴散 one-hot vectors，最佳化較困難。PreferGrow 改為直接在離散 item corpus 上運作，學習 item 之間的 log preference ratios，讓 diffusion modeling 自然連結 pairwise ranking 與 negative sampling。

在 forward preference-fading process 中，觀察到的 positive item 會依 timestep 決定保留機率，否則根據 fading matrix 被其他 item 取代。被替換的 item 可視為 sampled negative，因此不需要預設 Gaussian、Bernoulli 或其他 noise prior。論文證明 idempotent fading matrix 可使此過程具備 Markov property 與 reversibility；當 fading 收斂到共同的 non-preference state 時，還能得到 rank-one closed form。不同參數化方式可形成 point-wise、pair-wise 與 hybrid objectives，分別對應具物理意義的 negative-sampling schemes。

PreferGrow 以 SASRec 編碼 user history，並用 score-entropy loss 訓練網路，在各 timestep 估計 user-conditioned preference ratios。作者證明 score-entropy gradient 與 soft-label binary cross-entropy 具有相同下降方向與 optimum，支持其用於 ranking。Reverse generation 從 non-preference item 開始，再根據估計 ratios 逐步長回偏好訊號。訓練時也會以一定機率移除 user condition，學習 non-preference-user embedding；inference 時結合 conditional 與 unconditional ratios 強化 personalization，不需重新訓練。

實驗使用 MovieLens、Steam、Amazon Beauty、Toys、Sports，依使用者時間序列做 80/10/10 切分並採 full-item ranking。Hybrid PreferGrow 在所有回報的 HR 與 NDCG 設定皆最佳；例如 Steam 的 HR@20/NDCG@20 為 0.1413/0.0628，而各 baseline 的最強值為 0.1159/0.0394。五個 random seeds 的重跑結果也顯示 NDCG@5 提升達到 `p < 0.001`。Ablation 支持 pair-wise ratios 與 non-preference-user guidance 的貢獻。代價則是計算成本：Steam 上 PreferGrow 訓練 480 epochs 並執行 20 個 inference steps，SASRec 只需 61 epochs 與一步；即使最佳化後的 loss 與 inference 對 corpus size 為 `O(N)`，面對數十億 item 仍不實際，作者因此把 Semantic IDs 與 higher-rank fading matrices 列為未來方向。

## Notes

- The official implementation is available at https://github.com/Hugo-Chinn/PreferGrow.
- The five datasets range from 6,040 to 39,795 users, 3,883 to 18,357 items, and 138,444 to 2,949,605 interactions.
- The final 50% of training contributes only about a 5% NDCG@5 gain, suggesting that curriculum-style timestep sampling could reduce redundant optimization.
