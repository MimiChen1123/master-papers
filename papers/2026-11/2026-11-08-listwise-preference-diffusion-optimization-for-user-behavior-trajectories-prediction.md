---
date: 2026-11-08
title: "Listwise Preference Diffusion Optimization for User Behavior Trajectories Prediction"
authors: "Hongtao Huang, Chengkai Huang, Junda Wu, Tong Yu, Julian McAuley, Lina Yao"
venue: "NeurIPS 2025"
---

# Listwise Preference Diffusion Optimization for User Behavior Trajectories Prediction

- Paper page: https://proceedings.neurips.cc/paper_files/paper/2025/hash/e9aa0e8679691ba5404c5b0e7caac518-Abstract-Conference.html
- PDF: https://proceedings.neurips.cc/paper_files/paper/2025/file/e9aa0e8679691ba5404c5b0e7caac518-Paper-Conference.pdf
- Local PDF: [../../pdfs/2026-11/2026-11-08-listwise-preference-diffusion-optimization-for-user-behavior-trajectories-prediction.pdf](../../pdfs/2026-11/2026-11-08-listwise-preference-diffusion-optimization-for-user-behavior-trajectories-prediction.pdf)
- Venue: NeurIPS 2025

## English Summary

This paper argues that conventional sequential recommenders are myopic because they predict only the next item, even though a user's preferences and the consequences of recommendations evolve over multiple future actions. It formalizes User Behavior Trajectory Prediction (UBTP): given a user's history, the model predicts an ordered trajectory of the next k interactions and produces a Top-K candidate list at every future position. This setting must model preference drift, causal dependencies among future actions, and uncertainty that compounds over longer horizons.

The proposed Listwise Preference Diffusion Optimization (LPDO) generates the full future trajectory non-autoregressively in a continuous latent space. It concatenates historical context with noisy embeddings of the target trajectory and uses a causal Transformer plus cross-attention to denoise them. The main contribution is to incorporate a Plackett-Luce listwise ranking likelihood into the diffusion evidence lower bound. Instead of optimizing each future position independently, this objective jointly favors the ordered ground-truth trajectory over alternatives at every denoising step, while reconstruction and regularization terms preserve generation stability. The resulting training objective therefore couples diffusion fidelity with structured preference alignment.

The authors also introduce SeqMatch@K, a strict trajectory metric that counts a prediction as correct only when every ground-truth future item appears in the Top-K list at its corresponding position. SeqHR and SeqNDCG aggregate position-wise ranking quality with a geometric mean, while Perplexity measures probabilistic uncertainty. Experiments use Amazon Beauty with trajectory length 3, MovieLens-1M with lengths 5 and 10, and LastFM with lengths 5 and 10. Evaluation ranks against the full item set and compares LPDO with FPMC, SASRec, autoregressive SASRec, STOSA, DiffuRec, DreamRec, PreferDiff, and DCRec.

LPDO is best on every reported main metric, with statistically significant gains over the strongest baseline. On LastFM with length 5, it raises SeqHR@5 from 0.1931 to 0.2507 and SeqMatch@50 from 0.1723 to 0.2357; on MovieLens-1M with length 10, SeqMatch@50 improves from 0.0381 to 0.0447. Ranking loss is essential: removing the listwise term collapses ranking scores to zero in the ablation. LPDO also converges in about 25 epochs versus roughly 33 for DCRec. With one denoising step, its MovieLens-1M inference time is 3.40 seconds, close to SASRec's 3.34 seconds and much faster than DCRec's 12.83 seconds, while retaining better SeqMatch and Perplexity.

The work establishes a useful multi-step benchmark, but the evidence remains offline and may not reflect satisfaction or long-term engagement in a live system. The strict SeqMatch metric can also become increasingly difficult as trajectory length grows, and preprocessing leaves only 1,927 valid Beauty sequences for length 3. LPDO requires manually tuned loss and penalty weights, and its experiments cover trajectories of at most 10 steps, three public datasets, and item interactions without richer contextual features. The authors identify adaptive tuning, online A/B tests, longer trajectories, and richer context as future directions.

