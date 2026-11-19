---
date: 2026-11-19
title: "Theoretically Guaranteed Bidirectional Data Rectification for Robust Sequential Recommendation"
authors: "Yatong Sun, Xiaochun Yang, Zhu Sun, Bin Wang, Yan Wang"
venue: "NeurIPS 2023"
---

# Theoretically Guaranteed Bidirectional Data Rectification for Robust Sequential Recommendation

- Paper page: https://proceedings.neurips.cc/paper_files/paper/2023/hash/08309150af77fc7c79ade0bf8bb6a562-Abstract-Conference.html
- PDF: https://proceedings.neurips.cc/paper_files/paper/2023/file/08309150af77fc7c79ade0bf8bb6a562-Paper-Conference.pdf
- Local PDF: [../../pdfs/2026-11/2026-11-19-theoretically-guaranteed-bidirectional-data-rectification-for-robust-sequential-recommendation.pdf](../../pdfs/2026-11/2026-11-19-theoretically-guaranteed-bidirectional-data-rectification-for-robust-sequential-recommendation.pdf)
- Code: https://github.com/BRCDM/BirDRec
- Venue: NeurIPS 2023

## English Summary

Sequential recommenders usually treat every observed input-target pair as reliable, although accidental clicks, shared accounts, social influence, and other distractions can introduce mismatches. A noisy event can be a completely unreliable target for one training instance and later become an unreliable element inside another instance's input sequence. Prior robust methods often clean only one side and use predictions from a model trained on the same noisy data without explaining when those predictions are trustworthy.

The paper derives error-bounded conditions connecting model scores across epochs to data reliability under a relaxed multiclass Tsybakov assumption. Its Detecting and Rectifying Unreliable Targets strategy replaces a persistently low-scored target with a consistently higher-scored candidate. Its Detecting and Deleting Unreliable Input strategy trains a backward sequential model and removes input events that remain inconsistent with the target. BirDRec combines both directions: a self-ensembled forward model rectifies targets, a self-ensembled backward model rectifies inputs, and the cleaned instances train the corresponding models.

Two engineering mechanisms control cost. Rectification sampling maintains small candidate pools from nearby sequence items plus random samples, reducing per-epoch time from dependence on the full item vocabulary to dependence on pool size. Exponential-moving-average self-ensembles approximate predictions across epochs without storing every checkpoint and score. Across FPMC, Caser, GRU4Rec, SASRec, BERT4Rec, and MAGNN on ML-1M, Beauty, Yelp, and QK-Video, BirDRec improves every reported backbone-dataset metric. With SASRec it also beats BERD, FMLP-Rec, and STEAM; NDCG@10 reaches 0.1915 on ML-1M, 0.0537 on Beauty, 0.0687 on Yelp, and 0.0682 on QK-Video. Reported gains over the strongest robust baseline range from 19.87% on Beauty NDCG@10 to 45.24% on Yelp NDCG@10, with paired-test significance at p <= 0.001.

The theoretical guarantees depend on assumptions about preference margins, transition noise, prediction approximation, and thresholds that may be difficult to verify in a deployed system. Rectification can also erase genuine preference changes or unusual interests when low model scores are interpreted as noise, although this risk is not directly evaluated. Efficiency is improved relative to STEAM, but BirDRec remains about 1.6 times slower per epoch than its backbone; storage savings are limited when the item vocabulary is small. All evidence is offline, and the four datasets do not test temporal policy changes or online feedback loops.

## 繁中摘要

Sequential recommender 通常把每個 observed input-target pair 都視為可靠資料，但 accidental clicks、shared accounts、朋友影響或其他干擾都可能造成 mismatch。同一個 noisy event 在某個 training instance 中可能是完全不可靠的 target，之後又成為另一個 instance 的不可靠 input。既有 robust 方法常只清理其中一側，而且直接使用由同一批 noisy data 訓練出的模型預測，卻沒有說明何時這些預測值得信任。

論文在 relaxed multiclass Tsybakov assumption 下，推導跨 epoch model scores 與 data reliability 之間的 error-bounded conditions。Detecting and Rectifying Unreliable Targets 會把持續低分的 target 換成長期得分較高的 candidate；Detecting and Deleting Unreliable Input 則訓練 backward sequential model，移除與 target 持續不一致的 input events。BirDRec 將兩者結合：self-ensembled forward model 修正 targets，self-ensembled backward model 修正 inputs，再以清理後的 instances 訓練對應模型。

作者用兩個機制控制成本。Rectification sampling 從鄰近 sequence items 與隨機樣本維護小型 candidate pools，讓每個 epoch 的時間複雜度不再依賴完整 item vocabulary，而改為依賴 pool size。Exponential-moving-average self-ensemble 則近似多個 epochs 的預測，不必保存每個 checkpoint 與所有 scores。在 ML-1M、Beauty、Yelp、QK-Video 上，BirDRec 搭配 FPMC、Caser、GRU4Rec、SASRec、BERT4Rec、MAGNN 時，所有報告的 backbone-dataset metrics 都有改善。以 SASRec 為 backbone 時也優於 BERD、FMLP-Rec 與 STEAM；四個 datasets 的 NDCG@10 分別達 0.1915、0.0537、0.0687、0.0682。相較最強 robust baseline，NDCG@10 的相對提升從 Beauty 的 19.87% 到 Yelp 的 45.24%，paired test 為 p <= 0.001。

理論保證依賴 preference margin、transition noise、prediction approximation 與 thresholds 等 assumptions，在實際部署中未必容易驗證。把低 model score 視為 noise 也可能刪除真正的偏好轉變或少見興趣，但論文沒有直接評估此風險。BirDRec 雖比 STEAM 有效率，每個 epoch 仍平均比原 backbone 慢約 1.6 倍；當 item vocabulary 小時，storage savings 也較有限。所有證據皆來自 offline evaluation，四個 datasets 尚未測試 temporal policy changes 或 online feedback loops。

## Notes

- Dataset sizes range from 999,611 interactions on ML-1M to 2,268,935 on QK-Video; Beauty and Yelp are over 99.9% sparse.
- Each model is trained five times, and evaluation ranks over the full item set.
- The default configuration uses 64-dimensional embeddings, sequence length 5, rectification-pool size 10, and EMA decay 0.9.
- BirDRec delays rectification for the first ten epochs so the models can first reduce prediction error.
