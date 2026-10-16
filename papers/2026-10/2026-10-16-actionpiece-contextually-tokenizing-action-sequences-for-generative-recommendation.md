---
date: 2026-10-16
title: "ActionPiece: Contextually Tokenizing Action Sequences for Generative Recommendation"
authors: "Yupeng Hou, Jianmo Ni, Zhankui He, Noveen Sachdeva, Wang-Cheng Kang, Ed H. Chi, Julian McAuley, Derek Zhiyuan Cheng"
venue: "ICML 2025"
---

# ActionPiece: Contextually Tokenizing Action Sequences for Generative Recommendation

- Paper page: https://proceedings.mlr.press/v267/hou25f.html
- PDF: https://raw.githubusercontent.com/mlresearch/v267/main/assets/hou25f/hou25f.pdf
- Local PDF: [../../pdfs/2026-10/2026-10-16-actionpiece-contextually-tokenizing-action-sequences-for-generative-recommendation.pdf](../../pdfs/2026-10/2026-10-16-actionpiece-contextually-tokenizing-action-sequences-for-generative-recommendation.pdf)
- Venue: ICML 2025

## English Summary

Generative recommendation represents user actions as discrete token patterns and autoregressively predicts the next action. Existing tokenizers usually assign a fixed tokenization to each item independently of its sequence, even though the same action can imply different preferences depending on neighboring actions. ActionPiece addresses this mismatch by treating a history as an ordered sequence of actions, with each action itself represented as an unordered set of item features. Its tokens can describe one feature, several features within one item, all features of an item, or features spanning adjacent items.

Vocabulary construction follows a bottom-up process analogous to byte-pair encoding, but adapted to sequences of sets. Starting from single-feature tokens, ActionPiece repeatedly merges pairs with high weighted co-occurrence. It counts both pairs inside one action and pairs across adjacent actions; the latter directly encodes context. Pair weights are derived from the probability that two features would become adjacent after randomly permuting each unordered set. Cross-action merges are stored in intermediate linked-list nodes, while inverted indexes and a lazily updated heap reduce construction complexity from the naive O(QNLm^2) to O(log Q log H * NLm^2).

For segmentation, set permutation regularization (SPR) randomly permutes features within each action and applies ordinary BPE-style segmentation to the flattened sequence. Different permutations produce token sequences with the same semantics, serving as data augmentation during training. At inference, the model processes several segmentations and averages item scores across the resulting rankings. SPR raises training-token utilization from 56.89% under naive segmentation to 87.01% after one epoch and 95.33% after five epochs, although ensembling more segmentations adds computation and yields diminishing improvements beyond five to seven variants.

Experiments use Amazon Sports, Beauty, and CDs with leave-last-out evaluation, five random seeds, and Recall/NDCG at 5 and 10. ActionPiece achieves NDCG@10 of 0.0264, 0.0424, and 0.0451, improving over the strongest baseline by 12.82%, 6.00%, and 6.37%, respectively. Ablations show that context-aware merging, probabilistic weighting, and SPR all contribute; merely enlarging TIGER's vocabulary or adding SPR to a context-independent tokenizer does not reproduce the gains. Larger vocabularies improve accuracy and shorten sequences but increase embedding memory, while the five-way inference ensemble consumes extra FLOPs and relies on parallel hardware to maintain latency. The evidence is limited to three offline Amazon categories with histories truncated to 20 actions for generative models, quantized text-derived item features, and one next-item objective; multimodal actions, online serving behavior, and other sequence domains remain future work.

## 繁中摘要

Generative recommendation 會把使用者 actions 表示成 discrete token patterns，再以 autoregressive 方式預測下一個 action。既有 tokenizer 通常獨立處理每個 item，讓同一 item 在所有 sequences 中都有固定 tokenization；但同一 action 可能因前後 actions 不同而代表不同偏好。ActionPiece 將 history 視為按時間排序的 action sequence，而每個 action 本身是 unordered item-feature set。它的 token 可以表示單一 feature、同一 item 內多個 features、整個 item，或橫跨相鄰 items 的 features。

Vocabulary construction 類似 byte-pair encoding 的 bottom-up 流程，但專門處理 sequences of sets。方法從 single-feature tokens 開始，反覆合併 weighted co-occurrence 最高的 token pairs；計數同時包含單一 action 內的 pairs 與相鄰 actions 之間的 pairs，後者直接注入 context。Pair weight 來自每個 unordered set 隨機排列後，兩個 features 成為相鄰元素的機率。跨 action 的合併使用 intermediate linked-list nodes 儲存，搭配 inverted indexes 與 lazy-update heap，將 vocabulary construction complexity 從 naive O(QNLm^2) 降為 O(log Q log H * NLm^2)。

在 segmentation 階段，set permutation regularization（SPR）會隨機排列各 action 內的 features，攤平成 sequence 後套用一般 BPE-style segmentation。不同 permutations 可得到語意相同但 token sequence 不同的表示，於 training 時作為 data augmentation；inference 時則處理多種 segmentation，並平均各 ranking 的 item scores。SPR 將 naive segmentation 的 training-token utilization 由 56.89% 提升至第一個 epoch 的 87.01%，五個 epochs 後達 95.33%。不過，增加 inference segmentations 也會提高運算量，而且超過五至七個 variants 後改善趨緩。

實驗使用 Amazon Sports、Beauty、CDs，採 leave-last-out、五個 random seeds，並以 Recall/NDCG@5、@10 評估。ActionPiece 的 NDCG@10 分別為 0.0264、0.0424、0.0451，相對最強 baseline 提升 12.82%、6.00%、6.37%。Ablations 顯示 context-aware merging、probabilistic weighting 與 SPR 都有貢獻；單純擴大 TIGER vocabulary，或把 SPR 加到 context-independent tokenizer，都無法重現完整提升。較大的 vocabulary 可改善準確率並縮短 sequences，但會增加 embedding memory；五路 inference ensemble 也需要額外 FLOPs，論文仰賴 parallel hardware 維持 latency。證據仍限於三個離線 Amazon categories，generative models 的 histories 最長截為 20 actions，item features 來自量化的 text embeddings，且只評估 next-item objective；multimodal actions、線上服務行為與其他 sequence domains 仍待後續研究。

## Notes

- Official code: https://github.com/google-deepmind/action_piece
- Dataset sizes are 35,598 users/18,357 items/260,739 actions for Sports, 22,363/12,101/176,139 for Beauty, and 75,258/64,443/1,022,334 for CDs.
- The reported configuration uses a 40,000-token vocabulary, five inference segmentations, beam size 50, and a four-layer encoder-decoder Transformer.
- Each implemented model is trained on one 40 GB NVIDIA A100 GPU; ActionPiece is trained from scratch for up to 200 epochs with early stopping.
