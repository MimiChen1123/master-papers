---
date: 2026-11-04
title: "TV-Rec: Time-Variant Convolutional Filter for Sequential Recommendation"
authors: "Yehjin Shin, Jeongwhan Choi, Seojin Kim, Noseong Park"
venue: "NeurIPS 2025"
---

# TV-Rec: Time-Variant Convolutional Filter for Sequential Recommendation

- Paper page: https://proceedings.neurips.cc/paper_files/paper/2025/hash/ed31c00af5238b649171d64718c92cb2-Abstract-Conference.html
- PDF: https://proceedings.neurips.cc/paper_files/paper/2025/file/ed31c00af5238b649171d64718c92cb2-Paper-Conference.pdf
- Local PDF: [../../pdfs/2026-11/2026-11-04-tv-rec-time-variant-convolutional-filter-for-sequential-recommendation.pdf](../../pdfs/2026-11/2026-11-04-tv-rec-time-variant-convolutional-filter-for-sequential-recommendation.pdf)
- Code: https://github.com/yehjin-shin/TV-Rec
- Venue: NeurIPS 2025

## English Summary

Sequential recommenders must capture both recent actions and long-range preferences. Conventional convolution applies the same kernel at every sequence position, which provides a useful locality bias but can miss patterns that change over time. Self-attention models global dependencies but has quadratic sequence interaction costs and normally requires explicit positional information. TV-Rec addresses this trade-off with time-variant graph convolutional filters: each position receives a different filter, allowing the model to represent both position-specific behavior and global dependencies without self-attention.

TV-Rec treats padded sequence positions, rather than items, as nodes of a directed cycle graph and transforms their embeddings with a graph Fourier transform. A learned coefficient matrix combines normalized basis vectors to construct a separate spectral filter for each position. Stacked filter and feed-forward blocks then produce the representation used for next-item scoring. Because the graph spectrum and position-specific operation already encode order, the model does not use positional embeddings; the ablation study finds that adding them does not consistently help. The resulting filter is a linear operator that can be precomputed after training, reducing inference-time filtering to O(n^2 d), although filter construction and graph transforms add training work.

The authors evaluate TV-Rec on Beauty, Sports, Yelp, LastFM, MovieLens-1M, and Foursquare using HR and NDCG over the full item set without negative sampling. With maximum sequence length 50, TV-Rec is best on every reported metric and improves over the strongest baseline by 7.49% on average. Gains are especially large on LastFM (19.13% HR@10 and 18.34% NDCG@10) and Foursquare (22.17% and 23.85%), while improvements on Beauty and Sports are smaller but consistent. At sequence length 200, it also leads all metrics on MovieLens-1M and Foursquare, with an average 4.74% gain and an 11.27% improvement on Foursquare NDCG@20. Ten-seed comparisons against each dataset's strongest baseline support the reported advantage.

Runtime measurements show competitive training cost and generally low inference cost relative to attention-based and hybrid baselines; FMLPRec is slightly faster on several datasets but substantially less accurate. Important limitations remain. TV-Rec pads a line graph into a directed cycle graph and repeatedly performs graph transforms during training, increasing time and memory. Its filters depend on temporal position rather than sequence content, so they may not adapt to user-specific or irregular behavior. The evidence is limited to public offline benchmarks, and interaction logs still introduce privacy, bias, and diversity risks that faster inference alone does not address.

## 繁中摘要

Sequential recommender 必須同時捕捉近期行為與長期偏好。傳統 convolution 在每個 sequence position 使用相同 kernel，雖然具有良好的 locality bias，卻可能忽略隨時間位置改變的模式；self-attention 能建模全域依賴，但 sequence interaction cost 為平方級，通常也需要額外的 positional information。TV-Rec 以 time-variant graph convolutional filters 處理這項取捨：每個位置使用不同濾波器，因此能在不依賴 self-attention 的情況下，同時表示位置特定行為與全域依賴。

TV-Rec 將 padding 後的 sequence positions 而非 items 視為 directed cycle graph 的節點，並透過 graph Fourier transform 轉換 embeddings。模型以 learned coefficient matrix 組合 normalized basis vectors，為每個位置建立獨立的 spectral filter，再堆疊 filter、feed-forward 與 residual blocks，產生 next-item scoring 所需的表示。由於 graph spectrum 與 position-specific operation 本身已編碼順序，模型不使用 positional embeddings；ablation study 也顯示加入 positional embeddings 沒有一致效益。濾波器是 linear operator，訓練完成後可預先計算，使 inference-time filtering 降為 O(n^2 d)，但 filter construction 和 graph transforms 仍會增加訓練成本。

作者在 Beauty、Sports、Yelp、LastFM、MovieLens-1M 與 Foursquare 上，以完整 item set、無 negative sampling 的 HR 和 NDCG 評估模型。最大 sequence length 為 50 時，TV-Rec 在所有回報指標上皆為最佳，對各資料集最強 baseline 的平均相對提升為 7.49%。LastFM 的 HR@10 與 NDCG@10 分別提升 19.13% 和 18.34%，Foursquare 則提升 22.17% 和 23.85%；Beauty 與 Sports 的增幅較小，但仍一致為正。將 sequence length 提高至 200 後，TV-Rec 在 MovieLens-1M 和 Foursquare 的所有指標仍居首，平均提升 4.74%，其中 Foursquare NDCG@20 提升 11.27%。作者另以十個 random seeds 比較各資料集最強 baseline，結果仍支持其優勢。

Runtime measurements 顯示 TV-Rec 的 training cost 具有競爭力，inference cost 通常也低於 attention-based 與 hybrid baselines；FMLPRec 在數個資料集稍快，但準確度明顯較低。模型仍有重要限制：TV-Rec 將 line graph padding 成 directed cycle graph，訓練期間也反覆執行 graph transforms，因此增加時間與記憶體需求。濾波器只依賴 temporal position、不依賴 sequence content，可能難以適應 user-specific 或不規則行為。目前證據僅來自公開資料集的 offline evaluation；使用 interaction logs 也仍有 privacy、bias 與 diversity 風險，這些問題不會因 inference 變快而消失。

## Notes

- Standard experiments truncate or pad histories to 50 positions; long-range experiments use 200 positions on MovieLens-1M and Foursquare.
- Metrics are HR@5/10/20 and NDCG@5/10/20 over the entire item catalog, without sampled negatives.
- The comparison includes CNN, RNN, Transformer, Fourier-filtering, recurrent, hybrid, and GNN-based sequential recommenders.
- Ablations support the time-variant filter, learned normalized basis, and omission of positional embeddings.
