---
date: 2026-08-25
title: "Wukong: Towards a Scaling Law for Large-Scale Recommendation"
authors: "Buyun Zhang, Liang Luo, Yuxin Chen, Jade Nie, Xi Liu, Shen Li, Yanli Zhao, Yuchen Hao, Yantao Yao, Ellie Dingqiao Wen, Jongsoo Park, Maxim Naumov, Wenlin Chen"
venue: "ICML 2024"
---

# Wukong: Towards a Scaling Law for Large-Scale Recommendation

- Paper page: https://proceedings.mlr.press/v235/zhang24ao.html
- PDF: https://raw.githubusercontent.com/mlresearch/v235/main/assets/zhang24ao/zhang24ao.pdf
- Local PDF: [../../pdfs/2026-08/2026-08-25-wukong-towards-a-scaling-law-for-large-scale-recommendation.pdf](../../pdfs/2026-08/2026-08-25-wukong-towards-a-scaling-law-for-large-scale-recommendation.pdf)
- Venue: ICML 2024

## English Summary

This paper targets a core weakness of large-scale recommender systems: unlike language models, recommendation models often do not improve predictably when scaled up. The authors argue that the common strategy of sparse scaling, mainly enlarging embedding tables, is expensive and does not sufficiently improve the model's ability to capture complex feature interactions. They instead focus on dense scaling, where the interaction component of the model grows with compute and parameter budgets.

The proposed model, Wukong, is built from stacked Factorization Machine-based interaction layers. Each layer captures second-order interactions over its inputs, then transforms the interaction results into new embeddings that can be used by later layers. This stacked design is inspired by binary exponentiation, so taller and wider Wukong models can efficiently represent higher-order feature interactions without relying only on larger embedding tables.

Experiments show that Wukong achieves state-of-the-art AUC on six public recommendation datasets, including Frappe, MicroVideo, MovieLens Latest, KuaiVideo, TaobaoAds, and Criteo Terabyte. On a much larger internal dataset with 146B examples and 720 features, Wukong maintains a scaling trend across roughly two orders of magnitude in compute complexity and outperforms strong baselines such as DLRM, DCNv2, AutoInt+, FinalMLP, MaskNet, and AFN+. The paper is important because it frames recommender-system scaling as an architecture problem, not just an embedding-table-size problem.

## 繁中 Summary

這篇論文關注大型推薦系統的一個核心問題：推薦模型不像語言模型一樣，通常無法只靠放大模型就穩定提升效果。作者指出，既有推薦模型常見的 sparse scaling 主要是加大 embedding table，成本很高，但不一定能提升模型捕捉複雜 feature interaction 的能力。因此論文改從 dense scaling 出發，嘗試讓模型的 interaction component 隨著 compute 和參數預算擴大而有效變強。

作者提出的 Wukong 是由多層 Factorization Machine-based interaction layer 堆疊而成。每一層先針對輸入捕捉二階交互作用，再把 interaction 結果轉換成新的 embedding，供後續層繼續使用。這個設計受到 binary exponentiation 啟發，因此只要加深或加寬模型，就能更有效率地表示高階特徵交互，而不是單純依賴更大的 embedding table。

實驗顯示，Wukong 在六個公開推薦資料集上達到 state-of-the-art AUC，包括 Frappe、MicroVideo、MovieLens Latest、KuaiVideo、TaobaoAds 和 Criteo Terabyte。在更大的內部資料集上，該資料集包含 146B examples 與 720 個 features，Wukong 在約兩個數量級的 compute complexity 範圍內維持穩定 scaling trend，並優於 DLRM、DCNv2、AutoInt+、FinalMLP、MaskNet、AFN+ 等強 baseline。這篇論文的重點在於，它把推薦系統 scaling 視為架構問題，而不只是 embedding table 要不要加大的問題。

## Notes

- Wukong is especially relevant for industrial recommendation systems where sparse embedding tables already dominate cost.
- The paper argues for scaling the interaction network, not only the embedding tables.
- The strongest evidence comes from the internal 146B-example dataset, where Wukong keeps improving across much larger compute budgets than public benchmarks can test.
