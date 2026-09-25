---
date: 2026-09-25
title: "Think before Recommendation: Autonomous Reasoning-enhanced Recommender"
authors: "Xiaoyu Kong, Junguang Jiang, Bin Liu, Ziru Xu, Han Zhu, Jian Xu, Bo Zheng, Jiancan Wu, Xiang Wang"
venue: "NeurIPS 2025"
---

# Think before Recommendation: Autonomous Reasoning-enhanced Recommender

- Paper page: https://proceedings.neurips.cc/paper_files/paper/2025/hash/cea5bc68b890bffb10f18aaaab2becb1-Abstract-Conference.html
- PDF: https://proceedings.neurips.cc/paper_files/paper/2025/file/cea5bc68b890bffb10f18aaaab2becb1-Paper-Conference.pdf
- Local PDF: [../../pdfs/2026-09/2026-09-25-think-before-recommendation-autonomous-reasoning-enhanced-recommender.pdf](../../pdfs/2026-09/2026-09-25-think-before-recommendation-autonomous-reasoning-enhanced-recommender.pdf)
- Venue: NeurIPS 2025

## English Summary

This paper replaces the common teacher-distillation pipeline for reasoning-enhanced rating prediction with reinforcement learning. Prior systems ask a large teacher LLM to generate preference analyses and reasoning traces, then train smaller modules or students to imitate them. The authors argue that this is expensive, freezes potentially weak teacher reasoning into static supervision, and separates intermediate reasoning from the final recommendation objective. Their RecZero method instead trains one LLM end to end using only task-derived, rule-based rewards.

RecZero structures every output into four tagged stages: analyze the user's interests from history, summarize the target item, reason about user-item compatibility, and predict a numerical rating. A format reward enforces this schema, while a continuous answer reward increases as the predicted rating approaches the ground truth. Group Relative Policy Optimization samples eight trajectories per input and optimizes their relative advantages. RecOne is a hybrid variant that first warm-starts the model with 1,000 teacher-generated reasoning examples from DeepSeek-R1 and then applies the same RL procedure.

Experiments start from Qwen2.5-7B-Instruct-1M and evaluate offline rating prediction on Amazon Book, Amazon Music, and Yelp using MAE and RMSE. RecOne obtains the best result on all six dataset-metric combinations; relative to the strongest prior result, it reduces RMSE by 6.7%, 12.2%, and 6.2%, and MAE by 16.8%, 29.9%, and 7.5% on Book, Music, and Yelp. Pure-RL RecZero has the best MAE among baselines on all three datasets, although its RMSE is not always better than the strongest baseline. Ablations indicate that explicit multi-step reasoning, a graded rather than exact-match reward, and RL after warm-start each contribute to accuracy.

The cost study on Amazon Music reports that early-stopped RecZero uses 480 labeled instances and 0.4 GPU-hours to reach MAE 0.5419, while an SFT-only RecOne variant uses 20,000 instances and 0.6 GPU-hours yet reaches MAE 0.6472. Fully trained RecZero uses 2,400 samples and averages about 311 inference tokens per request. These figures support sample efficiency within the tested setup, but the full experiments use eight H20 GPUs, and generated reasoning is evaluated only indirectly through rating error rather than for faithfulness. The work is limited to offline rating prediction, does not test production ranking or online user response, and does not evaluate larger base models or iterative self-training.

## 繁中摘要

這篇論文以 reinforcement learning 取代推理式 rating prediction 常見的 teacher distillation 流程。既有方法通常先讓大型 teacher LLM 產生偏好分析與推理軌跡，再訓練較小的模組或 student 模仿。作者認為這種做法成本高，會把 teacher 可能不佳的推理固定成靜態監督，而且中間推理與最終推薦目標彼此分離。RecZero 改為使用任務本身可計算的 rule-based reward，端到端訓練單一 LLM。

RecZero 強制輸出四個帶標籤的階段：從歷史紀錄分析使用者興趣、摘要目標物品、推論使用者與物品的相容性，以及預測數值評分。Format reward 檢查輸出結構；連續型 answer reward 則依預測分數接近真實評分的程度給分。Group Relative Policy Optimization 對每個輸入取樣 8 條 trajectory，利用群組內相對 advantage 更新模型。RecOne 是混合版本，先用 DeepSeek-R1 產生的 1,000 筆推理資料 warm-start，再執行相同 RL。

實驗以 Qwen2.5-7B-Instruct-1M 為起點，在 Amazon Book、Amazon Music 與 Yelp 上進行離線 rating prediction，指標為 MAE 與 RMSE。RecOne 在三個資料集的六個組合上都最佳；相較先前最佳結果，Book、Music、Yelp 的 RMSE 分別降低 6.7%、12.2%、6.2%，MAE 分別降低 16.8%、29.9%、7.5%。只使用 RL 的 RecZero 在三個資料集都取得優於 baselines 的 MAE，但 RMSE 並非每次都勝過最強 baseline。消融結果顯示，明確的多步推理、連續而非 exact-match 的 reward，以及 warm-start 後繼續 RL 都有助於準確度。

Amazon Music 的成本實驗顯示，early-stopped RecZero 使用 480 筆標記資料與 0.4 GPU-hours，MAE 達 0.5419；只做 SFT 的 RecOne 變體使用 20,000 筆資料與 0.6 GPU-hours，MAE 仍為 0.6472。完整 RecZero 使用 2,400 筆樣本，每次請求平均約 311 個 inference tokens。這些數字支持方法在該設定下的樣本效率，但完整 LLM 實驗使用 8 張 H20 GPU，而且推理文字只透過 rating error 間接評估，沒有驗證其忠實性。研究也只涵蓋離線評分預測，未測試正式 ranking、線上使用者反應、更大的 base model 或多輪自我訓練。

## Notes

- RecZero's total reward is the sum of a format reward and a normalized continuous rating-error reward.
- The reported training setup uses batch size 8, learning rate `2e-6`, one epoch, temperature 1.0, eight rollouts per sample, and zero KL penalty.
- RecOne improves the RL starting point but reintroduces a teacher model for its cold-start data, so only RecZero is fully teacher-free.
