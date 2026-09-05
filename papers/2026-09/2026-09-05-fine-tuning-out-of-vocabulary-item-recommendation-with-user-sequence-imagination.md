---
date: 2026-09-05
title: "Fine-Tuning Out-of-Vocabulary Item Recommendation with User Sequence Imagination"
authors: "Ruochen Liu, Hao Chen, Yuanchen Bei, Qijie Shen, Fangwei Zhong, Senzhang Wang, Jianxin Wang"
venue: "NeurIPS 2024"
---

# Fine-Tuning Out-of-Vocabulary Item Recommendation with User Sequence Imagination

- Paper page: https://proceedings.neurips.cc/paper_files/paper/2024/hash/10d52f5d2ef0f69ac10da7c962fb6db9-Abstract-Conference.html
- PDF: https://proceedings.neurips.cc/paper_files/paper/2024/file/10d52f5d2ef0f69ac10da7c962fb6db9-Paper-Conference.pdf
- Local PDF: [../../pdfs/2026-09/2026-09-05-fine-tuning-out-of-vocabulary-item-recommendation-with-user-sequence-imagination.pdf](../../pdfs/2026-09/2026-09-05-fine-tuning-out-of-vocabulary-item-recommendation-with-user-sequence-imagination.pdf)
- Venue: NeurIPS 2024

## English Summary

This paper focuses on out-of-vocabulary item recommendation, where new items have content features but no interaction history. Traditional cold-start or OOV methods usually generate temporary item embeddings from content and directly mix them with well-trained in-vocabulary item embeddings. The authors argue that this is insufficient because IV embeddings are optimized through user-interaction backpropagation, while OOV embeddings remain stuck at a generated "makeshift" representation, leaving a content-behavior gap.

The proposed framework, User Sequence Imagination (USIM), fine-tunes OOV item embeddings by imagining useful user interaction sequences. USIM formulates the process as a reinforcement learning problem: the state is the current OOV item embedding, the action is selecting an imagined user, and the transition updates the item embedding through a backpropagation-like step. The reward combines embedding alignment, downstream recommendation performance, and step cost. To handle the huge user action space, the method builds an exploration set using similar users plus random actions, and trains a recommender-oriented PPO variant called RecPPO.

Experiments on CiteULike and MovieLens with both MF and GNN backbones show that USIM improves overall and OOV recommendation performance while preserving IV recommendation quality better than dropout-style baselines. Ablations confirm that the exploration set and recommendation-performance reward both matter. The paper also reports a two-week online A/B test on a large e-commerce platform, where USIM improved OOV item page views, predicted click-through rate, and gross merchandise value compared with Random, MetaEmb, and ALDI. A useful deployment takeaway is that USIM performs offline OOV embedding optimization, so online serving can remain close to standard embedding lookup.

## 繁中摘要

這篇論文處理 out-of-vocabulary item recommendation，也就是新商品、新影片、新貼文等沒有互動歷史的 item。傳統 OOV 方法多半從內容特徵產生一個臨時 embedding，再把它和已訓練好的 IV item embedding 一起推薦。但作者指出，IV embedding 是透過使用者互動資料反向傳播訓練出來的，OOV embedding 如果只靠內容生成，會和真正的 behavior embedding 有明顯落差。

作者提出 User Sequence Imagination (USIM)：先想像哪些使用者可能會和 OOV item 互動，再用這些 imagined user sequence 來 fine-tune OOV item embedding。USIM 把這件事建模成 reinforcement learning 問題：state 是目前的 OOV item embedding，action 是選擇一個想像中的使用者，transition 會根據該使用者更新 item embedding。reward 則結合 embedding alignment、下游推薦效果與 action cost。為了處理龐大的使用者 action space，USIM 會用相似使用者加上隨機 action 建立 exploration set，並用 recommender-oriented PPO，也就是 RecPPO，來訓練。

在 CiteULike 和 MovieLens 上，USIM 搭配 MF 與 GNN backbone 都能提升 overall 與 OOV recommendation，同時比 dropout-style baseline 更能維持 IV item 的推薦品質。消融實驗顯示 exploration set 和 recommendation-performance reward 都是關鍵。論文也包含大型電商平台兩週 A/B test，USIM 相比 Random、MetaEmb、ALDI 提升了 OOV item PV、PCTR 與 GMV。實務上值得注意的是，USIM 主要做離線的 OOV embedding optimization，因此線上 serving 仍可接近一般 embedding lookup 的形式。

## Notes

- This is useful for systems with a high volume of newly uploaded or AI-generated items.
- The main idea is to optimize OOV embeddings as if they had useful interaction histories, instead of only generating them from content.
- The method is attractive for production because the heavier imagination step can run offline before serving.
