import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FORBIDDEN_EXACT = {'N/A', 'TODO', 'TBD', 'PLACEHOLDER'}


def walk(value, path='$'):
    if isinstance(value, dict):
        yield path, value
        for key, child in value.items():
            yield from walk(child, f'{path}.{key}')
    elif isinstance(value, list):
        for index, child in enumerate(value):
            yield from walk(child, f'{path}[{index}]')


def source_records(value):
    for _, node in walk(value):
        if isinstance(node.get('line_id'), str) and isinstance(node.get('original_quote'), str):
            yield node


def load_json(path, findings):
    try:
        with path.open(encoding='utf-8') as handle:
            return json.load(handle)
    except Exception as error:
        findings.append(('json_parse', str(path.relative_to(ROOT)), '$', str(error)))
        return None


def main():
    findings = []
    payloads = {}
    for path in sorted(ROOT.rglob('*.json')):
        if '.git' in path.parts:
            continue
        payload = load_json(path, findings)
        if payload is not None:
            payloads[path.relative_to(ROOT).as_posix()] = payload

    source_index = {}
    for relative, payload in payloads.items():
        if relative.startswith('data/'):
            for record in source_records(payload):
                source_index[(Path(relative).name, record['line_id'])] = record['original_quote']

    known_basenames = {Path(path).name for path in payloads}
    for relative, payload in payloads.items():
        for location, node in walk(payload):
            if not isinstance(node, dict):
                continue
            for key, value in node.items():
                if not isinstance(value, str):
                    continue
                if value.strip().upper() in FORBIDDEN_EXACT or '...' in value:
                    findings.append(('forbidden_placeholder', relative, f'{location}.{key}', value))
                if key == 'engine_path' and (not value.startswith('$') or '[:' in value or ':]' in value):
                    findings.append(('engine_path_format', relative, f'{location}.{key}', value))
                if key.endswith('_file') and value.endswith('.json') and Path(value).name not in known_basenames:
                    findings.append(('missing_file_reference', relative, f'{location}.{key}', value))
            if {'data_file', 'line_id'}.issubset(node):
                quote = source_index.get((node['data_file'], node['line_id']))
                if quote is None:
                    findings.append(('unresolved_ssot_reference', relative, location, f"{node['data_file']}:{node['line_id']}"))
                else:
                    for field in ('original_quote_preview', 'normalized_preview'):
                        if field in node and node[field] != quote:
                            findings.append(('quote_fidelity', relative, f'{location}.{field}', f"{node['data_file']}:{node['line_id']}"))

    print(f'JSON files scanned: {len(payloads)}')
    print(f'SSOT records indexed: {len(source_index)}')
    print(f'Global logic findings: {len(findings)}')
    for rule, file, path, detail in findings:
        print(f'ERROR [{rule}] {file} {path} :: {detail}')
    return 1 if findings else 0


if __name__ == '__main__':
    sys.exit(main())
