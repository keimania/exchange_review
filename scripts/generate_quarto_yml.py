#!/usr/bin/env python3
"""
scripts/generate_quarto_yml.py
_quarto.yml을 qmd/ 디렉토리 기반으로 자동 생성한다.
"""

from pathlib import Path

BASE_DIR = Path(__file__).parent.parent   # project root
QMD_DIR  = BASE_DIR / "qmd"


def rel(p: Path) -> str:
    return str(p.relative_to(BASE_DIR)).replace("\\", "/")


def build_sidebar_block(domain_en, domain_ko, base_en, base_ko) -> str:
    lines = []
    for lang, base, label in [("en", base_en, domain_en), ("ko", base_ko, domain_ko)]:
        qbase = QMD_DIR / base
        overview    = f"qmd/{base}/01_overview.qmd"
        comparative = f"qmd/{base}/02_comparative_analysis.qmd"

        sub_dirs = sorted(qbase.glob("*/")) if qbase.exists() else []
        sub_dirs = [d for d in sub_dirs if d.is_dir()]

        sid = base.replace("/", "-")
        lines += [
            f"    - id: {sid}",
            f"      title: \"{label}\"",
            f"      style: docked",
            f"      contents:",
        ]
        if (BASE_DIR / overview).exists():
            lines.append(f"        - {overview}")
        if (BASE_DIR / comparative).exists():
            lines.append(f"        - {comparative}")

        section_labels = {
            "exchanges":     "Exchanges"    if lang == "en" else "거래소",
            "organizations": "Organizations" if lang == "en" else "청산기관",
            "systems":       "Trading Systems" if lang == "en" else "매매시스템",
            "regulations":   "Regulations"  if lang == "en" else "규제",
        }
        for sd in sub_dirs:
            qmds = sorted(sd.glob("*.qmd"))
            if not qmds:
                continue
            sec = section_labels.get(sd.name, sd.name.title())
            lines.append(f"        - section: \"{sec}\"")
            lines.append(f"          contents:")
            for q in qmds:
                lines.append(f"            - {rel(q)}")
    return "\n".join(lines)


def main():
    yml = [
        "project:",
        "  type: website",
        "  output-dir: docs",
        "  render:",
        "    - \"index.qmd\"",
        "    - \"qmd/**/*.qmd\"",
        "",
        "website:",
        "  title: \"Global Exchange Research\"",
        "  description: \"글로벌 거래소 조사 — 주식·파생상품·청산결제\"",
        "",
        "  navbar:",
        "    left:",
        "      - text: \"Home\"",
        "        href: index.qmd",
        "      - text: \"Equities\"",
        "        menu:",
        "          - text: \"Overview (EN)\"",
        "            href: qmd/01_equities/en/01_overview.qmd",
        "          - text: \"Overview (KO)\"",
        "            href: qmd/01_equities/ko/01_overview.qmd",
        "          - text: \"---\"",
        "          - text: \"Comparative Analysis (EN)\"",
        "            href: qmd/01_equities/en/02_comparative_analysis.qmd",
        "          - text: \"비교분석 (KO)\"",
        "            href: qmd/01_equities/ko/02_comparative_analysis.qmd",
        "      - text: \"Derivatives\"",
        "        menu:",
        "          - text: \"Overview (EN)\"",
        "            href: qmd/02_derivatives/en/01_overview.qmd",
        "          - text: \"Overview (KO)\"",
        "            href: qmd/02_derivatives/ko/01_overview.qmd",
        "          - text: \"---\"",
        "          - text: \"Comparative Analysis (EN)\"",
        "            href: qmd/02_derivatives/en/02_comparative_analysis.qmd",
        "          - text: \"비교분석 (KO)\"",
        "            href: qmd/02_derivatives/ko/02_comparative_analysis.qmd",
        "      - text: \"Clearing\"",
        "        menu:",
        "          - text: \"Overview (EN)\"",
        "            href: qmd/03_clearing/en/01_overview.qmd",
        "          - text: \"Overview (KO)\"",
        "            href: qmd/03_clearing/ko/01_overview.qmd",
        "          - text: \"---\"",
        "          - text: \"Comparative Analysis (EN)\"",
        "            href: qmd/03_clearing/en/02_comparative_analysis.qmd",
        "          - text: \"비교분석 (KO)\"",
        "            href: qmd/03_clearing/ko/02_comparative_analysis.qmd",
        "      - text: \"Glossary\"",
        "        menu:",
        "          - text: \"Glossary (EN)\"",
        "            href: qmd/reference/glossary_en.qmd",
        "          - text: \"용어집 (KO)\"",
        "            href: qmd/reference/glossary_ko.qmd",
        "          - text: \"---\"",
        "          - text: \"Final Review (EN)\"",
        "            href: qmd/reference/final_review.qmd",
        "          - text: \"최종 리뷰 (KO)\"",
        "            href: qmd/reference/ko/final_review.qmd",
        "    right:",
        "      - icon: github",
        "        href: https://github.com/keimania/exchange_review",
        "",
        "  sidebar:",
    ]

    yml.append(build_sidebar_block("Equities (EN)", "주식시장 (KO)",
                                    "01_equities/en", "01_equities/ko"))
    yml.append(build_sidebar_block("Derivatives (EN)", "파생상품 (KO)",
                                    "02_derivatives/en", "02_derivatives/ko"))
    yml.append(build_sidebar_block("Clearing (EN)", "청산결제 (KO)",
                                    "03_clearing/en", "03_clearing/ko"))

    yml += [
        "    - id: reference",
        "      title: \"Reference / 참고자료\"",
        "      style: docked",
        "      contents:",
    ]
    for p in ["qmd/reference/glossary_en.qmd", "qmd/reference/glossary_ko.qmd",
              "qmd/reference/final_review.qmd", "qmd/reference/ko/final_review.qmd"]:
        if (BASE_DIR / p).exists():
            yml.append(f"        - {p}")

    yml += [
        "",
        "format:",
        "  html:",
        "    theme: cosmo",
        "    css: styles.css",
        "    toc: true",
        "    toc-location: right",
        "    toc-title: \"목차 (Contents)\"",
        "    toc-depth: 3",
        "    number-sections: false",
        "    smooth-scroll: true",
        "    link-external-newwindow: true",
        "    page-navigation: true",
        "    back-to-top-navigation: true",
        "    grid:",
        "      sidebar-width: 270px",
        "      body-width: 1050px",
        "      margin-width: 260px",
    ]

    out = BASE_DIR / "_quarto.yml"
    out.write_text("\n".join(yml) + "\n", encoding="utf-8")
    print(f"생성: {out}  ({len(yml)} lines)")


if __name__ == "__main__":
    main()