## 繁中摘要

這篇論文認為傳統 sequential recommender 只預測下一個 item，忽略使用者偏好與推薦影響會在多個未來行為中持續演變，因此具有 myopic 問題。作者正式定義 User Behavior Trajectory Prediction（UBTP）：給定使用者歷史，模型要預測接下來 k 次互動的有序 trajectory，並在每個未來位置輸出 Top-K candidate list。這個設定需要同時處理 preference drift、未來行為間的 causal dependencies，以及隨預測長度累積的不確定性。

作者提出 Listwise Preference Diffusion Optimization（LPDO），在 continuous latent space 中以 non-autoregressive 方式一次生成完整未來 trajectory。模型將 historical context 與加入雜訊的 target-trajectory embeddings 串接，再使用 causal Transformer 與 cross-attention 逐步 denoise。核心貢獻是把 Plackett-Luce listwise ranking likelihood 納入 diffusion evidence lower bound。它不再獨立最佳化每個未來位置，而是在每個 denoising step 中，讓整個有序 ground-truth trajectory 相對於 alternatives 得到更高 likelihood；reconstruction 與 regularization terms 則維持生成穩定性，因此同時連結 diffusion fidelity 與 structured preference alignment。

論文也提出 SeqMatch@K：只有當每個 ground-truth future item 都出現在對應位置的 Top-K list 時，整條 trajectory 才算匹配。SeqHR 與 SeqNDCG 透過 geometric mean 聚合各位置的 ranking quality，Perplexity 則衡量機率不確定性。實驗包含 trajectory length 3 的 Amazon Beauty、length 5/10 的 MovieLens-1M，以及 length 5/10 的 LastFM；評估使用完整 item set，並與 FPMC、SASRec、autoregressive SASRec、STOSA、DiffuRec、DreamRec、PreferDiff、DCRec 比較。

LPDO 在主要表格的所有 metrics 都是最佳，且相較最強 baseline 的提升具有統計顯著性。LastFM length 5 的 SeqHR@5 從 0.1931 提升到 0.2507，SeqMatch@50 從 0.1723 提升到 0.2357；MovieLens-1M length 10 的 SeqMatch@50 則從 0.0381 提升到 0.0447。Ablation 顯示 ranking loss 不可或缺：移除 listwise term 後，ranking scores 全部降為零。LPDO 約 25 epochs 即收斂，DCRec 約需 33 epochs；只用一個 denoising step 時，MovieLens-1M inference time 為 3.40 秒，接近 SASRec 的 3.34 秒，遠快於 DCRec 的 12.83 秒，同時維持更好的 SeqMatch 與 Perplexity。

這項研究建立了有價值的 multi-step benchmark，但證據仍是 offline evaluation，未必等同真實系統中的 satisfaction 或 long-term engagement。Trajectory 越長，嚴格的 SeqMatch 也越難達成；經 preprocessing 後，Beauty length 3 僅剩 1,927 條有效 sequences。LPDO 需要手動調整 loss ratio 與 penalty factor，實驗最長只涵蓋 10 steps、三個公開 datasets，且未加入更豐富的 contextual features。作者將 adaptive tuning、online A/B tests、更長 trajectories 與 richer context 列為後續方向。

## Notes

- Original dataset sizes: Beauty has 22,363 sequences and 12,101 items; MovieLens-1M has 6,040 sequences and 3,416 items; LastFM has 891 sequences and 1,000 items.
- After trajectory filtering, the evaluation retains 1,927 Beauty sequences, 6,040/5,231 MovieLens-1M sequences for lengths 5/10, and 829/784 LastFM sequences for lengths 5/10.
- The default setup uses 128-dimensional embeddings, four Transformer blocks, 50 diffusion steps for training, one step for inference, and an RTX 3090 GPU.
- Increasing inference denoising steps from 1 to 50 only slightly improves MovieLens-1M SeqMatch while increasing time from 3.40 to 13.46 seconds for length 5.
