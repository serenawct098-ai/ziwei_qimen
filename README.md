# Ziwei × Qimen Decision Engine (Phase 2 Complete)

## 專案概述
本專案旨在構建一個可驗證、可追溯且具備自動化診斷能力的「紫微斗數 × 奇門遁甲」雙軌決策引擎。系統採用六層責任架構（L0-L5），確保從古典文本（SSOT）到現代解讀邏輯的物理對齊。

## 當前進度：Phase 2 完工
目前已完成 **AI 輔助診斷與 RAG 知識庫建置**。系統已具備 11 個核心維度的自動化診斷路由與報告生成能力。

### 1. 核心維度覆蓋 (11 Dimensions)
| 分類 | 維度名稱 | 核心宮位 / 邏輯 |
| :--- | :--- | :--- |
| **基礎維度** | 事業、感情、健康、財富 | 官祿、夫妻、疾厄、財帛 |
| **新增維度** | 心理韌性、原生家庭、人際網絡、外顯形象、居住資產、晚輩管理、運限轉折 | 福德、父母、交友/兄弟、遷移、田宅、子女、大限流年 |
| **奇門擴充** | 戰略局勢、空間風水、隱秘神煞、事件應期、出行避險、失物定位 | 日干對峙、九宮佈局、神煞感應、三元應期 |

### 2. 五層系統架構 (L1-L5)
- **L1 Data (文本層)**：6 份經審計的 JSON SSOT 文本，提供 word-by-word 的原始引述。
- **L2 Mapping (映射層)**：統一的宮位與星曜註冊表，鎖定標準鍵與別名治理。
- **L3 Compute (運算層)**：安星定局、四化鎖定（文墨天機標準）、動態疊盤協議。
- **L4 Fusion (融合層)**：紫微 12 宮與奇門 9 宮的物理橋接，實現雙軌同步診斷。
- **L5 Governance (治理層)**：斷語庫與風水 Overlay，禁止回寫核心引擎，確保算演分離。
- **L0 Reference (憲法層)**：`engine_reference_blueprint_v1.json` 負責全局引用合約。

### 3. RAG 索引庫 (rag_index_v1.json)
- **條目總數**：787 條。
- **Verified**：484 條（直接對齊古籍 `line_id`）。
- **Unverified**：303 條（標註系統設計來源，防止 AI 幻覺）。

## 檔案結構
- `/data`: 原始文本 SSOT。
- `/engines`: 核心引擎主檔（Truth, Compute, Fusion, Governance, Blueprint）。
- `/engines/diagnosis_router_module_v1.json`: 診斷意圖路由中心。
- `/engines/auto_report_generator_v1.json`: 報告生成組件與約束。
- `/engines/rag_index_v1.json`: 100% 溯源的 RAG 知識索引。

---
**Author**: Manus AI (L10 Strategist)
**Status**: Phase 2 Integrated & Verified
**Date**: 2026-08-06
