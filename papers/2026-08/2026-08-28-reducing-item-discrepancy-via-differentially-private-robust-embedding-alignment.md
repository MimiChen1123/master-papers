---
date: 2026-08-28
title: "Reducing Item Discrepancy via Differentially Private Robust Embedding Alignment for Privacy-Preserving Cross Domain Recommendation"
authors: "Weiming Liu, Xiaolin Zheng, Chaochao Chen, Jiahe Xu, Xinting Liao, Fan Wang, Yanchao Tan, Yew-Soon Ong"
venue: "ICML 2024"
---

# Reducing Item Discrepancy via Differentially Private Robust Embedding Alignment for Privacy-Preserving Cross Domain Recommendation

- Paper page: https://proceedings.mlr.press/v235/liu24cf.html
- PDF: https://raw.githubusercontent.com/mlresearch/v235/main/assets/liu24cf/liu24cf.pdf
- Local PDF: [../../pdfs/2026-08/2026-08-28-reducing-item-discrepancy-via-differentially-private-robust-embedding-alignment.pdf](../../pdfs/2026-08/2026-08-28-reducing-item-discrepancy-via-differentially-private-robust-embedding-alignment.pdf)
- Venue: ICML 2024

## English Summary

This paper studies privacy-preserving cross-domain recommendation, where the goal is to share useful knowledge across domains without exposing raw user-item ratings, reviews, or overlapping identities. This is a hard setting because many cross-domain recommendation methods assume shared users or items, but privacy constraints can make those links unavailable. The authors focus on the case where users and items do not overlap across domains.

The proposed model, RidCDR, combines a single-domain rating prediction module with a private-robust embedding alignment module. The alignment component uses Differentially Private-Robust Adaptation, which first applies differentially private projection to item embeddings and then uses robust reweighted sample adaptation based on unbalanced optimal transport. This design aims to align relevant items across domains while filtering unrelated or noisy items that could cause negative transfer.

Experiments on Amazon and Douban cross-domain recommendation datasets show that RidCDR improves HR and NDCG over single-domain recommendation models, adversarial cross-domain methods, and optimal-transport-based baselines. The ablation results indicate that both private projection and robust reweighting matter: domain alignment helps with sparsity, while robust sample selection reduces harmful transfer under privacy-preserving constraints.

## 繁中 Summary

這篇論文研究 privacy-preserving cross-domain recommendation，也就是希望跨 domain 分享有用知識，但不能暴露原始 user-item ratings、reviews，或依賴可辨識的重疊使用者與物品。這個設定很困難，因為許多 cross-domain recommendation 方法都假設有 shared users 或 shared items；但在隱私限制下，這些連結可能不存在或不能使用。作者特別處理 users 和 items 在不同 domains 之間都不重疊的情境。

作者提出的 RidCDR 結合了單一 domain 的 rating prediction module，以及 private-robust embedding alignment module。alignment 部分使用 Differentially Private-Robust Adaptation，先對 item embeddings 做 differentially private projection，再透過 unbalanced optimal transport 進行 robust reweighted sample adaptation。這樣可以在保護隱私的前提下對齊跨 domain 的相關 items，同時過濾不相關或 noisy items，降低 negative transfer。

在 Amazon 和 Douban 的 cross-domain recommendation datasets 上，RidCDR 在 HR 和 NDCG 上優於 single-domain recommendation models、adversarial cross-domain methods，以及 optimal-transport-based baselines。Ablation 顯示 private projection 和 robust reweighting 都有作用：domain alignment 有助於緩解 sparsity，而 robust sample selection 則能在 privacy-preserving constraints 下減少錯誤知識轉移。

## Notes

- This paper is useful for CDR scenarios where privacy rules prevent direct sharing of identities or raw interaction data.
- The key modeling choice is to align privacy-protected item embeddings instead of relying on overlapped users or items.
- RidCDR is especially relevant when cross-domain transfer risks negative transfer from unrelated items.
