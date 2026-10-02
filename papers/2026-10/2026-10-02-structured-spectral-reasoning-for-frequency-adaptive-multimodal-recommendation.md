---
date: 2026-10-02
title: "Structured Spectral Reasoning for Frequency-Adaptive Multimodal Recommendation"
authors: "Wei Yang, Rui Zhong, Yiqun Chen, Chi Lu, Peng Jiang"
venue: "NeurIPS 2025"
---

# Structured Spectral Reasoning for Frequency-Adaptive Multimodal Recommendation

- Paper page: https://proceedings.neurips.cc/paper_files/paper/2025/hash/288c9c3c9d214dd61282f885dfbc6117-Abstract-Conference.html
- PDF: https://proceedings.neurips.cc/paper_files/paper/2025/file/288c9c3c9d214dd61282f885dfbc6117-Paper-Conference.pdf
- Local PDF: [../../pdfs/2026-10/2026-10-02-structured-spectral-reasoning-for-frequency-adaptive-multimodal-recommendation.pdf](../../pdfs/2026-10/2026-10-02-structured-spectral-reasoning-for-frequency-adaptive-multimodal-recommendation.pdf)
- Venue: NeurIPS 2025

## English Summary

This paper addresses noise and semantic mismatch in multimodal graph recommendation. Visual, textual, and collaborative features encode different levels of detail, and graph propagation can spread modality-specific artifacts to unrelated nodes. Existing frequency-aware recommenders often apply fixed low-pass filters or static band weights, which may suppress useful local detail while retaining unstable components. Structured Spectral Reasoning (SSR) instead treats frequency bands as structured, context-dependent signals and organizes learning into decomposition, modulation, fusion, and alignment stages.

SSR first maps ID, image, and text features on the user-item graph into a shared spectral coordinate system using the normalized graph Laplacian. Small graphs can use explicit eigendecomposition, while larger graphs use Chebyshev polynomial filter banks. Spectral modes are grouped into approximately equal-energy bands. Spectral Band Masking then drops complete bands during training and minimizes the distance between full-spectrum and masked representations, discouraging dependence on a brittle frequency range. No masking is used at inference.

The Graph HyperSpectral Neural Operator (G-HSNO) uses compact low-rank mixing to model cross-band and cross-modality dependencies, followed by node-dependent gating and scale normalization. Spectral Contrastive Regularization aligns image and text representations within the same band while separating different items or bands. The final objective combines binary cross-entropy, masking consistency, spectral contrastive loss, and parameter regularization. Diagnostic analyses suggest low frequencies preserve stable modality-specific structure, middle frequencies carry stronger shared cross-modal semantics, and high frequencies offer discriminative but noise-sensitive details; cold-start cases consequently place more weight on low and middle bands.

Experiments use the five-core Amazon Baby, Sports, and Clothing datasets with chronological 80/10/10 splits and full-item ranking. SSR is best in all 12 reported Recall@10/20 and NDCG@10/20 combinations. For example, Recall@10 reaches 0.0728, 0.0825, and 0.0708 on Baby, Sports, and Clothing, respectively. In the cold-start subset of users with at most five interactions, SSR also leads every metric and improves Baby Recall@20 from SMORE's 0.1019 to 0.1125. Ablations show losses from removing semantic-aware fusion, G-HSNO, masking, contrastive alignment, or multimodal features. However, the paper reports no error bars or significance tests. Other limitations include additional spectral computation, heuristic and dataset-specific band granularity, a fixed spectral basis that may underfit non-stationary patterns, and evaluation limited to static graphs rather than temporal behavior.

## 繁中摘要

這篇論文處理 multimodal graph recommendation 中的雜訊與語意不一致。Visual、textual、collaborative features 所表達的細節層次不同，graph propagation 還可能把某個 modality 的假訊號擴散到不相關節點。既有 frequency-aware recommender 多採固定 low-pass filter 或 static band weighting，可能一方面壓掉有用的局部細節，另一方面保留不穩定成分。Structured Spectral Reasoning（SSR）則把 frequency bands 視為具有結構且依情境變化的訊號，將學習流程分成 decomposition、modulation、fusion、alignment 四個階段。

SSR 先透過 normalized graph Laplacian，把 user-item graph 上的 ID、image、text features 映射到共同 spectral coordinate system。小圖可直接 eigendecomposition，大圖則以 Chebyshev polynomial filter banks 近似；接著把 spectral modes 分成能量大致相等的 bands。Spectral Band Masking 在訓練時整段遮蔽 frequency bands，並縮小 full-spectrum 與 masked representations 的距離，避免模型依賴單一脆弱頻段；inference 時不使用 masking。

Graph HyperSpectral Neural Operator（G-HSNO）以低秩 mixing 建模 cross-band 與 cross-modality dependencies，再用 node-dependent gating 和 scale normalization 做自適應融合。Spectral Contrastive Regularization 讓同一 band 的 image 與 text representations 對齊，同時區分不同 item 或不同 band。最終 objective 結合 binary cross-entropy、masking consistency、spectral contrastive loss 與 parameter regularization。診斷結果顯示，low-frequency 保留較穩定且 modality-specific 的結構，mid-frequency 具有較強的 shared cross-modal semantics，high-frequency 則提供具辨識力但對雜訊敏感的細節；因此 cold-start 情境會更依賴 low 與 mid bands。

實驗使用經 five-core filtering 的 Amazon Baby、Sports、Clothing，按時間做 80/10/10 切分並採 full-item ranking。SSR 在 12 個 Recall@10/20、NDCG@10/20 組合全部最佳；例如三個資料集的 Recall@10 分別為 0.0728、0.0825、0.0708。在互動數不超過五次的 cold-start 使用者中，SSR 也領先所有指標，Baby Recall@20 從 SMORE 的 0.1019 提升到 0.1125。Ablation 顯示移除 semantic-aware fusion、G-HSNO、masking、contrastive alignment 或 multimodal features 都會降低表現。不過，論文沒有回報 error bars 或 significance tests；其他限制包括額外的 spectral computation、需依資料集調整的 heuristic band granularity、可能無法適應 non-stationary patterns 的固定 spectral basis，以及目前只驗證 static graphs，尚未涵蓋 temporal behavior。

## Notes

- The official implementation is available at https://github.com/llm-ml/SSR.
- The datasets contain 19,445-39,387 users, 7,050-23,033 items, and 139,110-256,308 interactions, with density from 0.026% to 0.101%.
- The paper finds that three or four frequency bands work best; too few limit expressiveness, while too many add noise and overfitting risk.
