---
date: 2026-11-20
title: "Generate What You Prefer: Reshaping Sequential Recommendation via Guided Diffusion"
authors: "Zhengyi Yang, Jiancan Wu, Zhicai Wang, Yancheng Yuan, Xiang Wang, Xiangnan He"
venue: "NeurIPS 2023"
---

# Generate What You Prefer: Reshaping Sequential Recommendation via Guided Diffusion

- Paper page: https://proceedings.neurips.cc/paper_files/paper/2023/hash/4c5e2bcbf21bdf40d75fddad0bd43dc9-Abstract-Conference.html
- PDF: https://proceedings.neurips.cc/paper_files/paper/2023/file/4c5e2bcbf21bdf40d75fddad0bd43dc9-Paper-Conference.pdf
- Local PDF: [../../pdfs/2026-11/2026-11-20-generate-what-you-prefer-reshaping-sequential-recommendation-via-guided-diffusion.pdf](../../pdfs/2026-11/2026-11-20-generate-what-you-prefer-reshaping-sequential-recommendation-via-guided-diffusion.pdf)
- Code: https://github.com/YangZhengyi98/DreamRec
- Venue: NeurIPS 2023

## English Summary

Most sequential recommenders use a learning-to-classify objective: given a user's interaction history and the next positive item, they sample non-interacted items as negatives and train the model to distinguish the positive. The authors argue that this formulation is constrained by the sampled candidate pool and can dilute preference signals with easy or mislabeled negatives. DreamRec instead treats next-item recommendation as generation of an idealized "oracle item" embedding conditioned on the user's history, followed by nearest-neighbor retrieval from the actual catalog.

DreamRec embeds the historical sequence with a Transformer encoder and uses that representation to condition a diffusion model over the target item's continuous embedding. During training, Gaussian noise is added to the observed next-item embedding, and an MLP learns to reconstruct the clean target at randomly sampled diffusion steps. The guidance representation is replaced with a dummy token for a fraction of examples, jointly training conditional and unconditional models. At inference, classifier-free guidance combines both predictions; a tunable weight controls how strongly the generated item follows the user's history. The final top-K list consists of catalog items with the largest inner products with the generated embedding. Training therefore uses no negative items, although catalog retrieval is still required at evaluation and deployment time.

Experiments use YooChoose, KuaiRec, and Zhihu with chronological 8:1:1 splits, ten-item histories, 64-dimensional embeddings, and full top-20 evaluation. DreamRec reports the best HR@20 and NDCG@20 among seven baselines on all three datasets. Its HR@20/NDCG@20 results are 4.78%/2.23% on YooChoose, 5.16%/4.11% on KuaiRec, and 2.26%/0.79% on Zhihu. Results are averages of five runs with standard deviations. T-SNE visualizations suggest that DreamRec's item embeddings occupy more of the latent space than SASRec embeddings, while guidance-strength experiments show a non-monotonic trade-off: moderate personalization improves accuracy, but overly strong guidance harms generation quality.

The main limitation is computational. Sampling iterates over many diffusion steps, making inference slow, and training is more expensive than classification-based models; the paper searches from 50 to 2,000 steps but does not provide a runtime table. The "oracle item" is also a modeling interpretation rather than an observed human cognitive state, and offline next-item accuracy does not validate that generated vectors correspond to genuinely desired or novel items. Evaluation covers three filtered datasets, excludes cold-start items, and retrieves only existing catalog items. Finally, the authors warn that generated oracle embeddings could potentially be decoded to expose user preferences, but they do not evaluate privacy attacks or defenses.

## 繁中摘要

多數 sequential recommender 採用 learning-to-classify objective：模型取得使用者的 interaction history 與下一個 positive item，再抽樣未互動 items 作為 negatives，學習區分正負樣本。作者認為這種設計受 sampled candidate pool 限制，而且 easy negatives 或實際上可能被喜歡的未互動 items 會稀釋 preference signal。DreamRec 改把 next-item recommendation 視為 generation task：根據使用者歷史產生理想化的「oracle item」embedding，再從真實 catalog 中做 nearest-neighbor retrieval。

DreamRec 先用 Transformer encoder 編碼歷史序列，再以該 representation 作為 target-item continuous embedding diffusion process 的條件。訓練時，系統對 observed next-item embedding 加入 Gaussian noise，並由 MLP 在隨機 diffusion step 重建乾淨 target。部分 training examples 會把 guidance representation 換成 dummy token，使 conditional 與 unconditional models 能共同訓練。推論時，classifier-free guidance 合併兩種預測，並以可調權重控制生成結果遵循使用者歷史的程度。最後依 generated embedding 與 catalog item embeddings 的 inner product 取出 top-K。訓練過程不需要 negative items，但 evaluation 與部署仍需要 catalog retrieval。

實驗使用 YooChoose、KuaiRec、Zhihu，採 chronological 8:1:1 split、十個歷史 items、64-dimensional embeddings 與完整 top-20 evaluation。DreamRec 在三個 datasets 的 HR@20 與 NDCG@20 均優於七個 baselines：YooChoose 為 4.78%/2.23%，KuaiRec 為 5.16%/4.11%，Zhihu 為 2.26%/0.79%。結果為五次執行的平均值並附 standard deviation。T-SNE visualization 顯示 DreamRec 的 item embeddings 比 SASRec 覆蓋更多 latent space；guidance-strength experiments 則呈現非單調 trade-off：適度加強 personalization 會改善 accuracy，但 guidance 過強會破壞 generation quality。

主要限制是計算成本。Sampling 必須執行多個 diffusion steps，推論較慢，訓練也比 classification-based models 昂貴；論文搜尋 50 到 2,000 steps，卻沒有提供 runtime table。「Oracle item」也是一種 modeling interpretation，並非直接觀測到的使用者心理狀態；offline next-item accuracy 不能證明 generated vector 真正對應使用者想要或具新穎性的 item。評估只有三個經過篩選的 datasets、排除 cold-start items，且最後仍只從既有 catalog 檢索。作者也警告 oracle embeddings 可能被解碼而洩露使用者偏好，但未實際測試 privacy attacks 或 defenses。

## Notes

- YooChoose contains 128,468 sequences, 9,514 items, and 539,436 interactions.
- KuaiRec contains 92,090 sequences, 7,261 items, and 737,163 interactions.
- Zhihu contains 11,714 sequences, 4,838 items, and 77,712 interactions.
- Baselines use uniform 1:1 negative sampling; DreamRec trains without negative sampling.
- The unconditional-training probability is fixed at 0.1; diffusion steps and guidance strength are tuned.
