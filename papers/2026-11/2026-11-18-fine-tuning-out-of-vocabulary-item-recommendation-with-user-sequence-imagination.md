---
date: 2026-11-18
title: "Fine-Tuning Out-of-Vocabulary Item Recommendation with User Sequence Imagination"
authors: "Ruochen Liu, Hao Chen, Yuanchen Bei, Qijie Shen, Fangwei Zhong, Senzhang Wang, Jianxin Wang"
venue: "NeurIPS 2024"
---

# Fine-Tuning Out-of-Vocabulary Item Recommendation with User Sequence Imagination

- Paper page: https://proceedings.neurips.cc/paper_files/paper/2024/hash/10d52f5d2ef0f69ac10da7c962fb6db9-Abstract-Conference.html
- PDF: https://proceedings.neurips.cc/paper_files/paper/2024/file/10d52f5d2ef0f69ac10da7c962fb6db9-Paper-Conference.pdf
- Local PDF: [../../pdfs/2026-11/2026-11-18-fine-tuning-out-of-vocabulary-item-recommendation-with-user-sequence-imagination.pdf](../../pdfs/2026-11/2026-11-18-fine-tuning-out-of-vocabulary-item-recommendation-with-user-sequence-imagination.pdf)
- Venue: NeurIPS 2024

## English Summary

This paper studies recommendation for out-of-vocabulary (OOV) items that have content features but no interaction history. Existing cold-start methods generate a one-shot "makeshift" item embedding from content, but this embedding does not necessarily occupy the same behaviorally meaningful space as embeddings learned from user interactions. USIM, the proposed User Sequence IMagination framework, instead refines an initial OOV embedding by imagining a short sequence of users whose interactions would make the item easier to recommend.

USIM formulates this refinement as a Markov decision process. The state contains the current item embedding and a countdown of remaining steps; an action selects a user or terminates. Selecting a user moves the item embedding in the direction of that user's fixed behavioral embedding, mirroring one gradient step on a recommendation objective. The reward combines improvement in distance to the item's known warm embedding during training, improvement in predicted scores for actual interacting users, and a per-step penalty. To make the enormous discrete action space tractable, an exploration set mixes users whose embeddings point toward the target item, randomly sampled users, and the termination action. A recommendation-oriented PPO objective adds known terminal states to train the value network.

Experiments designate 20% of items as OOV on CiteULike and MovieLens and evaluate full-ranking overall, OOV, and in-vocabulary recommendation with MF and NGCF backbones. USIM improves most overall and OOV Recall/NDCG results while preserving IV quality. With MF on CiteULike, overall Recall rises to 0.1926, a 19.00% gain over the strongest baseline, and OOV Recall reaches 0.2753, a 5.00% gain. A two-week production A/B test with 5% of users per group reports gains over ALDI of 4.90% in OOV-item page views, 1.10% in predicted click-through rate, and 13.60% in OOV-item gross merchandise value. Ablations show that targeted and random exploration, the restricted exploration set, and the recommendation-performance reward all matter.

The approach relies on warm items during training because their learned behavioral embeddings and interaction users define rewards and supervision; generalization to truly novel domains therefore depends on how well this training process transfers. The experiments cover only two public datasets and two collaborative-filtering backbones. The authors also identify four sensitive hyperparameters and autoregressive generation as costs. Their online efficiency table reports OOV embedding time of 0.102 seconds for USIM versus 0.044 and 0.047 seconds for MetaEmb and ALDI, although this is an offline one-time item process and content extraction dominates latency. Privacy and representational risks from selecting or encoding users are not substantively evaluated.

## 繁中摘要

這篇論文研究 out-of-vocabulary（OOV）items 的推薦問題：新 item 有 content features，卻沒有 interaction history。既有 cold-start 方法通常從內容一次產生「makeshift」item embedding，但這個向量未必位於由真實 user interactions 學得的 behavioral embedding space。作者提出 User Sequence IMagination（USIM），先產生 OOV item 的初始 embedding，再想像一小段可能與它互動的 user sequence，逐步把 embedding 調整到更適合推薦的位置。

USIM 將 refinement 表示成 Markov decision process。State 包含目前 item embedding 與剩餘步數；action 是選擇一位 user 或終止。選擇 user 後，item embedding 會沿該 user 的固定 behavioral embedding 方向移動，相當於對推薦目標做一次 gradient update。Reward 結合三部分：與訓練期間已知 warm-item embedding 的距離改善、對真實互動 users 的預測改善，以及每一步的 penalty。為了處理極大的離散 action space，exploration set 混合朝向 target item 的 users、隨機 users 與 termination action；recommendation-oriented PPO 另加入已知 terminal states 來訓練 value network。

實驗在 CiteULike 與 MovieLens 將 20% items 設為 OOV，並以 MF 與 NGCF backbones 進行 full-ranking overall、OOV 與 in-vocabulary recommendation 評估。USIM 在保留 IV 品質的同時，改善大部分 overall/OOV Recall 與 NDCG。以 CiteULike 的 MF 為例，overall Recall 達 0.1926，比最佳 baseline 提升 19.00%；OOV Recall 為 0.2753，提升 5.00%。兩週 production A/B test 每組使用 5% users；相較 ALDI，USIM 的 OOV-item page views、predicted CTR 與 gross merchandise value 分別提升 4.90%、1.10% 與 13.60%。Ablation 顯示 targeted/random exploration、受限 exploration set 與 recommendation-performance reward 都有實質貢獻。

此方法在訓練時依賴 warm items，因為已學得的 behavioral embeddings 與 interaction users 是 reward 和 supervision 的來源；它對真正新領域的效果取決於這套訓練流程能否轉移。公開實驗也只有兩個 datasets 與兩種 collaborative-filtering backbones。作者指出四個敏感 hyperparameters 與 autoregressive generation 會增加成本；online efficiency table 中，USIM 產生 OOV embedding 需 0.102 秒，而 MetaEmb、ALDI 分別為 0.044、0.047 秒，不過這是離線一次性流程，且 content extraction 才是主要延遲。論文未實質評估 user selection 或 user representations 可能造成的 privacy 與 representation risks。

## Notes

- CiteULike contains 5,551 users, 16,980 items, and 204,986 interactions; MovieLens contains 6,040 users, 3,883 items, and 1,000,210 interactions.
- Interactions for the 80% IV items are split 8:1:1; OOV interactions are split equally between validation and test.
- The public experiments compare against eight dropout- or generation-based OOV recommenders.
- Statistical markers in the main table compare USIM with the strongest baseline at p < 0.05 or p < 0.01.
