#!/usr/bin/env python3
"""
scripts/fix_internal_md_links.py
Converts all internal `.md` markdown links in qmd files to `.qmd` links,
eliminating Quarto build warnings and restoring full navigation.
"""

import os
import re
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent

def fix_links_in_file(file_path: Path):
    content = file_path.read_text(encoding="utf-8")
    original = content

    # Replace markdown links: [text.md](target.md) -> [text](target.qmd)
    # Also handles anchors if any: target.md#anchor -> target.qmd#anchor
    def replacer(match):
        text = match.group(1)
        target = match.group(2)
        
        # Only touch relative .md links (do not touch external urls)
        if target.startswith("http://") or target.startswith("https://") or target.startswith("mailto:"):
            return match.group(0)

        # Remove trailing .md from display text if it's just the filename
        if text.endswith(".md"):
            display_text = text[:-3]
        else:
            display_text = text

        new_target = re.sub(r'\.md($|#)', r'.qmd\1', target)
        return f"[{display_text}]({new_target})"

    new_content = re.sub(r'\[([^\]]+)\]\(([^)]+\.md(?:#[^)]*)?)\)', replacer, content)

    if new_content != original:
        file_path.write_text(new_content, encoding="utf-8")
        diff_count = len(re.findall(r'\[([^\]]+)\]\(([^)]+\.md(?:#[^)]*)?)\)', original))
        print(f"Fixed {diff_count} links in {file_path.relative_to(ROOT_DIR)}")
        return diff_count
    return 0

def main():
    total_fixed = 0
    qmd_dir = ROOT_DIR / "qmd"
    for root, _, files in os.walk(qmd_dir):
        for f in files:
            if f.endswith(".qmd"):
                p = Path(root) / f
                total_fixed += fix_links_in_file(p)

    print(f"\nSuccessfully converted {total_fixed} internal .md links to .qmd across all QMD files!")

if __name__ == '__main__':
    main()
