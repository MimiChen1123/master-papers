---
date: 2026-11-03
title: "Who You Are Matters: Bridging Interests and Social Roles via LLM-Enhanced Logic Recommendation"
authors: "Qing Yu, Xiaobei Wang, Shuchang Liu, Yandong Bai, Xiaoyu Yang, Xueliang Wang, Chang Meng, Shanshan Wu, Hailan Yang, Bin Wen, Huihui Xiao, Xiang Li, Fan Yang, Xiaoqiang Feng, Lantao Hu, Han Li, Kun Gai, Lixin Zou"
venue: "NeurIPS 2025"
---

# Who You Are Matters: Bridging Interests and Social Roles via LLM-Enhanced Logic Recommendation

- Paper page: https://proceedings.neurips.cc/paper_files/paper/2025/hash/7d25b1db211d99d5750ec45d65fd6e4e-Abstract-Conference.html
- PDF: https://proceedings.neurips.cc/paper_files/paper/2025/file/7d25b1db211d99d5750ec45d65fd6e4e-Paper-Conference.pdf
- Local PDF: [../../pdfs/2026-11/2026-11-03-who-you-are-matters-bridging-interests-and-social-roles-via-llm-enhanced-logic-recommendation.pdf](../../pdfs/2026-11/2026-11-03-who-you-are-matters-bridging-interests-and-social-roles-via-llm-enhanced-logic-recommendation.pdf)
- Code: https://github.com/Code2Q/TagCF
- Venue: NeurIPS 2025

## English Summary

This paper argues that recommendation models should represent not only which item topics a user likes but also which social roles or characteristics explain those preferences. A person may interact with the same topic as a parent, teacher, traveler, or professional, and these roles can shape how interests transfer between item categories. The authors formalize user-role identification and behavioral-logic modeling, then propose TagCF, an LLM-enhanced collaborative filtering framework that extracts role/topic tags and connects them through interpretable logic graphs.

TagCF first uses the multimodal model M3 on each item's audio, image, title, OCR, and ASR information to generate user-role tags and item-topic tags. Because open-ended tags grow rapidly, a dynamic greedy cover-set procedure retains a smaller, semantically distinct set. Lightweight distilled models then extend tag predictions from tens of thousands of MLLM-processed new items to millions of items. Qwen2.5-7B-Instruct infers two directed relations: user-role-to-item-topic logic and item-topic-to-user-role logic. These relations are distilled into graphs over the cover sets and updated offline each day.

The tag knowledge enters recommendation in three ways: a tag-aware sequential encoder augments ID embeddings, contrastive tag objectives align users and items with role embeddings, and an inference-time score adds matches from original or logic-expanded tags. TagCF-ut uses user-role tags, while TagCF-it uses item-topic tags; utility and exploration variants respectively emphasize direct matches or graph-expanded interests. On the industrial offline dataset, TagCF-ut improves NDCG@10 from the strongest baseline's 0.0186 to 0.0201, while TagCF-it provides the best diversity. The transferred graphs also improve accuracy and diversity on Books and Movies; for Books, TagCF-ut reaches NDCG@10 of 0.1881 versus 0.1705 for the strongest baseline.

Online tests run on a video platform serving more than half a billion users daily. Over at least 14 days, TagCF-util raises the combined interaction metric by 0.946%, while TagCF-expl increases diversity by 0.102% without losing interaction performance. A 40-day extension reports a 0.037% increase in the next-week retention/DAU metric. The approach has meaningful costs: three million videos are processed daily using 50 RTX 4090 GPUs, role inference depends on user history and therefore struggles with cold-start users, and the greedy cover set discards much fine-grained knowledge. Misidentified roles may also create privacy, fairness, stereotyping, or harmful-recommendation risks, so generated roles should not be treated as verified user attributes.

## 繁中摘要

這篇論文主張，推薦模型除了表示使用者喜歡哪些 item topics，也應建模哪些 social roles 或 characteristics 解釋了這些偏好。同一個人可能以家長、教師、旅人或專業工作者的角色接觸相同主題，而角色會影響興趣如何在不同 item categories 間轉移。作者正式定義 user-role identification 與 behavioral-logic modeling，並提出 TagCF：一個以 LLM 增強 collaborative filtering 的 framework，抽取 role/topic tags，再以可解釋的 logic graphs 連結兩者。

TagCF 先使用 multimodal model M3，根據每個 item 的 audio、image、title、OCR 與 ASR 資訊產生 user-role tags 和 item-topic tags。由於 open-ended tags 會快速增長，系統以動態 greedy cover-set procedure 保留規模較小且語意差異明顯的集合，再訓練輕量 distilled models，把只對數萬個新 items 執行 MLLM 的結果擴展到數百萬 items。Qwen2.5-7B-Instruct 推論兩種有向關係：user-role-to-item-topic logic 與 item-topic-to-user-role logic；這些關係被 distill 成 cover sets 上的 graphs，並每日離線更新。

Tag knowledge 透過三種方式進入推薦模型：tag-aware sequential encoder 補強 ID embeddings、contrastive tag objectives 對齊 users/items 與 role embeddings、inference-time score 融合原始或 logic-expanded tags 的匹配分數。TagCF-ut 使用 user-role tags，TagCF-it 使用 item-topic tags；utility 與 exploration variants 分別著重直接匹配和 graph-expanded interests。在 industrial offline dataset 上，TagCF-ut 將最強 baseline 的 NDCG@10 從 0.0186 提升到 0.0201，而 TagCF-it 的 diversity 最佳。移轉同一組 logic graphs 到 Books 與 Movies 也同時改善 accuracy 和 diversity；Books 上 TagCF-ut 的 NDCG@10 為 0.1881，最強 baseline 為 0.1705。

Online tests 在每日服務超過五億使用者的影音平台進行。至少 14 天的實驗中，TagCF-util 讓綜合 interaction metric 提升 0.946%；TagCF-expl 在不損失 interaction performance 的情況下，讓 diversity 提升 0.102%。延長至 40 天的實驗則報告 next-week retention/DAU metric 提升 0.037%。代價也相當明確：系統每天使用 50 張 RTX 4090 處理三百萬支影片；role inference 依賴 user history，因而難以處理 cold-start users；greedy cover set 也會捨棄大量細粒度知識。此外，錯誤辨識角色可能引發 privacy、fairness、stereotyping 或有害推薦風險，因此生成的 roles 不應被視為經驗證的使用者屬性。

## Notes

- The proceedings page uses “Bridging Interests,” while the PDF title page uses “Bridging Topics”; this entry follows the official proceedings title.
- Offline evaluation covers Books, Movies, and an industrial dataset with 89,417 users and 3.29 million interactions, averaged over five random seeds.
- The online system reranks 120 candidates to six results; tag extraction and graph updates run offline each day.
- TagCF-ut generally favors recommendation accuracy, while TagCF-it often provides stronger item coverage and lower Gini concentration.
