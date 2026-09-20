---
date: 2026-09-20
title: "Algorithmic Collective Action in Recommender Systems: Promoting Songs by Reordering Playlists"
authors: "Joachim Baumann, Celestine Mendler-Dünner"
venue: "NeurIPS 2024"
---

# Algorithmic Collective Action in Recommender Systems: Promoting Songs by Reordering Playlists

- Paper page: https://proceedings.neurips.cc/paper_files/paper/2024/hash/d79792543133425ff79513c147dc8881-Abstract-Conference.html
- PDF: https://proceedings.neurips.cc/paper_files/paper/2024/file/d79792543133425ff79513c147dc8881-Paper-Conference.pdf
- Local PDF: [../../pdfs/2026-09/2026-09-20-algorithmic-collective-action-in-recommender-systems-promoting-songs-by-reordering-playlists.pdf](../../pdfs/2026-09/2026-09-20-algorithmic-collective-action-in-recommender-systems-promoting-songs-by-reordering-playlists.pdf)
- Venue: NeurIPS 2024

## English Summary

This paper studies algorithmic collective action in a transformer-based music recommender: a group of fans coordinates to increase the visibility of an underrepresented artist by inserting one target song into playlists they already control. Unlike conventional shilling or poisoning attacks, the proposed actions must satisfy an authenticity constraint: each playlist may undergo only one edit, preserving its normal use. The strategies require no access to model weights and rely only on the recommender's tendency to learn sequential co-occurrence patterns and on aggregate song-frequency statistics.

The authors propose two insertion strategies. InClust concentrates the collective's effort around common contexts by repeatedly finding songs frequent within the collective's playlists and inserting the target immediately before those anchors. DirLoF exploits the long tail by finding globally rare anchor songs and inserting the target immediately after them, where a small amount of coordinated data can overpower weak existing signals. A hybrid uses InClust where an anchor has enough collective support and DirLoF elsewhere. Effectiveness is measured by amplification: the increase in test-time recommendation probability divided by the fraction of training playlists modified. Values above one mean the collective receives disproportionate influence relative to its data contribution.

The experiments train Deezer's public transformer-based automatic playlist continuation model on the Spotify Million Playlist Dataset, using 980,000 training playlists and five-fold evaluation. Tiny collectives can have large effects: at a collective size of 0.025% of playlists, DirLoF reaches amplification near 25, producing up to 40 times as many recommendations as a naturally occurring song with comparable training frequency. For larger groups, InClust becomes stronger and reaches amplification around 10 at a 2% share. Approximate popularity statistics are sufficient: current scraped stream counts retain more than 85% of full-information amplification for a 1% collective despite the dataset's age. Externality analysis finds only marginal aggregate quality loss, largely stable recommendations for participants, and no clear concentration of displaced exposure on a particular artist group. However, the same mechanism could be used by wealthy or already-popular actors, so favorable outcomes depend on incentives, coordination, and platform governance rather than on the technical strategy alone.

## 繁中摘要

這篇論文研究 transformer 音樂推薦系統中的演算法集體行動：一群粉絲透過協調，把同一首目標歌曲插入自己原本就擁有的播放清單，以提高弱勢或新興藝人的曝光。與一般 shilling 或資料 poisoning attack 不同，作者要求行動符合真實性限制：每份播放清單最多只進行一次編輯，因此仍可維持原本用途。這些策略不需要取得模型權重，只依賴推薦器會學習序列共現關係的特性，以及彙總後的歌曲出現頻率。

作者提出兩種插入策略。InClust 會把集體力量集中在常見情境：反覆找出集體播放清單中高頻的歌曲，並把目標歌曲插在這些 anchor 之前。DirLoF 則利用長尾分布，找出全體資料中低頻的 anchor 歌曲，把目標歌曲插在其後；因為原本訊號很弱，少量協調資料便可能取得主導地位。混合策略會在 anchor 獲得足夠集體支持時使用 InClust，其餘播放清單使用 DirLoF。論文以 amplification 衡量效果，也就是測試時推薦機率的增量除以被修改的訓練播放清單比例；若大於一，代表集體取得的影響力超過其資料貢獻比例。

實驗使用 Spotify Million Playlist Dataset，訓練 Deezer 公開的 transformer 自動播放清單續播模型，以 980,000 份清單訓練並進行五折評估。即使很小的集體也能產生顯著效果：當集體只控制 0.025% 播放清單時，DirLoF 的 amplification 接近 25，推薦次數最多可達訓練頻率相近之自然歌曲的 40 倍。集體較大時 InClust 更有效，在控制 2% 清單時 amplification 約為 10。策略不需要精確的完整資料統計；即使資料集較舊，使用目前抓取的串流次數作為近似值，1% 集體仍能保留完整資訊情境下超過 85% 的效果。外部性分析顯示，整體推薦品質只小幅下降，參與者收到的推薦大致穩定，被取代的曝光也沒有明顯集中傷害特定藝人群體。不過，相同機制也可能被資源雄厚或原本就受歡迎的參與者利用，因此是否帶來公平結果，仍取決於誘因、協調方式與平台治理，而不是技術策略本身。

## Notes

- The Spotify Million Playlist Dataset contains one million playlists with an average length of 66.35 tracks and songs from nearly 300,000 artists.
- Each strategy inserts exactly one target song per controlled playlist, satisfying an edit-distance-at-most-one authenticity constraint.
- The experiments vary collective control from 0.001% to 2% of training data; the paper separately discusses even smaller illustrative settings and reports bootstrapped 95% confidence intervals over five folds.
