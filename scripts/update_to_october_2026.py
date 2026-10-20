#!/usr/bin/env python3
"""
scripts/update_to_october_2026.py
Updates all 185 QMD files to the current date: 2026-10-20.
- Updates frontmatter `date: "2026-10-20"`
- Updates `<span class="doc-badge date">📅 2026-10-20</span>`
- Preserves 100% of underlying document analysis and text.
"""

import os
import re
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent
TARGET_DATE = "2026-10-20"

def update_file(file_path: Path) -> bool:
    content = file_path.read_text(encoding="utf-8")
    original = content

    # 1. Update frontmatter date
    content = re.sub(
        r'^(date:\s*["\']?)[0-9]{4}-[0-9]{2}-[0-9]{2}(["\']?)',
        rf'\g<1>{TARGET_DATE}\g<2>',
        content,
        flags=re.MULTILINE
    )

    # 2. Update doc-badge date
    content = re.sub(
        r'(<span class="doc-badge date">📅\s*)[0-9]{4}-[0-9]{2}-[0-9]{2}(</span>)',
        rf'\g<1>{TARGET_DATE}\g<2>',
        content
    )

    # 3. Update any explicit blockquote date line if present
    content = re.sub(
        r'(\*?\*?(?:최종\s*(?:수정일|업데이트)|Date)\*?\*?\s*:\s*\*?\*?)[0-9]{4}-[0-9]{2}-[0-9]{2}',
        rf'\g<1>{TARGET_DATE}',
        content,
        flags=re.IGNORECASE
    )

    if content != original:
        file_path.write_text(content, encoding="utf-8")
        return True
    return False

def main():
    count = 0
    # Process index.qmd
    index_file = ROOT_DIR / "index.qmd"
    if index_file.exists() and update_file(index_file):
        count += 1

    # Process all files in qmd/
    qmd_dir = ROOT_DIR / "qmd"
    for root, _, files in os.walk(qmd_dir):
        for f in files:
            if f.endswith(".qmd"):
                p = Path(root) / f
                if update_file(p):
                    count += 1

    print(f"Successfully updated {count} files to current date {TARGET_DATE}!")

if __name__ == '__main__':
    main()
