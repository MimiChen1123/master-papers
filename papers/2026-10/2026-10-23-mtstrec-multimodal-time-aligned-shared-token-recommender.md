---
date: 2026-10-23
title: "MTSTRec: Multimodal Time-Aligned Shared Token Recommender"
authors: "Ming-Yi Hong, Yen-Jung Hsu, Miao-Chen Chiang, Che Lin"
venue: "ICML 2025"
---

# MTSTRec: Multimodal Time-Aligned Shared Token Recommender

- Paper page: https://proceedings.mlr.press/v267/hong25b.html
- PDF: https://raw.githubusercontent.com/mlresearch/v267/main/assets/hong25b/hong25b.pdf
- Local PDF: [../../pdfs/2026-10/2026-10-23-mtstrec-multimodal-time-aligned-shared-token-recommender.pdf](../../pdfs/2026-10/2026-10-23-mtstrec-multimodal-time-aligned-shared-token-recommender.pdf)
- Venue: ICML 2025

## English Summary

MTSTRec addresses multimodal sequential recommendation in e-commerce. Item-ID recommenders such as SASRec and BERT4Rec model behavioral order but omit product content, while common early-fusion methods merge heterogeneous features too soon and late-fusion methods postpone cross-modal interaction until after sequence encoding. The paper argues that product ID, visual style, text, LLM-generated text, and price should retain modality-specific representations while exchanging information at the matching product position in a user's browsing sequence.

The feature extractors map IDs and normalized prices to embeddings, describe image style with VGG-19 Gram matrices, encode product titles and descriptions with Llama 3.1, and generate five prompt-based textual views with a gated combination. Separate self-attention encoders first process each modality. The Time-aligned Shared Token (TST) module then inserts one shared token for every product position; modality tokens attend to the shared token at the same time step, and shared tokens interact across the sequence and fusion layers. This mid-fusion design allows cross-modal exchange without collapsing each modality's specialized features or losing chronological correspondence.

Experiments use Food E-commerce, House-Hold E-commerce, and H&M Trousers, ranging from 12,345 to 416,794 sessions and from 94,984 to 3,576,972 actions. Sessions are split chronologically 75/12.5/12.5 for training, validation, and testing; sequences are capped at 20 products, and evaluation ranks each target against 100 sampled negatives. MTSTRec leads all baselines on every reported NDCG, hit-rate, and MRR metric. Its NDCG@5 is 0.8800 on Food, 0.8942 on House-Hold, and 0.2307 on H&M, compared with the strongest baseline values of 0.8512, 0.8401, and 0.1754. Direct ablations also favor TST over early and late fusion: on Food, NDCG@5 falls from 0.8800 to 0.8621 and 0.8211, respectively.

The modality ablations show that item identity and text are the strongest signals: removing IDs lowers Food NDCG@5 to 0.7582, while removing both original and prompted text lowers House-Hold NDCG@5 to 0.8191. Price and image-style features contribute little on those two datasets, and removing IDs actually improves H&M NDCG@5 from 0.2307 to 0.2724, indicating that content features help when the item catalog is larger and near-duplicate product IDs are sparse. Important limitations are the sampled-negative rather than full-catalog evaluation, two datasets originating from one commercial provider, and no online or cross-domain deployment study. MTSTRec also trades efficiency for accuracy on House-Hold: it has 59.24M parameters, trains for 83 minutes, and takes 12.43 seconds for inference, slower than all listed baselines despite being smaller than several multimodal models. The authors additionally flag possible amplification of multimodal bias and privacy risks in product and interaction data.

## 繁中摘要

MTSTRec 處理電商中的 multimodal sequential recommendation。SASRec、BERT4Rec 等 item-ID recommenders 能建模行為順序，卻缺少商品內容；常見 early fusion 太早合併異質 features，late fusion 則到 sequence encoding 完成後才讓 modalities 互動。論文主張 product ID、visual style、text、LLM-generated text 與 price 應保留各自的 representations，同時只在 browsing sequence 中相同商品位置交換資訊。

Feature extractors 將 IDs 與 normalized prices 轉成 embeddings，以 VGG-19 Gram matrices 描述 image style，用 Llama 3.1 編碼商品 title/description，並透過 gating 合併五種 prompt-generated textual views。各 modality 先由獨立的 self-attention encoder 處理；Time-aligned Shared Token（TST）module 再為每個商品位置加入一個 shared token。Modality tokens 會 attention 到同一時間步的 shared token，而 shared tokens 也會跨 sequence positions 與 fusion layers 互動。這種 mid-fusion 能交換跨模態資訊，同時避免抹平 modality-specific features 或破壞 chronological correspondence。

實驗使用 Food E-commerce、House-Hold E-commerce 與 H&M Trousers，規模從 12,345 到 416,794 sessions、94,984 到 3,576,972 actions。Sessions 依時間切成 75/12.5/12.5 的 train、validation、test，sequence 最長 20 個 products；評估時每個 target 與 100 個 sampled negatives 排名。MTSTRec 在所有回報的 NDCG、hit rate、MRR metrics 都領先 baselines。Food、House-Hold、H&M 的 NDCG@5 分別為 0.8800、0.8942、0.2307，而最佳 baseline 分別為 0.8512、0.8401、0.1754。Fusion ablations 也支持 TST：Food 的 NDCG@5 在改為 early fusion、late fusion 後，分別由 0.8800 降至 0.8621、0.8211。

Modality ablations 顯示 item identity 與 text 是最強 signals：移除 IDs 會讓 Food NDCG@5 降至 0.7582；同時移除原始與 prompted text，House-Hold NDCG@5 會降至 0.8191。Price 與 image-style features 在這兩個 datasets 的貢獻較小；H&M 移除 IDs 後，NDCG@5 反而從 0.2307 升至 0.2724，表示 catalog 較大、近似商品 IDs 稀疏時，content features 更重要。限制包括使用 sampled-negative 而非 full-catalog evaluation、兩個 datasets 來自同一商業資料提供者，以及缺乏 online 或 cross-domain deployment study。MTSTRec 也以效率換取準確率：在 House-Hold 上有 59.24M parameters、訓練 83 分鐘、inference 12.43 秒，雖然比多個 multimodal models 小，速度卻慢於所有列出的 baselines。作者也提醒 multimodal bias 可能被放大，以及商品與互動資料存在 privacy risks。

## Notes

- Official code and released datasets: https://github.com/idssplab/MTSTRec
- The model uses five modalities: item ID, image style, original text, prompt-generated text, and price.
- Food and House-Hold sessions contain historical page views followed by a multi-item purchase order; H&M uses purchases from the final day as the multi-label target.
- The one-shared-token-per-time-step configuration performs slightly better than using two or four shared tokens or global fusion bottlenecks.
