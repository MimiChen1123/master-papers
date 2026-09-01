---
date: 2026-09-01
title: "Data-efficient Fine-tuning for LLM-based Recommendation"
authors: "Xinyu Lin, Wenjie Wang, Yongqi Li, Shuo Yang, Fuli Feng, Yinwei Wei, Tat-Seng Chua"
venue: "SIGIR 2024"
---

# Data-efficient Fine-tuning for LLM-based Recommendation

- Paper page: https://doi.org/10.1145/3626772.3657807
- PDF: https://arxiv.org/pdf/2401.17197
- Local PDF: [../../pdfs/2026-09/2026-09-01-data-efficient-fine-tuning-for-llm-based-recommendation.pdf](../../pdfs/2026-09/2026-09-01-data-efficient-fine-tuning-for-llm-based-recommendation.pdf)
- Venue: SIGIR 2024

## English Summary

This paper addresses the cost of fine-tuning large language models for recommendation. LLM-based recommenders often need frequent adaptation because item catalogs and user behavior change quickly, but full-data fine-tuning is expensive. The authors frame this as a data pruning problem: select a small, representative subset of recommendation training samples that still lets the LLM adapt effectively.

The proposed method, DEALRec, uses two complementary scores. The influence score estimates how much removing each sample would affect empirical risk, using a smaller traditional recommender as a surrogate model to avoid repeatedly fine-tuning the LLM. The effort score compensates for the gap between the surrogate recommender and the LLM by measuring how much effort the LLM needs to fit each sample, using the gradient norm of the sample loss with respect to LLM parameters.

By combining influence and effort, DEALRec selects samples that are both representative of the full dataset and important for LLM adaptation. Experiments on Games, MicroLens-50K, and Book with LLM-based recommender backbones show that few-shot fine-tuning on selected samples can match or surpass full-data fine-tuning. A headline result is that using only about 2% of samples can outperform full-data fine-tuning while reducing time cost by roughly 97%.

## 繁中 Summary

這篇論文處理 LLM-based recommendation 的 fine-tuning 成本問題。這類推薦模型通常需要頻繁適應新的 item catalog 和 user behavior，但使用完整資料 fine-tune LLM 成本很高。作者把問題定義成 data pruning：從推薦訓練資料中挑出少量具代表性的 samples，讓 LLM 仍能有效適應推薦任務。

作者提出 DEALRec，使用兩種互補分數。Influence score 估計移除某個 sample 對 empirical risk 的影響，並用較小的傳統 recommender 作為 surrogate model，避免反覆 fine-tune LLM。Effort score 則用來補足 surrogate recommender 和 LLM 之間的差距，透過 sample loss 對 LLM parameters 的 gradient norm，衡量 LLM 擬合該 sample 需要多少 effort。

透過結合 influence 和 effort，DEALRec 能挑出既能代表完整資料、又對 LLM adaptation 重要的 samples。作者在 Games、MicroLens-50K 和 Book 三個資料集，以及 LLM-based recommender backbones 上實驗，結果顯示用 selected samples 做 few-shot fine-tuning 可以達到甚至超過 full-data fine-tuning。關鍵結果是，只使用約 2% samples 就能超過 full-data fine-tuning，並降低約 97% 的時間成本。

## Notes

- This paper is relevant when LLM-based recommenders must be refreshed frequently with new interaction data.
- DEALRec treats data selection as part of the training pipeline, not just a generic coreset problem.
- The influence score gives representativeness, while the effort score makes the selected subset more LLM-aware.
