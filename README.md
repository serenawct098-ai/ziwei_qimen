# Ziwei × Qimen Decision Engine

## 證據與映射層狀態（2026-08-08）

本版本以可物理讀取的 Text SSOT、逐筆 `line_id` 與正規化引文直接追溯作為引用判定基準。四化鎖定表保留為系統鎖定的設計規則，並不宣稱為本倉庫古籍逐字原文。

| 對象 | 條目數 | verified | unverified | verified 逐字可追溯 |
|---|---:|---:|---:|---:|
| `rag_index_v1.json` | 860 | 532 | 328 | 532 |
| `citation_ledger` | 861 | 531 | 330 | 531 |

- Verified 假來源：0；未標記 HALT 的 verified 引用錯配：0；未標記 HALT 的不存在 engine path：0。
- 13 筆原先僅存於 Citation Ledger 的有效文字引用已補入 RAG Tier 3；其中無法逐字追溯的引文保留原文並標為 HALT，未以相似句或固定偏移取代。
- 完整逐筆變更與驗證證據：`audit_output/mapping_layer_fix_audit.json`；驗證摘要：`audit_output/mapping_layer_fix_verification_summary.md`。

## 唯一真值來源

- Text SSOT：`data/ZWQS_Juan1_Consolidated.json`、`data/ZWQS_Juan1_PatternText.json`、`data/ZWQS_Juan2_Consolidated.json`、`data/ZWQS_Juan3_Consolidated.json`、`data/QMDJ_ShangJuan_Consolidated.json`、`data/QMDJ_XiaJuan_Consolidated.json`。
- 引用與路由：`engines/rag_index_v1.json`、`engines/engine_reference_blueprint_v1.json`。
- 十干四化：`engine_truth_registry_v1.static_truth_tables.sihua_matrix_presets.wenmo_tianji_standard`；屬 `design_rule`，每筆均附 `design_origin_note`，不含虛構的 `SHZH_TenStemSihua_Source.json` 或行號。

## 仍需人工決定的 HALT

- `engine_truth_registry_v1.name_registries.palace_name_registry[8].legacy_aliases[2]`：HALT：原文查無此段，需人工確認 original_quote_preview 本身是否為誤植的意譯句；已保留原 data_file、line_id 與引文，不以相似語句硬套。
- `engine_truth_registry_v1.name_registries.star_name_registry[14].display_name`：HALT：原文查無此段，需人工確認 original_quote_preview 本身是否為誤植的意譯句；已保留原 data_file、line_id 與引文，不以相似語句硬套。
- `engine_truth_registry_v1.name_registries.star_name_registry[15].display_name`：HALT：原文查無此段，需人工確認 original_quote_preview 本身是否為誤植的意譯句；已保留原 data_file、line_id 與引文，不以相似語句硬套。
- `engine_truth_registry_v1.static_truth_tables.boshi_12_stars[0]`：HALT：原文查無此段，需人工確認 original_quote_preview 本身是否為誤植的意譯句；已保留原 data_file、line_id 與引文，不以相似語句硬套。
- `engine_truth_registry_v1.static_truth_tables.boshi_12_stars[1]`：HALT：原文查無此段，需人工確認 original_quote_preview 本身是否為誤植的意譯句；已保留原 data_file、line_id 與引文，不以相似語句硬套。
- `engine_truth_registry_v1.static_truth_tables.boshi_12_stars[2]`：HALT：原文查無此段，需人工確認 original_quote_preview 本身是否為誤植的意譯句；已保留原 data_file、line_id 與引文，不以相似語句硬套。
- `engine_truth_registry_v1.static_truth_tables.boshi_12_stars[3]`：HALT：原文查無此段，需人工確認 original_quote_preview 本身是否為誤植的意譯句；已保留原 data_file、line_id 與引文，不以相似語句硬套。
- `engine_truth_registry_v1.static_truth_tables.boshi_12_stars[6]`：HALT：原文查無此段，需人工確認 original_quote_preview 本身是否為誤植的意譯句；已保留原 data_file、line_id 與引文，不以相似語句硬套。
- `engine_truth_registry_v1.static_truth_tables.boshi_12_stars[10]`：HALT：原文查無此段，需人工確認 original_quote_preview 本身是否為誤植的意譯句；已保留原 data_file、line_id 與引文，不以相似語句硬套。
- `engine_compute_protocol_v1.dynamic_overlay_compute.monthly_rules`：HALT：原文查無此段，需人工確認 original_quote_preview 本身是否為誤植的意譯句；已保留原 data_file、line_id 與引文，不以相似語句硬套。
- `engine_compute_protocol_v1.calendar_ephemeris_protocol.solar_time_correction`：missing field solar_time_correction
- `engine_compute_protocol_v1.calendar_ephemeris_protocol.solar_time_correction`：HALT：solar_time_correction 功能未實作，此為真正缺口非路徑錯誤，需人工決定是否移除該引用或補建此功能。
- `engine_truth_registry_v1.static_truth_tables.zhifu_zhishi_table`：HALT：原文查無此段，需人工確認 original_quote_preview 本身是否為誤植的意譯句；已保留原 data_file、line_id 與引文，不以相似語句硬套。
- `engine_truth_registry_v1.static_truth_tables.shensha_table.boshi_12_series.stars`：HALT：原文查無此段，需人工確認 original_quote_preview 本身是否為誤植的意譯句；已保留原 data_file、line_id 與引文，不以相似語句硬套。
- `engine_truth_registry_v1.static_truth_tables.shensha_table.boshi_12_series`：HALT：原文查無此段，需人工確認 original_quote_preview 本身是否為誤植的意譯句；已保留原 data_file、line_id 與引文，不以相似語句硬套。
- `engine_interpretation_fusion_v1.fusion_block.bridge_mapping_layer.kun_2_redirect_rule`：HALT：原文查無「天禽寄於坤二宮」此完整段落；現有 line_id 僅載「天禽星寄於」，需人工確認原始文本、意譯或規則來源，不以相似內容補行。

## 引擎分層

| 層級 | 主檔 | 職責 |
|---|---|---|
| L0 | `engine_reference_blueprint_v1.json` | 引用合約、Citation Ledger、五層映射 |
| L1 | `engine_truth_registry_v1.json` | 真值表、名詞正規化、四化鎖定 |
| L2 | `engine_compute_protocol_v1.json` | 起盤與疊盤運算協定 |
| L3 | `engine_interpretation_fusion_v1.json` | 格局與雙軌解讀融合 |
| L4 | `engine_overlay_governance_v1.json`、`overlays/time_sensitive_overlays_v1.json` | 治理與年度敏感 Overlay |

本 README 只反映本次獨立驗證可證明的狀態；歷史「已全數清零」或「已建立 SHZH 實體文本」等說法不再採用。
