---
date: 2026-09-02
title: "Federated Graph Learning for Cross-Domain Recommendation"
authors: "Ziqi Yang, Zhaopeng Peng, Zihui Wang, Jianzhong Qi, Chaochao Chen, Weike Pan, Chenglu Wen, Cheng Wang, Xiaoliang Fan"
venue: "NeurIPS 2024"
---

# Federated Graph Learning for Cross-Domain Recommendation

- Paper page: https://proceedings.neurips.cc/paper_files/paper/2024/hash/774164b966cc277c82a960934445140d-Abstract-Conference.html
- PDF: https://proceedings.neurips.cc/paper_files/paper/2024/file/774164b966cc277c82a960934445140d-Paper-Conference.pdf
- Local PDF: [../../pdfs/2026-09/2026-09-02-federated-graph-learning-for-cross-domain-recommendation.pdf](../../pdfs/2026-09/2026-09-02-federated-graph-learning-for-cross-domain-recommendation.pdf)
- Venue: NeurIPS 2024

## English Summary

This paper studies broader-source cross-domain recommendation, where a target domain can benefit from multiple source domains but must handle two practical risks: privacy leakage and negative transfer. Existing cross-domain recommendation methods often assume a simpler dual-domain setting or require careful manual control over how much source knowledge is transferred. In broader multi-domain settings, low-quality or mismatched source domains can degrade recommendation quality, while sharing embeddings across domains can expose sensitive user-item interactions.

The authors propose FedGCDR, a federated graph learning framework built around a horizontal-vertical-horizontal pipeline. Each source domain first trains a GAT-based federated recommender without centralizing local user ratings. Then a positive knowledge transfer module extracts source-domain embeddings, adds Gaussian differential privacy noise, and maps the source feature space into the target space. Finally, a positive knowledge activation module expands the target-domain graph with virtual social links, learns domain attention over transferred knowledge, and fine-tunes the target model to suppress harmful information.

Experiments on 4-domain, 8-domain, and 16-domain subsets of the Amazon review dataset show that FedGCDR and its differentially private variant outperform several cross-domain and federated recommendation baselines on Books and CDs target domains. The ablation study indicates that both modules matter: feature mapping is more important for information-poor target domains, while negative-transfer filtering is especially important for stronger target domains. The main limitation is that evaluation relies on Amazon domains and overlapping users, so generalization to other multi-domain datasets remains an open question.

## 繁中摘要

這篇論文研究的是 broader-source cross-domain recommendation：目標 domain 可以利用多個來源 domain 的知識來改善推薦，但同時會遇到兩個問題。第一是隱私，跨 domain 傳遞 embedding 可能讓其他參與方推回敏感的 user-item interaction。第二是 negative transfer，當某些來源 domain 品質差或和目標 domain 差異太大時，轉移過來的資訊反而會讓推薦表現變差。

作者提出 FedGCDR，一個 federated graph learning 架構，流程是 horizontal-vertical-horizontal。首先，每個來源 domain 用 GAT-based federated recommender 在不集中使用者評分資料的情況下訓練本地模型。接著，positive knowledge transfer module 會抽取來源 domain 的 embedding，加入 Gaussian differential privacy noise，並用 feature mapping 對齊到目標 domain 的表示空間。最後，positive knowledge activation module 會用 transferred embedding 擴充目標 domain 的圖結構，透過 domain attention 選擇有用知識，並 fine-tune 目標模型以降低 harmful source knowledge 的影響。

實驗使用 Amazon review dataset 的 4、8、16 個 domain 設定，並以 Books 和 CDs 作為目標 domain。結果顯示 FedGCDR 及其加入 DP 的版本在多個 HR/NDCG 指標上優於 FedGNN、EMCDR、PriCDR、FedCT、FedCDR 等 baseline。消融實驗也指出兩個模組各自重要：對資料較少的 domain，正確 mapping 外部知識較關鍵；對本身資訊較充分的 domain，過濾 negative transfer 更重要。不過，論文的主要限制是實驗集中在 Amazon domain 且需要 overlapping users，對其他真實多 domain 推薦資料的泛化仍需要更多驗證。

## Notes

- This is a good paper for privacy-preserving, multi-domain recommendation settings where source domains cannot directly share raw interactions.
- The core modeling idea is not only to transfer more cross-domain knowledge, but to control which transferred knowledge is activated in the target graph.
- The approach assumes overlapping users across domains, which may be a deployment constraint in real products.
