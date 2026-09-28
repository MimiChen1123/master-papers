---
date: 2026-09-28
title: "On Efficiency-Effectiveness Trade-off of Diffusion-based Recommenders"
authors: "Wenyu Mao, Jiancan Wu, Guoqing Hu, Zhengyi Yang, Wei Ji, Xiang Wang"
venue: "NeurIPS 2025"
---

# On Efficiency-Effectiveness Trade-off of Diffusion-based Recommenders

- Paper page: https://proceedings.neurips.cc/paper_files/paper/2025/hash/8573e433d2ff235a41c64e7e1d37c7a5-Abstract-Conference.html
- PDF: https://proceedings.neurips.cc/paper_files/paper/2025/file/8573e433d2ff235a41c64e7e1d37c7a5-Paper-Conference.pdf
- Local PDF: [../../pdfs/2026-09/2026-09-28-on-efficiency-effectiveness-trade-off-of-diffusion-based-recommenders.pdf](../../pdfs/2026-09/2026-09-28-on-efficiency-effectiveness-trade-off-of-diffusion-based-recommenders.pdf)
- Venue: NeurIPS 2025

## English Summary

This paper addresses the inference cost of diffusion-based sequential recommenders. Such models encode a user's interaction history, start from Gaussian noise, and iteratively denoise an embedding intended to represent the next item. Reducing the number of reverse steps lowers latency but enlarges the discretization error between the practical discrete trajectory and the underlying continuous stochastic differential equation. TA-Rec is a two-stage framework designed to produce the item embedding in one denoising step without accepting the usual accuracy loss.

During pretraining, Temporal Consistency Regularization (TCR) supplements the standard item-reconstruction objective. It requires the denoiser's outputs at adjacent noisy timesteps to remain close, smoothing the mapping so that an input from any point on the trajectory is projected toward the target item. Under Lipschitz and local smoothness assumptions, the paper bounds one-step generation error by `O(Delta t)`, the same order as the global discretization error of the multi-step approximation. This result explains why temporal consistency can support acceleration, although it depends on assumptions rather than guaranteeing the behavior of every trained network.

During fine-tuning, Adaptive Preference Alignment (APA) applies a diffusion version of direct preference optimization. The observed next item is paired with a sampled non-interacted item. Alignment strength decreases when the positive and negative items are semantically similar or the timestep is highly noisy, avoiding aggressive updates on ambiguous pairs and noisy states. At inference, the history Transformer produces guidance, one denoiser call maps noise to an oracle-item embedding, and all candidate items are ranked by dot product.

Primary experiments use YooChoose, KuaiRec, and Zhihu with chronological 80/10/10 splits, HR@20 and NDCG@20, five repeated runs, and an RTX 3090. TA-Rec is best on all six primary dataset-metric combinations, improving over the strongest baseline by 4.65%-31.82%. Appendix results on Steam, Amazon Beauty, and Amazon Toys show the same direction. Reported full inference times are comparable to SASRec: 6 seconds on YooChoose, 7 seconds on KuaiRec, and 1 second on Zhihu, versus 23:14, 28:02, and 5:04 for 1,000-step DreamRec. However, the offline experiments do not establish production latency or online user impact, and the two-stage training is more expensive than end-to-end training because TCR evaluates adjacent timesteps with two denoiser calls per iteration.

## 繁中摘要

這篇論文處理 diffusion-based sequential recommender 的 inference 成本。此類模型先編碼使用者互動歷史，從 Gaussian noise 開始，透過反覆去噪產生代表下一個物品的 embedding。減少 reverse steps 雖能降低延遲，卻會放大實際離散軌跡與理論 stochastic differential equation 之間的 discretization error。TA-Rec 是兩階段框架，目標是在不承受常見準確度損失的情況下，只用一次 denoising 產生物品 embedding。

Pretraining 階段的 Temporal Consistency Regularization（TCR）加入標準 item-reconstruction objective，要求相鄰 noisy timestep 的 denoiser 輸出保持接近，讓映射更平滑，使軌跡任一位置的輸入都能投影到目標物品。在 Lipschitz 與局部平滑假設下，論文把 one-step generation error 上界定為 `O(Delta t)`，與多步離散近似的 global discretization error 同階。這說明 temporal consistency 為何可能支援加速，但結果依賴理論假設，並不保證每個實際訓練網路都完全符合。

Fine-tuning 階段的 Adaptive Preference Alignment（APA）使用 diffusion 版本的 direct preference optimization。方法把真實下一個物品與一個使用者未互動的抽樣物品組成 preference pair；當正負物品語意相似，或 timestep 的 noise 很高時，alignment strength 會降低，避免對模糊 pair 與 noisy state 做過度更新。Inference 時，歷史 Transformer 產生 guidance，一次 denoiser call 把 noise 映射成 oracle-item embedding，再用 dot product 排序所有候選物品。

主要實驗使用 YooChoose、KuaiRec、Zhihu，依時間做 80/10/10 切分，以 HR@20、NDCG@20 評估，每個方法重複 5 次，硬體為 RTX 3090。TA-Rec 在六個主要資料集與指標組合都最佳，相對最強 baseline 提升 4.65%-31.82%；附錄的 Steam、Amazon Beauty、Amazon Toys 也呈現相同方向。回報的完整 inference 時間接近 SASRec：YooChoose 6 秒、KuaiRec 7 秒、Zhihu 1 秒；1,000-step DreamRec 則分別為 23:14、28:02、5:04。不過，離線實驗不能直接證明 production latency 或線上使用者效果，而且兩階段訓練比 end-to-end 方法昂貴，因為 TCR 每個 iteration 需對相鄰 timestep 執行兩次 denoiser。

## Notes

- Candidate ranking remains a full dot-product comparison between the generated embedding and the item corpus; one-step denoising removes diffusion iterations but not the retrieval stage.
- The main datasets contain 11,714-128,468 sequences and 4,838-9,514 items after filtering items with fewer than five interactions and sequences shorter than three.
- Ablations show gains from both TCR and APA, while adaptive pair- and timestep-aware weighting provides smaller incremental improvements over fixed preference alignment.
