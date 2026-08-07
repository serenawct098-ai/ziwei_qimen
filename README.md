# Ziwei × Qimen Decision Engine (v2.0: Full Structure Integration)

## 專案概述
本專案旨在構建一個具備**物理級可追溯性**與**契約化運算能力**的「紫微斗數 × 奇門遁甲」雙軌決策引擎。系統嚴格執行《全局邏輯審查指令 v4.0》，確保從古籍原文（SSOT）到動態疊盤運算的每一條邏輯均具備物理反查路徑。

## 當前進度：v2.0 全量結構併入 (Phase 3 Initial)
目前已完成**三合紫微與奇門轉盤結構**的物理落地。系統已從「語義描述層」升級為「結構化契約層」，實現了跨檔案的物理閉環。

### 1. 核心憲法鎖定 (L0 Constitution)
*   **奇門盤層**：固定採用**轉盤**規則；值符隨順/逆旋轉入九宮，九星八門依轉盤方式佈局，嚴禁混入飛盤邏輯。
*   **四化矩陣**：庚干（陽武同相）、壬干（梁紫左武）等十干四化已鎖定為文墨天機標準，禁止覆寫。
*   **換日規則**：晚子時（23:00–23:59）一律視為次日子時，時支恆為子。

### 2. 五層責任架構 (L0-L5)
| 層級 | 責任定義 | 當前狀態 |
| :--- | :--- | :--- |
| **L0 憲法層** | `engine_reference_blueprint_v1.json` 負責全局引用合約與版本鎖定。 | **v1.2 已鎖定** |
| **L1 真值層** | `engine_truth_registry_v1.json` 提供標準鍵、物理對宮表與 100% 溯源的結構表。 | **已併入奇門四盤與副曜神煞** |
| **L2 運算層** | `engine_compute_protocol_v1.json` 定義安星法、疊盤步驟與 Fail-closed 驗證閘。 | **結構化契約化完成** |
| **L3 融合層** | `engine_interpretation_fusion_v1.json` 實現紫微格局與奇門格局的物理橋接。 | **格局庫溯源修正完成** |
| **L4 治理層** | `engine_overlay_governance_v1.json` 管理斷語與風水 Overlay，禁止回寫核心。 | **持續迭代中** |

### 3. 核心功能更新 (v2.0)
*   **物理路徑閉環**：所有 Router 意圖（如出行避險、方位風水）均已連結至具備標準 JSON Path 的可執行 Selector，消除了 `lookup_miss`。
*   **疊盤判斷合約**：動態疊盤已從文字敘述升級為具備 `inputs`、`alignment_key` 與 `action` 的運算合約，並物理區分了「本命體用」與「年月體用」。
*   **1:1 粒度級溯源**：Citation Ledger 已達成「一筆資料對一條實體 Key」的精確映射，每一條旬空、驛馬數據均具備獨立的物理反查路徑。
*   **RAG 完整性修復**：已修復因「去省略號」導致的內容截斷問題，並對 `normalized_preview` 執行了回歸淨化，僅保留憲法授權的正規化映射。

## 檔案結構
- `/data`: 原始古籍 SSOT (ZWQS, QMDJ)。
- `/engines`: 核心引擎主檔（Blueprint, Truth, Compute, Fusion, Governance）。
- `/engines/diagnosis_router_module_v1.json`: 具備意圖層級驗證的路由中心。
- `/engines/cross_file_logic_audit_evidence.json`: **治理核心**，記錄所有 Task 的 Before/After Diff 與驗證實證。

---
**Author**: LUNA (Autonomous COO & System Architect)
**Status**: 已完成架構合約整合，待 RAG 全文完整性與正規化回歸審計
**Date**: 2026-08-07
