---
date: 2026-11-24
title: "Amazon-M2: A Multilingual Multi-locale Shopping Session Dataset for Recommendation and Text Generation"
authors: "Wei Jin, Haitao Mao, Zheng Li, Haoming Jiang, Chen Luo, Hongzhi Wen, Haoyu Han, Hanqing Lu, Zhengyang Wang, Ruirui Li, Zhen Li, Monica Cheng, Rahul Goutam, Haiyang Zhang, Karthik Subbian, Suhang Wang, Yizhou Sun, Jiliang Tang, Bing Yin, Xianfeng Tang"
venue: "NeurIPS 2023 Datasets and Benchmarks Track"
---

# Amazon-M2: A Multilingual Multi-locale Shopping Session Dataset for Recommendation and Text Generation

- Paper page: https://proceedings.neurips.cc/paper_files/paper/2023/hash/193df57a2366d032fb18dcac0698d09a-Abstract-Datasets_and_Benchmarks.html
- PDF: https://proceedings.neurips.cc/paper_files/paper/2023/file/193df57a2366d032fb18dcac0698d09a-Paper-Datasets_and_Benchmarks.pdf
- Local PDF: [../../pdfs/2026-11/2026-11-24-amazon-m2-a-multilingual-multi-locale-shopping-session-dataset-for-recommendation-and-text-generation.pdf](../../pdfs/2026-11/2026-11-24-amazon-m2-a-multilingual-multi-locale-shopping-session-dataset-for-recommendation-and-text-generation.pdf)
- Dataset and competition: https://www.aicrowd.com/challenges/amazon-kdd-cup-23-multilingual-recommendation-challenge
- Venue: NeurIPS 2023 Datasets and Benchmarks Track

## English Summary

Amazon-M2 is a large-scale dataset for multilingual, multi-locale session-based recommendation. It was built to address three weaknesses of common session datasets: limited product attributes, narrow geographic and linguistic coverage, and product catalogs that are much smaller than real e-commerce inventories. Each anonymous session is a chronological sequence of products interacted with during a 30-minute active window. Products are identified by ASIN and accompanied by attributes such as locale, title, brand, size, model, material, color, author, price, and bullet description.

The dataset covers the United Kingdom, Germany, Japan, Spain, France, and Italy, with product text primarily in English, German, Japanese, Spanish, French, and Italian. It contains 3,606,249 training sessions, 361,659 test sessions, 1,410,675 unique products, 15,306,183 training interactions, and 1,483,822 test interactions. The average session length is about 4.2. Data span three weeks: the first two weeks form the training set, and the final week is split equally into phase-1 and phase-2 test sets. UK, DE, and JP are the large locales, while ES, FR, and IT are treated as underrepresented locales. The paper finds long-tailed product frequency and session length, repeat behavior in about 35% of sessions, and meaningful but incomplete product overlap across locales.

Amazon-M2 defines three tasks. Task 1 predicts the next product within the large locales. Task 2 pretrains on UK, DE, and JP and transfers to ES, FR, and IT under language and locale shifts. Task 3 generates the title of a previously unseen next product from recent product titles, creating a generative cold-start setting. Benchmarks include popularity, GRU4Rec++, NARM, STAMP, SRGNN, CORE, MGS, and mT5. On Task 1 validation data, the popularity baseline achieves overall MRR@100 of 0.2426, exceeding every deep baseline; CORE obtains the best Recall@100 at 0.5591. For Task 2, pretraining and finetuning generally improve MRR and Recall over training only on the small locale, showing that cross-locale transfer is useful despite distribution shift. However, simply initializing models with multilingual Sentence-BERT title embeddings hurts performance, indicating that generic semantic representations do not automatically fit product-title recommendation.

For title generation, copying the last product title reaches test BLEU 0.2677, outperforming all reported mT5 variants; longer history and a larger mT5 model do not help. These results make the dataset valuable precisely because standard deep and language-model baselines leave substantial room for improvement. Important limitations remain: all interactions come from Amazon over only three weeks, so conclusions may not generalize across platforms, seasons, or domains. Six locales do not capture global linguistic and cultural diversity, product popularity is a strong shortcut, and the experiments mostly use product IDs despite the dataset's rich attributes. The anonymized behavioral data may also preserve demographic or preference biases, so fairness and privacy require continued scrutiny.

## 繁中摘要

Amazon-M2 是用於 multilingual、multi-locale session-based recommendation 的大型資料集，目標是改善常見 session datasets 的三項限制：product attributes 不完整、地理與語言涵蓋狹窄，以及 product catalogs 遠小於真實電商規模。每個匿名 session 都是一段 30 分鐘 active window 內，使用者依時間順序互動的 products。Products 以 ASIN 識別，並附有 locale、title、brand、size、model、material、color、author、price 與 bullet description 等 attributes。

資料涵蓋英國、德國、日本、西班牙、法國與義大利，product text 主要使用 English、German、Japanese、Spanish、French 與 Italian。資料共有 3,606,249 個 training sessions、361,659 個 test sessions、1,410,675 個 unique products、15,306,183 筆 training interactions，以及 1,483,822 筆 test interactions，平均 session length 約為 4.2。資料時間範圍為三週：前兩週作為 training set，最後一週平均切成 phase-1 與 phase-2 test sets。UK、DE、JP 是 large locales，ES、FR、IT 則視為 underrepresented locales。論文分析顯示 product frequency 與 session length 都呈 long-tail，約 35% sessions 有 repeat behavior，而不同 locales 之間具有顯著但不完整的 product overlap。

Amazon-M2 定義三個任務。Task 1 在 large locales 預測 next product；Task 2 先用 UK、DE、JP pretrain，再跨越 language 與 locale shifts 轉移到 ES、FR、IT；Task 3 根據最近的 product titles，生成訓練期間未出現之 next product title，形成 generative cold-start setting。Benchmarks 包含 popularity、GRU4Rec++、NARM、STAMP、SRGNN、CORE、MGS 與 mT5。Task 1 validation data 中，popularity baseline 的 overall MRR@100 為 0.2426，高於所有 deep baselines；CORE 則以 0.5591 取得最佳 Recall@100。Task 2 中，pretraining 加 finetuning 通常比只在 small locale 訓練有更好的 MRR 與 Recall，表示即使存在 distribution shift，cross-locale transfer 仍有幫助。然而，以 multilingual Sentence-BERT 的 title embeddings 初始化 models 反而降低表現，說明通用 semantic representations 不會自然適配 product-title recommendation。

Title generation 實驗中，直接複製 last product title 的 test BLEU 為 0.2677，優於所有 mT5 variants；增加歷史長度或改用更大的 mT5 都沒有改善。這些結果顯示 Amazon-M2 的價值正在於 standard deep models 與 language-model baselines 仍有很大的進步空間。資料仍有重要限制：所有 interactions 都來自 Amazon，且只涵蓋三週，因此未必能泛化到其他 platforms、季節或 domains；六個 locales 也無法代表全球語言與文化多樣性。Product popularity 是很強的 shortcut，而多數實驗雖然資料具有 rich attributes，仍主要只使用 product IDs。匿名 behavioral data 也可能保留 demographic 或 preference biases，因此 fairness 與 privacy 仍需持續檢視。

## Notes

- Amazon-M2 was used for the Amazon KDD Cup 2023 multilingual recommendation challenge.
- The dataset is released under the Apache 2.0 license.
- Underrepresented locales share many products with larger locales, especially Germany, but language and catalog differences still create substantial domain shift.
- The paper highlights pretraining, multilingual transfer, generative recommendation, cross-lingual entity alignment, graph learning, and item cold-start as follow-up directions.
