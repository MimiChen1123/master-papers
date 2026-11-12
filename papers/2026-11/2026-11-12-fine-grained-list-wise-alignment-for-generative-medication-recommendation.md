---
date: 2026-11-12
title: "Fine-grained List-wise Alignment for Generative Medication Recommendation"
authors: "Chenxiao Fan, Chongming Gao, Wentao Shi, Yaxin Gong, Zihao Zhao, Fuli Feng"
venue: "NeurIPS 2025"
---

# Fine-grained List-wise Alignment for Generative Medication Recommendation

- Paper page: https://proceedings.neurips.cc/paper_files/paper/2025/hash/44a1f7e0a1fe7867f586b10739a0c26a-Abstract-Conference.html
- PDF: https://proceedings.neurips.cc/paper_files/paper/2025/file/44a1f7e0a1fe7867f586b10739a0c26a-Paper-Conference.pdf
- Local PDF: [../../pdfs/2026-11/2026-11-12-fine-grained-list-wise-alignment-for-generative-medication-recommendation.pdf](../../pdfs/2026-11/2026-11-12-fine-grained-list-wise-alignment-for-generative-medication-recommendation.pdf)
- Code: https://github.com/cxfann/Flame
- Venue: NeurIPS 2025

## English Summary

This paper argues that medication recommendation should be treated as a list-wise decision problem rather than independent point-wise drug classification. A prescription must account for the combined therapeutic value of multiple drugs, redundancies, and adverse drug-drug interactions (DDIs), while point-wise models score each medication separately and assemble the final set afterward. The proposed FLAME framework instead generates and refines a medication list drug by drug, allowing every add or remove action to depend on the current prescription state.

FLAME first trains a drug-level classifier, then uses its output to initialize a list-wise policy that performs a small sequence of edits. The main optimization contribution is step-wise Group Relative Policy Optimization (GRPO). Standard GRPO assigns one outcome reward to every token in a generated list, whereas FLAME defines a potential function over intermediate medication sets and uses potential-based reward shaping to estimate the incremental value of each drug-level action. The shaped rewards preserve the optimal policy under the paper's assumptions while providing denser credit assignment. A configurable safety penalty explicitly trades recommendation accuracy against DDI rate.

Patient representation combines natural-language clinical context with structured and collaborative signals. FLAME uses the medical Llama3.1-Aloe-Beta-8B backbone and fuses textual embeddings with projected representations from RAREMed for patients, MICRON for diagnoses and procedures, and Mole-BERT for medication molecular structure. Evaluation trains on MIMIC-III and tests correctness, safety control, temporal transfer to MIMIC-IV, and external transfer to eICU. On MIMIC-III, FLAME obtains Jaccard 0.4836 and F1 0.6408, compared with 0.4701 and 0.6294 for the strongest reported baseline, LAMO. The list-wise policy makes only about 2.03 edits per patient on average, but removing it reduces Jaccard to 0.4785. Step-wise GRPO raises the list-wise refinement gain over the point-wise classifier by 82.1% relative to standard GRPO and shows faster, more stable reward convergence.

These are retrospective offline results and must not be interpreted as evidence that FLAME can safely prescribe medication. The model is trained and evaluated on static EHR datasets, not in prospective clinical workflows, and the authors identify deployment cost, incomplete automated multimodal processing, and manual GPT-4o API preprocessing as limitations. The NeurIPS checklist also states that no statistical significance tests were run because of compute and time constraints. DDI rate is only one dimension of medication safety; dosage, contraindications, allergies, organ function, causality, and clinician judgment require separate validation. The authors therefore position physician-in-the-loop evaluation as future work rather than claiming autonomous clinical readiness.

## 繁中摘要

這篇論文主張 medication recommendation 應被建模成 list-wise decision problem，而不是彼此獨立的 point-wise drug classification。處方需要同時考慮多種藥物的整體療效、重複用藥與 adverse drug-drug interactions（DDIs）；point-wise model 卻會分別評分每個藥物，再於事後組合成集合。作者提出的 FLAME 改為逐一生成與修正 medication list，使每一次新增或移除藥物的決策都能依賴目前的完整處方狀態。

FLAME 先訓練 drug-level classifier，再以其輸出初始化 list-wise policy，進行少量 add/remove edits。核心最佳化方法是 step-wise Group Relative Policy Optimization（GRPO）。標準 GRPO 會將單一 outcome reward 指派給清單中的所有 tokens；FLAME 則對中間 medication sets 定義 potential function，透過 potential-based reward shaping 衡量每個 drug-level action 的增量價值。在論文假設下，這種 shaped reward 不改變 optimal policy，但能提供更密集的 credit assignment。系統也加入可調整的 safety penalty，在推薦正確性與 DDI rate 之間進行顯式取捨。

Patient representation 結合 natural-language clinical context、structured signals 與 collaborative signals。FLAME 使用醫療領域的 Llama3.1-Aloe-Beta-8B，並融合 RAREMed 的 patient representations、MICRON 的 diagnosis/procedure embeddings，以及 Mole-BERT 的 medication molecular representations。實驗在 MIMIC-III 訓練並評估 correctness 與 safety control，也測試轉移到較新時期的 MIMIC-IV，以及跨機構的 eICU。FLAME 在 MIMIC-III 的 Jaccard/F1 為 0.4836/0.6408，優於最強 reported baseline LAMO 的 0.4701/0.6294。List-wise policy 平均每位病人只做約 2.03 次修改，但移除後 Jaccard 降至 0.4785；相較 standard GRPO，step-wise GRPO 讓 list-wise refinement 相對 point-wise classifier 的增益提高 82.1%，且 reward convergence 更快、更穩定。

這些是 retrospective offline results，不能解讀為 FLAME 已能安全開立處方。模型只在 static EHR datasets 上訓練與評估，未進入 prospective clinical workflow；作者也將部署成本、不完整的 automated multimodal processing，以及需手動呼叫 GPT-4o API 的 preprocessing 列為限制。NeurIPS checklist 明確表示受計算與時間限制，實驗未做 statistical significance tests。DDI rate 也只是 medication safety 的一個面向；劑量、禁忌症、過敏、器官功能、因果關係與 clinician judgment 都需要獨立驗證。因此作者將 physician-in-the-loop evaluation 列為後續工作，而非宣稱系統已具 autonomous clinical readiness。

## Notes

- MIMIC-III contains 14,207 visits from 6,226 patients after preprocessing; the medication vocabulary has 151 drugs.
- FLAME uses bf16 quantization, LoRA, and NVIDIA A100-SXM4-80GB GPUs for training.
- The point-wise classifier's DDI rate is 0.1336, close to the MIMIC-III ground-truth rate of 0.1369; the list-wise policy enables explicit adjustment through its safety penalty.
- This is a research result for clinical decision support and not a validated prescribing system.
