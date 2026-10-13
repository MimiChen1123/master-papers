---
date: 2026-10-13
title: "Data-Free Model Extraction for Black-box Recommender Systems via Graph Convolutions"
authors: "Zeyu Wang, Yidan Song, Shihao Qin, Shanqing Yu, Yujin Huang, Qi Xuan, Xin Zheng"
venue: "NeurIPS 2025"
---

# Data-Free Model Extraction for Black-box Recommender Systems via Graph Convolutions

- Paper page: https://papers.nips.cc/paper_files/paper/2025/hash/cce7576bf51b6a156346156c0976e7f6-Abstract-Conference.html
- PDF: https://papers.nips.cc/paper_files/paper/2025/file/cce7576bf51b6a156346156c0976e7f6-Paper-Conference.pdf
- Local PDF: [../../pdfs/2026-10/2026-10-13-data-free-model-extraction-for-black-box-recommender-systems-via-graph-convolutions.pdf](../../pdfs/2026-10/2026-10-13-data-free-model-extraction-for-black-box-recommender-systems-via-graph-convolutions.pdf)
- Venue: NeurIPS 2025

## English Summary

This paper studies model extraction attacks against recommender systems in a difficult data-free, black-box setting. The attacker has no member interactions or in-domain surrogate dataset, can only submit synthetic user histories under a limited query budget, and receives hard-label top-k recommendation lists. The authors first show that simply matching the victim's architecture is not necessarily optimal: graph-convolutional surrogates, especially LightGCN-like models, generalize better from synthetic queries to real user-item interactions than matrix-factorization or MLP alternatives.

DBGRME combines an interaction generator with a generalization-aware graph-convolutional surrogate. The generator initializes synthetic users from Gaussian noise, learns item embeddings, and converts their inner products into virtual implicit-feedback histories. Inspired by adversarial training, it maximizes a BPR disagreement objective so queries concentrate near regions where victim and surrogate rankings differ, making each API call more informative than random synthesis. The victim's returned top-k lists then supervise the surrogate through a ranking loss.

The surrogate is designed to avoid memorizing synthetic user IDs. It freezes synthetic-user embedding weights, maps user and item features through shared feed-forward projection layers, and propagates representations over the generated bipartite graph with normalized graph convolution. A constraint loss limits aggressive item-embedding updates, encouraging the projection and convolution modules to learn platform-level ranking patterns. Generator and surrogate are optimized alternately; the per-cycle complexity is linear in the number of synthetic users times the generator and surrogate update counts.

Experiments cover ML-100K, ML-1M, Yelp, and Gowalla, five victim architectures, and six extraction baselines, using Recall@50 and top-50 agreement (Agr@50). DBGRME is the strongest data-free method across the reported settings and averages a 17.4% gain over a partial-data querying attack when LightGCN is the victim. On ML-100K/LightGCN, it reaches Agr@50 of 0.7727 and Recall@50 of 0.3599, versus victim Recall@50 of 0.3921. Ablations support both the generalization-aware module and constraint loss, while larger query budgets eventually show diminishing returns. The threat model still assumes repeated access to a top-k recommendation API and uses budgets as large as 9 million queries on Yelp; experiments primarily use classical collaborative-filtering victims and offline public data. Detection, output perturbation, differential privacy, and real-service defenses are discussed but not evaluated, so practical stealth and robustness against deployed countermeasures remain open.

## 繁中摘要

這篇論文研究在困難的 data-free、black-box 條件下，如何對 recommender system 進行 model extraction attack。攻擊者沒有 member interactions 或同領域 surrogate dataset，只能在有限 query budget 下提交 synthetic user histories，並取得 hard-label top-k recommendation lists。作者先證明，surrogate 與 victim 採相同架構不一定最好；graph-convolutional surrogates，尤其類似 LightGCN 的模型，比 matrix-factorization 或 MLP alternatives 更能從 synthetic queries 泛化到真實 user-item interactions。

DBGRME 結合 interaction generator 與 generalization-aware graph-convolutional surrogate。Generator 以 Gaussian noise 初始化 synthetic users、學習 item embeddings，再把 inner products 轉成 virtual implicit-feedback histories。受到 adversarial training 啟發，它最大化 BPR disagreement objective，使 queries 集中在 victim 與 surrogate ranking 不一致的區域，因此每次 API call 都比 random synthesis 提供更多資訊。Victim 回傳的 top-k lists 隨後透過 ranking loss 監督 surrogate。

Surrogate 的設計目標是避免記住 synthetic user IDs。它凍結 synthetic-user embedding weights，讓 user 與 item features 通過 shared feed-forward projection layers，並在生成的 bipartite graph 上以 normalized graph convolution 傳播表示。Constraint loss 會限制 item-embedding 過度更新，促使 projection 與 convolution modules 學習 platform-level ranking patterns。Generator 與 surrogate 交替最佳化；每個 cycle 的 complexity 與 synthetic users 數量乘上 generator、surrogate 更新次數呈線性關係。

實驗涵蓋 ML-100K、ML-1M、Yelp、Gowalla、五種 victim architectures 與六個 extraction baselines，以 Recall@50 和 top-50 agreement（Agr@50）評估。DBGRME 在所有回報設定中都是最強 data-free method；當 victim 為 LightGCN 時，平均比可存取部分資料的 querying attack 高 17.4%。在 ML-100K/LightGCN 上，它取得 Agr@50 0.7727、Recall@50 0.3599，而 victim Recall@50 為 0.3921。Ablation 支持 generalization-aware module 與 constraint loss，query budget 增加到一定程度後則出現邊際效益遞減。此 threat model 仍假設攻擊者可重複存取 top-k recommendation API，Yelp 的 budget 更高達 900 萬次；主要實驗使用 classical collaborative-filtering victims 與離線公開資料。論文只討論 detection、output perturbation、differential privacy 與 real-service defenses，沒有實際評估，因此攻擊在部署環境中的隱蔽性與面對防禦時的穩健性仍未確定。

## Notes

- Official code: https://github.com/Vencent-Won/DBGRME
- Dataset query budgets are 200,000 for ML-100K, 400,000 for ML-1M, 9 million for Yelp, and 4 million for Gowalla.
- The supplement also evaluates Steam with 334,730 users and reports consistent gains over DFME and Sim4Rec.
- The authors frame model extraction as robustness research and recommend query anomaly detection, rate limiting, calibrated output noise, access controls, and legal safeguards as potential countermeasures.
