---
date: 2026-09-23
title: "Interpolating Item and User Fairness in Multi-Sided Recommendations"
authors: "Qinyi Chen, Jason Cheuk Nam Liang, Negin Golrezaei, Djallel Bouneffouf"
venue: "NeurIPS 2024"
---

# Interpolating Item and User Fairness in Multi-Sided Recommendations

- Paper page: https://proceedings.neurips.cc/paper_files/paper/2024/hash/59d4e18a60490b9ed9913f3be2b14839-Abstract-Conference.html
- PDF: https://proceedings.neurips.cc/paper_files/paper/2024/file/59d4e18a60490b9ed9913f3be2b14839-Paper-Conference.pdf
- Local PDF: [../../pdfs/2026-09/2026-09-23-interpolating-item-and-user-fairness-in-multi-sided-recommendations.pdf](../../pdfs/2026-09/2026-09-23-interpolating-item-and-user-fairness-in-multi-sided-recommendations.pdf)
- Venue: NeurIPS 2024

## English Summary

This paper studies recommendation on multi-sided platforms, where the platform, items or sellers, and users have objectives that can conflict. Optimizing only platform revenue can deprive niche items of exposure and reduce utility for users who prefer them, while optimizing only one stakeholder's fairness can impose a large cost on the others. The authors first define within-group benchmarks: an item-fair policy obtained by maximizing a configurable social-welfare function over item outcomes, and a user-fair policy that gives each user type its highest-utility item. Their FAIR framework then maximizes platform revenue subject to every item and user receiving at least fractions `delta_I` and `delta_U` of their respective fair-benchmark outcomes. These interpretable parameters expose the price-of-fairness tradeoff and allow different outcome definitions, fairness notions, and operational constraints.

The online setting is harder because user-type arrival rates and purchase probabilities are unknown, the platform observes only the purchase outcome of the displayed item, and even fairness-constraint satisfaction cannot be directly verified. The proposed Fair Online Recommendation algorithm for Multi-sided platforms (FORM) combines two mechanisms. It solves a version of FAIR whose constraints are relaxed according to confidence bounds on the estimated parameters, preventing estimation error from excluding a genuinely fair policy. It then mixes that solution with decaying randomized exploration so that low-probability items continue to receive enough observations. Arrival rates are estimated by sample means and purchase probabilities by inverse-probability weighting.

Under a local Lipschitz assumption on user outcomes and item-fair solutions, FORM achieves expected time-averaged revenue regret and fairness regret of `O(M N^(1/3) T^(-1/3))`, where `M` is the number of user types, `N` the number of items, and `T` the number of rounds. For common fairness notions such as max-min fairness, Kalai-Smorodinsky bargaining, and demographic parity, each round is dominated by linear programs with `MN` variables. The paper also extends the framework to periodic arrivals and assortment recommendation; the periodic version retains the same regret order.

The main case study uses Amazon Clothing, Shoes and Jewelry reviews. Users are clustered into five types, 30 products with high cross-type relevance variance are selected, each arriving user sees up to three products, and each run contains 2,000 arrivals. Results averaged over ten simulations show FORM's revenue converging toward the hindsight FAIR optimum. In this setup, setting both fairness levels to 0.2 keeps revenue loss below roughly 10%, whereas FairRec and TFROM lose about 38% because they do not optimize platform revenue. FORM also brings item and user outcomes close to their requested fairness levels. These are simulated case studies rather than a live deployment; the authors identify evolving preferences, long-term fairness, and evaluation using satisfaction, retention, and diversity as future work.

## 繁中摘要

這篇論文研究多邊平台上的推薦問題，其中平台、物品或賣家，以及使用者的目標可能互相衝突。若只最大化平台營收，利基物品可能失去曝光，偏好這些物品的使用者也可能獲得較低效用；但若只追求單一利害關係人的公平，也可能讓其他群體付出很大代價。作者先定義群體內公平基準：物品端透過可自訂的社會福利函數，找出最大化物品 outcomes 的公平政策；使用者端則讓每種使用者取得效用最高的物品。接著，FAIR 框架在最大化平台營收的同時，要求每個物品與每種使用者至少取得各自公平基準的 `delta_I` 與 `delta_U` 比例。這兩個可解釋參數能直接呈現公平成本，也可搭配不同 outcome、公平定義與營運限制。

線上情境更困難，因為平台不知道使用者類型的到達率與購買機率，只能觀察被展示物品是否被購買，甚至無法直接判定公平約束是否滿足。作者提出 FORM（Fair Online Recommendation algorithm for Multi-sided platforms），結合兩個機制。第一，依參數估計的信賴界限放寬 FAIR 的公平約束，避免估計誤差把真正公平的政策排除在可行集合外。第二，把此解與逐步衰減的隨機探索混合，讓推薦機率較低的物品仍有足夠觀測。到達率以樣本平均估計，購買機率則用 inverse-probability weighting 估計。

在使用者 outcome 與物品公平解滿足局部 Lipschitz 條件時，FORM 的期望平均營收 regret 與公平 regret 都具有 `O(M N^(1/3) T^(-1/3))` 上界，其中 `M` 是使用者類型數、`N` 是物品數、`T` 是互動輪數。對 max-min fairness、Kalai-Smorodinsky bargaining 與 demographic parity 等常見公平定義，每輪主要成本是求解含 `MN` 個變數的線性規劃。論文也擴充到週期性到達與 assortment recommendation；週期性版本保留相同量級的 regret 保證。

主要案例使用 Amazon Clothing, Shoes and Jewelry 評論資料。作者把使用者分成 5 類，選出 30 個跨類型 relevance 差異較大的商品，每次最多展示 3 個商品，每次模擬包含 2,000 次使用者到訪。10 次模擬的平均結果顯示，FORM 的營收會收斂到事後計算的 FAIR 最佳值；在此設定中，兩端公平參數都設為 0.2 時，營收損失可控制在約 10% 以內，而不考慮平台營收的 FairRec 與 TFROM 約損失 38%。FORM 也能讓物品與使用者 outcomes 接近指定公平水準。不過，這些結果仍是模擬案例而非真實線上部署；作者把偏好隨時間變動、長期公平，以及使用者滿意度、留存率與推薦多樣性等評估列為後續工作。

## Notes

- The framework supports item outcomes based on visibility, market share, revenue, or weighted combinations of these metrics.
- FORM's fairness regret is the largest time-averaged violation among all item and user fairness constraints, rather than a guarantee that every individual round is fair.
- The Amazon experiment uses matrix factorization and k-means to define user types and a multinomial-logit model to translate relevance scores into simulated purchase probabilities and user utilities.
