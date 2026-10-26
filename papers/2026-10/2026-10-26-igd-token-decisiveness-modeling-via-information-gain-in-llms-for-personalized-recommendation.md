---
date: 2026-10-26
title: "IGD: Token Decisiveness Modeling via Information Gain in LLMs for Personalized Recommendation"
authors: "Zijie Lin, Yang Zhang, Xiaoyan Zhao, Fengbin Zhu, Fuli Feng, Tat-Seng Chua"
venue: "NeurIPS 2025"
---

# IGD: Token Decisiveness Modeling via Information Gain in LLMs for Personalized Recommendation

- Paper page: https://proceedings.neurips.cc/paper_files/paper/2025/hash/707e34efcabd2b9375f7a64019600aa8-Abstract-Conference.html
- PDF: https://proceedings.neurips.cc/paper_files/paper/2025/file/707e34efcabd2b9375f7a64019600aa8-Paper-Conference.pdf
- Local PDF: [../../pdfs/2026-10/2026-10-26-igd-token-decisiveness-modeling-via-information-gain-in-llms-for-personalized-recommendation.pdf](../../pdfs/2026-10/2026-10-26-igd-token-decisiveness-modeling-via-information-gain-in-llms-for-personalized-recommendation.pdf)
- Code: https://github.com/ZJLin2oo1/IGD
- Venue: NeurIPS 2025

## English Summary

This paper studies a token-level mismatch in LLM-based recommendation. Item recommendation is commonly formulated as autoregressive generation of an item's title, yet cross-entropy training and beam search treat every title token as equally useful. Generic or repeated tokens can be easy for the model to predict and receive high logits even when they do little to distinguish one item from another. The authors model item generation as a sequential decision process and define a token's decisiveness as the Information Gain (IG), or reduction in entropy over the candidate item set after that token is observed.

The proposed Information Gain-based Decisiveness-aware Token Handling (IGD) applies this signal in both training and inference. A prefix tree built from training-set item titles supplies the candidate set and empirical item prior for each prefix. During fine-tuning, IGD assigns a reduced weight to zero-IG tokens while retaining full weight for tokens that reduce uncertainty. During decoding, it modifies the cumulative beam-search score using normalized IG so that highly discriminative candidate tokens receive more influence. The method is model-agnostic and is evaluated as an add-on to BIGRec and D3 rather than as a new recommender backbone.

Experiments use Amazon CDs, Games, Toys, and Books with Qwen2.5-1.5B by default. Between 55.96% and 72.97% of title tokens in these datasets have zero IG. On BIGRec, IGD improves average HR@10 by 20.9% and NDCG@10 by 21.5%; on D3, the average gains are 18.9% and 20.1%, respectively. The largest gains occur on Books and Games: D3+IGD raises Books HR@10 from 0.0315 to 0.0424 and NDCG@10 from 0.0228 to 0.0313, while Games improves from 0.0773/0.0477 to 0.0946/0.0598. Ablations show that both tuning and decoding reweighting help, with tuning responsible for most of the gain. Results with LLaMA3-8B and an additional Steam dataset suggest that the effect is not tied to one tokenizer, model size, or domain.

IGD is a simple intervention with a clear interpretation: it reallocates optimization and search effort toward tokens that actually narrow the item space. Its current evidence is nevertheless limited to offline title-generation recommendation. The method requires a prefix tree and training-set item priors, examines text tokens rather than semantic IDs or multimodal tokens, and uses hyperparameters to balance likelihood against decisiveness. The reported main experiments use one fixed random seed without error bars or significance tests, so the stability of the improvements across runs is not established.

## 繁中摘要

這篇論文研究 LLM-based recommendation 中 token 層級的目標錯置。常見做法會把 item recommendation 轉成自回歸生成 item title，但 cross-entropy training 與 beam search 對每個 title token 一視同仁。通用或重複的 tokens 往往容易預測、logit 也高，卻未必能區分不同 items。作者把 item generation 視為 sequential decision process，並以 Information Gain（IG）定義 token decisiveness：觀察該 token 後，candidate item set 的 entropy 降低多少。

作者提出 Information Gain-based Decisiveness-aware Token Handling（IGD），把這個訊號同時用於 training 與 inference。系統先從 training-set item titles 建立 prefix tree，取得各 prefix 對應的 candidate set 與 empirical item prior。Fine-tuning 時，IGD 降低 zero-IG tokens 的 loss weight，對能降低不確定性的 tokens 則保留完整權重；decoding 時，再利用 normalized IG 修改 beam-search cumulative score，增加高辨識力 candidate tokens 的影響。這個方法不綁定特定 model，實驗中是以 add-on 方式套用在 BIGRec 與 D3，而不是另建新的 recommender backbone。

實驗預設使用 Qwen2.5-1.5B，涵蓋 Amazon CDs、Games、Toys、Books。這四個 datasets 中有 55.96% 到 72.97% 的 title tokens 屬於 zero IG。套用在 BIGRec 時，IGD 平均讓 HR@10 提升 20.9%、NDCG@10 提升 21.5%；套用在 D3 時，平均提升分別為 18.9% 與 20.1%。Books 與 Games 的增益最明顯：D3+IGD 將 Books 的 HR@10/NDCG@10 從 0.0315/0.0228 提升到 0.0424/0.0313，Games 則從 0.0773/0.0477 提升到 0.0946/0.0598。Ablation 顯示 tuning 與 decoding reweighting 都有效，但主要增益來自 tuning；LLaMA3-8B 與額外 Steam dataset 的結果也表示效果並非只適用單一 tokenizer、model scale 或 domain。

IGD 的優點是修改幅度小且容易解釋：把 optimization 與 search effort 重新分配給真正能縮小 item space 的 tokens。不過，目前證據限於 offline title-generation recommendation；方法需要 prefix tree 與 training-set item priors，尚未處理 semantic IDs 或 multimodal tokens，並需透過 hyperparameters 平衡 likelihood 與 decisiveness。主要實驗只使用一個固定 random seed，沒有 error bars 或 significance tests，因此尚無法確認多次執行時的穩定性。

## Notes

- Dataset item counts range from 11,037 on Games to 41,722 on Books; all users and items are filtered to have at least five interactions.
- Evaluation uses all-item ranking with HR@5, HR@10, NDCG@5, and NDCG@10.
- The default Qwen2.5-1.5B experiments compare IGD against position normalization and causal fine-tuning as alternative token-handling strategies.
- The LLaMA3-8B study uses 4-bit QLoRA; Steam adds roughly 982,000 interactions and retains improvements over D3.
