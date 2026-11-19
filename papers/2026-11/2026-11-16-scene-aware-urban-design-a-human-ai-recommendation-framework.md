---
date: 2026-11-16
title: "Scene-Aware Urban Design: A Human-AI Recommendation Framework Using Co-Occurrence Embeddings and Vision-Language Models"
authors: "Rodrigo A. Gallardo, Alexander Htet Kyaw, Oz Fishman"
venue: "NeurIPS 2025 Creative AI Track"
---

# Scene-Aware Urban Design: A Human-AI Recommendation Framework Using Co-Occurrence Embeddings and Vision-Language Models

- Paper page: https://proceedings.neurips.cc/paper_files/paper/2025/hash/bf24636574309c92f5ea2b0c55e8c23a-Abstract-Creative_AI_Track.html
- PDF: https://proceedings.neurips.cc/paper_files/paper/2025/file/bf24636574309c92f5ea2b0c55e8c23a-Paper-Creative_AI_Track.pdf
- Local PDF: [../../pdfs/2026-11/2026-11-16-scene-aware-urban-design-a-human-ai-recommendation-framework.pdf](../../pdfs/2026-11/2026-11-16-scene-aware-urban-design-a-human-ai-recommendation-framework.pdf)
- Venue: NeurIPS 2025 Creative AI Track

## English Summary

This paper presents a human-in-the-loop recommendation workflow for proposing small urban design interventions, such as adding a bench, tree, sign, bike rack, or shade structure to a public space. Its goal is not to automate planning, but to help residents explore locally grounded options while retaining control over selection and refinement. The system combines empirical object co-occurrence, vision-language reasoning, and text-to-3D generation in a staged interface.

The pipeline first filters ADE20K scenes for urban categories and visible pedestrian activity, then uses open-vocabulary Grounding DINO detections to build a symmetric object co-occurrence matrix. Each row is normalized into a conditional probability vector, so an anchor object chosen by the user can retrieve five frequently co-occurring complements. These vectors are empirical contextual embeddings rather than representations learned by backpropagation. After the user selects one complement, a vision-language model receives the scene, object crops and bounding boxes, and a compact scene description. It proposes five additional objects with materials, dimensions, colors, placement cues, and justifications, while feasibility filters remove options unsupported by the visible environment.

The final stage converts a selected recommendation into a structured prompt for the Meshy text-to-3D API, normalizes the generated mesh to real-world scale, and prepares a low-polygon version for augmented reality. Pilot examples show intuitive statistical associations, such as benches with trees, signs, and lamp posts, while the vision-language stage proposes more scene-specific objects such as kiosks, bus stops, and wayfinding signs. The paper also reports failures: Grounding DINO confuses objects in cluttered scenes, the VLM can produce near-duplicate or policy-sensitive suggestions, and generated meshes sometimes omit requested geometry.

The evidence is exploratory rather than a controlled recommender-system evaluation. The paper provides interface demonstrations and qualitative examples, but no user study, ranking metric, comparison baseline, or measured effect on civic decisions. The main text says the filtering process yields about 900 images, while the appendix describes a curated subset of about 300 scenes, an internal reporting inconsistency. More fundamentally, 2D co-occurrence does not encode real 3D proximity, ADE20K has geographic and cultural biases, and visual models lack legal, accessibility, traffic, utility, terrain, and budget information. The authors therefore position participatory evaluation, diverse data, 3D scene understanding, and post-deployment feedback as future work.

## 繁中摘要

這篇論文提出一個 human-in-the-loop 推薦流程，用來協助居民構想公共空間中的小尺度城市設計介入，例如增加長椅、樹木、標誌、自行車架或遮蔭設施。系統目的不是自動取代規劃工作，而是讓使用者在保有選擇與修改權的情況下，探索與現場情境相關的方案。整體流程結合物件 co-occurrence、vision-language reasoning 與 text-to-3D generation。

系統先從 ADE20K 篩選城市場景與具有明顯行人活動的影像，再利用 open-vocabulary Grounding DINO 偵測物件，建立對稱的 object co-occurrence matrix。每一列正規化為 conditional probability vector；當使用者指定 anchor object 後，系統會取回五個常共同出現的互補物件。這些向量是從真實影像統計得到的 contextual embeddings，而不是透過 backpropagation 學習。使用者選定其中一個物件後，vision-language model 會接收完整場景、物件裁切與 bounding boxes，以及簡短場景描述，再提出五個候選物件，包含材質、尺寸、顏色、位置提示與理由；feasibility filters 會排除影像條件不支持的選項。

最後，系統把選定建議轉成結構化 prompt，交給 Meshy text-to-3D API 產生模型，再進行真實尺度正規化並建立適合 AR 的 low-poly 版本。Pilot examples 顯示，統計層能找出長椅與樹、標誌、路燈等直觀關係，而 VLM 層則能提出 kiosk、bus stop、wayfinding sign 等更依賴場景的建議。論文也記錄多種失敗：Grounding DINO 在雜亂場景會混淆物件，VLM 偶爾產生近似重複或涉及政策敏感性的選項，3D mesh 也可能遺漏 prompt 指定的幾何細節。

目前證據仍屬探索性展示，而不是完整的 recommender-system evaluation。論文沒有 user study、ranking metric、comparison baseline，也未衡量對公民決策的實際影響。此外，正文稱篩選後約有 900 張影像，appendix 卻寫約 300 個場景，存在內部報告不一致。更根本的限制是 2D co-occurrence 無法表示真實 3D 距離，ADE20K 帶有地理與文化偏差，而 visual models 也缺少法規、無障礙、交通、地下管線、地形與預算資訊。因此作者將 participatory evaluation、更具多樣性的資料、3D scene understanding 與 deployment feedback 列為後續方向。

## Notes

- Users choose the anchor, select a statistical complement, and may accept, reject, or re-prompt semantic recommendations before placement.
- The co-occurrence table includes 18 anchor classes and returns five complements per class.
- The work is a design prototype in the Creative AI Track, not an offline benchmark of personalized item ranking.
- No human-subject study or statistical significance test is reported.
