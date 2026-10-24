---
date: 2026-10-24
title: "Adaptive Gradient Masking for Balancing ID and MLLM-based Representations in Recommendation"
authors: "Yidong Wu, Siyuan Chen, Binrui Wu, Fan Li, Jiechao Gao"
venue: "NeurIPS 2025"
---

# Adaptive Gradient Masking for Balancing ID and MLLM-based Representations in Recommendation

- Paper page: https://proceedings.neurips.cc/paper_files/paper/2025/hash/15163b538e6be5446614de2ecbbfa026-Abstract-Conference.html
- PDF: https://proceedings.neurips.cc/paper_files/paper/2025/file/15163b538e6be5446614de2ecbbfa026-Paper-Conference.pdf
- Local PDF: [../../pdfs/2026-10/2026-10-24-adaptive-gradient-masking-for-balancing-id-and-mllm-based-representations-in-recommendation.pdf](../../pdfs/2026-10/2026-10-24-adaptive-gradient-masking-for-balancing-id-and-mllm-based-representations-in-recommendation.pdf)
- Venue: NeurIPS 2025

## English Summary

This paper studies convergence inconsistency when recommendation models jointly train ID features and representations produced by a Multimodal Large Language Model (MLLM). ID embeddings quickly memorize collaborative patterns, while multimodal image and text representations start from a different semantic distribution and converge more slowly. Under ordinary joint training, the fast ID branch can dominate optimization and suppress the multimodal branch, so simply concatenating ID and multimodal features may perform worse than an ID-only model.

The proposed two-stage framework first fine-tunes Qwen2-VL-2B to construct unified multimodal item and user representations. It learns item embeddings from images and text, aggregates a user's interacted items into a user embedding, and post-aligns the multimodal user representation with a pretrained frozen ID embedding. The second stage jointly trains separate ID and multimodal branches using Adaptive Gradient Masking (AGM). AGM estimates each branch's relative contribution for every minibatch, smooths the estimates with an exponential moving average, and combines them with diagonal Fisher information to sample non-uniform gradient masks. The dominant branch consequently updates fewer important parameters, while the lagging branch receives more optimization capacity. Because the mask and stochastic gradient are statistically dependent, the basic AGM estimator is biased; AGM* applies inverse-probability weighting to the retained gradients, yielding an unbiased variant with a stronger convergence guarantee.

Offline experiments cover Amazon Baby, Electronics, Sports, and MicroLens with MLP, DCN, and FiBiNet backbones. AGM* achieves the highest AUC in all 12 dataset-backbone combinations. With MLP, for example, it improves Baby AUC from 0.6741 for ID-only and 0.6719 for naive ID+MM to 0.6864; on Sports, it reaches 0.7145 versus 0.7012 and 0.7072. Against multimodal baselines including VBPR, FREEDOM, BM3, AlignRec, MGCN, LGMRec, GUME, and MM-Rec, AGM* also records the best AUC and LogLoss on all four datasets. Ablations show that both backbone and fusion masking help, with backbone masking contributing most.

The authors further deploy the method on a short-video platform serving hundreds of millions of users. In a 14-day online A/B test, AGM* improves watch time by 0.175%, app usage by 0.124%, and long views by 0.678% over the production baseline, while short views decrease by 0.235%; the full model has since been deployed platform-wide. The method nevertheless adds a two-stage MLLM fine-tuning pipeline, Fisher-based importance estimation, and masking logic to training. Its effectiveness also depends on the quality and diversity of available multimodal content, and the paper evaluates broader applicability only within recommendation scenarios.

## 繁中摘要

這篇論文研究推薦模型同時訓練 ID features 與 Multimodal Large Language Model（MLLM）representations 時的 convergence inconsistency。ID embeddings 能快速記憶 collaborative patterns；影像與文字的 multimodal representations 則來自不同的 semantic distribution，收斂速度較慢。在一般 joint training 下，較快的 ID branch 容易主導最佳化並壓制 multimodal branch，因此直接串接 ID 與 multimodal features，表現甚至可能低於只使用 ID 的模型。

作者提出兩階段 framework。第一階段 fine-tune Qwen2-VL-2B，以影像和文字建立統一的 multimodal item representations，再聚合使用者互動過的 items 形成 user embedding，並將 multimodal user representation 與預先訓練且凍結的 ID embedding 做 post-alignment。第二階段分別保留 ID 與 multimodal branches，並以 Adaptive Gradient Masking（AGM）共同訓練。AGM 在每個 minibatch 估計兩個 branches 的相對貢獻，以 exponential moving average 平滑估計，再結合 diagonal Fisher information 非均勻地抽樣 gradient masks。主導 branch 因此只更新較少的重要參數，落後 branch 則獲得更多最佳化空間。由於 mask 與 stochastic gradient 並不獨立，基本 AGM 的估計存在 bias；AGM* 對保留的 gradients 使用 inverse-probability weighting，得到 unbiased estimator 與更強的 convergence guarantee。

離線實驗涵蓋 Amazon Baby、Electronics、Sports 與 MicroLens，並使用 MLP、DCN、FiBiNet 三種 backbones。AGM* 在 12 個 dataset-backbone 組合的 AUC 全部最高。例如使用 MLP 時，Baby 的 AUC 從 ID-only 的 0.6741、naive ID+MM 的 0.6719 提升到 0.6864；Sports 則由 0.7012、0.7072 提升到 0.7145。與 VBPR、FREEDOM、BM3、AlignRec、MGCN、LGMRec、GUME、MM-Rec 等 multimodal baselines 比較時，AGM* 在四個 datasets 的 AUC 與 LogLoss 也全部最佳。Ablation 顯示 backbone masking 與 fusion masking 都有效，其中 backbone masking 的影響最大。

作者也把方法部署到服務數億使用者的短影音平台。在 14 天 online A/B test 中，相較 production baseline，AGM* 讓 watch time 提升 0.175%、app usage 提升 0.124%、long views 提升 0.678%，同時 short views 下降 0.235%；完整模型其後已全面部署。代價是訓練流程增加兩階段 MLLM fine-tuning、Fisher-based importance estimation 與 masking logic。方法成效也依賴 multimodal content 的品質與多樣性，而論文尚未驗證 recommendation 以外的應用是否能直接沿用。

## Notes

- The MLLM backbone is Qwen2-VL-2B; the representation-learning stage is fine-tuned for five epochs on four A100 GPUs.
- Offline evaluation uses Amazon Baby, Electronics, Sports, and MicroLens; AGM training is reported with TensorFlow 2.15 on one RTX 4090.
- AGM* is consistently but modestly better than biased AGM, supporting the inverse-probability correction.
- The online deployment reports engagement changes rather than ranking metrics, and the paper does not disclose the platform or absolute traffic allocation.
