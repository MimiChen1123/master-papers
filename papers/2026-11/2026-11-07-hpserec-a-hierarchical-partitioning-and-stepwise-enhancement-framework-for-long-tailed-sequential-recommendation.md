---
date: 2026-11-07
title: "HPSERec: A Hierarchical Partitioning and Stepwise Enhancement Framework for Long-tailed Sequential Recommendation"
authors: "Xiaolong Xu, Xudong Zhao, Haolong Xiang, Xuyun Zhang, Wei Shen, Hongsheng Hu, Lianyong Qi"
venue: "NeurIPS 2025"
---

# HPSERec: A Hierarchical Partitioning and Stepwise Enhancement Framework for Long-tailed Sequential Recommendation

- Paper page: https://proceedings.neurips.cc/paper_files/paper/2025/hash/a6b3466b787dbfc4fadd9a611c9ee40b-Abstract-Conference.html
- PDF: https://proceedings.neurips.cc/paper_files/paper/2025/file/a6b3466b787dbfc4fadd9a611c9ee40b-Paper-Conference.pdf
- Local PDF: [../../pdfs/2026-11/2026-11-07-hpserec-a-hierarchical-partitioning-and-stepwise-enhancement-framework-for-long-tailed-sequential-recommendation.pdf](../../pdfs/2026-11/2026-11-07-hpserec-a-hierarchical-partitioning-and-stepwise-enhancement-framework-for-long-tailed-sequential-recommendation.pdf)
- Code: https://github.com/bolunxier123/HPSERec
- Venue: NeurIPS 2025

## English Summary

HPSERec addresses the long-tail problem in sequential recommendation, where a small number of popular items receive most interactions while sparse tail items are poorly represented. Existing methods commonly define the top 20% of items as the head and transfer information directly from head to tail. The paper argues that a fixed split ignores dataset-specific interaction distributions, while the large representation gap between head and tail can turn direct transfer into negative transfer. HPSERec therefore replaces the binary head-tail split with multiple data-dependent levels and transfers knowledge step by step between adjacent levels.

The framework has three modules. The Distribution Balancing module sorts items by interaction frequency and uses a nonlinear imbalance score plus a partition-size penalty to divide them into several subsets through dynamic programming. Each expert receives a cumulative item range: the first focuses on the sparsest tail items, and later experts progressively include more popular items until the final expert models the full catalog. The Feedforward module uses adjacent-expert knowledge distillation so tail-focused experts guide increasingly global experts without crossing a large capability gap. The Feedback module then reverses the direction: entropy-regularized optimal transport and Sinkhorn iterations softly align user representations from adjacent experts, allowing global preference information to refine tail-focused representations. Training alternates between these feedforward and feedback stages.

Experiments use Yelp, Amazon Beauty, and Amazon Music with SASRec as the main backbone and compare against BERT4Rec, CITIES, MELT, RLMRec, LLMInit, and LLM-ESR. Results are averaged over five random seeds after hyperparameter selection, and reported improvements over the strongest baseline use a two-sided t-test with p < 0.05. HPSERec obtains overall HR@10/NDCG@10 of 0.5281/0.3665 on Beauty, 0.6827/0.4231 on Yelp, and 0.6592/0.4786 on Music. Its HR@10 exceeds the strongest baseline, LLM-ESR, by 6.8%, 10.3%, and 10.6%, respectively. Tail-item gains are especially large: on Music, HR@10 rises from LLM-ESR's 0.3318 to 0.4425, while head-item HR@10 also improves slightly from 0.8961 to 0.8989.

Ablations show that distribution-aware partitioning contributes the largest gain, while feedforward distillation and feedback alignment provide complementary improvements. HPSERec also improves tail users even without a user-specific tail module because better item embeddings propagate into the shared representation space. Important limitations remain: evaluation ranks the target against 100 sampled negatives rather than the full catalog; the framework introduces several sensitive hyperparameters and multiple experts; and the dynamic-programming partitioner has relatively high computational complexity. The authors therefore position the current method for moderate-sized catalogs and suggest optimized or incremental partitioning for large-scale deployment.

## 繁中摘要

HPSERec 處理 sequential recommendation 的 long-tail 問題：少數熱門 items 集中大部分 interactions，而稀疏 tail items 的 representations 學得較差。既有方法常直接把互動數最高的 20% items 定義為 head，再將 head 資訊轉移到 tail。作者指出，固定比例無法反映不同 datasets 的互動分布；head 與 tail 的 representation gap 過大時，直接 transfer 反而可能造成 negative transfer。因此 HPSERec 不再只切成 head/tail 兩組，而是依資料特性建立多個層級，並在相鄰層級間逐步傳遞知識。

Framework 包含三個 modules。Distribution Balancing module 先依互動頻率排序 items，再結合非線性 imbalance score 與 partition-size penalty，透過 dynamic programming 分成多個 subsets。每個 expert 使用累積式 item range：第一個 expert 專注最稀疏的 tail items，後續 experts 逐步納入較熱門 items，最後一個 expert 覆蓋完整 catalog。Feedforward module 透過相鄰 experts 的 knowledge distillation，讓 tail-focused expert 引導越來越完整的 global expert，避免跨越過大的能力差距。Feedback module 則反向傳遞資訊，利用 entropy-regularized optimal transport 與 Sinkhorn iterations，在相鄰 experts 間 soft-align user representations，讓 global preference 回頭改善 tail-focused representations。訓練過程交替執行 feedforward 與 feedback stages。

實驗使用 Yelp、Amazon Beauty、Amazon Music，以 SASRec 為主要 backbone，並和 BERT4Rec、CITIES、MELT、RLMRec、LLMInit、LLM-ESR 比較。完成 hyperparameter selection 後，各方法以五個 random seeds 訓練；相較最佳 baseline 的提升使用雙尾 t-test，p < 0.05。HPSERec 在 Beauty、Yelp、Music 的整體 HR@10/NDCG@10 分別為 0.5281/0.3665、0.6827/0.4231、0.6592/0.4786；HR@10 相較最強 baseline LLM-ESR 分別提升 6.8%、10.3%、10.6%。Tail-item 增益尤其明顯：Music 的 HR@10 從 LLM-ESR 的 0.3318 提升到 0.4425，head-item HR@10 也由 0.8961 小幅提高到 0.8989。

Ablation 顯示，distribution-aware partitioning 帶來最大增益，而 feedforward distillation 與 feedback alignment 則有互補效果。HPSERec 即使沒有專門處理 tail users 的 module，仍能改善 tail-user 表現，原因是更好的 item embeddings 會透過共享 representation space 影響 user representations。限制方面，評估是將 ground truth 和 100 個 sampled negatives 排序，並非 full-catalog ranking；framework 也增加多個敏感 hyperparameters 與多組 experts，而 dynamic-programming partitioner 的運算複雜度偏高。因此作者認為目前較適合中等規模 catalog，大型部署仍需更有效率或 incremental 的 partitioning 方法。

## Notes

- Dataset statistics after filtering: Beauty has 52,204 users, 57,289 items, and 394,908 interactions; Yelp has 4,722 users, 15,720 items, and 192,214 interactions; Music has 20,165 users, 20,356 items, and 132,595 interactions.
- The default setup uses four item subsets, 128-dimensional embeddings, Adam with a learning rate of 1e-4, and two RTX 3090 GPUs.
- Group-level reporting still uses the conventional top-20% definition for analysis, even though model training uses the proposed distribution-aware multi-subset partitioning.
- The full Music ablation improves overall HR@10 from 0.5431 for the base configuration to 0.6524 when all three modules are enabled.
