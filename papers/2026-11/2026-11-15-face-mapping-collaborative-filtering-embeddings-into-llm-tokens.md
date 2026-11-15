---
date: 2026-11-15
title: "FACE: A General Framework for Mapping Collaborative Filtering Embeddings into LLM Tokens"
authors: "Chao Wang, Yixin Song, Jinhui Ye, Chuan Qin, Dazhong Shen, Lingfeng Liu, Xiang Wang, Yanyong Zhang"
venue: "NeurIPS 2025"
---

# FACE: A General Framework for Mapping Collaborative Filtering Embeddings into LLM Tokens

- Paper page: https://proceedings.neurips.cc/paper_files/paper/2025/hash/d6f034bb216b472fc7d32ec7aff20342-Abstract-Conference.html
- PDF: https://proceedings.neurips.cc/paper_files/paper/2025/file/d6f034bb216b472fc7d32ec7aff20342-Paper-Conference.pdf
- Local PDF: [../../pdfs/2026-11/2026-11-15-face-mapping-collaborative-filtering-embeddings-into-llm-tokens.pdf](../../pdfs/2026-11/2026-11-15-face-mapping-collaborative-filtering-embeddings-into-llm-tokens.pdf)
- Code: https://github.com/YixinRoll/FACE
- Venue: NeurIPS 2025

## English Summary

This paper addresses a representation mismatch between collaborative filtering (CF) recommenders and large language models. CF embeddings encode valuable user-item interaction patterns but are continuous, entangled, and generally lack explicit linguistic meaning; LLMs are instead pretrained to process discrete text tokens. Earlier adapters can project CF vectors into an LLM embedding space, but the projected vectors need not coincide with actual vocabulary tokens and often require LLM fine-tuning. FACE is a model-agnostic framework that converts CF user and item embeddings into short sets of genuine, semantically meaningful LLM tokens called descriptors, without fine-tuning the LLM.

FACE first filters an LLM vocabulary to retain meaningful full words and freezes their pretrained embeddings as a quantization codebook. A multi-projector decomposes each CF embedding into several concept-specific vectors, and a Transformer models dependencies among these components. Multi-level residual quantization maps every component to nearby codebook vectors while improving reconstruction accuracy; the first-level tokens become the readable descriptors. A reverse Transformer and concat-projector reconstruct the original CF embedding, so the mapping is trained to preserve collaborative information rather than merely select plausible words.

Semantic alignment forms the second part of the framework. An LLM creates structured textual summaries from item metadata and reviews or from a user's interacted items, while an embedding model encodes both these summaries and sentences formed from FACE descriptors. A contrastive objective pulls each descriptor representation toward its matching summary and away from other users or items. Training proceeds in three stages for stability: pretrain the CF backbone, train the quantized autoencoder without alignment, and finally optimize recommendation, mapping, and semantic-alignment losses jointly. The resulting plugin can be attached to GMF, LightGCN, SimGCL, LightGCL, or the already text-enhanced RLMRec.

Experiments use Amazon-book, Yelp, and Steam with full-ranking Recall and NDCG at 5 and 20. Adding FACE improves nearly every backbone-metric combination; the largest reported relative gains are 7.31% on Amazon-book, 11.55% on Yelp, and 8.00% on Steam. With LightGCN, Amazon-book Recall@5 rises from 0.0659 to 0.0705 and NDCG@20 from 0.0961 to 0.1009; Yelp Recall@20 rises from 0.1141 to 0.1203; Steam Recall@20 rises from 0.1361 to 0.1439. Ablations show that semantic alignment contributes the most: removing it from LightGCN+FACE reduces Amazon-book Recall@20 from 0.1622 to 0.1565 and Yelp Recall@20 from 0.1203 to 0.1171.

Interpretability is evaluated through item retrieval, item generation, and interaction explanations. For example, LLaMA2-based FACE descriptors recover the correct item among 50 candidates with accuracies of 0.7024, 0.6469, and 0.7322 on Amazon-book, Yelp, and Steam. In a study with 40 Amazon users and ten human annotators, explanations based on 16-token descriptors receive slightly better rankings than paragraph-length RLMRec profiles. However, this study is small and uses sampled positive and negative interactions rather than measuring end-user usefulness. The authors also note that experiments use relatively small language models, do not validate larger models, and cover only collaborative filtering rather than sequential recommendation. LLM biases can affect descriptors and explanations, while language-model computation may limit accessibility.

