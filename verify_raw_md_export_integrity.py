import csv
import hashlib
from pathlib import Path

ROOT = Path(__file__).resolve().parent
MANIFEST_PATH = ROOT / "raw_answers_md" / "manifest.csv"
EXPORT_DIR = ROOT / "raw_answers_md"


def sha256_text(text):
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def main():
    if not MANIFEST_PATH.exists():
        raise FileNotFoundError(f"Manifest not found: {MANIFEST_PATH}")

    with MANIFEST_PATH.open("r", encoding="utf-8", newline="") as handle:
        rows = list(csv.DictReader(handle))

    total_rows = len(rows)
    files_found = 0
    files_missing = 0
    hash_matches = 0
    hash_mismatches = 0
    mismatches = []

    for row in rows:
        md_path = (EXPORT_DIR / row["md_path"]).resolve()
        if md_path.exists():
            files_found += 1
            content = md_path.read_text(encoding="utf-8")
            computed_hash = sha256_text(content)
            manifest_hash = row["answer_sha256"]
            if computed_hash == manifest_hash:
                hash_matches += 1
            else:
                hash_mismatches += 1
                mismatches.append(
                    {
                        "run_id": row["run_id"],
                        "md_path": row["md_path"],
                        "manifest_hash": manifest_hash,
                        "computed_hash": computed_hash,
                        "file_char_length": len(content),
                    }
                )
        else:
            files_missing += 1
            print(f"missing_file run_id={row['run_id']} md_path={row['md_path']}")

    print(f"total_manifest_rows={total_rows}")
    print(f"files_found={files_found}")
    print(f"files_missing={files_missing}")
    print(f"hash_matches={hash_matches}")
    print(f"hash_mismatches={hash_mismatches}")

    for mismatch in mismatches:
        print(
            f"mismatch run_id={mismatch['run_id']} md_path={mismatch['md_path']} manifest_hash={mismatch['manifest_hash']} computed_hash={mismatch['computed_hash']} file_char_length={mismatch['file_char_length']}"
        )


if __name__ == "__main__":
    main()
