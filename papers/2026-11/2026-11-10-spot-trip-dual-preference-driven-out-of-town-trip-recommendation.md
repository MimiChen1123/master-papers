---
date: 2026-11-10
title: "SPOT-Trip: Dual-Preference Driven Out-of-Town Trip Recommendation"
authors: "Yinghui Liu, Hao Miao, Guojiang Shen, Yan Zhao, Xiangjie Kong, Ivan Lee"
venue: "NeurIPS 2025"
---

# SPOT-Trip: Dual-Preference Driven Out-of-Town Trip Recommendation

- Paper page: https://proceedings.neurips.cc/paper_files/paper/2025/hash/d32abef446ead79ac1e7f80419a7b82f-Abstract-Conference.html
- PDF: https://proceedings.neurips.cc/paper_files/paper/2025/file/d32abef446ead79ac1e7f80419a7b82f-Paper-Conference.pdf
- Local PDF: [../../pdfs/2026-11/2026-11-10-spot-trip-dual-preference-driven-out-of-town-trip-recommendation.pdf](../../pdfs/2026-11/2026-11-10-spot-trip-dual-preference-driven-out-of-town-trip-recommendation.pdf)
- Code: https://github.com/Yinghui-Liu/SPOT-Trip
- Venue: NeurIPS 2025

## English Summary

SPOT-Trip introduces out-of-town trip recommendation: given a user's hometown history plus an origin, destination, and number of stops in an unfamiliar region, the model generates the intermediate sequence of points of interest (POIs). This differs from conventional next-POI recommendation because it must construct a complete itinerary under severe out-of-town data sparsity. The paper argues that user preference has two complementary parts: stable interests learned from hometown behavior and dynamic interests that evolve continuously with time, location, and trip context.

The framework has three modules. Knowledge-Enhanced Static Preference Learning builds a POI attribute knowledge graph from categories, ratings, reviews, and regions, then uses relation-aware attention to enrich POI representations. An alignment objective maps aggregated hometown preference into the out-of-town preference space. ODE-Based Dynamic Preference Learning encodes spatiotemporal behavior with a Transformer, uses a neural ordinary differential equation to model continuous and irregular preference drift, and combines it with a temporal point process that estimates the instantaneous likelihood of behavioral events. A final Transformer-based fusion module combines the static preference, dynamic state, and trip query to generate intermediate POIs.

Experiments use Foursquare and Yelp with user-disjoint 80/10/10 train, validation, and test splits. Evaluation reports F1 and order-aware PairsF1 on intermediate POIs, plus full-trip variants that include the fixed origin and destination. SPOT-Trip is best on all eight main metrics. On Foursquare it reaches F1 0.0400 and PairsF1 0.0109, improving over the strongest baselines by 6.67% and 15.96%; on Yelp it reaches 0.0399 and 0.0190, gains of 17.01% and 13.90%. Ablations show that removing static preference learning causes a 10.02% F1 and 21.79% PairsF1 drop on Yelp. The model also remains strongest when only 40%-80% of hometown trajectories are retained.

The method is a substantial new formulation, but absolute intermediate-POI scores remain low, which underlines the difficulty of exact itinerary reconstruction. Evaluation is limited to two location-based social-network datasets and offline overlap with recorded trips; it does not measure live user satisfaction, feasibility constraints such as opening hours or travel time, or fairness across regions. The authors also observe repeated recommendations at nearby positions, which can reduce itinerary diversity, and weaker performance when a query specifies only an origin or destination. Neural ODE solving, knowledge-graph construction, and multiple loss components add complexity and require dataset-specific tuning.

## 繁中摘要

SPOT-Trip 提出 out-of-town trip recommendation：給定使用者的 hometown history，以及陌生地區中的 origin、destination 與 stops 數量，模型要生成中間的 Points of Interest（POIs）序列。這不同於傳統 next-POI recommendation，因為模型必須在 out-of-town data 極度稀疏時建構完整 itinerary。作者將 user preference 分成兩個互補部分：從 hometown behavior 學到的穩定長期興趣，以及隨時間、位置與旅程情境持續變化的 dynamic interests。

框架包含三個模組。Knowledge-Enhanced Static Preference Learning 以 POI categories、ratings、reviews 與 regions 建立 attribute knowledge graph，再透過 relation-aware attention 強化 POI representations，並以 alignment objective 將 aggregated hometown preference 映射到 out-of-town preference space。ODE-Based Dynamic Preference Learning 先用 Transformer 編碼 spatiotemporal behavior，再用 neural ordinary differential equation 建模連續且不規則的 preference drift，並結合 temporal point process 估計各時間點 behavioral events 的即時機率。最後，Transformer-based fusion module 整合 static preference、dynamic state 與 trip query，生成 intermediate POIs。

實驗使用 Foursquare 與 Yelp，並依使用者切分為 80/10/10 的 train、validation、test sets。評估包含 intermediate POIs 的 F1、考慮順序的 PairsF1，以及納入固定 origin/destination 的 full-trip variants。SPOT-Trip 在八個主要 metrics 都是最佳。Foursquare 的 F1/PairsF1 為 0.0400/0.0109，相較最強 baselines 提升 6.67%/15.96%；Yelp 則為 0.0399/0.0190，提升 17.01%/13.90%。Ablation 顯示移除 static preference learning 後，Yelp 的 F1 與 PairsF1 分別下降 10.02% 與 21.79%。即使只保留 40%-80% hometown trajectories，SPOT-Trip 仍優於比較方法。

這項工作提出重要的新問題設定，但 intermediate-POI 的絕對分數仍低，顯示精確重建 itinerary 非常困難。評估只涵蓋兩個 location-based social-network datasets，且以 offline recorded-trip overlap 為主，未衡量真實使用者滿意度、營業時間或旅行時間等 feasibility constraints，也未分析不同地區間的 fairness。作者亦觀察到相鄰位置可能重複推薦，降低行程多樣性；query 只提供 origin 或 destination 時，表現也較弱。Neural ODE solver、knowledge-graph construction 與多個 loss components 增加了系統複雜度，並需要針對資料集調參。

## Notes

- The paper frames this as the first systematic study of complete out-of-town trip recommendation rather than only next-POI prediction.
- Foursquare and Yelp records are filtered to retain users with both hometown and out-of-town check-ins and valid trip durations.
- The implementation uses 32-dimensional embeddings, four Transformer layers in the dynamic module, a dopri5 ODE solver, and an RTX 4090 GPU.
- The authors release code at https://github.com/Yinghui-Liu/SPOT-Trip.