## 繁中摘要

這篇論文處理 collaborative filtering（CF）推薦模型與 large language models 之間的 representation mismatch。CF embeddings 包含有價值的 user-item interaction patterns，但它們是 continuous、entangled，通常也沒有明確語言意義；LLM 則以 discrete text tokens 進行預訓練。既有 adapter 雖能把 CF vectors 投影到 LLM embedding space，投影結果卻不一定對應真實 vocabulary tokens，而且常需要 fine-tune LLM。FACE 是 model-agnostic framework，能在不調整 LLM 參數的情況下，把 CF user/item embeddings 轉成一小組具有語意的真實 LLM tokens，作者稱為 descriptors。

FACE 先過濾 LLM vocabulary，只保留有意義的完整單字，並凍結其 pretrained embeddings 作為 quantization codebook。Multi-projector 把每個 CF embedding 分解成多個 concept-specific vectors，再由 Transformer 建模各成分間的關係。Multi-level residual quantization 將每個成分映射到鄰近 codebook vectors，同時改善 reconstruction accuracy；第一層 tokens 就是可讀的 descriptors。反向 Transformer 與 concat-projector 再重建原始 CF embedding，使 mapping 保留 collaborative information，而不只是挑選看似合理的單字。

Semantic alignment 是框架的第二部分。LLM 從 item metadata、reviews 或使用者互動過的 items 產生 structured textual summaries，embedding model 則同時編碼這些 summaries 與由 FACE descriptors 組成的句子。Contrastive objective 讓每個 descriptor representation 接近對應 summary，並遠離其他 users/items。為了穩定訓練，流程分成三階段：先預訓練 CF backbone，再於沒有 alignment 的情況下訓練 quantized autoencoder，最後共同最佳化 recommendation、mapping 與 semantic-alignment losses。這個 plugin 可套用到 GMF、LightGCN、SimGCL、LightGCL，以及已使用文字資訊的 RLMRec。

實驗使用 Amazon-book、Yelp 與 Steam，採用 full-ranking Recall 與 NDCG at 5/20。加入 FACE 後，幾乎所有 backbone-metric combinations 都有改善；三個 datasets 的最大相對提升分別為 7.31%、11.55% 與 8.00%。以 LightGCN 為例，Amazon-book Recall@5 從 0.0659 升至 0.0705，NDCG@20 從 0.0961 升至 0.1009；Yelp Recall@20 從 0.1141 升至 0.1203；Steam Recall@20 從 0.1361 升至 0.1439。Ablation 顯示 semantic alignment 貢獻最大：移除後，LightGCN+FACE 的 Amazon-book Recall@20 從 0.1622 降至 0.1565，Yelp 則從 0.1203 降至 0.1171。

Interpretability 透過 item retrieval、item generation 與 interaction explanations 評估。例如 LLaMA2-based FACE descriptors 在 50 個 candidates 中找回正確 item 的 accuracy，在 Amazon-book、Yelp、Steam 分別為 0.7024、0.6469、0.7322。由 40 位 Amazon users 與十位 human annotators 組成的研究中，依據 16-token descriptors 產生的解釋，排名略優於 paragraph-length RLMRec profiles。不過此研究規模小，且以抽樣 positive/negative interactions 評估，並未直接衡量 end-user usefulness。作者也指出，實驗只使用較小的 language models，尚未驗證更大模型，且目前僅涵蓋 collaborative filtering，未延伸到 sequential recommendation。LLM 既有 bias 可能影響 descriptors 與 explanations，語言模型的運算成本也可能限制可及性。

## Notes

- Amazon-book has 11,000 users, 9,332 items, and 120,464 interactions; Yelp has 11,091 users, 11,010 items, and 166,620 interactions; Steam has 23,310 users, 5,237 items, and 316,190 interactions.
- The default setup uses 16 descriptors, a 256-dimensional codebook, a 0.02 contrastive temperature, 256-dimensional CF embeddings, Adam with learning rate 0.01, batch size 128, and a 3:1:1 train/validation/test split.
- The main implementation uses a LLaMA2-7B-derived embedding model; appendices also test MiniLM-L6 and Qwen2-7B variants, which generally retain the recommendation gains.
- Complexity is linear in the total number of users and items when batch size is treated as much smaller, although codebook nearest-neighbor search and LLM encoding add substantial constants.
- Main recommendation results are averaged over three runs; the paper does not report confidence intervals or significance tests in the main comparison.
