---
date: 2026-09-29
title: "P-Law: Predicting Quantitative Scaling Law with Entropy Guidance in Large Recommendation Models"
authors: "Tingjia Shen, Hao Wang, Chuhan Wu, Chin Jin Yao, Wei Guo, Yong Liu, Huifeng Guo, Defu Lian, Ruiming Tang, Enhong Chen"
venue: "NeurIPS 2025"
---

# P-Law: Predicting Quantitative Scaling Law with Entropy Guidance in Large Recommendation Models

- Paper page: https://proceedings.neurips.cc/paper_files/paper/2025/hash/133e588e1429f9f1e25b215da145580e-Abstract-Conference.html
- PDF: https://proceedings.neurips.cc/paper_files/paper/2025/file/133e588e1429f9f1e25b215da145580e-Paper-Conference.pdf
- Local PDF: [../../pdfs/2026-09/2026-09-29-p-law-predicting-quantitative-scaling-law-with-entropy-guidance-in-large-recommendation-models.pdf](../../pdfs/2026-09/2026-09-29-p-law-predicting-quantitative-scaling-law-with-entropy-guidance-in-large-recommendation-models.pdf)
- Venue: NeurIPS 2025

## English Summary

This paper studies whether scaling laws can predict the actual ranking quality of large sequential recommendation models, rather than only their training loss. Directly transferring language-model scaling laws is unreliable for recommendation because equal token counts can contain very different amounts of collaborative information, and because a lower training loss can coexist with worse ranking performance after overfitting. The authors therefore propose Performance Law (P-Law), a fitted function that predicts HR and NDCG from model depth, embedding dimension, and an entropy-adjusted measure of data scale.

P-Law addresses data quality by estimating Real Entropy from repeated subsequences using Lempel-Ziv-style minimum match lengths. Because the paper's Real Entropy convention grows with duplication, it uses the inverse value and defines effective data scale as `#Tokens x inverse Real Entropy`. This discounts repetitive, low-information interaction sequences that raw token counts would treat as equally useful. On the model side, P-Law adds logarithmic and reciprocal decay terms for depth, embedding dimension, and data size. These terms allow the fitted performance surface to rise and then fall, representing the overfitting behavior that a monotonic loss-based scaling law cannot capture.

Experiments use MovieLens-1M, Amazon Books, KuaiRand-Pure, and a private music dataset with more than 19 million users and 513 million interactions in its largest configuration. Models are evaluated with leave-one-out splits using HR@10 and NDCG@10. The entropy-adjusted data measure reaches an `R^2` of 0.9881 for loss-related fitting and above 0.99 for HR/NDCG data-parameter fitting, compared with 0.8776 or lower for token count alone. Across dataset and sequence-length settings, P-Law consistently fits performance better than the original Scaling Law and Precision Scaling Law. Its `R^2` ranges from 0.649 to 0.951 in the main table, while the baseline can fall as low as 0.142. The fitted law also identifies strong global and constrained depth/embedding configurations, and its trends transfer to HSTU, LLaMA2, SASRec, LightGCN, Mamba, Wukong, and DiffuRec analyses.

The practical contribution is a cheaper way to screen model and data configurations before committing to the largest training runs. However, P-Law is an empirical fitting framework rather than a universal causal law: it still requires a grid of completed experiments, depends on the chosen architecture and metric, and reports weaker fits in some small-data settings. The private dataset also limits reproducibility. The authors identify the present scope as sequential recommendation and leave broader ranking and retrieval tasks, as well as validation on larger datasets, for future work.

## 繁中摘要

這篇論文研究 scaling law 能否直接預測大型 sequential recommendation 模型的排序品質，而不只是 training loss。把語言模型的 scaling law 直接搬到推薦系統並不可靠：相同 token 數可能包含差異很大的 collaborative information，而且模型過度擬合後，training loss 下降不代表實際 ranking performance 會提升。作者因此提出 Performance Law（P-Law），用模型深度、embedding dimension 與經 entropy 修正的 data scale，直接擬合並預測 HR 和 NDCG。

在資料品質方面，P-Law 透過類似 Lempel-Ziv minimum match length 的方法，從重複子序列估計 Real Entropy。由於論文定義下的 Real Entropy 會隨重複程度增加，方法使用其倒數，並把有效 data scale 定義為 `#Tokens x inverse Real Entropy`，讓大量重複、資訊量低的互動序列不會被 raw token count 高估。模型端則對 depth、embedding dimension 與 data size 加入 logarithmic 與 reciprocal decay terms，使擬合曲面能呈現效能先上升再下降的型態，捕捉單調 loss-based scaling law 無法描述的 overfitting。

實驗涵蓋 MovieLens-1M、Amazon Books、KuaiRand-Pure，以及一個擁有超過 1,900 萬使用者、最大設定約 5.13 億筆互動的私有音樂資料集，採 leave-one-out evaluation，指標為 HR@10 與 NDCG@10。Entropy-adjusted data measure 在 loss fitting 的 `R^2` 達 0.9881，在 HR/NDCG data-parameter fitting 則超過 0.99；只使用 token count 時最高為 0.8776，HR/NDCG 更低於 0.83。主要表格中，P-Law 在不同資料集與 sequence length 設定的 `R^2` 為 0.649 至 0.951，皆優於原始 Scaling Law 與 Precision Scaling Law，baseline 最低只有 0.142。擬合結果也能找出表現良好的全域或受限 depth/embedding 設定，並延伸到 HSTU、LLaMA2、SASRec、LightGCN、Mamba、Wukong 與 DiffuRec 的分析。

實務上，P-Law 可在投入最大規模訓練前，先篩選較有潛力的模型與資料設定，降低反覆調參成本。不過，它仍是 empirical fitting framework，而非普遍成立的 causal law：方法需要先完成一組參數網格實驗，結果會受 architecture 與 metric 影響，在部分小資料設定的 fitting 也較弱；私有資料集則限制了完整重現。作者指出目前驗證範圍集中在 sequential recommendation，未來才會擴展到更大型資料，以及 ranking、retrieval 等其他推薦任務。

## Notes

- The official source code is available at https://github.com/USTC-StarTeam/P-Law.
- The largest reported experiment used 48 industrial GPUs and took 24 hours, so the fitting stage itself is not cost-free.
- The paper reports statistical significance for the main fitting comparisons, and provides MAE and RMSE results in the appendix in addition to `R^2`.
