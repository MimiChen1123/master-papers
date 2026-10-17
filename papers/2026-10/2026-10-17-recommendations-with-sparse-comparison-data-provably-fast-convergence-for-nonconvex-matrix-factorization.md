---
date: 2026-10-17
title: "Recommendations with Sparse Comparison Data: Provably Fast Convergence for Nonconvex Matrix Factorization"
authors: "Suryanarayana Sankagiri, Jalal Etesami, Matthias Grossglauser"
venue: "ICML 2025"
---

# Recommendations with Sparse Comparison Data: Provably Fast Convergence for Nonconvex Matrix Factorization

- Paper page: https://proceedings.mlr.press/v267/sankagiri25a.html
- PDF: https://raw.githubusercontent.com/mlresearch/v267/main/assets/sankagiri25a/sankagiri25a.pdf
- Local PDF: [../../pdfs/2026-10/2026-10-17-recommendations-with-sparse-comparison-data-provably-fast-convergence-for-nonconvex-matrix-factorization.pdf](../../pdfs/2026-10/2026-10-17-recommendations-with-sparse-comparison-data-provably-fast-convergence-for-nonconvex-matrix-factorization.pdf)
- Venue: ICML 2025

## English Summary

This paper develops a theoretical foundation for recommender systems that learn from pairwise item comparisons rather than numerical ratings. Comparisons can be obtained from implicit choices or explicit questions, avoid user-specific rating-scale bias, and may be cognitively easier to provide. The model gives every user and item a low-dimensional latent vector; their inner product defines utility, and a smooth discrete-choice link function maps the utility difference between two items to the probability that a user prefers one over the other. The resulting low-rank utility matrix is learned by maximum likelihood.

Optimizing directly over the full utility matrix admits convex analyses but is expensive at scale. The paper instead factorizes the matrix and studies the practical nonconvex objective over user and item features. It adds a balancing regularizer to remove scale ambiguity and projections that preserve incoherence and remove shift invariance. Under a sufficiently accurate warm start, projected gradient descent remains in a neighborhood where the empirical loss behaves like a strongly convex and smooth function, despite the global nonconvexity.

The main theorem states that, with high probability, the iterates converge exponentially to the ground-truth feature class when the number of comparisons is at least on the order of n r^2 log n, up to dependencies on incoherence, condition number, and the link function. This is a sparse regime because the number of observations grows almost linearly with the combined number of users and items rather than with all user-item pairs. The proof extends matrix-completion concentration techniques to samples containing one user and an item pair, using matrix Bernstein inequalities to show that empirical curvature stays close to its population counterpart.

Synthetic simulations use rank-3 Gaussian matrices at sizes 200 x 300 and 2,000 x 3,000. They confirm linear convergence once the sample count is large enough and suggest that the theoretically required warm start and projection steps may not be necessary in practice. Additional experiments varying rank 2-6 and 30,000-100,000 comparisons show error increasing with rank and decreasing with data; empirically, the required samples appear roughly linear in rank, leaving a gap from the O(n r^2) theory. The guarantees nevertheless rely on exact expected choice probabilities rather than noisy binary outcomes, uniformly sampled independent comparisons, low-rank incoherent factors, a known link function, and an unavailable warm start. Evaluation is entirely synthetic because no suitable public comparison dataset exists, so behavior under biased exposure, real implicit feedback, and production-scale noise remains unverified.

## 繁中摘要

這篇論文為「從成對項目比較而非數值評分學習」的推薦系統建立理論基礎。Comparison feedback 可來自 implicit choices 或明確詢問，能避免不同使用者對 rating scale 的偏差，也可能比抽象評分更容易回答。模型為每個 user 與 item 配置低維 latent vector，以 inner product 定義 utility，再由平滑 discrete-choice link function 將兩個 items 的 utility difference 映射成使用者偏好其中一個的機率；最後以 maximum likelihood 學習 low-rank utility matrix。

直接在完整 utility matrix 上最佳化雖可使用 convex analysis，卻難以擴展。論文改為 factorize matrix，分析實務上較有效率的 user/item feature nonconvex objective。方法加入 balancing regularizer 消除 scale ambiguity，並透過 projections 維持 incoherence、排除 shift invariance。在足夠接近真值的 warm start 下，projected gradient descent 會停留在局部鄰域；此時 empirical loss 即使整體非凸，仍具有類似 strong convexity 與 smoothness 的性質。

主要定理指出，若 comparisons 數量至少約為 n r^2 log n，外加 incoherence、condition number 與 link function 相關因子，則 iterates 會以高機率 exponential convergence 到等價的 ground-truth feature class。這仍屬 sparse regime，因為 observations 幾乎隨 users 和 items 的總數線性成長，而非隨全部 user-item pairs 成長。證明把 matrix completion 的 concentration 技巧延伸到「一個 user 加一對 items」的 samples，並以 matrix Bernstein inequalities 證明 empirical curvature 接近 population counterpart。

Synthetic simulations 使用 rank-3 Gaussian matrices，規模分別為 200 x 300 與 2,000 x 3,000；當 sample count 足夠時可觀察到 linear convergence，也顯示理論要求的 warm start 與 projection steps 在實務模擬中可能不是必要條件。另一組實驗把 rank 設為 2-6、comparisons 設為 30,000-100,000，結果顯示 error 隨 rank 增加、隨資料量下降；經驗上的 sample requirement 約與 rank 線性相關，仍與 O(n r^2) 理論存在差距。不過，保證依賴 exact expected choice probabilities，而非 noisy binary outcomes，也假設 comparisons 為 uniform independent sampling、factors 低秩且 incoherent、link function 已知，並需要目前無法建構的 warm start。由於沒有合適的公開 comparison dataset，所有評估均為 synthetic，因此 biased exposure、真實 implicit feedback 與 production-scale noise 下的行為仍未驗證。

## Notes

- Official code: https://github.com/indy-lab/matrix-factorization-comparisons
- The software repository contains notebooks reproducing Figures 1 and 2 rather than a production recommender implementation.
- The main result identifies latent factors only up to the model's rotational, scale, and shift symmetries.
- The authors explicitly leave noisy binary comparisons, random initialization guarantees, and tighter O(n r) sample complexity as future work.
