#!/usr/bin/env python3
"""
scripts/convert_md_to_qmd.py
모든 콘텐츠 .md 파일을 Quarto YAML 헤더가 포함된 .qmd 파일로 변환한다.
출력 위치: {project_root}/qmd/ (MD 원본과 동일한 계층 구조)
"""

from pathlib import Path

BASE_DIR = Path(__file__).parent.parent   # project root
QMD_DIR  = BASE_DIR / "qmd"
DATE     = "2026-04-17"

# 변환 대상 (BASE_DIR 기준 상대경로 glob)
INCLUDE_PATTERNS = [
    "md/01_equities/en/**/*.md",
    "md/01_equities/ko/**/*.md",
    "md/02_derivatives/en/**/*.md",
    "md/02_derivatives/ko/**/*.md",
    "md/03_clearing/en/**/*.md",
    "md/03_clearing/ko/**/*.md",
    "md/_common/final_review.md",
    "md/_common/glossary_en.md",
    "md/_common/glossary_ko.md",
    "md/_common/ko/final_review.md",
]

EXCLUDE_NAMES = {
    "CLAUDE.md", "README.md", "SESSION_PLAN.md",
    "RESEARCH_GUIDE.md", "TRANSLATION_GUIDE.md",
    "TEMPLATE_EXCHANGE.md", "TEMPLATE_SYSTEM.md", "TEMPLATE_CLEARING.md",
    "INVENTORY.md",
}

SUBTITLE_MAP = {
    "md/01_equities/en/exchanges":  "Equities > Exchanges",
    "md/01_equities/en/systems":    "Equities > Trading Systems",
    "md/01_equities/en/regulations":"Equities > Regulations",
    "md/01_equities/en":            "Equities",
    "md/01_equities/ko/exchanges":  "주식시장 > 거래소",
    "md/01_equities/ko/systems":    "주식시장 > 매매시스템",
    "md/01_equities/ko/regulations":"주식시장 > 규제",
    "md/01_equities/ko":            "주식시장",
    "md/02_derivatives/en/exchanges":  "Derivatives > Exchanges",
    "md/02_derivatives/en/systems":    "Derivatives > Trading Systems",
    "md/02_derivatives/en/regulations":"Derivatives > Regulations",
    "md/02_derivatives/en":            "Derivatives",
    "md/02_derivatives/ko/exchanges":  "파생상품 > 거래소",
    "md/02_derivatives/ko/systems":    "파생상품 > 매매시스템",
    "md/02_derivatives/ko/regulations":"파생상품 > 규제",
    "md/02_derivatives/ko":            "파생상품",
    "md/03_clearing/en/organizations": "Clearing & Settlement > Organizations",
    "md/03_clearing/en/systems":       "Clearing & Settlement > Systems",
    "md/03_clearing/en/regulations":   "Clearing & Settlement > Regulations",
    "md/03_clearing/en":               "Clearing & Settlement",
    "md/03_clearing/ko/organizations": "청산결제 > 청산기관",
    "md/03_clearing/ko/systems":       "청산결제 > 시스템",
    "md/03_clearing/ko/regulations":   "청산결제 > 규제",
    "md/03_clearing/ko":               "청산결제",
    "md/_common/ko":                   "참고자료",
    "md/_common":                      "Reference",
}


def get_subtitle(rel_path: str) -> str:
    parent = str(Path(rel_path).parent).replace("\\", "/")
    for key in sorted(SUBTITLE_MAP.keys(), key=len, reverse=True):
        if parent == key or parent.startswith(key + "/"):
            return SUBTITLE_MAP[key]
    return "Global Exchange Research"


def get_lang(rel_path: str) -> str:
    p = rel_path.replace("\\", "/")
    if "/ko/" in p or p.startswith("_common/ko/") or p.startswith("md/_common/ko/"):
        return "ko"
    return "en"


def extract_title_and_body(content: str) -> tuple[str, str]:
    lines = content.split("\n")
    title, idx = "Untitled", None
    for i, line in enumerate(lines):
        if line.strip().startswith("# "):
            title = line.strip()[2:].strip()
            idx = i
            break
    if idx is None:
        return title, content
    before = lines[:idx]
    after  = lines[idx + 1:]
    if after and after[0].strip() == "":
        after = after[1:]
    return title, "\n".join(before + after)


def yaml_escape(s: str) -> str:
    return s.replace("\\", "\\\\").replace('"', '\\"')


def make_yaml_header(title: str, subtitle: str, lang: str) -> str:
    return f'''---
title: "{yaml_escape(title)}"
subtitle: "{yaml_escape(subtitle)}"
date: "{DATE}"
lang: {lang}
toc: true
toc-depth: 3
number-sections: false
format:
  html:
    theme: cosmo
    toc: true
    toc-location: left
    self-contained: false
---

'''


def md_rel_to_qmd_path(rel_str: str) -> Path:
    """
    MD 상대경로 → qmd/ 아래 대응 경로
    예) md/_common/glossary_en.md → qmd/reference/glossary_en.qmd
        md/_common/ko/final_review.md → qmd/reference/ko/final_review.qmd
        md/01_equities/en/exchanges/nyse.md → qmd/01_equities/en/exchanges/nyse.qmd
    """
    rel = Path(rel_str)
    parts = list(rel.parts)

    # Strip leading "md/" prefix
    if parts[0] == "md":
        parts = parts[1:]

    if parts[0] == "_common":
        # _common → reference
        new_parts = ["reference"] + parts[1:]
    else:
        new_parts = parts

    qmd_rel = Path(*new_parts).with_suffix(".qmd")
    return QMD_DIR / qmd_rel


def convert_file(md_path: Path) -> Path | None:
    if md_path.name in EXCLUDE_NAMES:
        return None
    if "docx" in md_path.parts:
        return None

    rel_str = str(md_path.relative_to(BASE_DIR)).replace("\\", "/")
    content  = md_path.read_text(encoding="utf-8")
    title, body = extract_title_and_body(content)
    subtitle = get_subtitle(rel_str)
    lang     = get_lang(rel_str)

    qmd_path = md_rel_to_qmd_path(rel_str)
    qmd_path.parent.mkdir(parents=True, exist_ok=True)
    qmd_path.write_text(make_yaml_header(title, subtitle, lang) + body, encoding="utf-8")
    return qmd_path


def main():
    converted, skipped = [], []
    for pattern in INCLUDE_PATTERNS:
        for md_path in sorted(BASE_DIR.glob(pattern)):
            if md_path.name in EXCLUDE_NAMES or "docx" in md_path.parts:
                skipped.append(md_path)
                continue
            result = convert_file(md_path)
            if result:
                converted.append(result)
                print(f"  ✓ {result.relative_to(BASE_DIR)}")
    print(f"\n변환 완료: {len(converted)}개 / 제외: {len(skipped)}개")
    return converted


if __name__ == "__main__":
    main()
