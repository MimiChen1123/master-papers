---
date: 2026-11-07
title: "Can LLMs Outshine Conventional Recommenders? A Comparative Evaluation"
authors: "Qijiong Liu, Jieming Zhu, Lu Fan, Kun Wang, Hengchang Hu, Wei Guo, Yong Liu, Xiao-Ming Wu"
venue: "NeurIPS 2025 Datasets and Benchmarks Track"
---

# Can LLMs Outshine Conventional Recommenders? A Comparative Evaluation

- Paper page: https://proceedings.neurips.cc/paper_files/paper/2025/hash/129292da836f35bc051ccef07a245ab7-Abstract-Datasets_and_Benchmarks_Track.html
- PDF: https://proceedings.neurips.cc/paper_files/paper/2025/file/129292da836f35bc051ccef07a245ab7-Paper-Datasets_and_Benchmarks_Track.pdf
- Local PDF: [../../pdfs/2026-11/2026-11-07-can-llms-outshine-conventional-recommenders-a-comparative-evaluation.pdf](../../pdfs/2026-11/2026-11-07-can-llms-outshine-conventional-recommenders-a-comparative-evaluation.pdf)
- Benchmark and code: https://recbench.github.io
- Data: https://www.kaggle.com/datasets/qijiang/recbench/
- Venue: NeurIPS 2025 Datasets and Benchmarks Track

## English Summary

This paper introduces RecBench, a benchmark for comparing conventional deep learning recommender models with systems that use large language models directly as recommenders. It evaluates both pair-wise click-through-rate prediction and list-wise sequential recommendation, rather than treating LLM recommendation as a single task. The benchmark also separates four item representations: arbitrary unique identifiers, raw text, pretrained semantic embeddings, and discrete semantic identifiers produced by quantizing text embeddings. Experiments span fashion, news, video, books, and music through H&M, MIND, MicroLens, Goodreads, and Amazon CDs.

For pair-wise recommendation, RecBench compares conventional CTR architectures, zero-shot LLMs, and LoRA-fine-tuned LLMs. Most zero-shot models perform poorly, showing that general language ability alone does not reliably recover preferences from interaction histories. Instruction tuning improves accuracy by 22% to 43%, and large text-based models achieve more than a 5% relative AUC improvement over the strongest conventional model. However, conventional models initialized with LLM semantic embeddings retain about 95% of the best LLM accuracy while running thousands of times faster. This makes the LLM-FOR-RS pattern, where an LLM supplies offline features to a conventional model, more practical than using an LLM as the online ranker.

For sequential recommendation, semantic identifiers generally outperform plain item IDs because their token structure carries content similarity. Conditional beam search further helps by restricting generation to valid paths in the semantic-identifier tree. Fine-tuned LLM recommenders can outperform SASRec, with the paper reporting gains of up to 170% in NDCG@10 and up to 83% when semantic identifiers replace unique IDs in matched LLM comparisons. Results are highly model- and dataset-dependent, however: the best overall table entry is not one architecture on every domain, deeper SASRec narrows the semantic-identifier advantage, and few-shot prompts sometimes reduce performance. These details make RecBench more useful as a trade-off map than as evidence that one LLM universally dominates.

Efficiency is the decisive limitation. In the list-wise table, conventional SASRec variants take roughly 23-103 ms per CPU inference, while large semantic-ID LLMs with constrained decoding take up to 177,540 ms; the authors summarize the gap as nearly 1,000 times. Latency is averaged over 1,000 runs, and trained results are averaged over five runs on one A100 GPU. The benchmark uniformly downsamples datasets, caps histories at 20, and uses fixed-size fine-tuning and test sets, which improves comparability but does not reproduce full production traffic distributions. RecBench also does not evaluate fairness or privacy, and the authors caution that foundation models may amplify data bias and stereotypes.

## 繁中摘要

這篇論文提出 RecBench，用來比較傳統 deep learning recommender models 與直接以 large language models 執行推薦的系統。Benchmark 同時涵蓋 pair-wise click-through-rate prediction 與 list-wise sequential recommendation，而不是把 LLM recommendation 視為單一任務；也區分四種 item representations：任意 unique identifiers、raw text、pretrained semantic embeddings，以及將 text embeddings 量化後得到的 discrete semantic identifiers。實驗透過 H&M、MIND、MicroLens、Goodreads 與 Amazon CDs，涵蓋 fashion、news、video、books 和 music 五個領域。

在 pair-wise recommendation 中，RecBench 比較傳統 CTR architectures、zero-shot LLMs 與使用 LoRA fine-tuning 的 LLMs。多數 zero-shot models 表現不佳，顯示一般語言能力本身無法可靠地從 interaction histories 推斷偏好。Instruction tuning 可提升 22% 至 43% 的準確度，大型 text-based models 相對最強傳統模型的 AUC 提升超過 5%。然而，以 LLM semantic embeddings 初始化的傳統模型能保留最佳 LLM 約 95% 的準確度，速度卻快數千倍。因此，由 LLM 離線提供 features、再交給傳統模型線上推論的 LLM-FOR-RS，比直接以 LLM 擔任 online ranker 更實際。

在 sequential recommendation 中，semantic identifiers 通常優於一般 item IDs，因為 token structure 包含 content similarity。Conditional beam search 進一步限制生成結果只能沿 semantic-identifier tree 的有效路徑。Fine-tuned LLM recommenders 可勝過 SASRec；論文回報 NDCG@10 最高提升 170%，而在 matched LLM comparisons 中，以 semantic identifiers 取代 unique IDs 最高提升 83%。不過，結果高度依賴 model 與 dataset：表格中並非同一 architecture 在所有領域最佳；加深 SASRec 後，semantic-identifier 的優勢會縮小；few-shot prompts 有時甚至降低表現。因此，RecBench 更適合用來觀察 trade-offs，而不是證明某個 LLM 能全面取代其他方法。

效率是最明顯的限制。List-wise 表格中，傳統 SASRec variants 每次 CPU inference 約需 23-103 ms；大型 semantic-ID LLM 搭配 constrained decoding 則最高達 177,540 ms，作者將整體差距概括為接近 1,000 倍。Latency 以 1,000 次執行平均，訓練結果以單張 A100 GPU 上五次執行平均。Benchmark 對資料集做 uniform downsampling、將 histories 上限設為 20，並使用固定大小的 fine-tuning 和 test sets；這提升了可比較性，卻不等同完整 production traffic distribution。RecBench 也尚未評估 fairness 或 privacy，作者並提醒 foundation models 可能放大 data bias 與 stereotypes。

## Notes

- RecBench evaluates up to 17 large models and 10 conventional recommender models.
- Pair-wise fine-tuning uses about 100,000 samples per dataset; list-wise fine-tuning uses 40,000 sequences and testing uses 5,000 sequences per dataset.
- Fine-tuned models use LoRA; latency is the average of 1,000 inference runs.
- The paper reports AUC for CTR and NDCG@10 for SeqRec in the main tables, with additional NDCG, MRR, F1, and recall results in the appendix and released benchmark.
