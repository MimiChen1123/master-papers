---
date: 2026-09-24
title: "AgentRecBench: Benchmarking LLM Agent-based Personalized Recommender Systems"
authors: "Yu Shang, Peijie Liu, Yuwei Yan, Zijing Wu, Leheng Sheng, Yuanqing Yu, Chumeng Jiang, An Zhang, Fengli Xu, Yu Wang, Min Zhang, Yong Li"
venue: "NeurIPS 2025 Datasets and Benchmarks Track"
---

# AgentRecBench: Benchmarking LLM Agent-based Personalized Recommender Systems

- Paper page: https://proceedings.neurips.cc/paper_files/paper/2025/hash/e2d6f7249add096e26679eade1b4cc6f-Abstract-Datasets_and_Benchmarks_Track.html
- PDF: https://proceedings.neurips.cc/paper_files/paper/2025/file/e2d6f7249add096e26679eade1b4cc6f-Paper-Datasets_and_Benchmarks_Track.pdf
- Local PDF: [../../pdfs/2026-09/2026-09-24-agentrecbench-benchmarking-llm-agent-based-personalized-recommender-systems.pdf](../../pdfs/2026-09/2026-09-24-agentrecbench-benchmarking-llm-agent-based-personalized-recommender-systems.pdf)
- Venue: NeurIPS 2025 Datasets and Benchmarks Track

## English Summary

AgentRecBench is a benchmark for LLM-based recommendation agents that can actively retrieve information before ranking items. Instead of presenting a fixed feature matrix, its textual simulator organizes Yelp, Goodreads, and Amazon data as a navigable User-Review-Item network. Agents can issue standardized user, item, and review queries, choose structured or textual responses, and sort retrieved data by criteria such as time, relevance, or popularity. Scenario-level time and item filters prevent access to information that should be hidden for a particular task.

The benchmark covers three settings. Classic recommendation exposes complete profiles and interaction histories. Evolving-interest recommendation uses three-month and one-week windows to test long- and short-term adaptation. Cold-start tasks select users or items with few interactions to test whether agents can exploit textual context beyond IDs. Each test instance contains 20 candidates: one held-out positive and 19 unobserved negatives. Performance is measured by Hit Rate at 1, 3, and 5. The accompanying modular framework identifies planning, reasoning, tool use, and memory as core components and compares matrix factorization, graph recommenders, simple LLM agents, Agent4Rec, and three top systems from the AgentSociety Challenge.

The results show that agent workflow design matters more than merely adding chain-of-thought or memory. Platform-aware systems such as Baseline666, DummyAgent, and RecHackers substantially outperform the simple BaseAgent variants on Amazon and Goodreads; their key practices are selecting informative historical reviews and engineering platform-specific item attributes. In the evolving-interest tests, the strongest agents are relatively stable and often improve on short-term Amazon and Goodreads tasks. However, agentic methods are not uniformly superior: traditional or graph-based recommenders remain much stronger on several Yelp settings, and simple CoT or memory additions provide little consistent benefit.

The benchmark was used in a 295-team challenge with more than 1,400 submissions, providing evidence that the environment supports iterative system development. Its scope remains limited to textual, single-agent evaluation, and the authors identify multimodal and multi-agent extensions as future work. The fixed 20-candidate, one-positive protocol is also narrower than production retrieval and ranking, so benchmark gains should not be interpreted as direct evidence of online business impact.

## 繁中摘要

AgentRecBench 是針對 LLM 推薦 agent 的評測基準，重點是 agent 能在排序前主動檢索資訊，而不是只能接收固定的特徵矩陣。其文字模擬器把 Yelp、Goodreads 與 Amazon 資料整理成可探索的 User-Review-Item 網路。Agent 可以查詢使用者、物品與評論，選擇結構化或文字格式，並依時間、相關性或熱門度排序結果；scenario 層級的時間與物品過濾則避免 agent 讀到該任務不應取得的資訊。

基準包含三類情境。Classic recommendation 提供完整 profile 與互動歷史；evolving-interest recommendation 以三個月與一週時間窗測試長短期偏好適應；cold-start 則挑選互動很少的使用者或物品，檢驗 agent 能否利用 ID 以外的文字脈絡。每個測試案例有 20 個候選物品，包括 1 個保留的正例與 19 個未觀察負例，指標是 Hit Rate@1、@3、@5。配套的模組化框架把 planning、reasoning、tool use 與 memory 視為核心元件，並比較矩陣分解、圖推薦模型、簡單 LLM agent、Agent4Rec，以及 AgentSociety Challenge 的前三名系統。

結果顯示，完整 workflow 設計比單純加入 chain-of-thought 或 memory 更重要。Baseline666、DummyAgent 與 RecHackers 等具平台感知能力的系統，在 Amazon 與 Goodreads 上明顯優於簡單 BaseAgent 變體；其共同做法包括挑選資訊量高的歷史評論，以及依平台設計物品特徵。在 evolving-interest 測試中，最強 agent 相對穩定，並常在 Amazon 與 Goodreads 的短期任務上提升。不過 agent 並非全面較好：傳統或圖推薦模型在多個 Yelp 設定仍大幅領先，而只增加 CoT 或 memory 也沒有一致收益。

此基準曾用於 295 個團隊、超過 1,400 次提交的競賽，顯示環境可支援反覆開發與比較。目前範圍仍限於文字和單一 agent，作者把多模態與多 agent 列為後續方向。此外，固定 20 個候選、單一正例的評估比實際系統的 retrieval 與 ranking 窄，因此不能直接把 benchmark 提升解讀為線上商業效果。

## Notes

- The released environment unifies user profiles, item metadata, ratings, review text, timestamps, social links, and review-helpfulness signals when available.
- Main-table experiments use Qwen-72B-Instruct, DeepSeek-V3, and GPT-4o-mini, with each experiment repeated five times.
- The benchmark evaluates autonomous information gathering, but its final task is still offline candidate ranking rather than interaction with live users.
