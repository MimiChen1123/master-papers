---
date: 2026-10-20
title: "SHARP-Distill: A 68x Faster Recommender System with Hypergraph Neural Networks and Language Models"
authors: "Saman Forouzandeh, Parham Moradi, Mahdi Jalili"
venue: "ICML 2025"
---

# SHARP-Distill: A 68x Faster Recommender System with Hypergraph Neural Networks and Language Models

- Paper page: https://proceedings.mlr.press/v267/forouzandeh25a.html
- PDF: https://raw.githubusercontent.com/mlresearch/v267/main/assets/forouzandeh25a/forouzandeh25a.pdf
- Local PDF: [../../pdfs/2026-10/2026-10-20-sharp-distill-a-68x-faster-recommender-system-with-hypergraph-neural-networks-and-language-models.pdf](../../pdfs/2026-10/2026-10-20-sharp-distill-a-68x-faster-recommender-system-with-hypergraph-neural-networks-and-language-models.pdf)
- Venue: ICML 2025

## English Summary

SHARP-Distill addresses a practical tension in graph-based recommendation: hypergraph neural networks can model high-order user-item relationships, and language models can add semantics from reviews, but deploying both at inference time is expensive. The paper uses a teacher-student framework to transfer this rich information into a much smaller recommender. Its teacher contains separate user and item HGNNs for structural signals, DeBERTa for textual review embeddings, and an MLP prediction head. Cross-modal and intra-domain contrastive objectives align the structural and semantic representations before fusion.

The student is CompactGCN, a single graph-convolution layer without nonlinear activation followed by an MLP. During training, its embeddings are interpolated with teacher embeddings, while hard targets and temperature-scaled soft labels provide prediction supervision. A second distillation channel combines teacher-student embedding similarity with hypergraph positional similarity in user- and item-level contrastive losses. This is intended to preserve topology and high-order dependencies that output-only knowledge distillation would discard. At deployment, the HGNN and DeBERTa teacher are removed and only the 0.5M-parameter student is used.

Experiments cover Yelp and four Amazon review datasets: CDs, Cellphones, Beauty, and Sports. The largest, Amazon CDs, has 71,258 users, 65,443 items, and 1,243,755 reviews. The evaluation reserves 20% of each dataset for validation and 10% for testing, repeats accuracy experiments with ten random seeds, and compares against LightGCN, HCCF, HGAtt, GCGM, SAID, POD, KRD, and LightHGNN. SHARP-Distill obtains the best result in 11 of the 15 main Precision@10, Recall@10, and NDCG@10 dataset-metric combinations. Removing DeBERTa decreases aggregate performance by 20.13% on Yelp and 5.62% on Amazon CDs; removing contrastive learning causes larger drops of 32.35% and 8.49%, respectively.

On Amazon CDs, the student records 9.77 ms inference latency versus 395.45 ms for LightGCN and 668.23 ms for HGNN, corresponding to 40x and 68x speedups; on Yelp it reaches 8.79 ms versus 342.67 ms and 552.34 ms. These measurements use an NVIDIA V100, batch size 1, and average per-query latency over 10,000 runs. The student has 0.5M parameters versus 1.5M for LightGCN and 145M for the teacher, although teacher training takes roughly twice as long as LightGCN and remains an offline prerequisite. Limitations include non-temporal offline splits, dependence on review text and a heavy teacher during training, no reported online A/B test or cold-start-specific evaluation, and privacy risks from processing user-generated reviews. The authors also note that faster personalization can intensify filter bubbles and engagement harms unless deployments add fairness, diversity, transparency, and data-governance safeguards.

## 繁中摘要

SHARP-Distill 處理 graph-based recommendation 的實務取捨：hypergraph neural networks 能捕捉高階 user-item relationships，language models 能從 reviews 補充語意，但兩者同時用於線上 inference 的成本很高。論文以 teacher-student framework 把這些資訊轉移到較小的 recommender。Teacher 包含分別處理 users 與 items 的 HGNNs、產生 review text embeddings 的 DeBERTa，以及 MLP prediction head；融合前再以 cross-modal 與 intra-domain contrastive objectives 對齊 structural 和 semantic representations。

Student 是 CompactGCN，由不含 nonlinear activation 的單層 graph convolution 與 MLP 組成。訓練時，student embeddings 會與 teacher embeddings interpolation，並同時接受 hard targets 與 temperature-scaled soft labels 的 prediction supervision。第二條 distillation channel 把 teacher-student embedding similarity 與 hypergraph positional similarity 結合到 user-level、item-level contrastive losses，目的是保留僅蒸餾 outputs 容易遺失的 topology 與 high-order dependencies。部署時會移除 HGNN 和 DeBERTa teacher，只保留 0.5M parameters 的 student。

實驗涵蓋 Yelp 與四個 Amazon review datasets：CDs、Cellphones、Beauty、Sports。最大規模的 Amazon CDs 有 71,258 users、65,443 items 與 1,243,755 reviews。資料中 20% 用於 validation、10% 用於 testing，accuracy experiments 以十個 random seeds 重複執行；比較方法包括 LightGCN、HCCF、HGAtt、GCGM、SAID、POD、KRD 與 LightHGNN。SHARP-Distill 在主要的 15 個 Precision@10、Recall@10、NDCG@10 dataset-metric combinations 中拿到 11 個最佳結果。移除 DeBERTa 後，Yelp 與 Amazon CDs 的整體表現分別下降 20.13% 與 5.62%；移除 contrastive learning 的降幅更大，分別為 32.35% 與 8.49%。

在 Amazon CDs 上，student inference latency 為 9.77 ms，LightGCN 與 HGNN 分別為 395.45 ms、668.23 ms，相當於 40x 與 68x speedups；Yelp 則為 8.79 ms，兩個 baselines 分別是 342.67 ms 與 552.34 ms。這些數據是在 NVIDIA V100、batch size 1 下，對 10,000 次 runs 的 per-query latency 取平均。Student 為 0.5M parameters，LightGCN 為 1.5M，teacher 為 145M；不過 teacher training 約為 LightGCN 的兩倍，仍是必要的離線前置成本。限制包括非 temporal 的 offline splits、訓練階段依賴 review text 與大型 teacher、未提供 online A/B test 或 cold-start-specific evaluation，以及處理 user-generated reviews 帶來的 privacy 風險。作者也指出，更快的 personalization 可能加劇 filter bubbles 與 engagement harms，實際部署仍需加入 fairness、diversity、transparency 和 data-governance safeguards。

## Notes

- Official software: https://github.com/S-Forouzandeh/SHARP-Distill-----ICML-2026/tree/main
- SHARP stands for Speedy Hypergraph And Review-based Personalised Distillation.
- The main deployment comparison uses the CompactGCN student only; the HGNN + DeBERTa teacher is an offline training component.
- The five datasets contain 85,472 to 1,243,755 reviews and cover local businesses, music, cellphones, beauty products, and sports products.
