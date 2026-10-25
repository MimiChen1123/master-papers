---
date: 2026-10-25
title: "Can LLMs Outshine Conventional Recommenders? A Comparative Evaluation"
authors: "Qijiong Liu, Jieming Zhu, Lu Fan, Kun Wang, Hengchang Hu, Wei Guo, Yong Liu, Xiao-Ming Wu"
venue: "NeurIPS 2025 Datasets and Benchmarks Track"
---

# Can LLMs Outshine Conventional Recommenders? A Comparative Evaluation

- Paper page: https://proceedings.neurips.cc/paper_files/paper/2025/hash/129292da836f35bc051ccef07a245ab7-Abstract-Datasets_and_Benchmarks_Track.html
- PDF: https://proceedings.neurips.cc/paper_files/paper/2025/file/129292da836f35bc051ccef07a245ab7-Paper-Datasets_and_Benchmarks_Track.pdf
- Local PDF: [../../pdfs/2026-10/2026-10-25-can-llms-outshine-conventional-recommenders-a-comparative-evaluation.pdf](../../pdfs/2026-10/2026-10-25-can-llms-outshine-conventional-recommenders-a-comparative-evaluation.pdf)
- Venue: NeurIPS 2025 Datasets and Benchmarks Track

## English Summary

This paper introduces RECBENCH, a benchmark designed to answer when large language models are actually better recommenders than conventional deep learning-based recommender models (DLRMs). It evaluates pair-wise click-through-rate prediction and list-wise sequential recommendation across five domains: H&M fashion, MIND news, MicroLens video, Goodreads books, and Amazon CDs music. The comparison includes up to 17 language models and 10 conventional recommenders, under both zero-shot and fine-tuned settings, while controlling dataset sizes and measuring inference latency as well as recommendation quality.

RECBENCH systematically varies how items are represented. Unique identifiers learn only from interaction signals; text exposes item content directly; semantic embeddings initialize conventional models with LLM-derived representations; and semantic identifiers use an RQ-VAE to encode each item as four discrete tokens from 256-entry codebooks. For sequential recommendation, the authors also introduce conditional beam search, which restricts generation to paths that correspond to valid semantic identifiers. LLMs are fine-tuned with LoRA, and the benchmark covers model families including BERT, OPT, Llama, Mistral, Qwen, GLM, Phi, P5, and RecGPT.

For CTR prediction, most zero-shot LLMs are near random and remain weaker than ID-based DLRMs; Mistral, GLM, and Qwen-2 are notable exceptions but still trail fine-tuned systems. Fine-tuning improves LLM accuracy by 22% to 43%. Text-based Llama-3 7B and Mistral-2 7B achieve the best overall AUC, with Mistral reaching 0.7578 versus 0.7171 for the strongest semantic-embedding DLRM. However, the latter retains about 95% of the accuracy and is dramatically faster. The results therefore favor using frozen LLM semantic embeddings inside conventional CTR models when deployment efficiency matters.

For sequential recommendation, semantic identifiers consistently improve both SASRec-style models and LLMs, especially when paired with conditional beam search. SID-BERT with conditional beam search obtains the best mean NDCG@10 of 0.1877, compared with 0.0698 for the strongest standard SASRec, an improvement of roughly 169%. Yet LLM recommenders require nearly 1,000 times more inference time overall, and the reported SID-Llama configuration takes 177,540 ms per CPU inference. The study is broad and reproducible, but its balanced subsampling does not reproduce the traffic scale or distributions of production systems, only offline metrics are tested, and foundation models may amplify biases or stereotypes. The appendix adds activity-group fairness checks and avoids sensitive user attributes, but broader fairness and privacy evaluation remains incomplete.

## 繁中摘要

這篇論文提出 RECBENCH，用來回答大型語言模型在什麼條件下真的比傳統 deep learning-based recommender models（DLRMs）更適合做推薦。Benchmark 同時評估 pair-wise click-through-rate prediction 與 list-wise sequential recommendation，涵蓋 H&M fashion、MIND news、MicroLens video、Goodreads books、Amazon CDs music 五個領域；比較最多 17 個 language models 與 10 個傳統 recommenders，也包含 zero-shot、fine-tuning、推薦品質與 inference latency。

RECBENCH 系統性比較四種 item representations。Unique identifier 只從互動訊號學習；text 直接提供物品內容；semantic embedding 以 LLM 產生的 representations 初始化傳統模型；semantic identifier 則用 RQ-VAE，把每個 item 編碼成來自四層、每層 256 個 codewords 的離散 tokens。對 sequential recommendation，作者另提出 conditional beam search，只允許生成能對應到有效 semantic identifier 的路徑。LLMs 使用 LoRA fine-tune，評估範圍包括 BERT、OPT、Llama、Mistral、Qwen、GLM、Phi、P5 與 RecGPT。

在 CTR prediction 中，多數 zero-shot LLMs 接近隨機表現，也低於 ID-based DLRMs；Mistral、GLM、Qwen-2 是較明顯的例外，但仍不及 fine-tuned systems。Fine-tuning 可讓 LLM 準確率提升 22% 到 43%。使用 text 的 Llama-3 7B 與 Mistral-2 7B 取得最高整體 AUC，其中 Mistral 為 0.7578，最佳 semantic-embedding DLRM 則為 0.7171。不過後者保留約 95% 的準確率，速度卻快非常多。因此若重視部署效率，結果更支持把 frozen LLM semantic embeddings 接入傳統 CTR model，而不是直接以 LLM 推論。

在 sequential recommendation 中，semantic identifiers 對 SASRec 類模型與 LLMs 都有幫助，搭配 conditional beam search 時尤其明顯。SID-BERT 加 conditional beam search 的平均 NDCG@10 為 0.1877，最佳標準 SASRec 為 0.0698，約提升 169%。但 LLM recommender 的整體 inference time 接近 SASRec 的 1,000 倍，文中 SID-Llama 設定每次 CPU inference 更需 177,540 ms。這項研究涵蓋面廣且提供可重現資源，但平衡後的 subsampling 無法重現 production traffic 的規模與分布，實驗也只有 offline metrics；foundation models 還可能放大偏差與刻板印象。附錄雖加入不同使用者活躍度的 fairness 檢查並避免 sensitive user attributes，更全面的 fairness 與 privacy 評估仍未完成。

## Notes

- Benchmark website and code: https://recbench.github.io
- Released benchmark data: https://www.kaggle.com/datasets/qijiong/recbench/
- All training experiments use one Nvidia A100; fine-tuned results are averaged over five runs, except zero-shot evaluations.
- Pair-wise histories are truncated to 20 items; the benchmark uses 100,000 fine-tuning samples per dataset and about 20,000 test samples.
- List-wise experiments use 40,000 fine-tuning sequences and 5,000 test sequences per dataset.
