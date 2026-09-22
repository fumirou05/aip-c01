"""Validate integrated lab fixtures without network access or third-party packages."""

from __future__ import annotations

import json
import sys
from pathlib import Path


LAB_ROOT = Path(__file__).resolve().parents[1]


def load_json(path: Path) -> object:
    with path.open(encoding="utf-8") as handle:
        return json.load(handle)


def load_jsonl(path: Path) -> list[dict[str, object]]:
    records: list[dict[str, object]] = []
    with path.open(encoding="utf-8") as handle:
        for line_number, line in enumerate(handle, start=1):
            if line.strip():
                try:
                    records.append(json.loads(line))
                except json.JSONDecodeError as error:
                    raise ValueError(f"{path}:{line_number}: {error}") from error
    return records


def validate() -> list[str]:
    errors: list[str] = []

    required_lab_files = [
        LAB_ROOT / "aws/README.md",
        LAB_ROOT / "artifacts/_template.md",
        LAB_ROOT / "artifacts/cost-log-template.md",
    ]
    for path in required_lab_files:
        if not path.is_file():
            errors.append(f"missing lab file: {path}")

    manifest_path = LAB_ROOT / "data/knowledge-base/manifest.json"
    manifest = load_json(manifest_path)
    for document in manifest["documents"]:
        document_path = manifest_path.parent / document["path"]
        if not document_path.is_file():
            errors.append(f"missing knowledge document: {document_path}")

    datasets = {
        "golden": LAB_ROOT / "data/evaluation/golden.jsonl",
        "security": LAB_ROOT / "data/security/adversarial.jsonl",
    }
    required_fields = {
        "golden": {"id", "question", "expected_facts", "expected_sources", "should_answer"},
        "security": {"id", "category", "prompt", "expected_action"},
    }
    for name, path in datasets.items():
        records = load_jsonl(path)
        if not records:
            errors.append(f"empty dataset: {path}")
            continue
        for record in records:
            missing = required_fields[name] - record.keys()
            if missing:
                errors.append(f"{path}: {record.get('id', '<unknown>')} missing {sorted(missing)}")

    catalog = load_json(LAB_ROOT / "config/model-catalog.json")
    if len(catalog.get("models", [])) < 3:
        errors.append("model catalog must contain at least three models")

    faults = load_json(LAB_ROOT / "data/faults/scenarios.json")
    if len(faults.get("scenarios", [])) != 5:
        errors.append("fault fixture must contain exactly five scenarios")

    return errors


def main() -> int:
    errors = validate()
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    print("AWS/local GenAI integrated lab setup: OK")
    print(f"Lab root: {LAB_ROOT}")
    print("AWS connectivity and budget guardrails must be checked separately; see aws/README.md")
    return 0


if __name__ == "__main__":
    sys.exit(main())
