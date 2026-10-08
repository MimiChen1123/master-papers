---
date: 2026-10-08
title: "ORBIT - Open Recommendation Benchmark for Reproducible Research with Hidden Tests"
authors: "Jingyuan He, Jiongnan Liu, Vishan Oberoi, Bolin Wu, Mahima Jagadeesh Patel, Kangrui Mao, Chuning Shi, I-Ta Lee, Arnold Overwijk, Chenyan Xiong"
venue: "NeurIPS 2025 Datasets and Benchmarks Track"
---

# ORBIT - Open Recommendation Benchmark for Reproducible Research with Hidden Tests

- Paper page: https://proceedings.neurips.cc/paper_files/paper/2025/hash/e1a6951efe00913c584b48e668bc2215-Abstract-Datasets_and_Benchmarks_Track.html
- PDF: https://proceedings.neurips.cc/paper_files/paper/2025/file/e1a6951efe00913c584b48e668bc2215-Paper-Datasets_and_Benchmarks_Track.pdf
- Local PDF: [../../pdfs/2026-10/2026-10-08-orbit-open-recommendation-benchmark-for-reproducible-research-with-hidden-tests.pdf](../../pdfs/2026-10/2026-10-08-orbit-open-recommendation-benchmark-for-reproducible-research-with-hidden-tests.pdf)
- Venue: NeurIPS 2025 Datasets and Benchmarks Track

## English Summary

This paper introduces ORBIT, a recommendation benchmark designed to reduce ambiguity caused by inconsistent preprocessing, data splits, candidate pools, and metrics. Its public component standardizes sequential next-item evaluation on MovieLens-1M and four Amazon Reviews 2023 domains: Beauty, Toys, Sports, and Books. Every model ranks the target against the full item catalog under a chronological leave-one-out split, and the benchmark reports Recall and NDCG at 1, 10, 50, and 100. A public leaderboard and shared code are intended to make comparisons reproducible as new models are added.

ORBIT's second contribution is ClueWeb-Reco, a hidden-test webpage recommendation task. The authors collected consented browsing histories from U.S. adults through Mechanical Turk and Prolific under a Carnegie Mellon IRB-approved protocol. Online and offline quality control reduced 41,760 submitted URL-timestamp records to 12,282 records in 1,024 sessions. To mitigate residual privacy risks, every private URL is replaced by a semantically similar public page from the 87,208,655-page English ClueWeb22-B corpus. MiniCPM embeddings and a DiskANN index perform this one-to-one soft matching, and exact URL matches are deliberately skipped so that the released sequences remain synthetic.

The paper validates the mapping with retrieval scores and human judgments: five annotators label 100 sampled mappings, with Cohen's kappa of 0.372, and higher embedding similarity generally corresponds to higher relevance. ORBIT then evaluates nine sequential ID models and three content-based models on the public benchmark. HLLM has the best average NDCG@10 at 0.0641, but performance varies substantially by domain; for example, its billion-scale architecture performs poorly on the very small Amazon Beauty split. This variation reinforces the paper's argument that conclusions drawn from one dataset or evaluation recipe may not generalize.

On the zero-shot ClueWeb-Reco hidden test, content models trained on Amazon Books achieve very low recall over the 87-million-page candidate pool: HLLM reaches Recall@10 of 0.0088. LLM-QueryGen instead prompts an LLM to summarize a session into a search query and retrieves the closest page; DeepSeek-V3 is the strongest reported variant with Recall@10/NDCG@10 of 0.0127/0.0082 and Recall@100 of 0.0371. These absolute numbers show that the task remains difficult despite the relative advantage of LLM query generation. Important limitations are the small, U.S.-only session sample, semantic distortion introduced by synthetic soft matching, separate licensing required for ClueWeb page content, and unequal maximum histories for HLLM and other public baselines due to compute limits.

## 繁中摘要

這篇論文提出 ORBIT，目標是降低推薦研究因 preprocessing、data split、candidate pool 與 metrics 不一致而造成的比較歧義。公開 benchmark 統一評估 MovieLens-1M 與 Amazon Reviews 2023 的 Beauty、Toys、Sports、Books 四個領域，將任務設定為 sequential next-item prediction。每個模型都在 chronological leave-one-out split 下，從完整 item catalog 排出目標 item，並回報 K 為 1、10、50、100 時的 Recall 與 NDCG。公開 leaderboard 與共用 codebase 則讓後續新增模型時維持可重現的比較方式。

ORBIT 的第二項貢獻是 ClueWeb-Reco，一個以 hidden test 評估的 webpage recommendation task。作者在 Carnegie Mellon IRB 核准的 protocol 下，透過 Mechanical Turk 與 Prolific 向美國成年使用者取得同意並蒐集 browsing histories。經過 online 與 offline quality control，41,760 筆 URL-timestamp records 最後保留 1,024 個 sessions、12,282 筆 records。為降低殘餘隱私風險，每個私人 URL 都會被替換成英文 ClueWeb22-B corpus 中語意相近的公開頁面；該 corpus 含 87,208,655 個 pages。系統使用 MiniCPM embeddings 與 DiskANN index 做一對一 soft matching，並刻意跳過完全相同的 URL，使釋出的 sequences 保持 synthetic。

論文透過 retrieval scores 與人工標註驗證映射品質：五位 annotators 評估 100 組 mappings，Cohen's kappa 為 0.372，而較高的 embedding similarity 整體上對應較高 relevance。公開 benchmark 評估九個 sequential ID models 與三個 content-based models；HLLM 的平均 NDCG@10 最佳，為 0.0641，但不同領域的結果差異很大。例如其 billion-scale architecture 在資料量極小的 Amazon Beauty split 表現不佳。這種變動支持論文的核心主張：只依賴單一 dataset 或 evaluation recipe 得到的結論未必能 generalize。

在 zero-shot ClueWeb-Reco hidden test 上，使用 Amazon Books 訓練的 content models 面對 8,721 萬頁 candidate pool 時 recall 很低，HLLM 的 Recall@10 僅 0.0088。LLM-QueryGen 會先要求 LLM 把 session 摘要成 search query，再 retrieval 最接近的頁面；其中 DeepSeek-V3 最佳，Recall@10/NDCG@10 為 0.0127/0.0082，Recall@100 為 0.0371。這些絕對數值顯示，即使 LLM query generation 具有相對優勢，任務仍非常困難。主要限制包括樣本只有 1,024 個且僅來自美國、synthetic soft matching 可能造成語意失真、存取 ClueWeb 頁面內容需另簽研究授權，以及受算力限制，HLLM 與其他公開 baselines 使用不同的 maximum history length。

## Notes

- ORBIT benchmark and code: https://www.open-reco-bench.ai
- ClueWeb-Reco dataset: https://huggingface.co/datasets/cx-cmu/ClueWeb-Reco
- ClueWeb-Reco sequence IDs are released under the MIT license, while accessing ClueWeb22 page content requires a separate research license.
- Offline quality control discarded 70% of the initially retained submissions; the final sessions average 11.99 records and have a maximum length of 137.
