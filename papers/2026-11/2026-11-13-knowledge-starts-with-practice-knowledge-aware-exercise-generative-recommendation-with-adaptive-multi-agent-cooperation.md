---
date: 2026-11-13
title: "Knowledge Starts with Practice: Knowledge-Aware Exercise Generative Recommendation with Adaptive Multi-Agent Cooperation"
authors: "Yangtao Zhou, Hua Chu, Yongxiang Chen, Ziwen Wang, Jiacheng Liu, Jianan Li, Yueying Feng, Xiangming Li, Zihan Han, Qingshan Li"
venue: "NeurIPS 2025"
---

# Knowledge Starts with Practice: Knowledge-Aware Exercise Generative Recommendation with Adaptive Multi-Agent Cooperation

- Paper page: https://proceedings.neurips.cc/paper_files/paper/2025/hash/85dbd2fb8b355e4231b51e454c08ec1c-Abstract-Conference.html
- PDF: https://proceedings.neurips.cc/paper_files/paper/2025/file/85dbd2fb8b355e4231b51e454c08ec1c-Paper-Conference.pdf
- Local PDF: [../../pdfs/2026-11/2026-11-13-knowledge-starts-with-practice-knowledge-aware-exercise-generative-recommendation-with-adaptive-multi-agent-cooperation.pdf](../../pdfs/2026-11/2026-11-13-knowledge-starts-with-practice-knowledge-aware-exercise-generative-recommendation-with-adaptive-multi-agent-cooperation.pdf)
- Code: https://github.com/dsz532/exeGen
- Venue: NeurIPS 2025

## English Summary

This paper introduces Knowledge-aware Exercise Generative Recommendation (KEGR), a task that combines diagnosis and recommendation in a closed loop. Instead of selecting an existing exercise from a fixed pool, a KEGR system first infers a student's evolving knowledge state from past answers and then generates a new exercise tailored to the diagnosed strengths and weaknesses. The proposed ExeGen framework uses LLM agents to connect these stages and produce an interpretable knowledge report together with personalized practice material.

ExeGen coordinates four specialized roles. A Recommendation Manager supervises the workflow; a Knowledge Perceiver diagnoses mastery; an Exercise Generator writes candidate questions; and a group of Quality Evaluation Experts assesses relevance, clarity, answer correctness, difficulty, engagement, and safety. Its human-simulated knowledge-perception mechanism uses a domain knowledge graph to construct demonstrations and a dual-matching strategy that combines precise and fuzzy retrieval for in-context reasoning. Its exercise generation-adversarial mechanism then iterates between generation and multi-dimensional expert feedback until the manager accepts the result.

Experiments use the computer-science portion of MOOCCubeX and compare ExeGen with GPT-4o zero-shot, in-context learning, chain-of-thought, and ICL+CoT baselines across single-choice, multiple-choice, and judgment exercises. Evaluation combines six GPT-scored dimensions with Error Hit Rate and Error Recall. ExeGen is best on every reported metric. For multiple-choice generation, it obtains Knowledge Relevance 4.82, Clarity 4.73, Answer Accuracy 4.79, Difficulty Appropriateness 4.80, Engagement and Fun 4.58, Safety and Ethics 4.69, Error Hit Rate 0.79, and Error Recall 0.82. Removing the Knowledge Perceiver causes the largest ablation drop, while removing quality experts, human-simulated perception, or adversarial refinement also substantially degrades performance.

The authors also deploy student- and teacher-facing web interfaces and conduct manual evaluation with 20 student volunteers and three computer-science teachers reviewing 20 cases. These assessments broadly agree with the GPT-based scores, but the sample is too small to establish learning gains or deployment safety. The knowledge graph is especially sparse in prerequisite relations: only 0.063725% of concept pairs have them. Long student histories can also destabilize LLM reasoning, and generation with GPT-4o costs about USD 0.1787 per student. The paper does not report a large-scale randomized or longitudinal learning study, so ExeGen's strong content-quality scores should not be interpreted as evidence that it improves educational outcomes over time.

## 繁中摘要

這篇論文提出 Knowledge-aware Exercise Generative Recommendation（KEGR），將診斷與推薦整合成 closed loop。KEGR 不只是從固定 exercise pool 中選題，而是先根據學生過去的作答推論持續變化的 knowledge state，再針對診斷出的強項與弱點生成新的習題。作者提出 ExeGen，以多個 LLM agents 串接這兩個階段，同時輸出可解釋的 knowledge report 與個人化練習內容。

ExeGen 協調四種專門角色：Recommendation Manager 負責全局流程；Knowledge Perceiver 診斷 mastery；Exercise Generator 產生候選題目；多個 Quality Evaluation Experts 則從 relevance、clarity、answer correctness、difficulty、engagement 與 safety 等面向評估。Human-simulated knowledge-perception mechanism 以 domain knowledge graph 建立 demonstrations，並透過結合 precise/fuzzy retrieval 的 dual-matching strategy 支援 in-context reasoning。Exercise generation-adversarial mechanism 再讓生成器與多面向 experts 反覆互動，直到 manager 接受最終結果。

實驗使用 MOOCCubeX 的 computer-science 資料，並在 single-choice、multiple-choice 與 judgment exercises 上，與 GPT-4o zero-shot、in-context learning、chain-of-thought、ICL+CoT 比較。評估結合六個 GPT-scored dimensions、Error Hit Rate 與 Error Recall，ExeGen 在所有 reported metrics 都是最佳。Multiple-choice generation 的 Knowledge Relevance、Clarity、Answer Accuracy、Difficulty Appropriateness、Engagement and Fun、Safety and Ethics 分別為 4.82、4.73、4.79、4.80、4.58、4.69，Error Hit Rate/Recall 為 0.79/0.82。Ablation 中移除 Knowledge Perceiver 的退步最大；移除 quality experts、human-simulated perception 或 adversarial refinement 也會明顯降低表現。

作者另部署 student/teacher web interfaces，並邀請 20 位學生志願者及三位 computer-science teachers 評估 20 個案例。人工評估大致與 GPT-based scores 一致，但樣本太小，無法證明真實 learning gain 或 deployment safety。Knowledge graph 的 prerequisite relations 特別稀疏，只有 0.063725% concept pairs 具有此標註；較長的 student history 也可能讓 LLM reasoning 不穩定。使用 GPT-4o 為每位學生生成推薦的平均成本約為 0.1787 美元。論文未進行大規模 randomized 或 longitudinal learning study，因此優秀的內容品質分數不能直接解讀為 ExeGen 能長期提升教育成效。

## Notes

- MOOCCubeX preprocessing retains 18,638 students, 5,015 exercises, 27,918 knowledge concepts, and 6,153 student-exercise relations.
- The main implementation uses GPT-4o through the OpenAI API without model fine-tuning and runs on two RTX 4090 GPUs.
- The interfaces allow optional agent deactivation, post-generation editing, and TXT/PDF/JSON export.
- The released code is available at https://github.com/dsz532/exeGen.
