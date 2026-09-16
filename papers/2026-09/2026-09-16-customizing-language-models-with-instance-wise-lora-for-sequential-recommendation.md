---
date: 2026-09-16
title: "Customizing Language Models with Instance-wise LoRA for Sequential Recommendation"
authors: "Xiaoyu Kong, Jiancan Wu, An Zhang, Leheng Sheng, Hui Lin, Xiang Wang, Xiangnan He"
venue: "NeurIPS 2024"
---

# Customizing Language Models with Instance-wise LoRA for Sequential Recommendation

- Paper page: https://proceedings.neurips.cc/paper_files/paper/2024/hash/cd476d01692c508ddf1cb43c6279a704-Abstract-Conference.html
- PDF: https://proceedings.neurips.cc/paper_files/paper/2024/file/cd476d01692c508ddf1cb43c6279a704-Paper-Conference.pdf
- Local PDF: [../../pdfs/2026-09/2026-09-16-customizing-language-models-with-instance-wise-lora-for-sequential-recommendation.pdf](../../pdfs/2026-09/2026-09-16-customizing-language-models-with-instance-wise-lora-for-sequential-recommendation.pdf)
- Venue: NeurIPS 2024

## English Summary

This paper studies LLM-based sequential recommendation, where user behavior sequences are converted into instruction-tuning data and a language model is fine-tuned to predict the next item. Many recent methods use a single LoRA module for all user sequences. The authors argue that this uniform LoRA setup is too coarse because user behavior sequences can represent very different tasks, and forcing them through the same adaptation parameters can create negative transfer.

The proposed method, Instance-wise LoRA (iLoRA), treats sequential recommendation as a multi-task learning problem. Instead of assigning a separate LoRA module to every sequence, which would be impractical, iLoRA integrates the Mixture-of-Experts idea into LoRA. It divides LoRA capacity into multiple experts, uses a conventional sequential recommender to produce a sequence representation, and feeds that representation into a gating network. The gate then generates instance-specific expert weights, dynamically assembling a customized LoRA update for each user sequence while keeping the trainable parameter count close to standard LoRA.

Experiments on LastFM, MovieLens, and Steam compare iLoRA with traditional sequential recommenders and LLM-based recommendation baselines such as TALLRec and LLaRA. iLoRA achieves the strongest HitRatio@1 results, with an average relative improvement of 11.4% over basic LoRA while adding less than 1% relative trainable parameters. Gradient-similarity analysis and ablations support the claim that iLoRA reduces negative transfer and that sequence-representation-guided gating is important. The practical takeaway is that PEFT for recommendation should adapt to user-sequence heterogeneity rather than using one shared LoRA behavior for all sequences.

## 繁中摘要

這篇論文研究 LLM-based sequential recommendation，也就是把使用者行為序列轉成 instruction-tuning 資料，再 fine-tune 語言模型來預測下一個 item。許多近期方法會對所有 user sequences 使用同一個 LoRA module。作者認為這種 uniform LoRA 太粗糙，因為不同使用者序列可能代表非常不同的任務，若共用同一組 adaptation 參數，容易在差異大的序列之間產生 negative transfer。

作者提出 Instance-wise LoRA (iLoRA)，把 sequential recommendation 視為 multi-task learning 問題。它不是為每個 sequence 訓練一個獨立 LoRA，因為那在資源上不可行；而是把 Mixture-of-Experts 的概念整合進 LoRA。iLoRA 將 LoRA capacity 分成多個 experts，先用傳統 sequential recommender 產生 sequence representation，再把這個表示送進 gating network。gate 會為每個使用者序列產生 instance-specific expert weights，動態組合出客製化的 LoRA update，同時讓可訓練參數量接近標準 LoRA。

實驗在 LastFM、MovieLens、Steam 上比較 iLoRA、傳統 sequential recommender，以及 TALLRec、LLaRA 等 LLM-based recommendation baseline。iLoRA 在 HitRatio@1 上表現最好，相比 basic LoRA 平均相對提升 11.4%，但可訓練參數相對增加不到 1%。梯度相似度分析和消融實驗也支持 iLoRA 能降低 negative transfer，且由 sequence representation 引導的 gating 很重要。實務上的重點是：推薦任務中的 PEFT 不應對所有使用者序列套同一種 LoRA 行為，而應該根據序列異質性動態調整。

## Notes

- Useful for LLM-based sequential recommendation systems that fine-tune with LoRA.
- The core idea is parameter-level personalization: different sequences activate different LoRA expert mixtures.
- The method improves recommendation quality without materially increasing trainable parameter count.
