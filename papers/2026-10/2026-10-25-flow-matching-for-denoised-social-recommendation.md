---
date: 2026-10-25
title: "Flow Matching for Denoised Social Recommendation"
authors: "Yinxuan Huang, Ke Liang, Zhuofan Dong, Xiaodong Qu, Tianxiang Wang, Yue Han, Jingao Xu, Bin Zhou, Ye Wang"
venue: "ICML 2025"
---

# Flow Matching for Denoised Social Recommendation

- Paper page: https://proceedings.mlr.press/v267/huang25p.html
- PDF: https://raw.githubusercontent.com/mlresearch/v267/main/assets/huang25p/huang25p.pdf
- Local PDF: [../../pdfs/2026-10/2026-10-25-flow-matching-for-denoised-social-recommendation.pdf](../../pdfs/2026-10/2026-10-25-flow-matching-for-denoised-social-recommendation.pdf)
- Code: https://github.com/AfraThroneUp/RecFlow
- Venue: ICML 2025

## English Summary

This paper addresses noise in graph-based social recommendation, where redundant or missing user-user edges can distort message propagation. The authors argue that social representations are anisotropic: relationships concentrate along particular directions rather than resembling isotropic Gaussian noise. Standard diffusion denoisers are therefore a poor structural match. RecFlow replaces the stochastic, multi-step diffusion trajectory with flow matching, learning a continuous velocity field intended to preserve and recover the directional structure of social graphs.

RecFlow has three parts. Separate LightGCN encoders propagate information over the user-item collaborative graph and the user-user social graph. Its flow module linearly interpolates between Gaussian noise and the social embedding at a uniformly sampled time, then trains a two-layer vector-field estimator with conditional flow-matching loss. An ODE solver integrates the learned reverse-time field to reconstruct a clean user representation. Finally, the reconstructed social signal adjusts the collaborative user embedding, and the whole model is trained jointly with Bayesian Personalized Ranking, conditional flow-matching, and regularization objectives.

Experiments use Ciao, Yelp, and Epinions with a 7:1:2 train-validation-test split and compare against 12 social recommendation baselines. Against the strongest diffusion baseline, RecDiff, RecFlow raises Recall/NDCG from 0.712/0.419 to 0.725/0.438 on Ciao, from 0.597/0.308 to 0.618/0.341 on Yelp, and from 0.460/0.336 to 0.486/0.341 on Epinions. Removing the flow module lowers Recall by roughly 7-13% and NDCG by 13-31% across the datasets; removing conditional guidance also consistently hurts performance. An adaptive ODE solver performs better than Euler, Heun, multistep Heun, and RK4 in the reported comparison, while the residual-error plots show faster convergence than DDPM.

The results support flow matching as a useful denoiser for social recommendation, especially when relational noise has directional structure. However, the evidence remains offline and limited to three public datasets, and the paper does not report latency, memory use with large real-world social graphs, statistical significance, or an online evaluation. Its impact statement also acknowledges possible bias amplification, but fairness is not measured. The robustness subsection contains inconsistent wording about the direction of the noise-scale change, so its qualitative claim should be interpreted more cautiously than the main benchmark and ablation results.

## 繁中摘要

這篇論文處理 graph-based social recommendation 中的雜訊問題：多餘或缺失的 user-user edges 會扭曲 message propagation。作者認為 social representations 具有 anisotropy，也就是使用者關係會集中在特定方向，而非符合 isotropic Gaussian noise；因此一般 diffusion denoiser 與這類結構並不匹配。RecFlow 改以 flow matching 取代隨機且多步的 diffusion trajectory，學習連續 velocity field，目標是保留並恢復 social graph 的方向性結構。

RecFlow 包含三個部分。首先以兩個 LightGCN encoders 分別在 user-item collaborative graph 與 user-user social graph 上傳遞資訊。接著，flow module 在均勻抽樣的時間點，對 Gaussian noise 與 social embedding 做線性 interpolation，並以 conditional flow-matching loss 訓練兩層 vector-field estimator；推論時再用 ODE solver 積分 reverse-time field，重建乾淨的 user representation。最後，重建後的 social signal 會調整 collaborative user embedding，整個模型則共同最佳化 Bayesian Personalized Ranking、conditional flow-matching 與 regularization objectives。

實驗使用 Ciao、Yelp、Epinions，依 7:1:2 切分 training、validation、test sets，並與 12 個 social recommendation baselines 比較。相較最強的 diffusion baseline RecDiff，RecFlow 在 Ciao 將 Recall/NDCG 從 0.712/0.419 提升到 0.725/0.438，在 Yelp 從 0.597/0.308 提升到 0.618/0.341，在 Epinions 從 0.460/0.336 提升到 0.486/0.341。移除 flow module 後，三個 datasets 的 Recall 約下降 7-13%，NDCG 約下降 13-31%；移除 conditional guidance 也都會降低表現。採用 adaptive ODE solver 的結果優於 Euler、Heun、multistep Heun 與 RK4，而 residual-error 圖則顯示 RecFlow 比 DDPM 更快收斂。

結果顯示，當 relational noise 具有方向性結構時，flow matching 是 social recommendation 中有潛力的 denoising 方法。不過，目前證據只來自三個公開 datasets 的 offline evaluation；論文沒有報告大型真實 social graphs 上的 latency、memory cost、statistical significance 或 online evaluation。Impact statement 也承認可能放大 bias，但實驗未衡量 fairness。此外，robustness 小節對 noise scale 變化方向的文字描述前後不一致，因此該段定性結論應比主要 benchmark 與 ablation results 更審慎解讀。

## Notes

- Dataset sizes range from 1,925 users and 23,223 interactions on Ciao to 99,262 users and 672,513 interactions on Yelp; Epinions contains 233,261 items.
- The authors train on an NVIDIA RTX A800 and tune embedding dimensions from 64 to 512 and one to four GNN layers.
- The flow module is conditioned on social embeddings and uses an adaptive ODE solver for reconstruction; the model is optimized jointly with a BPR ranking objective.
- The public implementation is linked from the paper, while the datasets are inherited from the RecDiff repository.
