import json
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / 'data'
RAG_PATH = ROOT / 'engines' / 'rag_index_v1.json'
REPORT_PATH = ROOT / 'audit' / 'rag_integrity_report.json'

def records(value):
    if isinstance(value, dict):
        if isinstance(value.get('line_id'), str) and isinstance(value.get('original_quote'), str):
            yield value
        for child in value.values():
            yield from records(child)
    elif isinstance(value, list):
        for child in value:
            yield from records(child)

def nodes(value):
    if isinstance(value, dict):
        yield value
        for child in value.values():
            yield from nodes(child)
    elif isinstance(value, list):
        for child in value:
            yield from nodes(child)

def main():
    source_index = {}
    for path in sorted(DATA_DIR.rglob('*.json')):
        with path.open(encoding='utf-8') as handle:
            payload = json.load(handle)
        for record in records(payload):
            source_index[(path.name, record['line_id'])] = record['original_quote']

    with RAG_PATH.open(encoding='utf-8') as handle:
        rag = json.load(handle)

    scanned = 0
    repaired_original = 0
    repaired_normalized = 0
    unresolved = []
    for node in nodes(rag):
        if not {'data_file', 'line_id', 'original_quote_preview'}.issubset(node):
            continue
        scanned += 1
        quote = source_index.get((node['data_file'], node['line_id']))
        if quote is None:
            unresolved.append({
                'data_file': node['data_file'],
                'line_id': node['line_id'],
                'engine_path': node.get('engine_path', '')
            })
            continue
        if node['original_quote_preview'] != quote:
            node['original_quote_preview'] = quote
            repaired_original += 1
        if 'normalized_preview' in node and node['normalized_preview'] != quote:
            node['normalized_preview'] = quote
            repaired_normalized += 1

    with RAG_PATH.open('w', encoding='utf-8') as handle:
        json.dump(rag, handle, ensure_ascii=False, indent=2)
        handle.write('\n')

    REPORT_PATH.parent.mkdir(parents=True, exist_ok=True)
    report = {
        'generated_at_utc': datetime.now(timezone.utc).isoformat(),
        'source_records_indexed': len(source_index),
        'rag_entries_scanned': scanned,
        'original_quote_preview_repaired': repaired_original,
        'normalized_preview_repaired': repaired_normalized,
        'unresolved_entries': unresolved,
        'unresolved_entry_count': len(unresolved),
        'normalization_policy': 'normalized_preview is restored to original_quote until an authorized context-safe normalization transform is implemented'
    }
    with REPORT_PATH.open('w', encoding='utf-8') as handle:
        json.dump(report, handle, ensure_ascii=False, indent=2)
        handle.write('\n')

if __name__ == '__main__':
    main()
