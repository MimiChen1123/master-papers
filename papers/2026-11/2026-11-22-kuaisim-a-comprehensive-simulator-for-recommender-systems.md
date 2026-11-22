---
date: 2026-11-22
title: "KuaiSim: A Comprehensive Simulator for Recommender Systems"
authors: "Kesen Zhao, Shuchang Liu, Qingpeng Cai, Xiangyu Zhao, Ziru Liu, Dong Zheng, Peng Jiang, Kun Gai"
venue: "NeurIPS 2023 Datasets and Benchmarks Track"
---

# KuaiSim: A Comprehensive Simulator for Recommender Systems

- Paper page: https://proceedings.neurips.cc/paper_files/paper/2023/hash/8c7f8f98f9a8f5650922dd4545254f28-Abstract.html
- PDF: https://proceedings.neurips.cc/paper_files/paper/2023/file/8c7f8f98f9a8f5650922dd4545254f28-Paper-Datasets_and_Benchmarks.pdf
- Local PDF: [../../pdfs/2026-11/2026-11-22-kuaisim-a-comprehensive-simulator-for-recommender-systems.pdf](../../pdfs/2026-11/2026-11-22-kuaisim-a-comprehensive-simulator-for-recommender-systems.pdf)
- Code: https://github.com/Applied-Machine-Learning-Lab/KuaiSim
- Venue: NeurIPS 2023 Datasets and Benchmarks Track

## English Summary

KuaiSim is a simulator and benchmark for reinforcement-learning recommender systems, intended to reduce the cost and user risk of training policies through live A/B tests. Unlike earlier environments that focus on one task or simplified feedback, it models a hierarchy of request-level list recommendation, whole-session sequential recommendation, and cross-session retention optimization. The environment returns multiple immediate behaviors, a leave signal, and a delayed return-time signal.

The simulator contains three learned or parameterized modules. A Transformer-based immediate-response model encodes user features and interaction history, predicts multiple feedback types, and penalizes highly correlated items in a slate to represent diversity preference. A leave model maintains a configurable patience value that decreases according to recommendation reward. A retention model combines global, personal, and response-dependent biases into a next-day return probability, then samples return time from a geometric distribution. KuaiSim is primarily built from KuaiRand-Pure, which contains randomized exposures, and the authors also demonstrate migration to MovieLens-1M.

The benchmark supplies algorithms and metrics for all three levels. At request level, ListCVAE obtains the highest maximum list reward and diversity among CF, ListCVAE, and PRM. At whole-session level, HAC achieves the best depth, average reward, total reward, coverage, and intra-list diversity among the reported RL policies, including a total reward of 10.1742. At cross-session level, RLUR lowers mean return day to 3.481 and raises simulated retention to 0.607. When the same DDPG agent is trained with different simulators, KuaiSim reports higher click AUC (0.7234), depth (14.86), average reward (0.679), and total reward (10.081) than RL4RS, RecoGym, RecSim, and VirtualTaobao; these differences are significant at p < 0.05. Results average five runs.

These numbers demonstrate internal simulator fidelity and policy performance within the learned environment, not real online gains. The immediate-response model is trained from logged data, while leave and retention dynamics include assumptions and tunable rules, so policies may exploit simulator artifacts and fail under real distribution shift. KuaiRand-Pure is less biased than ordinary logs because of randomized exposure, but it still comes from one short-video platform; MovieLens is also a video-rating domain. KuaiSim does not yet model explainability, fairness, or broader diversity objectives, and the paper provides no simulator-to-production validation. Anonymous identifiers reduce direct privacy exposure, but training on behavioral logs can still encode sensitive preference patterns.

## 繁中摘要

KuaiSim 是為 reinforcement-learning recommender systems 設計的 simulator 與 benchmark，目的在降低直接透過 live A/B tests 訓練 policy 的成本與使用者風險。不同於只處理單一任務或簡化 feedback 的既有環境，它同時建模三個層級：request-level list recommendation、whole-session sequential recommendation，以及 cross-session retention optimization。環境會回傳多種 immediate behaviors、leave signal 與延遲的 return-time signal。

Simulator 包含三個 learned 或 parameterized modules。Transformer-based immediate-response model 編碼 user features 與 interaction history，預測多種 feedback types，並懲罰 slate 中高度相關的 items，以表示 diversity preference。Leave model 維護可調整的 patience value，依 recommendation reward 逐步下降。Retention model 將 global、personal 與 response-dependent biases 合成 next-day return probability，再從 geometric distribution 抽樣 return time。KuaiSim 主要建立於具有 randomized exposures 的 KuaiRand-Pure，作者也示範移植到 MovieLens-1M。

Benchmark 為三個層級提供 algorithms 與 metrics。在 request level，ListCVAE 在 CF、ListCVAE、PRM 中取得最高 maximum list reward 與 diversity。Whole-session level 中，HAC 在文中比較的 RL policies 裡取得最佳 depth、average reward、total reward、coverage 與 intra-list diversity，其中 total reward 為 10.1742。Cross-session level 中，RLUR 將 simulated mean return day 降至 3.481，retention 提升至 0.607。使用相同 DDPG agent 比較不同 simulators 時，KuaiSim 的 click AUC（0.7234）、depth（14.86）、average reward（0.679）與 total reward（10.081）皆高於 RL4RS、RecoGym、RecSim、VirtualTaobao，差異在 p < 0.05 下顯著。結果為五次執行平均。

這些數字證明的是 simulator 內部 fidelity 與 learned environment 中的 policy performance，不代表真實 online gains。Immediate-response model 從 logged data 訓練，而 leave 與 retention dynamics 含有 assumptions 與可調規則，因此 policy 可能利用 simulator artifacts，並在真實 distribution shift 下失效。KuaiRand-Pure 透過 randomized exposure 減少一般 logs 的偏差，但資料仍來自單一 short-video platform；MovieLens 也屬影片評分領域。KuaiSim 尚未建模 explainability、fairness 或更廣泛的 diversity objectives，也沒有 simulator-to-production validation。Anonymous identifiers 降低直接 privacy exposure，但 behavioral logs 仍可能編碼敏感偏好。

## Notes

- Processed KuaiRand-Pure has 27,077 users, 7,551 items, 1,436,609 interactions, and 246,738 sessions.
- The simulator uses six positive feedback signals plus hate and leave signals; return time is capped at ten days.
- Whole-session metrics include depth, average and total reward, coverage, and intra-list diversity.
- The paper evaluates data migration on MovieLens-1M but does not cover non-video domains.
