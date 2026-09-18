---
date: 2026-09-18
title: "On Softmax Direct Preference Optimization for Recommendation"
authors: "Yuxin Chen, Junfei Tan, An Zhang, Zhengyi Yang, Leheng Sheng, Enzhi Zhang, Xiang Wang, Tat-Seng Chua"
venue: "NeurIPS 2024"
---

# On Softmax Direct Preference Optimization for Recommendation

- Paper page: https://proceedings.neurips.cc/paper_files/paper/2024/hash/30732ddb12d9faf7180f5d0e8b5b5da7-Abstract-Conference.html
- PDF: https://proceedings.neurips.cc/paper_files/paper/2024/file/30732ddb12d9faf7180f5d0e8b5b5da7-Paper-Conference.pdf
- Local PDF: [../../pdfs/2026-09/2026-09-18-on-softmax-direct-preference-optimization-for-recommendation.pdf](../../pdfs/2026-09/2026-09-18-on-softmax-direct-preference-optimization-for-recommendation.pdf)
- Venue: NeurIPS 2024

## English Summary

This paper argues that the standard language-modeling objective used by many LM-based sequential recommenders is mismatched with the ranking objective of recommendation. Training a model to generate only the positive item's title does not explicitly teach it to prefer that item over alternatives. The authors therefore introduce Softmax Direct Preference Optimization (S-DPO), a preference-alignment stage that pairs each user-history prompt with one positive item and multiple sampled negative items.

S-DPO generalizes pairwise DPO from the Bradley-Terry model to a Plackett-Luce formulation for partial rankings, where the observed constraint is that the positive item should outrank every sampled negative while the relative order among negatives is unspecified. The resulting softmax-style objective reduces to ordinary DPO when there is only one negative. The paper also connects DPO to BPR and S-DPO to sampled softmax loss. Its gradient analysis shows that negatives receiving higher implicit rewards receive larger weights, so the objective automatically emphasizes hard negatives while increasing the likelihood of the preferred item.

Experiments use Llama2-7B and three sequential recommendation datasets: MovieLens-100K, Goodreads, and LastFM. After supervised fine-tuning, S-DPO adds three epochs of preference training. Evaluated by selecting the correct item from a 21-item candidate set, S-DPO achieves the best HR@1 on all three datasets and improves over the second-best baseline by 11.10% to 47.03%, while maintaining a high valid-response ratio. Ablations show that pairwise DPO improves over supervised fine-tuning and that adding more negatives further improves accuracy, accelerates loss reduction, and yields stronger preferred-item rewards. S-DPO also processes multiple negatives more efficiently than independently applying pairwise DPO to each negative. Important limitations are that experiments use at most 15 negatives, larger negative sets increase LM training cost, and the random candidate-set HR@1 evaluation does not directly measure full-catalog ranking quality.

## 繁中摘要

這篇論文指出，許多基於語言模型的序列推薦器使用標準語言建模目標，但這個目標與推薦所需的排序目標並不一致。只訓練模型生成正樣本物品的名稱，並不會明確教導模型應該把該物品排在其他候選物品之前。作者因此提出 Softmax Direct Preference Optimization（S-DPO），在監督式微調之後加入偏好對齊階段，將每個使用者歷史提示與一個正樣本及多個抽樣負樣本配對。

S-DPO 將以 Bradley-Terry 模型為基礎的成對 DPO，推廣成適用於部分排序的 Plackett-Luce 形式。觀測到的限制只有正樣本必須高於所有負樣本，負樣本之間不需要指定順序。由此得到的 softmax 型目標，在只有一個負樣本時會退化成一般 DPO。論文也建立了 DPO 與 BPR、S-DPO 與負樣本 softmax loss 之間的關係。梯度分析顯示，隱含獎勵較高的負樣本會得到較大的權重，因此模型會自動聚焦較難區分的負樣本，同時提高偏好物品的生成機率。

實驗以 Llama2-7B 為骨幹，使用 MovieLens-100K、Goodreads 與 LastFM 三個序列推薦資料集。完成監督式微調後，再進行三個 epoch 的 S-DPO 偏好訓練。在從 21 個候選物品中找出正確物品的評估設定下，S-DPO 在三個資料集的 HR@1 都排名第一，相較第二佳方法提升 11.10% 至 47.03%，同時維持很高的有效回覆比例。消融實驗顯示，成對 DPO 已優於單純監督式微調，而加入更多負樣本還能繼續提高準確率、加快 loss 下降，並為偏好物品產生更強的獎勵；相較於對每個負樣本各自執行成對 DPO，S-DPO 處理多個負樣本也更有效率。主要限制是實驗最多只測到 15 個負樣本，負樣本數增加仍會提高語言模型訓練成本，而且隨機候選集上的 HR@1 並不能直接代表完整物品庫的排序品質。

## Notes

- Main-dataset statistics: MovieLens has 943 sequences and 1,682 items; Goodreads has 6,031 sequences and 4,500 items; LastFM has 1,220 sequences and 4,606 items.
- The main experiments use four NVIDIA A100 GPUs, Llama2-7B, three preference-training epochs, and three to five negatives selected by validation.
- The temperature-like parameter beta balances preference signals against staying close to the reference model; the paper uses beta = 1 after observing that values that are too small or too large hurt performance.
