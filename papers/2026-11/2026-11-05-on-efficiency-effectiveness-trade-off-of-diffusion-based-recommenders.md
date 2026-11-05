---
date: 2026-11-05
title: "On Efficiency-Effectiveness Trade-off of Diffusion-based Recommenders"
authors: "Wenyu Mao, Jiancan Wu, Guoqing Hu, Zhengyi Yang, Wei Ji, Xiang Wang"
venue: "NeurIPS 2025"
---

# On Efficiency-Effectiveness Trade-off of Diffusion-based Recommenders

- Paper page: https://proceedings.neurips.cc/paper_files/paper/2025/hash/8573e433d2ff235a41c64e7e1d37c7a5-Abstract-Conference.html
- PDF: https://proceedings.neurips.cc/paper_files/paper/2025/file/8573e433d2ff235a41c64e7e1d37c7a5-Paper-Conference.pdf
- Local PDF: [../../pdfs/2026-11/2026-11-05-on-efficiency-effectiveness-trade-off-of-diffusion-based-recommenders.pdf](../../pdfs/2026-11/2026-11-05-on-efficiency-effectiveness-trade-off-of-diffusion-based-recommenders.pdf)
- Code: https://github.com/maowenyu-11/TA-Rec
- Venue: NeurIPS 2025

## English Summary

Diffusion-based sequential recommenders generate a representation of the next item by repeatedly denoising a random vector under the guidance of a user's interaction history. Their many reverse steps can be expensive, but simply reducing the number of steps increases discretization error and can weaken preference alignment. This paper proposes TA-Rec, a two-stage training framework designed to make a diffusion recommender generate in one step while preserving or improving recommendation quality.

The pretraining stage adds Temporal Consistency Regularization (TCR) to the usual item-reconstruction objective. For adjacent noisy states at timesteps t and t-1, TCR encourages the denoiser to produce consistent estimates of the clean target item, smoothing the denoising function so that it can map noise directly to an oracle-item embedding. The fine-tuning stage uses Adaptive Preference Alignment (APA), a diffusion preference objective built from a ground-truth next item and a sampled negative item. Its alignment strength decreases when the positive and negative items are similar or when the input contains more noise, reducing aggressive updates on ambiguous preference pairs. At inference, a Transformer encodes the history, one Gaussian-noise vector passes through the denoiser once, and candidate items are ranked by dot product with the generated embedding.

The main evaluation uses YooChoose, KuaiRec, and Zhihu, with HR@20 and NDCG@20 averaged over five runs. TA-Rec is best on all six dataset-metric combinations. Relative to the strongest baseline, its gains range from 7.14% to 31.82% on YooChoose, 4.65% to 7.54% on KuaiRec, and 7.52% to 9.64% on Zhihu. The ablations show that TCR improves one-step generation beyond DDPM and accelerated DDIM variants, while APA and both its timestep-aware and pair-similarity-aware components add further gains. Appendix experiments report consistent improvements on Steam, Beauty, and Toys, and show that the method retains coverage comparable to DreamRec.

The runtime comparison illustrates the practical benefit: on YooChoose, inference takes 6 seconds for TA-Rec versus 23 minutes 14 seconds for 1,000-step DreamRec and 14 seconds for 10-20-step PreferDiff; TA-Rec is similar to SASRec on all three datasets. This is an offline benchmark result rather than a production latency measurement, and the experiments use short histories of length 10 after filtering out sparse items and sequences, so the evidence does not establish performance for cold-start or long-history settings. Training is also not free: the framework has separate pretraining and fine-tuning stages, and TCR evaluates the denoiser twice per pretraining iteration for adjacent timesteps, increasing compute relative to end-to-end methods.

## 繁中摘要

Diffusion-based sequential recommender 會以使用者 interaction history 作為條件，反覆對 random vector 去噪，逐步產生 next-item representation。多個 reverse steps 會造成高推論成本，但直接減少步數又會放大 discretization error，並可能削弱 preference alignment。這篇論文提出 TA-Rec，一個兩階段訓練 framework，目標是在維持或改善推薦品質的同時，讓 diffusion recommender 只需一步即可完成生成。

預訓練階段在一般 item-reconstruction objective 上加入 Temporal Consistency Regularization（TCR）。對 timestep t 與 t-1 的相鄰 noisy states，TCR 要求 denoiser 產生一致的 clean target item estimates，使 denoising function 更平滑，因而能將 noise 直接映射成 oracle-item embedding。Fine-tuning 階段使用 Adaptive Preference Alignment（APA），以 ground-truth next item 和 sampled negative item 建立 diffusion preference objective。當正負 items 很相似，或 input noise 較大時，APA 會降低 alignment strength，避免模型對模糊 preference pairs 做過度激進的更新。Inference 時，Transformer 先編碼 history，一個 Gaussian-noise vector 只通過 denoiser 一次，再以生成 embedding 與候選 items 的 dot product 排名。

主要實驗使用 YooChoose、KuaiRec 與 Zhihu，評估 HR@20 和 NDCG@20，並回報五次執行的平均結果。TA-Rec 在六組 dataset-metric 組合上皆為最佳；相對最強 baseline，YooChoose 提升 7.14% 至 31.82%，KuaiRec 提升 4.65% 至 7.54%，Zhihu 提升 7.52% 至 9.64%。Ablation 顯示，TCR 的單步生成優於 DDPM 與加速後的 DDIM variants；加入 APA，以及同時考慮 timestep 與 pair similarity，也會進一步改善結果。附錄在 Steam、Beauty 與 Toys 上仍得到一致提升，coverage 也與 DreamRec 接近。

Runtime comparison 呈現了實際效益：在 YooChoose 上，TA-Rec inference 為 6 秒，1,000-step DreamRec 為 23 分 14 秒，10-20-step PreferDiff 為 14 秒；TA-Rec 在三個資料集上的時間都接近 SASRec。不過，這些是 offline benchmark 結果，不是 production latency；實驗也將 history length 設為 10，並過濾稀疏 items 和短 sequences，因此尚不能證明模型適用於 cold-start 或 long-history 場景。訓練成本同樣不可忽略：framework 分成 pretraining 和 fine-tuning，且 TCR 在每次預訓練 iteration 中需為相鄰 timesteps 執行兩次 denoiser，比 end-to-end methods 使用更多 compute。

## Notes

- The main datasets contain 128,468 YooChoose sequences, 92,090 KuaiRec sequences, and 11,714 Zhihu sequences.
- Histories are truncated or padded to length 10; items with fewer than five interactions and sequences shorter than three interactions are removed.
- Main results use HR@20 and NDCG@20 and report means and standard deviations over five runs.
- Training and runtime experiments use one Nvidia GeForce RTX 3090.
