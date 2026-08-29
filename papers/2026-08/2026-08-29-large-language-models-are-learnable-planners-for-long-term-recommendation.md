---
date: 2026-08-29
title: "Large Language Models are Learnable Planners for Long-Term Recommendation"
authors: "Wentao Shi, Xiangnan He, Yang Zhang, Chongming Gao, Xinyue Li, Jizhi Zhang, Qifan Wang, Fuli Feng"
venue: "SIGIR 2024"
---

# Large Language Models are Learnable Planners for Long-Term Recommendation

- Paper page: https://doi.org/10.1145/3626772.3657683
- PDF: https://arxiv.org/pdf/2403.00843
- Local PDF: [../../pdfs/2026-08/2026-08-29-large-language-models-are-learnable-planners-for-long-term-recommendation.pdf](../../pdfs/2026-08/2026-08-29-large-language-models-are-learnable-planners-for-long-term-recommendation.pdf)
- Venue: SIGIR 2024

## English Summary

This paper explores how large language models can be used as planners for long-term recommendation. The motivation is that many recommender systems optimize immediate responses such as clicks, while long-term recommendation needs policies that consider future engagement and avoid effects such as repetitive recommendations or filter bubbles. Existing reinforcement-learning methods can model long-term reward, but sparse recommendation data makes RL difficult to train and prone to instability.

The authors propose Bi-level Learnable LLM Planning, or BiLLP. The framework uses multiple LLM roles. At the macro level, a Planner generates high-level recommendation plans and a Reflector extracts lessons from completed trajectories. At the micro level, an Actor turns the plan into personalized item actions, while a Critic evaluates actions with respect to long-term goals. This separates high-level planning principles from user-specific action selection.

Experiments use simulated interactive environments built from Steam and Amazon-Book recommendation logs. BiLLP is compared with RL-based methods such as SQN, DQN, A2C, CQL, BCQ, CRR, and DORL, as well as LLM-based baselines such as ActOnly, ReAct, and Reflexion. Results show that BiLLP achieves the strongest long-term metrics, especially trajectory length and cumulative reward, suggesting that explicit planning, reflection, and personalization can make LLMs useful for long-term recommendation.

## 繁中 Summary

這篇論文探討如何把大型語言模型用作 long-term recommendation 的 planner。動機是許多推薦系統主要最佳化即時反應，例如 click，但長期推薦需要考慮未來 engagement，並避免重複推薦、filter bubble 等問題。既有 reinforcement learning 方法可以建模 long-term reward，但推薦資料通常稀疏，使 RL 訓練不穩定，也容易 overfit。

作者提出 Bi-level Learnable LLM Planning，簡稱 BiLLP。這個框架使用多個 LLM 角色：在 macro level，Planner 產生高層次推薦計畫，Reflector 從完成的互動 trajectory 中整理經驗；在 micro level，Actor 把計畫轉成個人化 item actions，Critic 則評估 action 對長期目標的價值。這樣把高層次 planning principles 和使用者層級的 action selection 分開處理。

實驗使用 Steam 和 Amazon-Book logs 建立 simulated interactive environments。BiLLP 和 SQN、DQN、A2C、CQL、BCQ、CRR、DORL 等 RL methods，以及 ActOnly、ReAct、Reflexion 等 LLM baselines 比較。結果顯示 BiLLP 在 long-term metrics 上表現最好，尤其是 trajectory length 和 cumulative reward，說明明確的 planning、reflection 與 personalization 能讓 LLM 更適合長期推薦任務。

## Notes

- This paper is useful if you are interested in LLM-based recommendation beyond one-shot ranking.
- The key design is role separation: Planner and Reflector learn high-level strategy, while Actor and Critic handle personalized execution.
- The evaluation is based on simulated environments, so online validation would still be important before production use.
