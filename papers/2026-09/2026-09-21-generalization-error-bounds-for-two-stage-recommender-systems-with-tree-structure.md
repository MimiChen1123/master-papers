---
date: 2026-09-21
title: "Generalization Error Bounds for Two-stage Recommender Systems with Tree Structure"
authors: "Jin Zhang, Ze Liu, Defu Lian, Enhong Chen"
venue: "NeurIPS 2024"
---

# Generalization Error Bounds for Two-stage Recommender Systems with Tree Structure

- Paper page: https://proceedings.neurips.cc/paper_files/paper/2024/hash/4140fe26102db5fea1f40118afc7137b-Abstract-Conference.html
- PDF: https://proceedings.neurips.cc/paper_files/paper/2024/file/4140fe26102db5fea1f40118afc7137b-Paper-Conference.pdf
- Local PDF: [../../pdfs/2026-09/2026-09-21-generalization-error-bounds-for-two-stage-recommender-systems-with-tree-structure.pdf](../../pdfs/2026-09/2026-09-21-generalization-error-bounds-for-two-stage-recommender-systems-with-tree-structure.pdf)
- Venue: NeurIPS 2024

## English Summary

This paper develops generalization-error bounds for a common large-scale recommendation architecture: a fast tree-structured retriever first reduces the item catalog to a candidate set, then a more expressive ranker chooses from those candidates. The authors begin with an exact error decomposition. Overall error equals the probability that retrieval misses the target item plus the ranker's conditional error when the target was retrieved, weighted by retrieval success. This separates the two ways the pipeline can fail and makes clear that a ranker cannot recover an item omitted by the first stage.

For tree retrievers using beam search, the paper bounds retrieval error through Rademacher complexity. The analysis covers linear, multilayer perceptron, and target-attention scoring functions. The bounds exhibit the usual inverse-square-root dependence on sample size and also expose effects from model complexity, tree depth, beam search, and branching factor. In particular, the tree-dependent term improves as the number of children per node grows, predicting that flatter, more highly branched trees generalize better. This is not free: in the limit, a tree with one branch per item degenerates into scoring the entire catalog, so branching represents an accuracy-versus-computation tradeoff.

The ranker analysis introduces an additional term measuring the mismatch between its training distribution and the inference distribution induced by the retriever. Training the ranker only on examples whose targets are successfully retrieved reduces this distribution-shift term, but also reduces the available sample size. Experiments with an improved TDM retriever on MIND and MovieLens-10M support both conclusions: Recall@20 rises as branches increase from 2 to 32, and a DIN ranker trained on the harmonized subset consistently improves top-1 accuracy over ordinary two-stage training for candidate sizes 40, 80, and 120. The gains are modest and depend on sufficient retriever recall; the authors report that recall above roughly 10% is generally needed so that distribution alignment does not lose too much training data.

## 繁中摘要

這篇論文為常見的大規模推薦架構建立泛化誤差上界：第一階段由快速的樹狀 retriever 從完整物品庫取出候選集合，第二階段再由能力較強但成本較高的 ranker 從候選中選出結果。作者先提出精確的誤差分解：整體錯誤等於 retriever 漏掉目標物品的機率，加上目標已被取回時 ranker 的條件錯誤率，再乘以取回成功率。這個分解把兩階段失敗來源分開，也直接說明第二階段無法補救第一階段未取回的物品。

對使用 beam search 的樹狀 retriever，論文利用 Rademacher complexity 建立取回誤差上界，涵蓋線性模型、MLP 與 target-attention 三種節點評分函數。上界除了具有常見的樣本數平方根反比關係，也顯示模型複雜度、樹深、beam search 與分支數的影響。特別是，隨著每個節點的子節點數增加，與樹結構相關的界限會改善，因此較扁平、分支較多的樹通常有較好的泛化能力。但這並非沒有成本：若根節點直接連到所有物品，樹模型便退化成掃描完整物品庫，因此分支數本質上是在準確度與計算效率之間取捨。

ranker 的分析則加入一個衡量訓練分布與 retriever 所誘導之推論分布差異的額外項。若只使用「目標物品確實被 retriever 取回」的訓練樣本來訓練 ranker，可以降低這個分布偏移；但同時也會減少可用樣本數。作者以改良 TDM retriever 在 MIND 與 MovieLens-10M 上驗證兩項結論：當分支數從 2 增加到 32 時，Recall@20 持續上升；以對齊後子集合訓練的 DIN ranker，在候選數 40、80、120 下，top-1 accuracy 都優於一般兩階段訓練。改善幅度不大，而且依賴 retriever 有足夠 recall；作者觀察到通常需要約 10% 以上 recall，分布對齊的收益才不會被樣本量損失抵銷。

## Notes

- MIND contains 36,281 users, 7,129 items, and 5,610,960 interactions; MovieLens-10M contains 69,878 users, 10,677 items, and 10,000,054 interactions after preprocessing.
- The branch-number experiment uses beam size 100 and reports the best Recall@20 after hyperparameter search.
- Harmonized training improves top-1 accuracy on MIND from 0.6500 to 0.6565 at K=40 and on Movie from 0.3516 to 0.3555; improvements remain consistent as K increases.
