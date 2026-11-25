---
date: 2026-11-25
title: "Wyze Rule: Federated Rule Dataset for Rule Recommendation Benchmarking"
authors: "Mohammad Mahdi Kamani, Yuhang Yao, Hanjia Lyu, Zhongwei Cheng, Lin Chen, Liangju Li, Carlee Joe-Wong, Jiebo Luo"
venue: "NeurIPS 2023 Datasets and Benchmarks Track"
---

# Wyze Rule: Federated Rule Dataset for Rule Recommendation Benchmarking

- [Official paper page](https://proceedings.neurips.cc/paper_files/paper/2023/hash/02b9d1e6d1b5295a6f883969ddc1bbbd-Abstract-Datasets_and_Benchmarks.html)
- [Official PDF](https://proceedings.neurips.cc/paper_files/paper/2023/file/02b9d1e6d1b5295a6f883969ddc1bbbd-Paper-Datasets_and_Benchmarks.pdf)
- [Local PDF](../../pdfs/2026-11/2026-11-25-wyze-rule-federated-rule-dataset-for-rule-recommendation-benchmarking.pdf)
- Venue: NeurIPS 2023 Datasets and Benchmarks Track

## English Summary

Wyze Rule benchmarks smart-home automation recommendations using over one million rules from roughly 300,000 users. The anonymized release pairs user-created trigger-action rules with household device inventories. Rules and devices are unevenly distributed across users, creating a non-IID setting for cross-device federated learning. Unlike a flat user-item matrix, a device graph represents each physical device as a separate node, so a model can distinguish two devices of the same type and recommend a rule for the intended pair.

The benchmark ranks held-out rules. In Table 2, centralized GraphRule reaches Hit Rate@50 of 0.9100, versus 0.8445 for graph convolutional matrix completion and 0.8138 for matrix factorization. GraphRule scores 0.6396 when distinguishing multiple instances of the same device type, a case the matrix baselines cannot represent. On the expanded dataset (Tables 3 and 4), positive mean rank is 10.46 for centralized GraphRule, 30.92 for FedRule with FedAvg, and 37.99 with FedGate; lower is better. These results show a ranking gap despite convergence of both federated variants.

Device locations are unavailable, and the dataset does not measure users' acceptance of recommended rules. Recovering a held-out rule therefore does not establish that a recommendation is useful in deployment.

## 繁中摘要

Wyze Rule 是智慧家庭自動化規則的推薦基準，收錄約 30 萬名使用者建立的逾 100 萬條規則。匿名資料包含觸發條件、執行動作，以及使用者擁有的裝置清單。各使用者的裝置組合和規則數量差異大，形成跨裝置聯邦學習中的非獨立同分布（non-IID）情境。相較於把規則當成單一項目的使用者－項目矩陣，裝置圖將每台實體裝置建成獨立節點，因此能辨別同類型的不同裝置，並對指定的裝置組合推薦規則。

實驗以保留的規則做離線排序評估。表 2 中，集中式 GraphRule 的 Hit Rate@50 為 0.9100，高於圖卷積矩陣補全的 0.8445 與矩陣分解的 0.8138；在需區分同類型裝置的情境，GraphRule 為 0.6396，而矩陣方法無法表示這項差異。擴大資料集後（表 3、4），集中式 GraphRule 的正例平均名次為 10.46，FedRule 搭配 FedAvg 與 FedGate 則分別為 30.92 和 37.99（越低越好）。兩種聯邦方法都能收斂，但排序仍落後集中式方法。

資料不包含裝置所在位置，也沒有使用者對推薦規則的採用或滿意度回饋。因此，離線找回保留規則並不能證明推薦在實際家庭中有用。
