---
date: 2026-10-11
title: "SecEmb: Sparsity-Aware Secure Federated Learning of On-Device Recommender System with Large Embedding"
authors: "Peihua Mai, Youlong Ding, Ziyan Lyu, Minxin Du, Yan Pang"
venue: "ICML 2025"
---

# SecEmb: Sparsity-Aware Secure Federated Learning of On-Device Recommender System with Large Embedding

- Paper page: https://proceedings.mlr.press/v267/mai25a.html
- PDF: https://raw.githubusercontent.com/mlresearch/v267/main/assets/mai25a/mai25a.pdf
- Local PDF: [../../pdfs/2026-10/2026-10-11-secemb-sparsity-aware-secure-federated-learning-of-on-device-recommender-system-with-large-embedding.pdf](../../pdfs/2026-10/2026-10-11-secemb-sparsity-aware-secure-federated-learning-of-on-device-recommender-system-with-large-embedding.pdf)
- Venue: ICML 2025

## English Summary

Federated recommender systems keep user interactions on edge devices, but conventional secure aggregation still requires each device to download the full model and upload a full-sized masked update. This is particularly expensive when item embeddings dominate the model. SecEmb exploits the fact that each user interacts with only a small fraction of all items, so the item-embedding gradient is row-sparse. Its goal is to make client communication and computation depend on the number of relevant items rather than the full catalog while hiding both the rated item indices and individual gradient values from the servers.

SecEmb combines two protocols based on function secret sharing (FSS) and two non-colluding servers. In private embedding retrieval, a client encodes each rated item index as a distributed point function; each server evaluates its key against the embedding table and returns a share, allowing the client to reconstruct only the needed rows without revealing their indices. For upload, each non-zero embedding-gradient row is encoded as another point function, and the servers aggregate their shares before reconstructing only the summed update. Row-wise encoding reduces one key per embedding coordinate to one key per updated item, while reusing the FSS tree path between retrieval and aggregation removes repeated key material and pseudorandom operations. With a padded, predetermined update count, each server learns neither a client's rated-item set nor its number of rated items, beyond the final aggregate.

Experiments cover ML100K, ML1M, ML10M, ML25M, and Yelp with MF, NCF, FM, and DeepFM, plus Caser and SASRec on sequential recommendation. Relative to secure FedRec, SecEmb reduces upload and download traffic by roughly 4x to 90x for sparse latent-factor models and lowers client-side secret-generation time by as much as 70x; savings grow with catalog size. On Amazon sequential recommendation, upload reduction exceeds 2,300x because the catalog contains over nine million items. Unlike quantization or low-rank compression, SecEmb is lossless and therefore avoids their average utility degradation. The tradeoffs are important: security assumes two non-colluding servers, FSS evaluation shifts work to the servers, users must pad or truncate updates to a common size, and the largest benefits require item embeddings to dominate the model and per-user updates to remain sparse. Differential privacy is compatible but optional, so the base protocol protects individual updates during aggregation rather than making the released aggregate itself differentially private.

## 繁中摘要

Federated recommender system 能讓 user interactions 保留在 edge devices，但傳統 secure aggregation 仍要求每台裝置下載完整模型，並上傳與完整模型等大的 masked update。當 item embeddings 佔據大部分參數時，這會造成嚴重的通訊、記憶體與計算負擔。SecEmb 利用每位使用者只與全部 items 中一小部分互動的特性，因此 item-embedding gradient 其實是 row-sparse。它的目標是讓 client 成本取決於相關 items 的數量，而不是完整 catalog 大小，同時不向 server 洩漏 rated item indices 或個別 gradient values。

SecEmb 由 function secret sharing（FSS）與兩台不串通的 servers 組成兩個協定。在 private embedding retrieval 中，client 把每個 rated item index 編碼成 distributed point function；兩台 server 各自以 secret key 對 embedding table 求值並回傳 share，使 client 只能重建需要的 embedding rows，而 server 不知道其 indices。上傳時，每個 non-zero embedding-gradient row 也被編碼成 point function，servers 先聚合 shares，最後只重建總和更新。Row-wise encoding 把「每個 embedding coordinate 一把 key」縮減成「每個 updated item 一把 key」；retrieval 與 aggregation 共用 FSS tree path，則進一步移除重複 key material 與 pseudorandom operations。若以預先指定的 update count 做 padding，單一 server 除了最終 aggregate 外，無法得知 client 的 rated-item set 或實際互動數量。

實驗涵蓋 ML100K、ML1M、ML10M、ML25M、Yelp，以及 MF、NCF、FM、DeepFM，另以 Caser 和 SASRec 驗證 sequential recommendation。相較 secure FedRec，對 sparse latent-factor models 而言，SecEmb 可把 upload/download traffic 降低約 4 到 90 倍，client 產生 secret shares 的時間最多降低 70 倍，而且 catalog 越大，效益越明顯。在擁有超過九百萬 items 的 Amazon sequential recommendation 上，upload reduction 超過 2,300 倍。SecEmb 不同於 quantization 或 low-rank compression，是 lossless protocol，因此不會承受這些方法的平均 utility degradation。不過，它依賴兩台 servers 不串通的假設，FSS evaluation 會把部分計算成本轉移到 server，使用者必須把 updates pad 或 truncate 到共同大小，而且只有在 item embeddings 主導模型且每位使用者更新持續稀疏時，效益才最大。Differential privacy 可以額外整合但不是預設，因此 base protocol 保護的是 aggregation 過程中的個別 updates，而非讓發布的 aggregate 自動具備 differential privacy。

## Notes

- Code: https://github.com/NusIoraPrivacy/SecEmb
- The security parameter is 128 bits, and the main utility experiments report the mean and standard deviation of four runs.
- The appendix also evaluates differential privacy, memory and storage savings, server computation, sparse aggregation baselines, and dynamic user-item interactions.
