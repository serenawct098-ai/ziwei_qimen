import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ENGINES = ROOT / 'engines'
DATA = ROOT / 'data'
NOTE = 'Physical trace missing in current SSOT consolidated files; downgraded to unverified.'
SOURCE_FIELDS = ('data_file', 'line_id', 'original_quote', 'original_quote_preview', 'normalized_preview')


def walk(value):
    if isinstance(value, dict):
        yield value
        for child in value.values():
            yield from walk(child)
    elif isinstance(value, list):
        for child in value:
            yield from walk(child)


def records(value):
    for node in walk(value):
        if isinstance(node.get('line_id'), str) and isinstance(node.get('original_quote'), str):
            yield node


def load(path):
    with path.open(encoding='utf-8') as handle:
        return json.load(handle)


def save(path, value):
    with path.open('w', encoding='utf-8') as handle:
        json.dump(value, handle, ensure_ascii=False, indent=2)
        handle.write('\n')


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--apply', action='store_true')
    args = parser.parse_args()

    index = {}
    for path in sorted(DATA.rglob('*.json')):
        for node in records(load(path)):
            index[(path.name, node['line_id'])] = node['original_quote']

    downgraded = []
    restored = []
    for path in sorted(ENGINES.rglob('*.json')):
        if path.name == 'cross_file_logic_audit_evidence.json':
            continue
        payload = load(path)
        changed = False
        for node in walk(payload):
            if not isinstance(node, dict) or not {'data_file', 'line_id'}.issubset(node):
                continue
            key = (node['data_file'], node['line_id'])
            quote = index.get(key)
            if quote is None:
                for field in SOURCE_FIELDS:
                    node.pop(field, None)
                if node.get('status') == 'verified':
                    node['status'] = 'unverified'
                node['verification_status'] = 'unverified'
                node['source_type'] = 'design_rule'
                node['design_origin_note'] = NOTE
                downgraded.append(f'{path.relative_to(ROOT)}::{key[0]}::{key[1]}')
                changed = True
                continue
            if 'original_quote_preview' in node and node['original_quote_preview'] != quote:
                node['original_quote_preview'] = quote
                restored.append(f'{path.relative_to(ROOT)}::{key[0]}::{key[1]}::original_quote_preview')
                changed = True
            if 'normalized_preview' in node and node['normalized_preview'] != quote:
                node['normalized_preview'] = quote
                restored.append(f'{path.relative_to(ROOT)}::{key[0]}::{key[1]}::normalized_preview')
                changed = True
        if changed and args.apply:
            save(path, payload)

    mode = 'APPLY' if args.apply else 'DRY-RUN'
    print(f'Mode: {mode}')
    print(f'SSOT records indexed: {len(index)}')
    print(f'Unresolvable references downgraded: {len(downgraded)}')
    print(f'RAG previews restored: {len(restored)}')
    for item in downgraded:
        print(f'DOWNGRADE {item}')
    for item in restored:
        print(f'RESTORE {item}')


if __name__ == '__main__':
    main()
