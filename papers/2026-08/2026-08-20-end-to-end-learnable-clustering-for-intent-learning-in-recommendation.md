---
date: 2026-08-20
title: "End-to-end Learnable Clustering for Intent Learning in Recommendation"
authors: "Yue Liu, Shihao Zhu, Jun Xia, Yingwei Ma, Jian Ma, Xinwang Liu, Shengju Yu, Kejun Zhang, Wenliang Zhong"
venue: "NeurIPS 2024"
---

# End-to-end Learnable Clustering for Intent Learning in Recommendation

- Paper page: https://proceedings.neurips.cc/paper_files/paper/2024/hash/0b5669c3b07bb8429af19a7919376ff5-Abstract-Conference.html
- PDF: ../../pdfs/2026-08/2026-08-20-end-to-end-learnable-clustering-for-intent-learning-in-recommendation.pdf
- Venue: NeurIPS 2024
- Code: https://github.com/yueliu1999/ELCRec

## English Summary

This paper focuses on intent learning for recommendation, where the goal is to infer latent user intents from historical behavior sequences and use those intents to improve item recommendation. Prior intent-learning approaches often follow an EM-like workflow: first cluster user behavior embeddings to infer intents, then train or refine behavior representations with self-supervised objectives, repeating these steps alternately. The paper argues that this alternating process is cumbersome, hard to scale because clustering must run over full data, and suboptimal because representation learning and clustering are optimized separately.

The proposed method, ELCRec, turns intent learning into an end-to-end learnable clustering problem. It encodes user behavior sequences, treats cluster centers as learnable neural parameters representing latent intents, and trains them jointly with the recommender through a clustering loss that both separates different intent centers and pulls behavior embeddings toward the relevant centers. The authors also add intent-assisted contrastive learning, using the learned cluster centers as self-supervision signals for representation learning. Across benchmark datasets, ELCRec consistently improves over sequential recommendation and intent-learning baselines; on the Beauty dataset, it improves NDCG@5 by 8.9% over the runner-up while reducing computational cost by 22.5%. The paper also reports deployment in a large industrial recommendation system with 130 million page views, showing practical value beyond offline benchmarks.

## 繁中摘要

這篇論文處理推薦系統中的 intent learning：如何從使用者歷史行為序列中學出潛在意圖，並用這些意圖改善推薦。既有 intent learning 方法常用類似 EM 的交替最佳化流程，先對使用者行為 embedding 做 clustering 來得到 latent intents，再用 self-supervised learning 更新行為表示，反覆交替進行。作者指出這種流程有兩個問題：第一，clustering 需要在完整資料上執行，面對大型工業資料時容易有記憶體和時間瓶頸；第二，行為表示學習和意圖學習被分開最佳化，可能造成次佳表現，也增加部署複雜度。

ELCRec 的核心做法是把 clustering 本身變成可端到端學習的神經網路模組。模型先編碼使用者行為序列，接著把 cluster centers 設成可訓練參數，這些中心代表不同 latent intents。訓練時的 clustering loss 一方面推開不同 intent center，使意圖彼此解耦；另一方面拉近行為 embedding 和對應 intent center，讓模型從行為中學到更清楚的意圖。此外，作者提出 intent-assisted contrastive learning，直接用 cluster centers 作為自監督訊號來強化表示學習。實驗顯示 ELCRec 在多個推薦 benchmark 上優於序列推薦和 intent learning baseline，並且在 Beauty dataset 上相較第二名提升 NDCG@5 8.9%、降低計算成本 22.5%。論文也報告了在 1.3 億 page views 的工業推薦系統部署結果，說明這個方法不只適合離線實驗，也有實務可行性。

## Notes

- Main problem: existing intent learning methods rely on alternating clustering and representation learning, which hurts scalability and makes optimization indirect.
- Main method: ELCRec uses learnable cluster centers as latent intents and optimizes clustering with recommendation end-to-end.
- Key module: ELCM separates intent centers while pulling behavior embeddings toward the nearest intent centers.
- Additional signal: intent-assisted contrastive learning uses cluster centers as self-supervision signals.
- Practical relevance: the paper reports both benchmark gains and industrial deployment, making it useful for large-scale recommendation settings.
