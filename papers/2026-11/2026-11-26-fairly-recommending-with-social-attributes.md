---
date: 2026-11-26
title: "Fairly Recommending with Social Attributes: A Flexible and Controllable Optimization Approach"
authors: "Jinqiu Jin, Haoxuan Li, Fuli Feng, Sihao Ding, Peng Wu, Xiangnan He"
venue: "NeurIPS 2023 Main Conference"
---

# Fairly Recommending with Social Attributes: A Flexible and Controllable Optimization Approach

- [Official paper page](https://proceedings.neurips.cc/paper_files/paper/2023/hash/436d042b2dd81214d23ae43eb196b146-Abstract.html)
- [Official PDF](https://proceedings.neurips.cc/paper_files/paper/2023/file/436d042b2dd81214d23ae43eb196b146-Paper-Conference.pdf)
- [Local PDF](../../pdfs/2026-11/2026-11-26-fairly-recommending-with-social-attributes.pdf)

## English Summary

Equal exposure across item groups can still produce unequal potential reach if some groups are shown to users with larger social networks. The paper extends statistical parity and equal opportunity with Neighborhood SP (NSP) and Neighborhood EO (NEO). Both weight predicted interaction probabilities by estimated social utility; NEO restricts the comparison to observed positive interactions. SoFA uses multi-objective gradient updates to train models for different trade-offs between direct and social exposure disparities while constraining the BPR training loss.

The offline evaluation uses KuaiRec and Epinions, with follower and trustor counts as proxies for social utility. On KuaiRec (Table 1), the BPR matrix-factorization baseline has NDCG@5 of 0.2426, SP of 0.0966, and NSP of 0.1119. One SoFA setting obtains 0.2413, 0.0074, and 0.0194, respectively; another reduces NSP further to 0.0096 but raises SP to 0.0296 relative to that setting. The training-loss constraint does not directly guarantee test NDCG, and the social counts do not measure actual downstream sharing or engagement.

## 繁中摘要

即使不同商品群組獲得相近的直接曝光，如果其中一組較常推薦給社交網絡較大的使用者，潛在的二次觸及仍可能不均。作者把統計同等（SP）和機會均等（EO）延伸為 NSP 與 NEO：兩者都以估計的社交效益加權預測互動機率，NEO 則僅比較觀測到的正向互動。SoFA 以多目標梯度更新，在不同的直接曝光與社交曝光取捨下訓練模型，並限制 BPR 訓練損失。

離線實驗使用 KuaiRec 與 Epinions，分別以追蹤者人數與信任該使用者的人數代理社交效益。KuaiRec 表 1 中，BPR 矩陣分解基準的 NDCG@5、SP、NSP 分別為 0.2426、0.0966、0.1119；其中一組 SoFA 設定分別為 0.2413、0.0074、0.0194。另一組設定將 NSP 進一步降到 0.0096，但 SP 相對上升至 0.0296。限制訓練損失不等於直接保證測試集的 NDCG；社交人數也不代表實際的下游分享或互動。
