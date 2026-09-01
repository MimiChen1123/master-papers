---
date: 2026-08-31
title: "Reinforcement Learning-based Recommender Systems with Large Language Models for State Reward and Action Modeling"
authors: "Jie Wang, Alexandros Karatzoglou, Ioannis Arapakis, Joemon M. Jose"
venue: "SIGIR 2024"
---

# Reinforcement Learning-based Recommender Systems with Large Language Models for State Reward and Action Modeling

- Paper page: https://doi.org/10.1145/3626772.3657767
- PDF: https://eprints.gla.ac.uk/323432/1/323432.pdf
- Local PDF: [../../pdfs/2026-08/2026-08-31-reinforcement-learning-based-recommender-systems-with-large-language-models-for-state-reward-and-action-modeling.pdf](../../pdfs/2026-08/2026-08-31-reinforcement-learning-based-recommender-systems-with-large-language-models-for-state-reward-and-action-modeling.pdf)
- Venue: SIGIR 2024

## English Summary

This paper studies offline reinforcement-learning-based sequential recommendation, where models need useful user states and reward signals but cannot freely interact with real users during training. Standard RL recommenders often reuse hidden states from sequential models and rely on simple hand-designed rewards, such as fixed values for clicks or purchases. The authors argue that these signals are too weak to capture nuanced user preferences.

The proposed approach adapts a large language model as a Language Environment, or LE. The LE is fine-tuned with a small subset of user-item interaction data and item textual information, then used as both a state model and a reward model. As a state model, it produces richer user representations from interaction histories. As a reward model, it estimates action-specific rewards that better reflect user preference than uniform behavior labels.

The paper also proposes LE Augmentation, or LEA, where the LE generates additional positive actions to enrich limited offline data. These augmented signals are used to train both the supervised recommendation head and the RL policy. Experiments on two real-world datasets show that adding LE-derived states, rewards, and augmentation improves strong RL sequential recommendation frameworks such as SNQN and SA2C, while inference remains efficient because the deployed recommender is still the lean sequential model rather than the LLM.

## 繁中 Summary

這篇論文研究 offline reinforcement-learning-based sequential recommendation。在這個設定中，模型需要好的 user state 和 reward signal，但訓練時不能任意和真實使用者互動。傳統 RL recommender 常常直接重用 sequential model 的 hidden state，並使用簡單手工設計的 reward，例如 click 或 purchase 給固定分數。作者認為這些訊號不足以表達細緻的使用者偏好。

作者提出把大型語言模型改造成 Language Environment，簡稱 LE。LE 透過少量 user-item interaction data 和 item textual information 進行 fine-tuning，之後同時作為 state model 和 reward model。作為 state model 時，它能從互動歷史產生更豐富的 user representation；作為 reward model 時，它能估計和 action 相關的 reward，比固定行為標籤更能反映使用者偏好。

論文也提出 LE Augmentation，也就是讓 LE 產生額外的 positive actions 來補強有限的 offline data。這些 augmented signals 會同時用於 supervised recommendation head 和 RL policy 的訓練。在兩個真實資料集上的實驗顯示，加入 LE 產生的 state、reward 和 augmentation，可以提升 SNQN、SA2C 等強 RL sequential recommendation frameworks；而推論階段仍只使用較小的 sequential model，不需要部署 LLM，因此保留效率。

## Notes

- This paper is useful when applying RL to recommendation but reliable online feedback is unavailable.
- The LLM is not used as the final recommender; it is used as an offline environment to improve training signals.
- LEA is practical because it augments limited offline interaction data while keeping inference lightweight.
