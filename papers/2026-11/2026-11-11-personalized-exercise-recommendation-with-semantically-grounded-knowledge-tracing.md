---
date: 2026-11-11
title: "Personalized Exercise Recommendation with Semantically-Grounded Knowledge Tracing"
authors: "Yilmazcan Ozyurt, Tunaberk Almaci, Stefan Feuerriegel, Mrinmaya Sachan"
venue: "NeurIPS 2025"
---

# Personalized Exercise Recommendation with Semantically-Grounded Knowledge Tracing

- Paper page: https://proceedings.neurips.cc/paper_files/paper/2025/hash/13707aad517ddd6c09ea02e0f55e1e7a-Abstract-Conference.html
- PDF: https://proceedings.neurips.cc/paper_files/paper/2025/file/13707aad517ddd6c09ea02e0f55e1e7a-Paper-Conference.pdf
- Local PDF: [../../pdfs/2026-11/2026-11-11-personalized-exercise-recommendation-with-semantically-grounded-knowledge-tracing.pdf](../../pdfs/2026-11/2026-11-11-personalized-exercise-recommendation-with-semantically-grounded-knowledge-tracing.pdf)
- Code: https://github.com/oezyurty/ExRec
- Venue: NeurIPS 2025

## English Summary

This paper introduces ExRec, an end-to-end framework for personalized exercise recommendation in online education. Existing reinforcement-learning recommenders often represent questions only by IDs, carry the full interaction history as the student state, and repeatedly score the entire question set to compute rewards. ExRec instead grounds recommendations in the semantic content of exercises and in the structured evolution of student knowledge. Its goal is not merely to predict whether a student will answer correctly, but to select a sequence of exercises that improves targeted knowledge concepts (KCs).

The pipeline has four modules. First, GPT-4o generates solution steps, annotates their KCs according to mathematics curriculum standards, and maps each step to the concepts it uses. Second, a BERT encoder is contrastively trained to align question and solution-step embeddings with their KCs while clustering semantically equivalent concepts to avoid false negatives. Third, a recurrent knowledge-tracing model compresses the exercise history into a fixed student state and is calibrated to predict KC-level mastery directly. Fourth, this calibrated model becomes the environment for multiple continuous- and discrete-action RL algorithms. The authors additionally propose model-based value estimation (MVE), which initializes the critic from the knowledge-tracing transition and prediction components so Q-learning estimates expected knowledge gains from the modeled student dynamics rather than learning entirely from trial and error.

The main evaluation uses XES3G5M, containing 7,652 math questions and 5.5 million interactions from 18,066 students. Policies are evaluated over ten recommended exercises for 2,048 held-out students on four goals: global knowledge improvement, improvement in a recently practiced KC, preparation for an upcoming KC, and improvement in the student's currently weakest KC. Across these tasks, random and historical-data policies yield marginal or negative gains, value-based continuous methods generally outperform policy-gradient counterparts, and MVE consistently improves DDPG, SAC, and TD3. The benefit is most pronounced for the adaptive weakest-KC task, where the target changes during the episode. The framework also supports unseen questions generated to triple the corpus size; MVE variants remain robust while several default policies deteriorate.

An additional experiment on Eedi covers 2,324,162 interactions from 47,560 students and 4,019 questions. For global knowledge improvement, MVE raises SAC from 8.97% to 20.08%, TD3 from 9.62% to 16.85%, and DDPG from 16.65% to 18.87% of the maximum possible improvement; Rainbow reaches 37.00%. These results support the framework's portability, but they are generated inside a learned knowledge-tracing simulator rather than through a prospective classroom or platform study. Therefore, recommendation quality is bounded by simulator accuracy and may amplify its errors. The current representation also omits question difficulty and misconception-specific signals, and both datasets provide only binary correctness rather than the exact wrong answer. LLM-based annotation adds cost and potential labeling bias, while real deployment would require teacher oversight, learner-safety checks, and direct measurement of learning outcomes.

## 繁中摘要

這篇論文提出 ExRec，一個用於線上教育 personalized exercise recommendation 的 end-to-end framework。既有 reinforcement-learning recommenders 常只用 ID 表示題目、把完整 interaction history 當成 student state，並反覆評分整個 question set 來計算 reward。ExRec 改為讓推薦建立在題目語義與學生知識的結構化演進上；目標不只是預測學生能否答對，而是選出能改善特定 knowledge concepts（KCs）的習題序列。

流程包含四個模組。第一，GPT-4o 生成解題步驟、依數學課程標準標註 KCs，並把每個步驟對應到實際使用的 concepts。第二，以 contrastive learning 訓練 BERT encoder，讓 question/solution-step embeddings 與相關 KCs 對齊，並先聚類語義等價 concepts 以減少 false negatives。第三，recurrent knowledge-tracing model 將 exercise history 壓縮成固定長度的 student state，再校準成可直接預測 KC-level mastery。第四，這個 calibrated model 成為多種 continuous- 與 discrete-action RL algorithms 的 environment。作者另提出 model-based value estimation（MVE），以 knowledge-tracing transition 與 prediction components 初始化 critic，使 Q-learning 能直接依據模擬的 student dynamics 估計預期 knowledge gain，而不必完全從 trial and error 開始學習。

主要實驗使用 XES3G5M，包含 7,652 道數學題、18,066 位學生與 550 萬筆 interactions。系統針對 2,048 位 held-out students，各推薦十道題，評估四種目標：整體 knowledge improvement、最近練習 KC 的改善、下一個 KC 的預備學習，以及目前 weakest KC 的改善。Random 與 historical-data policies 只帶來極小甚至負向增益；value-based continuous methods 通常優於 policy-gradient methods，而 MVE 在四個任務中都能改善 DDPG、SAC、TD3。它在 weakest-KC 任務尤其有效，因為 target 會隨 episode 動態改變。作者也將 question corpus 擴充為三倍來測試 unseen questions；多個 default policies 表現下降，但 MVE variants 仍保持穩健。

額外的 Eedi 實驗涵蓋 47,560 位學生、4,019 道題與 2,324,162 筆 interactions。在 global knowledge improvement 上，MVE 將 SAC 從最大可能增益的 8.97% 提升到 20.08%，TD3 從 9.62% 提升到 16.85%，DDPG 從 16.65% 提升到 18.87%；Rainbow 達到 37.00%。這些結果支持框架的可移植性，但成效來自 learned knowledge-tracing simulator，並非前瞻性的課堂或平台實驗，因此推薦品質受 simulator accuracy 限制，也可能放大其錯誤。現有表示尚未納入 question difficulty 與 misconception-specific signals，兩個資料集也只有 binary correctness，沒有學生實際選擇的錯誤答案。LLM-based annotation 另有成本與 labeling bias；真正部署時仍需教師監督、learner-safety checks 與直接的學習成果評估。

## Notes

- The paper releases code and trained models at https://github.com/oezyurty/ExRec.
- GPT-4o is queried three times per XES3G5M question; the paper reports an annotation cost of approximately USD 50 for 7,652 questions.
- The representation encoder is trained on one NVIDIA A100 for under six hours; knowledge tracing uses one RTX 3090 for about 2.5 hours.
- Question embeddings for newly added exercises do not require rerunning KC annotation at inference time.
