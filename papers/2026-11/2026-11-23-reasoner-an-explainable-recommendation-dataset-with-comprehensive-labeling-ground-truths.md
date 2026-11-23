---
date: 2026-11-23
title: "REASONER: An Explainable Recommendation Dataset with Comprehensive Labeling Ground Truths"
authors: "Xu Chen, Jingsen Zhang, Lei Wang, Quanyu Dai, Zhenhua Dong, Ruiming Tang, Rui Zhang, Li Chen, Wayne Xin Zhao, Ji-Rong Wen"
venue: "NeurIPS 2023 Datasets and Benchmarks Track"
---

# REASONER: An Explainable Recommendation Dataset with Comprehensive Labeling Ground Truths

- Paper page: https://proceedings.neurips.cc/paper_files/paper/2023/hash/2ebf43d20e5933ab6d98225bbb908ade-Abstract.html
- PDF: https://proceedings.neurips.cc/paper_files/paper/2023/file/2ebf43d20e5933ab6d98225bbb908ade-Paper-Datasets_and_Benchmarks.pdf
- Local PDF: [../../pdfs/2026-11/2026-11-23-reasoner-an-explainable-recommendation-dataset-with-comprehensive-labeling-ground-truths.pdf](../../pdfs/2026-11/2026-11-23-reasoner-an-explainable-recommendation-dataset-with-comprehensive-labeling-ground-truths.pdf)
- Project: https://reasoner2023.github.io/
- Venue: NeurIPS 2023 Datasets and Benchmarks Track

## English Summary

REASONER is a dataset and evaluation library for explainable recommendation. Earlier datasets often treat reviews as explanations, use annotators who are not the actual users, focus on one explanation purpose, or support only text. REASONER instead collects recommendation interactions and explanation labels from the same people, covers textual tags and visual key-frame previews, and distinguishes three goals: persuading a user to watch, accurately describing the item, and reflecting the features that satisfied the user.

The authors built a short-video recommendation platform and recruited roughly 3,000 paid labelers. Videos are exposed uniformly rather than selected by an existing recommender. Before watching, users identify features that attract or repel them; after watching every video, they label informative and satisfying features, give a 1-5 rating, and write a review. Candidate text comes from author tags and processed comments, while five deduplicated key frames provide visual candidates. Users also complete a Big Five personality questionnaire and provide demographic information. Quality controls remove users with implausibly short completion times, excessive repeated answers, inconsistent repeated-question answers, or cross-question conflicts identified through independent manual review and voting.

The released data contain 2,997 users, 4,672 videos, 6,115 tags, and 58,497 interactions, with reviews averaging 17 words. Tags chosen for different explanation purposes overlap only moderately: average Jaccard similarities are 0.423 for persuasiveness versus informativeness, 0.364 for persuasiveness versus satisfaction, and 0.410 for informativeness versus satisfaction. About 36%-39% of users select both textual and visual evidence, supporting the need for multi-modal evaluation. The accompanying library unifies feature-based and natural-language explanation models and benchmarks tag prediction, rating prediction, top-K recommendation, and review generation with F1/NDCG, RMSE/MAE, and BLEU/ROUGE metrics. Experiments use an 8:1:1 random split and report results for multiple single- and multi-aspect targets.

The dataset is limited to short videos from one industrial platform and fewer than 3,000 retained users, so cultural, platform, and domain generalization remain open. Explanation labels are subjective; rule-based filtering and manual conflict review improve consistency but may remove valid atypical preferences. Random interaction splitting can place the same users and items across train and test, making the benchmark less demanding than cold-start or temporal evaluation. BLEU and ROUGE also do not directly measure whether generated explanations are truthful or useful. Although IDs are desensitized and participants consented to research use, the combination of demographics, income, education, personality, and detailed preferences carries re-identification and sensitive-inference risks that require careful access and fairness practices.

## 繁中摘要

REASONER 是用於 explainable recommendation 的 dataset 與 evaluation library。既有資料集常把 reviews 直接視為 explanations、由非真實使用者的 annotators 標註、只處理單一 explanation purpose，或只支援文字。REASONER 則由同一批人同時產生 recommendation interactions 與 explanation labels，涵蓋 textual tags 與 visual key-frame previews，並區分三種目的：說服使用者觀看、準確描述 item，以及反映真正讓使用者滿意的 features。

作者建立 short-video recommendation platform，招募約 3,000 位付費 labelers。Videos 以 uniform exposure 呈現，而不是由既有 recommender 選擇。觀看前，使用者標記吸引或排斥自己的 features；觀看每支影片後，再標記 informative 與 satisfying features、給予 1-5 rating，並撰寫 review。文字 candidates 來自作者 tags 與處理後的 comments，五張去重 key frames 則提供 visual candidates。使用者也完成 Big Five personality questionnaire 並提供 demographic information。Quality controls 會移除完成時間不合理、過度重複答案、重複題目回答不一致，或經獨立人工審查與投票認定跨題矛盾的 users。

發布的資料包含 2,997 users、4,672 videos、6,115 tags 與 58,497 interactions，reviews 平均 17 words。不同 explanation purposes 選出的 tags 只有中度重疊：persuasiveness 與 informativeness 的平均 Jaccard similarity 為 0.423，persuasiveness 與 satisfaction 為 0.364，informativeness 與 satisfaction 為 0.410。約 36%-39% users 同時選擇 textual 與 visual evidence，支持 multi-modal evaluation 的必要性。附帶 library 統一 feature-based 與 natural-language explanation models，並以 F1/NDCG、RMSE/MAE、BLEU/ROUGE 評估 tag prediction、rating prediction、top-K recommendation 與 review generation。實驗使用 8:1:1 random split，涵蓋多種 single- 與 multi-aspect targets。

資料只來自單一 industrial platform 的短影片，保留 users 少於 3,000，因此文化、平台與 domain generalization 仍未解決。Explanation labels 本質上主觀；rule-based filtering 與人工 conflict review 雖提升一致性，也可能刪除合理但少見的偏好。Random interaction split 可能讓相同 users/items 同時出現在 train 與 test，難度低於 cold-start 或 temporal evaluation。BLEU、ROUGE 也無法直接衡量 generated explanations 是否真實或對使用者有幫助。雖然 IDs 已 desensitized，參與者也同意研究用途，但 demographics、income、education、personality 與細緻 preferences 的組合仍有 re-identification 與 sensitive-inference 風險，需要審慎的資料存取與 fairness practices。

## Notes

- Every user receives at least 18 uniformly sampled video recommendations and watches each selected or rejected item before completing post-watch labels.
- Labelers were paid USD 8 each; the paper reports a total collection cost of about USD 28,000.
- About 38.9%, 39.0%, and 35.9% of users select multi-modal evidence for persuasiveness, informativeness, and satisfaction, respectively.
- The dataset and library are released under CC BY-NC 4.0.
