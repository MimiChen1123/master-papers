---
date: 2026-08-30
title: "On Softmax Direct Preference Optimization for Recommendation"
authors: "Yuxin Chen, Junfei Tan, An Zhang, Zhengyi Yang, Leheng Sheng, Enzhi Zhang, Xiang Wang, Tat-Seng Chua"
venue: "NeurIPS 2024"
---

# On Softmax Direct Preference Optimization for Recommendation

- Paper page: https://proceedings.neurips.cc/paper_files/paper/2024/hash/30732ddb12d9faf7180f5d0e8b5b5da7-Abstract-Conference.html
- PDF: https://proceedings.neurips.cc/paper_files/paper/2024/file/30732ddb12d9faf7180f5d0e8b5b5da7-Paper-Conference.pdf
- Local PDF: [../../pdfs/2026-08/2026-08-30-on-softmax-direct-preference-optimization-for-recommendation.pdf](../../pdfs/2026-08/2026-08-30-on-softmax-direct-preference-optimization-for-recommendation.pdf)
- Venue: NeurIPS 2024

## English Summary

This paper studies a mismatch in language-model-based recommendation. Many LM-based recommenders convert a user's interaction history into a prompt and fine-tune the model to generate the positive target item with a standard language modeling loss. The authors argue that this objective does not directly optimize personalized ranking and ignores negative items, even though recommendation is fundamentally about distinguishing preferred items from less preferred candidates.

To address this, the paper proposes Softmax Direct Preference Optimization, or S-DPO. It adapts DPO from pairwise preference alignment to recommendation settings with one positive item and multiple negative items. The method extends the Plackett-Luce preference model to partial rankings, then derives a softmax-style DPO loss that explicitly pushes the language model to rank the preferred item above multiple dispreferred candidates.

Theoretically, the paper connects ordinary DPO to BPR-style pairwise ranking and connects S-DPO to softmax loss with negative sampling. This helps explain why multiple negatives matter: S-DPO assigns stronger learning signals to hard negatives, making it better suited to ranking tasks. Experiments on three real-world sequential recommendation datasets show that S-DPO improves HR@1 and validity over traditional sequential recommenders and LM-based baselines, while giving higher rewards to preferred items.

## 繁中 Summary

這篇論文討論 language-model-based recommendation 中的目標函數不匹配問題。許多 LM-based recommenders 會把使用者歷史互動轉成 prompt，再用標準 language modeling loss 讓模型生成正樣本 item。作者認為這個訓練目標沒有直接最佳化 personalized ranking，也忽略 negative items；但推薦任務本質上是要把使用者偏好的 item 和較不偏好的 candidates 區分開。

為了解決這個問題，論文提出 Softmax Direct Preference Optimization，簡稱 S-DPO。它把 DPO 從 pairwise preference alignment 改造成適合推薦的形式，也就是一個 positive item 搭配多個 negative items。方法上，作者把 Plackett-Luce preference model 延伸到 partial rankings，並推導出 softmax-style DPO loss，讓語言模型明確學會把 preferred item 排在多個 dispreferred candidates 前面。

理論上，論文把一般 DPO 和 BPR-style pairwise ranking 連結起來，並把 S-DPO 和 negative sampling 下的 softmax loss 連結起來。這解釋了為什麼 multiple negatives 很重要：S-DPO 會對 hard negatives 給出更強的 learning signals，因此更適合 ranking tasks。三個真實 sequential recommendation datasets 的實驗顯示，S-DPO 在 HR@1 和 validity 上優於傳統 sequential recommenders 與 LM-based baselines，也能給 preferred items 更高的 reward。

## Notes

- This paper is directly relevant to aligning LLM-based recommenders with ranking objectives.
- The key contribution is replacing positive-only language modeling with multi-negative preference optimization.
- S-DPO is positioned as a recommendation-specific DPO objective connected to softmax ranking loss.
