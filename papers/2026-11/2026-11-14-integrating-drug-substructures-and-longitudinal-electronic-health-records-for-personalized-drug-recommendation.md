---
date: 2026-11-14
title: "Integrating Drug Substructures and Longitudinal Electronic Health Records for Personalized Drug Recommendation"
authors: "Wenjie Du, Xuqiang Li, Jinke Feng, Shuai Zhang, Zhang Wen, Yang Wang"
venue: "NeurIPS 2025"
---

# Integrating Drug Substructures and Longitudinal Electronic Health Records for Personalized Drug Recommendation

- Paper page: https://proceedings.neurips.cc/paper_files/paper/2025/hash/5b0c0b2c2efdd736a53688ebfdc3bcdb-Abstract-Conference.html
- PDF: https://proceedings.neurips.cc/paper_files/paper/2025/file/5b0c0b2c2efdd736a53688ebfdc3bcdb-Paper-Conference.pdf
- Local PDF: [../../pdfs/2026-11/2026-11-14-integrating-drug-substructures-and-longitudinal-electronic-health-records-for-personalized-drug-recommendation.pdf](../../pdfs/2026-11/2026-11-14-integrating-drug-substructures-and-longitudinal-electronic-health-records-for-personalized-drug-recommendation.pdf)
- Venue: NeurIPS 2025

## English Summary

This paper proposes SubRec for personalized multi-label drug recommendation from longitudinal electronic health records (EHRs). Existing systems often model patient histories or drug molecular structures, but do not explicitly connect a patient's current condition to the particular molecular substructures that may drive efficacy and safety. SubRec jointly learns in patient and drug spaces: it represents the current and historical visits, identifies condition-relevant portions of candidate drug graphs, and reuses recurring patient-drug interaction patterns through a discrete latent codebook.

On the drug side, SubRec uses an enhanced conditional information bottleneck to compress each molecular graph into a patient-conditioned subgraph. The objective retains substructures that are predictive for the current clinical context while removing less relevant molecular information, avoiding fixed rule-based fragmentation that can break functional groups. On the patient side, a Transformer encodes longitudinal diagnoses, procedures, and medications. Adaptive vector quantization maps the continuous patient-drug representation to the nearest entry in a condition-aware codebook, yielding discrete prototypes that summarize recurring clinical prescribing patterns. The final multi-label predictor combines the patient representation, selected molecular substructures, and codebook memory, with an additional DDI loss for safety control.

Experiments use MIMIC-III and MIMIC-IV with 4:1:1 train, validation, and test splits and compare against nine baselines. On MIMIC-III, SubRec reaches Jaccard 0.5585, PRAUC 0.7927, F1 0.7016, and DDI rate 0.0623; the strongest baseline Jaccard and F1 are 0.5412 and 0.6844. On MIMIC-IV, it obtains Jaccard 0.4635, PRAUC 0.7023, and F1 0.6216. The improvements are reported with 95% t-test confidence. Ablations show that removing condition-aware substructure capture lowers MIMIC-III Jaccard to 0.5228, while replacing the learned codebook with noise lowers it to 0.5257. A codebook size of 32 provides a practical trade-off because larger codebooks add training time with little predictive gain.

SubRec is heavier than several baselines: on a shared V100 it uses about 1,762 MB, has 2.97 million parameters, and trains for 20.63 hours, although early stopping reduces this to 8.71 hours and a dedicated GPU to 7.23 hours. More importantly, these are retrospective benchmark results, not prospective evidence of prescribing safety or improved patient outcomes. The discrete codebook reflects the training distribution and may require retraining or extension for out-of-distribution patients. The framework also assumes molecular graphs are available for every candidate drug. DDI rate covers only one safety dimension and does not replace validation of dosage, contraindications, allergies, organ function, causal effects, or clinician review.

## 繁中摘要

這篇論文提出 SubRec，利用 longitudinal electronic health records（EHRs）進行 personalized multi-label drug recommendation。既有系統通常只建模 patient histories 或 drug molecular structures，較少明確連結病人的當前狀況與可能影響療效、安全性的特定 molecular substructures。SubRec 同時在 patient space 與 drug space 學習：表示當前及歷史 visits、找出與病況相關的 candidate-drug graph 區域，並透過 discrete latent codebook 重複利用常見的 patient-drug interaction patterns。

在 drug side，SubRec 使用 enhanced conditional information bottleneck，將 molecular graph 壓縮成依病人條件而定的 subgraph。目標是保留能預測當前 clinical context 的 substructures，移除較不相關的 molecular information，避免固定 rule-based fragmentation 破壞 functional groups。在 patient side，Transformer 編碼 longitudinal diagnoses、procedures 與 medications。Adaptive vector quantization 將 continuous patient-drug representation 映射到 condition-aware codebook 中最接近的 entry，形成可概括常見 clinical prescribing patterns 的 discrete prototypes。最終 multi-label predictor 結合 patient representation、selected molecular substructures 與 codebook memory，並加入 DDI loss 控制安全性。

實驗使用 MIMIC-III 與 MIMIC-IV，依 4:1:1 分割 train/validation/test，並與九個 baselines 比較。SubRec 在 MIMIC-III 的 Jaccard、PRAUC、F1、DDI rate 分別為 0.5585、0.7927、0.7016、0.0623；最強 baseline 的 Jaccard 與 F1 分別為 0.5412、0.6844。在 MIMIC-IV 上則取得 Jaccard 0.4635、PRAUC 0.7023、F1 0.6216；論文以 95% t-test confidence 報告改善。Ablation 顯示移除 condition-aware substructure capture 後，MIMIC-III Jaccard 降至 0.5228；以 noise 取代 learned codebook 後降至 0.5257。Codebook size 32 是較實用的取捨，因為更大的 codebook 會增加訓練時間，但預測增益很小。

SubRec 的成本高於多個 baselines：在 shared V100 上約使用 1,762 MB、包含 2.97 million parameters，訓練需 20.63 小時；early stopping 可降至 8.71 小時，dedicated GPU 則為 7.23 小時。更重要的是，這些只是 retrospective benchmark results，不能視為處方安全或改善 patient outcomes 的 prospective evidence。Discrete codebook 反映 training distribution，面對 out-of-distribution patients 時可能需要 retraining 或擴充；框架也假設所有 candidate drugs 都有 molecular graphs。DDI rate 只涵蓋一個安全面向，不能取代對劑量、禁忌症、過敏、器官功能、因果效應與 clinician review 的驗證。

## Notes

- The recommendation objective combines binary cross-entropy, multi-label margin loss, substructure compression, vector-quantization, and DDI penalties.
- Diagnosis similarity and recommended-drug similarity have a reported Pearson correlation of 0.53 on sampled MIMIC-III visits.
- SubRec remains comparatively strong for patients with few or no historical medication records.
- This is a research model evaluated on retrospective EHR data, not a clinically validated prescribing system.
