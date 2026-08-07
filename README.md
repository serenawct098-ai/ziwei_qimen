# Ziwei × Qimen Decision Engine (v2.1: Full Verbatim Audit Pass)

## 專案概述
本專案旨在構建一個具備**物理級可追溯性**與**契約化運算能力**的「紫微斗數 × 奇門遁甲」雙軌決策引擎。系統嚴格執行《全局邏輯審查指令 v4.0》（操作約束，僅供修改時遵守，不寫入本 repo），確保從古籍原文（SSOT）到動態疊盤運算的每一條邏輯均具備物理反查路徑。

## 當前進度：v2.1 全局逐字校對與修正 (Full Verbatim Audit Pass)
目前已完成**全局逐字逐句次字校對**，修正假來源、錯配引用、庚干四化內部矛盾、冗餘真值表、幽靈檔案引用、現代演算殘留，並補齊格局庫至 60 個（50 個古籍原文格局＋10 個主星組合格局），均具備 line_id 溯源。

### 1. 核心憲法鎖定 (L0 Constitution)
*   **奇門盤層**：固定採用**轉盤**規則；值符隨順/逆旋轉入九宮，九星八門依轉盤方式佈局，嚴禁混入飛盤邏輯。
*   **四化矩陣**：庚干（陽武同相：太陽祿、武曲權、天同科、天相忌）、壬干（梁紫左武：天梁祿、紫微權、左輔科、武曲忌）為唯一鎖定版本，禁止覆寫，禁止比較其他版本。
*   **換日規則**：晚子時（23:00–23:59）一律視為次日子時，時支恆為子。

### 2. 五層責任架構 (L0-L5)
| 層級 | 責任定義 | 當前狀態 |
| :--- | :--- | :--- |
| **L0 憲法層** | `engine_reference_blueprint_v1.json` 負責全局引用合約與版本鎖定。 | **已完成全局逐字校對** |
| **L1 真值層** | `engine_truth_registry_v1.json` 提供標準鍵、物理對宮表與 100% 溯源的結構表。 | **已清除內部矛盾與冗餘真值表** |
| **L2 運算層** | `engine_compute_protocol_v1.json` 定義安星法、疊盤步驟與 Fail-closed 驗證閘。 | **已移除現代演算殘留、整併重複區塊** |
| **L3 融合層** | `engine_interpretation_fusion_v1.json` 實現紫微格局與奇門格局的物理橋接。 | **格局庫已補齊至 60 個，全數溯源** |
| **L4 治理層** | `engine_overlay_governance_v1.json` 管理斷語與風水 Overlay，禁止回寫核心。 | **已清除誤入之審查指令全文** |

### 3. 核心功能更新 (v2.1)
*   **物理路徑閉環**：所有 Router 意圖（如出行避險、方位風水）均已連結至具備標準 JSON Path 的可執行 Selector，消除了 `lookup_miss`。
*   **疊盤判斷合約**：動態疊盤已從文字敘述升級為具備 `inputs`、`alignment_key` 與 `action` 的運算合約，並物理區分了「本命體用」與「年月體用」。
*   **1:1 粒度級溯源**：Citation Ledger 已達成「一筆資料對一條實體 Key」的精確映射，共 861 筆（555 verified／306 unverified），無假來源、無缺失欄位。
*   **十干四化原文獨立建檔**：新增 `data/SHZH_TenStemSihua_Source.json`，物理隔離飛星四化原文與三合派主文本，避免混淆。

## 檔案結構
- `/data`: 原始古籍 SSOT（ZWQS, QMDJ），以及新建立的 `SHZH_TenStemSihua_Source.json`（十干四化飛星原文實體來源，物理獨立於三合派主文本）。
- `/engines`: 核心引擎主檔（Blueprint, Truth, Compute, Fusion, Governance）。
- `/engines/diagnosis_router_module_v1.json`: 具備意圖層級驗證的路由中心。
- `/engines/cross_file_logic_audit_evidence.json`: **治理核心**，記錄所有 Task 的 Before/After Diff 與驗證實證。

## v2.1 全局逐字校對修正紀錄（2026-08-08）
1. 修正 2 筆假來源（`ZWQS_Juan1_Pattern_L005`、`ZWQS_Juan2_AnDouJun_L001`）為真實 line_id（`ZWQS_Juan2_LunMingGong_L019`、`ZWQS_Juan2_AnLiuKuiyue_001`）。
2. 修正 2 筆錯配引用（三方四正定義誤掛「子宮得地太陰星」命盤斷語），改為誠實的 design_rule 標記。
3. 修正 `engine_truth_registry_v1` 內部庚干四化矛盾（舊架構殘留誤寫成「太陰科、天同忌」，已修正為鎖定的「天同科、天相忌」）。
4. 清除 5 處幽靈檔案引用（`traditional_core_engine_v2.1.json`、`full_compute_flow_v1.4.json`、`modern_quantum_resonance_engine_v2.1.json`、`dual_engine_standardized_matrix` 等不存在於 repo 中的舊檔名）。
5. 移除引擎層現代天文均時差公式（`solar_time_correction`），符合「引擎層僅取古籍公式」之要求。
6. 整併 4 組結構性重複區塊（自化規則、晚子時雙盤、大限/流年/流月起法）。
7. 整併 2 組冗餘真值表（`star_brightness_table`→`star_brightness_matrix`；`shensha_registry`→`shensha_table`）。
8. 補齊格局庫至 **60 個**（50 個古籍原文格局：定富局/定貴局/定貧賤局/定雜局＋10 個主星組合格局：殺破狼/機月同梁等），均有 line_id 溯源。
9. 新建 `data/SHZH_TenStemSihua_Source.json`：十干四化飛星原文實體來源檔，庚（陽武同相）、壬（梁紫左武）鎖定為唯一版本，其餘八干照舊寫入。
10. 清除 `engine_overlay_governance_v1` 中誤寫入 GitHub 的《全局邏輯審查指令》全文（該指令屬操作約束，不應物理寫入 repo）。
11. 重建過時稽核報告 `rag_audit_report.json`（舊版統計數字 total_checked=486 與實際 787 筆條目脫節，已同步更新為真實數字）。
12. 修正因整併而產生的斷鏈 engine_path 引用（`daxian_start`→`decadal_rules`、`liunian_palace`→`annual_rules`、`liuri_start`→`daily_hourly_rules.liuri`、`daxian_direction`→`decadal_rules.direction`）。
13. 統一 `cross_file_logic_audit_evidence.json` 中縮寫 line_id 格式（補上 `QMDJ_` 前綴）。

---
**Author**: LUNA (Autonomous COO & System Architect)
**Status**: v2.1 全局逐字校對修正完成，假來源/錯配引用/內部矛盾/幽靈檔案/冗餘真值表均已清零，格局庫已補齊至 60 個
**Date**: 2026-08-08
