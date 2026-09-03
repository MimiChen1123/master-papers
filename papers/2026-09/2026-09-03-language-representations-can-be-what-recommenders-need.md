---
date: 2026-09-03
title: "Language Representations Can be What Recommenders Need: Findings and Potentials"
authors: "Leheng Sheng, An Zhang, Yi Zhang, Yuxin Chen, Xiang Wang, Tat-Seng Chua"
venue: "ICLR 2025"
---

# Language Representations Can be What Recommenders Need: Findings and Potentials

- Paper page: https://proceedings.iclr.cc/paper_files/paper/2025/hash/e4bab1843c8d5a69f5abfd0824593493-Abstract-Conference.html
- PDF: https://proceedings.iclr.cc/paper_files/paper/2025/file/e4bab1843c8d5a69f5abfd0824593493-Paper-Conference.pdf
- Local PDF: [../../pdfs/2026-09/2026-09-03-language-representations-can-be-what-recommenders-need.pdf](../../pdfs/2026-09/2026-09-03-language-representations-can-be-what-recommenders-need.pdf)
- Venue: ICLR 2025

## English Summary

This paper asks whether language models already encode useful recommendation signals, rather than treating language representations as only semantic side information. The authors test whether item title embeddings from advanced language models can be mapped into a behavior space for collaborative filtering. Their empirical finding is that a simple mapping from language representation space to recommendation behavior space can produce strong recommendation performance, suggesting a possible homomorphism between the two spaces.

Motivated by this finding, the paper proposes AlphaRec, a simple collaborative filtering model that uses frozen language-model representations of item textual metadata instead of ID-based item embeddings. AlphaRec applies a two-layer MLP to project item and user language representations, uses lightweight graph convolution over the user-item interaction graph, and optimizes with an InfoNCE contrastive loss. The design is intentionally simple: the contribution is mainly about exposing the recommendation potential already present in advanced language representations, not inventing a complex new recommender architecture.

Across Movies & TV, Video Games, and Books datasets, AlphaRec outperforms strong ID-based and LM-enhanced collaborative filtering baselines such as LightGCN, SGL, XSimGCL, KAR, and RLMRec. The analysis further shows three useful properties: faster convergence from better item initialization, strong zero-shot transfer to new datasets without user or item overlap, and the ability to adjust recommendations using text-based user intentions. The main limitations are that the work lacks a theoretical guarantee, uses a shared MLP rather than personalized projection, and evaluates intention-aware recommendation with fixed generated intentions rather than more realistic personalized user requests.

## 繁中摘要

這篇論文想回答一個推薦系統裡很關鍵的問題：language model 的 representation 是否已經隱含使用者偏好與 collaborative signal，而不只是提供語意 side information。作者先測試能不能把 item title 的 language embedding 線性映射到推薦用的 behavior space。結果顯示，進階 LM 產生的 item representation 經過簡單映射後，可以得到很強的推薦效果，暗示 language space 和 recommendation behavior space 之間可能存在某種可對應的結構。

基於這個觀察，作者提出 AlphaRec。它不用傳統 ID-based item embedding，而是使用 frozen language model 對 item 文字 metadata 產生 representation，再透過 two-layer MLP 做 projection，接著在 user-item interaction graph 上做輕量 graph convolution，最後用 InfoNCE contrastive loss 訓練。這個模型刻意保持簡單，重點不是提出複雜架構，而是證明 advanced language representation 本身已經有很大的推薦潛力。

在 Movies & TV、Video Games、Books 等資料集上，AlphaRec 優於 LightGCN、SGL、XSimGCL、KAR、RLMRec 等 ID-based 或 LM-enhanced CF baseline。論文也展示三個延伸價值：language representation 可以作為好的 item initialization，因此收斂較快；在沒有 user/item overlap 的新資料集上有不錯的 zero-shot recommendation 能力；也可以結合文字形式的 user intention 來調整推薦結果。限制方面，作者指出目前缺乏理論保證，AlphaRec 只有一個共享 MLP、沒有個人化 projection，而且 intention-aware 實驗使用固定生成的 user intention，距離真實產品裡多樣化、個人化的自然語言需求還有差距。

## Notes

- This paper is useful if you are thinking about replacing or initializing item ID embeddings with language-model representations.
- The strongest takeaway is that language representations may already contain collaborative preference structure, especially after mapping into a behavior space.
- AlphaRec is simple by design, so the paper is more about evidence and research direction than a heavily engineered production recommender.
