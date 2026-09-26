---
date: 2026-09-26
title: "How Does Topology Bias Distort Message Passing in Graph Recommender? A Dirichlet Energy Perspective"
authors: "Yanbiao Ji, Yue Ding, Dan Luo, Chang Liu, Yuxiang Lu, Xin Xin, Hongtao Lu"
venue: "NeurIPS 2025"
---

# How Does Topology Bias Distort Message Passing in Graph Recommender? A Dirichlet Energy Perspective

- Paper page: https://proceedings.neurips.cc/paper_files/paper/2025/hash/40b5237c3e025c72c02dd8b6716dac76-Abstract-Conference.html
- PDF: https://proceedings.neurips.cc/paper_files/paper/2025/file/40b5237c3e025c72c02dd8b6716dac76-Paper-Conference.pdf
- Local PDF: [../../pdfs/2026-09/2026-09-26-how-does-topology-bias-distort-message-passing-in-graph-recommender.pdf](../../pdfs/2026-09/2026-09-26-how-does-topology-bias-distort-message-passing-in-graph-recommender.pdf)
- Venue: NeurIPS 2025

## English Summary

This paper studies why message passing in graph recommender systems amplifies popularity bias already present in the user-item interaction graph. The authors call the skewed degree structure topology bias and analyze it through Dirichlet energy. For LightGCN-style propagation, they show an equivalence to minimizing normalized graph Dirichlet energy with Tikhonov regularization around the initial embeddings. Under this formulation, a node's optimized squared embedding norm has a degree-dependent lower bound, so high-degree items tend to acquire larger norms and consequently larger inner-product recommendation scores. They also bound each node's one-layer embedding update by its local Dirichlet energy; since popular nodes empirically have more local energy, repeated propagation can create a self-reinforcing advantage.

The proposed Test-time Simplicial Propagation (TSP) extends inference from pairwise graph edges to higher-order simplicial complexes. It first constructs a semantic graph by connecting pretrained node embeddings above a similarity threshold, which gives tail nodes additional semantic neighbors. It then lifts nodes and cliques into simplices, averages information within each simplex, propagates signals between simplices of the same order using Hodge Laplacians, and maps the resulting multi-order representations back to nodes for mean fusion with the original embeddings. A contraction result for part of the simplicial signal space provides the theoretical motivation for reducing oversized, popularity-dominated embedding norms.

Experiments use LightGCN, SimGCL, and LightGCL backbones on Adressa, Gowalla, Yelp2018, MovieLens-10M, and Globo. Data are split 80/10/10, and evaluation reports Recall@20 and NDCG@20 both overall and for the 20% least-popular items. Across the 15 backbone-dataset combinations, TSP consistently improves tail-item recommendation; many gains over the next-best debiasing method are statistically significant, with especially large relative gains for contrastive backbones. With LightGCN, TSP also improves Expected Free Discovery and Average Percentage of Tail Items across all five datasets. The Gowalla ablation shows that semantic-graph propagation helps, but the full higher-order simplicial pipeline provides substantially larger gains.

TSP is a post-training method and does not retrain the recommender. Its one-time preprocessing ranges from 2.54 to 91.34 seconds in the reported datasets, while inference adds roughly 0.061 seconds on Adressa and 0.075 seconds on MovieLens-10M relative to LightGCN. These measurements support practical use in the evaluated offline setting, but building a semantic graph and simplicial complex may behave differently at production scale. More importantly, the theoretical analysis assumes simplified message passing without edge weights or nonlinear activations, so it does not fully characterize more complex GNN recommenders. The reported fairness metrics concern long-tail exposure and discovery, not demographic or user-group fairness.

## 繁中摘要

這篇論文研究圖推薦系統的 message passing 為何會放大使用者-物品互動圖中原本就存在的熱門度偏差。作者把偏斜的 degree 結構稱為 topology bias，並從 Dirichlet energy 分析。對 LightGCN 類型的傳播，他們證明其等價於在初始 embedding 附近，以 Tikhonov regularization 最小化正規化圖 Dirichlet energy。在此形式下，節點最佳化後的 embedding norm 平方具有與 degree 有關的下界，因此高 degree 物品傾向取得較大的 norm，進而獲得較高的 inner-product 推薦分數。論文也證明單層 embedding 更新幅度受 local Dirichlet energy 上界約束；由於熱門節點在實驗中具有較高 local energy，反覆傳播可能形成自我強化優勢。

作者提出 Test-time Simplicial Propagation（TSP），把 inference 從成對 graph edge 擴充到高階 simplicial complex。方法先依 pretrained node embedding 的相似度門檻建立 semantic graph，替 tail node 增加語意鄰居；再把節點與 clique 提升為 simplex，在 simplex 內平均資訊，利用 Hodge Laplacian 在同階 simplex 之間傳播，最後把各階表示映射回 node，並與原始 embedding 做平均融合。針對部分 simplicial signal space 的 contraction 結果，提供縮小受熱門度支配之過大 embedding norm 的理論依據。

實驗把 TSP 套用到 LightGCN、SimGCL 與 LightGCL，資料集包括 Adressa、Gowalla、Yelp2018、MovieLens-10M 與 Globo。資料依 80/10/10 切分，並同時回報整體與熱門度最低 20% 物品的 Recall@20、NDCG@20。在 15 個 backbone 與資料集組合中，TSP 都提升 tail-item 推薦；許多相對次佳 debiasing 方法的增益具有統計顯著性，contrastive backbone 的相對增益尤其大。使用 LightGCN 時，TSP 在五個資料集也都提升 Expected Free Discovery 與 Average Percentage of Tail Items。Gowalla 消融實驗顯示 semantic graph 本身有幫助，但完整的高階 simplicial pipeline 帶來更大的提升。

TSP 是 post-training 方法，不需要重新訓練推薦模型。論文中各資料集的一次性 preprocessing 約為 2.54 至 91.34 秒；相對 LightGCN，Adressa inference 約增加 0.061 秒，MovieLens-10M 約增加 0.075 秒。這些數字支持其在該離線設定中的實用性，但 production scale 下建立 semantic graph 與 simplicial complex 的成本可能不同。更重要的是，理論只分析沒有 edge weight 與 nonlinear activation 的簡化 message passing，因此不能完整描述更複雜的 GNN 推薦模型。此外，文中的公平指標衡量 long-tail 曝光與探索，不等同人口屬性或使用者群體公平。

## Notes

- The five datasets range from 744 items and 116,321 interactions in Adressa to 158,323 users and 2,520,171 interactions in Globo.
- All reported runs use a single 48 GB Nvidia RTX A6000 Ada GPU and average results over three repetitions.
- TSP's semantic graph is derived from pretrained embeddings, so its correction still depends on the quality and biases of the original model representation.
