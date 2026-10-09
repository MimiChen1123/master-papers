---
date: 2026-10-09
title: "Tree of Preferences for Diversified Recommendation"
authors: "Hanyang Yuan, Ning Tang, Tongya Zheng, Jiarong Xu, Xintong Hu, Renhong Huang, Shunyu Liu, Jiacong Hu, Jiawei Chen, Mingli Song"
venue: "NeurIPS 2025"
---

# Tree of Preferences for Diversified Recommendation

- Paper page: https://proceedings.neurips.cc/paper_files/paper/2025/hash/e41f42c87e0492cdf1673e28fdaf47b2-Abstract-Conference.html
- PDF: https://proceedings.neurips.cc/paper_files/paper/2025/file/e41f42c87e0492cdf1673e28fdaf47b2-Paper-Conference.pdf
- Local PDF: [../../pdfs/2026-10/2026-10-09-tree-of-preferences-for-diversified-recommendation.pdf](../../pdfs/2026-10/2026-10-09-tree-of-preferences-for-diversified-recommendation.pdf)
- Venue: NeurIPS 2025

## English Summary

This paper studies recommendation diversity as a data-bias problem. Observed interactions are incomplete because exposure bias hides items a user never had the chance to see, while selection bias makes some interests more likely to produce feedback than others. A recommender trained only on these observations can overemphasize dominant interests, but naive diversification often adds irrelevant items. Tree of Preferences Recommendation (ToP-Rec) uses an LLM's external knowledge to infer underexplored yet plausible interests and turns those inferences into synthetic training interactions, preserving ordinary recommender inference.

ToP-Rec first constructs one global Tree of Preferences shared by all users. A semantically diverse subset of items is selected through text encoding and k-means, and an LLM recursively partitions the item preference space from coarse concepts to fine-grained leaves. For each user, the LLM performs a top-down, breadth-first traversal using textual attributes and interaction history, selects paths that explain observed behavior, summarizes the rationale, and revisits the tree to identify plausible preferences absent from the history. Items are assigned to their best-matching leaf once, creating candidate pools for every fine-grained preference.

Synthetic interactions are selected with a weighted combination of relevance and diversity. Relevance is the cosine similarity between pretrained text representations of the user and item; diversity contribution is inversely related to how frequently the item's preference already occurs in the user's history. The selected items are added to the observed interactions, and a general recommender such as LightGCN is trained on the combined data. Because per-user LLM generation is expensive, ToP-Rec periodically estimates user influence from alignment between local gradients and the model's parameter-update trajectory, augmenting only influential users. The LLM work is therefore shifted to offline data construction, while online inference uses the trained recommender.

Experiments use Twitter, Weibo, and Amazon with Recall@50/100 for relevance and Category-Entropy@50/100 for diversity. With LightGCN, ToP-Rec obtains the strongest result in 11 of 12 dataset-metric combinations and is narrowly second on Weibo Recall@100. It also traces the best relevance-diversity frontier, retains similar inference latency to traditional methods, and improves both metrics with MF and NGCF backbones. Results are averaged over five runs with standard deviations. However, synthetic interactions remain inferred rather than observed preferences and can introduce false positives. The method depends on rich, high-quality user and item text, incurs offline LLM and gradient-tracking costs, and explicitly targets within-list diversity rather than novelty or long-tail exposure.

## 繁中摘要

這篇論文把推薦多樣性視為 data bias 問題。Exposure bias 使使用者沒有機會看到的物品無法產生互動；selection bias 則讓某些興趣比其他興趣更容易留下回饋。只用觀測資料訓練的 recommender 可能過度強化主導興趣，但直接增加多樣性又常帶入不相關物品。Tree of Preferences Recommendation（ToP-Rec）利用 LLM 的外部知識推論尚未充分展現、但合理的潛在興趣，再把推論結果轉成 synthetic training interactions，同時保留一般 recommender 的推論流程。

ToP-Rec 先建立所有使用者共用的一棵全域 Tree of Preferences。方法以 text encoder 和 k-means 選出語意多樣的 item subset，再讓 LLM 從粗略概念到細緻 leaf 遞迴切分偏好空間。對每位使用者，LLM 根據 textual attributes 與 interaction history 由上而下做 breadth-first traversal，選擇能解釋既有行為的路徑、摘要行為原因，再重新檢查偏好樹，找出歷史中沒有出現但可能存在的偏好。每個 item 只需一次指派到最符合的 leaf，形成各種細緻偏好的 candidate pools。

Synthetic interactions 由 relevance 與 diversity 的加權分數選出。Relevance 使用 pretrained text representations 的 user-item cosine similarity；diversity contribution 則與該 item 所屬偏好在使用者歷史中的出現頻率成反比。選中的 item 會加入原始互動，再以合併資料訓練 LightGCN 等一般 recommender。由於逐一呼叫 LLM 的成本高，ToP-Rec 會定期衡量 local gradient 與模型 parameter-update trajectory 的對齊程度，只替 influential users 生成資料。因此 LLM 成本位於離線資料建構階段，線上 inference 仍由訓練後的 recommender 執行。

實驗使用 Twitter、Weibo、Amazon，以 Recall@50/100 衡量 relevance、Category-Entropy@50/100 衡量 diversity。搭配 LightGCN 時，ToP-Rec 在 12 個資料集與指標組合中有 11 個最佳，僅 Weibo Recall@100 略居第二；它也呈現最佳 relevance-diversity frontier、維持接近傳統方法的 inference latency，並在 MF 與 NGCF backbone 上同時改善兩類指標。結果為五次實驗平均並回報 standard deviations。不過，synthetic interactions 仍是推論而非真實觀測偏好，可能引入 false positives；方法依賴豐富且高品質的 user/item text，也需要離線 LLM 與 gradient tracking 成本，而且目標是 within-list diversity，不包含 novelty 或 long-tail exposure。

## Notes

- The official implementation is available at https://github.com/xxx08796/ToP_Rec_NIPS.
- The datasets contain 2,118-14,663 users, 5,711-8,747 items, and 40,223-661,783 interactions.
- The main experiments use Qwen2.5-32B-Instruct; appendix tests with Qwen2.5-7B-Instruct and Llama3-70B show similar behavior.
