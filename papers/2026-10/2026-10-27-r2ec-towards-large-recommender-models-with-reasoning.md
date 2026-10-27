---
date: 2026-10-27
title: "R2ec: Towards Large Recommender Models with Reasoning"
authors: "Runyang You, Yongqi Li, Xinyu Lin, Xin Zhang, Wenjie Wang, Wenjie Li, Liqiang Nie"
venue: "NeurIPS 2025"
---

# R²ec: Towards Large Recommender Models with Reasoning

- Paper page: https://proceedings.neurips.cc/paper_files/paper/2025/hash/5a05d477fef5a43c805d3377700efa40-Abstract-Conference.html
- PDF: https://proceedings.neurips.cc/paper_files/paper/2025/file/5a05d477fef5a43c805d3377700efa40-Paper-Conference.pdf
- Local PDF: [../../pdfs/2026-10/2026-10-27-r2ec-towards-large-recommender-models-with-reasoning.pdf](../../pdfs/2026-10/2026-10-27-r2ec-towards-large-recommender-models-with-reasoning.pdf)
- Code and checkpoints: https://github.com/YRYangang/RRec
- Venue: NeurIPS 2025

## English Summary

This paper asks whether a large recommender model can learn to reason before ranking items without relying on a separate teacher or human-written reasoning traces. Existing reasoning-augmented recommenders often use multiple models or stages, which increases memory and latency and can leave the generated rationale weakly coupled to the final recommendation. R²ec instead unifies explicit reasoning and item ranking in one decoder-only model and trains the complete reasoning-then-recommendation trajectory with reinforcement learning.

The model adds two task-specific heads to a shared backbone. The language-modeling head autoregressively generates a reasoning sequence from the user's interaction history. The final hidden state then enters a recommendation head, which scores every candidate by its inner product with cached item embeddings derived from item descriptions. This discriminative head permits item-catalog updates by changing the embedding table rather than retraining an item tokenizer. RecPO samples multiple reasoning trajectories per user and optimizes them with a clipped policy objective. Its fused reward combines a dominant discrete NDCG term with a small continuous target-item softmax-similarity term, providing finer distinctions when different trajectories produce the same ranking. All sampled paths update reasoning, while only the highest-advantage path contributes the final recommendation-action gradient.

Experiments use full-catalog ranking on Amazon Musical Instruments, CDs and Vinyl, and Video Games, evaluated with Hit Rate and NDCG at 5, 10, and 20. With Gemma2-2B-Instruct, R²ec reaches H@10/N@10 of 0.0397/0.0203 on Instruments, 0.0804/0.0472 on CDs, and 0.0531/0.0271 on Games. Relative to the best baseline for each metric, the reported H@10 gains are 77.23%, 71.43%, and 24.07%, respectively; marked improvements are statistically significant at p < 0.05. Removing reasoning lowers the aggregate metrics by roughly 15%, and replacing the tightly coupled recommendation head with a classification head causes a much larger decline. The ranking reward is more important than the similarity reward, but their weighted combination is generally strongest.

R²ec reports an average single-query latency of 1.67 seconds on one RTX 3090, compared with 1.90 seconds for LangPTune, 4.62 for D3, and 5.23 for LLaRA; vLLM reduces R²ec latency to 0.0945 seconds, though SASRec remains faster at 0.014 seconds. Additional Gemma-9B, Electronics, GoodReads, and MovieLens results support broader applicability. Important caveats remain: explicit autoregressive reasoning still adds latency, training uses four RTX 3090 GPUs, and the study relies on LoRA rather than full-parameter fine-tuning. The sampled rationales are useful for analysis but should not automatically be treated as faithful causal explanations of model decisions.

## 繁中摘要

這篇論文探討：large recommender model 能否在不依賴額外 teacher model 或人工 reasoning traces 的情況下，先推理再排序 items。既有 reasoning-augmented recommenders 往往需要多個 models 或多階段流程，不只增加 memory 與 latency，產生的 rationale 也可能和最終 recommendation 缺乏緊密連結。R²ec 改以單一 decoder-only model 統一 explicit reasoning 與 item ranking，並透過 reinforcement learning 最佳化完整的 reasoning-then-recommendation trajectory。

模型在共享 backbone 上加入兩個 task-specific heads。Language-modeling head 根據使用者 interaction history 自回歸生成 reasoning sequence；最後一個 hidden state 再交給 recommendation head，與由 item descriptions 建立並快取的 item embeddings 做 inner product，對所有 candidates 評分。這個 discriminative head 讓 item catalog 更新時只需修改 embedding table，不必重新訓練 item tokenizer。RecPO 會為每位使用者抽樣多條 reasoning trajectories，再以 clipped policy objective 最佳化。它的 fused reward 以 discrete NDCG 為主，加入小比例的 target-item softmax similarity，讓產生相同 ranking 的 trajectories 仍可獲得細緻區分。所有 sampled paths 都會更新 reasoning，但只有 advantage 最高的路徑會提供最終 recommendation action 的 gradient。

實驗在 Amazon Musical Instruments、CDs and Vinyl、Video Games 上做 full-catalog ranking，以 Hit Rate 與 NDCG@5/10/20 評估。使用 Gemma2-2B-Instruct 時，R²ec 在 Instruments 的 H@10/N@10 為 0.0397/0.0203，CDs 為 0.0804/0.0472，Games 為 0.0531/0.0271。相較每個 metric 的最佳 baseline，三個 datasets 的 H@10 分別提升 77.23%、71.43%、24.07%；表中標記的提升在 p < 0.05 下達統計顯著。移除 reasoning 後，整體 metrics 約下降 15%；把緊密耦合的 recommendation head 換成 classification head，退步更明顯。Ranking reward 比 similarity reward 更重要，但兩者加權組合通常最佳。

在單張 RTX 3090、batch size 1 的測試中，R²ec 平均單次 query latency 為 1.67 秒，LangPTune 為 1.90 秒、D3 為 4.62 秒、LLaRA 為 5.23 秒；使用 vLLM 後 R²ec 可降到 0.0945 秒，但仍慢於 SASRec 的 0.014 秒。額外的 Gemma-9B、Electronics、GoodReads、MovieLens 結果支持其跨規模與跨 domain 適用性。主要限制是 explicit autoregressive reasoning 仍增加 latency，訓練需要四張 RTX 3090，且實驗採用 LoRA 而非 full-parameter fine-tuning。產生的 rationales 雖可供分析，也不應直接視為模型決策的忠實 causal explanations。

## Notes

- The three primary datasets contain 7,701-29,230 users and roughly 10,000-12,000 items; histories are truncated to the latest 20 actions and split 80/10/10.
- The default backbones are Gemma2-2B-Instruct and Qwen2.5-3B-Instruct, fine-tuned with LoRA for at most three epochs.
- RecPO uses four sampled trajectories by default, temperature 1.5, top-K 200, NDCG@1000 reward, and a 0.05 weight on continuous similarity.
- Training uses four NVIDIA RTX 3090 GPUs, with one reserved for vLLM trajectory generation and three for policy optimization.
