# Ziwei × Qimen: 全局邏輯治理系統

本專案旨在建立一個基於 **SSOT (Single Source of Truth)** 原則的紫微斗數與奇門遁甲集成運算系統。系統採用 **六層責任架構 (L0-L5)**，實現了算演分離、資料與規則分離，並通過物理鎖定機制確保核心命理邏輯的真實性與穩定性。

---

## 核心架構 (Six-Layer Architecture)

系統由 1 份治理藍圖 (L0) 與 4 份核心引擎主檔 (L2-L5) 組成，所有運算均依賴於 L1 的古籍數位化文本。

### L0: Reference & Blueprint (`engine_reference_blueprint_v1.json`)
*   **職責**：系統憲法與引用合約。
*   **內容**：定義五層架構映射、三合派命盤框架映射及 Text ↔ Engine 的引用分類帳 (`citation_ledger`)。

### L1: Data Layer (`data/*.json`)
*   **職責**：原始文本數位化 SSOT。
*   **來源**：《紫微斗數全書》、《奇門遁甲秘笈大全》等古籍的逐字數位化文本，包含真實 `line_id` 溯源。

### L2: Truth & Registry (`engine_truth_registry_v1.json`)
*   **職責**：核心真值與命名註冊。
*   **內容**：十干四化矩陣 (文墨天機標準)、星曜註冊表、宮位註冊表、洛書九宮及星曜廟旺表。

### L3: Compute Protocol (`engine_compute_protocol_v1.json`)
*   **職責**：運算協議與驗證門控。
*   **內容**：曆法修正 (晚子時換日)、安星定局流程、動態疊盤邏輯及斷言驗證 (`halt_assertions`)。

### L4: Interpretation & Fusion (`engine_interpretation_fusion_v1.json`)
*   **職責**：解讀引擎與雙軌融合。
*   **內容**：傳統命理格局庫、現代壓測模型及紫微/奇門跨維度融合橋接層。

### L5: Overlay & Governance (`engine_overlay_governance_v1.json`)
*   **職責**：應用層治理與覆蓋規則。
*   **內容**：斷語庫、風水佈局模組及年度時效性數據表。

---

## 核心治理原則 (Governance Protocols)

1.  **SSOT 優先**：所有運算必須引用 `engine_truth_registry_v1` 中的鎖定值。
2.  **Naming Lock**：嚴禁在解讀層或應用層自行定義新宮位或星曜名稱，必須對齊 Registry。
3.  **算演分離**：計算層 (L3) 僅處理邏輯與數值，嚴禁包含語義文本。
4.  **禁止回寫**：應用層 (L5) 數據嚴禁回寫至核心引擎，確保系統底層不被污染。
5.  **真實溯源**：每一條核心規則必須透過 `line_id` 物理映射至 L1 文本層。

---

## 核心數據鎖定 (Standard Settings)

*   **十干四化 (文墨天機版)**：
    *   **庚干**：太陽祿、武曲權、天同科、天相忌
    *   **壬干**：天梁祿、紫微權、左輔科、武曲忌
*   **天魁天鉞**：辛干鎖定「魁寅鉞午」。
*   **晚子時**：23:00 後執行 `lunar_day += 1` 換日邏輯。
*   **宮位標準**：統一收束為「夫妻宮」、「交友宮」等標準顯示名。

---

_Last Updated: 2026-08-05 | System Architect: Serena (L10)_
