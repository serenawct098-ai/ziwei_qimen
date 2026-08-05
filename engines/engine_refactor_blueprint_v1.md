# Ziwei × Qimen 引擎層結構重構藍圖 v1.0

## 1. 重構概況
本次重構將原本分散的 11 份 JSON 檔案收束為 **4 份核心主檔**，實現了職責的高度內聚與邏輯的徹底解耦。

### 檔案對照表
| 新主檔名 | 責任域 | 合併來源 |
| :--- | :--- | :--- |
| `engine_truth_registry_v1.json` | **Truth / Registry** | `traditional_core_engine` (靜態表), `Palace Registry`, `Star Registry` |
| `engine_compute_protocol_v1.json` | **Compute / Validation** | `full_compute_flow`, `traditional_core_engine` (公式), 曆法起盤流程 |
| `engine_interpretation_fusion_v1.json` | **Interpretation / Fusion** | `interpretation_engine`, `mythos_engine`, `resonance_engine`, `fusion_engine` |
| `engine_overlay_governance_v1.json` | **Overlay / Governance** | `judgment_library`, `fengshui_module`, 年度化煞表, 治理規則 |

---

## 2. 核心架構說明

### A. Truth Layer (SSOT)
- **唯一性**：全系統名詞、索引、四化標準只在此處定義。
- **鎖定性**：庚干、壬干四化標準已物理鎖定，禁止動態修改。

### B. Compute Layer (Protocol)
- **算演分離**：只負責從輸入到矩陣的純數學運算，不包含任何文本描述。
- **驗證門控**：獨立的 `validation_gate` 確保輸入數據的合法性。

### C. Interpretation Layer (Fusion)
- **雙軌並行**：傳統命理軌與現代壓測軌在同檔內分 block 運算，互不污染。
- **橋接映射**：紫微 12 宮與奇門 9 宮的映射邏輯集中管理。

### D. Overlay Layer (Governance)
- **時效性隔離**：年度化煞、風水建議等易變內容與核心引擎物理隔離。
- **應用治理**：強制執行 `writeback_forbidden` 政策，防止應用層數據污染核心。

---

## 3. 已清理的舊檔案清單
- `traditional_core_engine_v2.1.json`
- `full_compute_flow_v1.4.json`
- `interpretation_engine_v1.1.json`
- `dual_parallel_fusion_engine_v1.1.json`
- `traditional_mythos_engine_v1.3.1.json`
- `modern_quantum_resonance_engine_v2.1.json`
- `mapping_contract_v1.1.json`
- `star_name_registry_v1.0.json`
- `qimen_judgment_library_v1.0.json`
- `qimen_fengshui_layout_module_v0.1.json`
- `qimen_2026_2027_sha_qi_resolution_table.json`

---

## 4. 風險與注意事項
- **依賴關係**：所有下游調用必須更新路徑，指向新的 4 份主檔。
- **Schema 變更**：舊有的 `metadata` 與 `governance` 欄位已按指令瘦身或移位，請確保消費端已對齊。
- **SSOT 強制力**：嚴禁在 `engine_truth_registry_v1` 之外定義任何新的星曜或宮位名詞。

---

## 5. Next Action
1. **全鏈路測試**：驗證 4 份主檔之間的數據流傳遞是否通暢。
2. **文本層對齊**：確保 `data/` 層的原文引述能正確指向新註冊表中的 `standard_key`。
3. **治理稽核**：定期掃描是否有開發者試圖在 Compute 層回寫語義文本。
