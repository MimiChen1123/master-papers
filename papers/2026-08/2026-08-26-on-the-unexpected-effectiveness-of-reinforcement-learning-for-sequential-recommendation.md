---
date: 2026-08-26
title: "On the Unexpected Effectiveness of Reinforcement Learning for Sequential Recommendation"
authors: "Alvaro Labarca Silva, Denis Parra, Rodrigo Toro Icarte"
venue: "ICML 2024"
---

# On the Unexpected Effectiveness of Reinforcement Learning for Sequential Recommendation

- Paper page: https://proceedings.mlr.press/v235/silva24b.html
- PDF: https://raw.githubusercontent.com/mlresearch/v235/main/assets/silva24b/silva24b.pdf
- Local PDF: [../../pdfs/2026-08/2026-08-26-on-the-unexpected-effectiveness-of-reinforcement-learning-for-sequential-recommendation.pdf](../../pdfs/2026-08/2026-08-26-on-the-unexpected-effectiveness-of-reinforcement-learning-for-sequential-recommendation.pdf)
- Venue: ICML 2024

## English Summary

This paper investigates a counterintuitive result in sequential recommendation: reinforcement learning methods often improve next-item prediction metrics, even though RL optimizes long-term return while next-item prediction evaluates only short-term ranking accuracy. The authors first formalize this mismatch and show that an optimal RL policy can be arbitrarily worse than a self-supervised model under next-item prediction metrics, so there is no theoretical reason to expect RL itself to improve this offline evaluation protocol.

The paper then studies Self-Supervised Q-learning (SQN), where RL is used as an auxiliary loss on top of a sequential self-supervised recommender. The key finding is that the performance gain does not seem to come from learning a better long-term policy. Instead, the auxiliary RL objective appears to encourage the hidden representation to encode information about the user's previous interactions, especially sequence-history information such as how many items have already been interacted with.

To test this explanation, the authors replace the RL objective with simpler auxiliary prediction losses, including a loss that predicts the number of past interactions. These non-RL auxiliary objectives achieve performance gains comparable to the RL auxiliary loss on session-based recommendation benchmarks such as RetailRocket and RC15. The result suggests that some reported RL gains in sequential recommendation may come from useful representation regularization rather than from reinforcement learning's long-term decision-making objective.

## 繁中 Summary

這篇論文探討 sequential recommendation 裡一個反直覺現象：許多 reinforcement learning 方法在 next-item prediction 指標上表現很好，但 RL 的目標是最佳化長期 reward，而 next-item prediction 評估的是短期排序準確率。作者先形式化這個目標不一致問題，並證明在 next-item prediction 指標下，最佳 RL policy 甚至可能任意地比 self-supervised model 更差，因此理論上不應該直接期待 RL 本身會提升這種離線評估。

接著論文分析 Self-Supervised Q-learning (SQN)，也就是把 RL 作為 sequential self-supervised recommender 的 auxiliary loss。核心發現是，效能提升似乎不是來自學到更好的長期 policy，而是 RL auxiliary objective 促使模型 hidden representation 編碼使用者過去互動的資訊，尤其是和 session history 有關的訊號，例如使用者已經互動過多少 items。

為了驗證這個解釋，作者把 RL objective 換成更簡單的 auxiliary prediction loss，包括預測 past interactions 數量的 loss。這些非 RL 的 auxiliary objectives 在 RetailRocket 和 RC15 等 session-based recommendation benchmark 上，達到和 RL auxiliary loss 相近的提升。這代表某些 sequential recommendation 中觀察到的 RL 效果，可能主要來自有用的 representation regularization，而不是 RL 對長期決策目標的最佳化。

## Notes

- This is a useful paper for interpreting RL results in recommender systems, especially when evaluation is based on next-item prediction.
- The paper distinguishes long-term policy learning from auxiliary representation learning.
- A practical takeaway is that simple auxiliary losses may reproduce part of the gain attributed to RL, with less conceptual and implementation complexity.
