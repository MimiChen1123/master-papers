---
date: 2026-09-22
title: "Gaussian Process Bandits for Top-k Recommendations"
authors: "Mohit Yadav, Daniel Sheldon, Cameron Musco"
venue: "NeurIPS 2024"
---

# Gaussian Process Bandits for Top-k Recommendations

- Paper page: https://proceedings.neurips.cc/paper_files/paper/2024/hash/8874a21bfb43738f5af2eb348f2bc693-Abstract-Conference.html
- PDF: https://proceedings.neurips.cc/paper_files/paper/2024/file/8874a21bfb43738f5af2eb348f2bc693-Paper-Conference.pdf
- Local PDF: [../../pdfs/2026-09/2026-09-22-gaussian-process-bandits-for-top-k-recommendations.pdf](../../pdfs/2026-09/2026-09-22-gaussian-process-bandits-for-top-k-recommendations.pdf)
- Venue: NeurIPS 2024

## English Summary

This paper addresses online top-k recommendation under full-bandit feedback: at each round the system chooses an ordered list of k distinct items but observes only one scalar reward for the entire list. This is more general than semi-bandit or cascade models, which expose item-level outcomes or assume a fixed browsing process, and it can represent list-level objectives such as relevance-diversity tradeoffs. The difficulty is combinatorial: the number of possible ordered lists grows on the order of n^k.

The proposed GP-TopK algorithm models rewards with a Gaussian process over a product of user-context similarity and ranking similarity, then selects lists using an upper-confidence-bound acquisition function. Ranking similarity is represented with Kendall kernels. The paper introduces a weighted convolutional Kendall (WCK) kernel that combines position-sensitive weights with information about items outside the intersection of two top-k lists. This fixes undesirable behavior in earlier weighted and convolutional variants, such as treating reversed rankings at different positions as equally similar. GP-TopK therefore shares observations across structurally related rankings instead of learning each combinatorial arm independently.

To make Gaussian-process inference practical, the authors derive sparse feature representations and fast kernel matrix-vector products. The WCK kernel can be evaluated in O(k^2), and, under a fixed number of iterative-solver steps, total GP-TopK computation over T rounds is reduced from a naive O(T^4) to O(k^2 c l T^2), where c is context dimension and l is the number of local-search evaluations. The regret analysis gives high-probability sublinear growth in T and replaces the naive exponential dependence on the number of rankings with a near-quadratic dependence on the item count under the stated GP or RKHS assumptions.

Experiments use a simulator built from MovieLens-1M collaborative-filtering embeddings. In small action spaces (20 items, top-3), GP-TopK variants outperform random, epsilon-greedy, and independent-arm UCB across contextual and non-contextual rewards based on nDCG and nDCG plus diversity; WCK performs best. In large spaces with 50 items and top-3 or top-5 lists, covering more than 10^5 and 10^10 possible rankings, WCK retains the lowest regret using local search. The evidence is simulation-based, and the theoretical regret bound does not include errors introduced by approximate local-search arm selection, which are important limitations for real deployment.

## 繁中摘要

這篇論文研究 full-bandit feedback 下的線上 top-k 推薦：系統每輪選出一份由 k 個不同物品組成的有序清單，但只能觀察整份清單的一個純量回饋。這比 semi-bandit 或 cascade 模型更一般，因為不需要取得每個物品的個別結果，也不假設使用者依固定順序瀏覽；因此可直接表示相關性與多樣性等清單層級目標。主要困難是組合爆炸，有序清單數量約以 n^k 成長。

作者提出 GP-TopK，以 Gaussian process 建模使用者 context 與排名清單的聯合 reward，再以 upper confidence bound 在探索與利用之間取捨。清單相似度由 Kendall kernel 表示。論文進一步提出 weighted convolutional Kendall（WCK）kernel，同時保留位置敏感權重，以及不在兩份 top-k 交集內物品的資訊，修正既有 weighted 與 convolutional 版本的不合理行為，例如無法區分發生在不同排名位置的反轉。如此一來，GP-TopK 可以在結構相近的排名間共享觀測，而不必把每份組合清單視為完全獨立的 arm。

為降低 Gaussian process 推論成本，作者推導稀疏特徵表示與快速 kernel matrix-vector product。WCK kernel 可在 O(k^2) 時間計算；若迭代解法步數固定，T 輪 GP-TopK 的總運算量可由直接方法的 O(T^4) 降至 O(k^2 c l T^2)，其中 c 是 context 維度，l 是 local search 的評估次數。理論分析在指定的 GP 或 RKHS 假設下給出對 T 次線性的高機率 regret bound，並把對排名組合數的直接指數依賴，改善為接近物品數平方的依賴。

實驗使用 MovieLens-1M 協同過濾 embedding 建立模擬器。在小型 action space（20 個物品、top-3）中，GP-TopK 各版本在 contextual 與 non-contextual、nDCG 及 nDCG 加多樣性等設定下，都優於 random、epsilon-greedy 與把每個 arm 獨立處理的 UCB，其中 WCK 最佳。在 50 個物品、top-3 或 top-5 的大型空間中，可能排名超過 10^5 與 10^10，WCK 搭配 local search 仍維持最低 regret。不過，這些證據來自模擬而非真實線上部署，而且理論 regret bound 沒有納入 local search 近似選 arm 所造成的誤差，這是實際應用時的重要限制。

## Notes

- MovieLens-1M contains one million ratings from 6,040 users for 3,677 items; the simulator uses five-dimensional user and item embeddings.
- The contextual kernel multiplies a dot-product context kernel by a Kendall ranking kernel, allowing feedback sharing across both similar users and similar lists.
- The paper also warns that optimizing engagement-oriented rewards may reinforce biases in historical data, so deployment requires monitoring beyond regret alone.
