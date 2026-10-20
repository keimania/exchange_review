#!/usr/bin/env python3
"""
scripts/enhance_detail_pages.py
Enhances all 184 detail qmd files:
1. Removes 'toc-location: left' so right-side TOC is used.
2. Replaces crude markdown blockquote headers with a premium visual meta card.
3. Adds cross-language navigation button (KO <-> EN).
4. Keeps 100% of existing document content intact.
"""

import os
import re
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent
QMD_DIR = ROOT_DIR / "qmd"

DOMAIN_LABELS = {
    '01_equities': ('주식시장', 'Equities'),
    '02_derivatives': ('파생상품', 'Derivatives'),
    '03_clearing': ('청산·결제', 'Clearing & Settlement'),
    'reference': ('참고자료', 'Reference'),
}

CATEGORY_LABELS = {
    'exchanges': ('거래소 프로필', 'Exchange Profile'),
    'systems': ('매매체결 시스템', 'Trading System'),
    'regulations': ('시장 규제 체계', 'Regulation'),
    'organizations': ('청산·예탁기관', 'Clearing & CSD'),
    'ko': ('한국어 리포트', 'Korean Report'),
    'en': ('영문 리서치', 'English Research'),
}

def get_counterpart_url(rel_path: Path) -> str:
    """Find the corresponding KO <-> EN relative file URL."""
    p_str = str(rel_path).replace("\\", "/")
    
    # Check reference cases
    if "glossary_ko.qmd" in p_str:
        return "glossary_en.html"
    elif "glossary_en.qmd" in p_str:
        return "glossary_ko.html"
    elif "reference/ko/final_review.qmd" in p_str:
        return "../final_review.html"
    elif "reference/final_review.qmd" in p_str:
        return "ko/final_review.html"
        
    # Standard cases: .../ko/... <-> .../en/...
    if "/ko/" in p_str:
        counterpart_qmd = ROOT_DIR / p_str.replace("/ko/", "/en/")
        if counterpart_qmd.exists():
            # How many levels down from rel_path?
            depth = len(rel_path.parts) - 1
            # replace /ko/ with /en/ and .qmd with .html
            target_str = p_str.replace("/ko/", "/en/").replace(".qmd", ".html")
            # Calculate relative path from this file to target
            target_path = Path(target_str)
            return os.path.relpath(target_path, rel_path.parent).replace("\\", "/")
    elif "/en/" in p_str:
        counterpart_qmd = ROOT_DIR / p_str.replace("/en/", "/ko/")
        if counterpart_qmd.exists():
            target_str = p_str.replace("/en/", "/ko/").replace(".qmd", ".html")
            target_path = Path(target_str)
            return os.path.relpath(target_path, rel_path.parent).replace("\\", "/")
            
    return ""

def process_qmd_file(file_path: Path):
    content = file_path.read_text(encoding="utf-8")
    
    # Split frontmatter
    parts = content.split("---", 2)
    if len(parts) < 3:
        return
        
    fm_raw = parts[1]
    body = parts[2].lstrip()
    
    # 1. Clean frontmatter: remove toc-location: left
    fm_lines = []
    for line in fm_raw.splitlines():
        if "toc-location:" in line:
            continue
        fm_lines.append(line)
    new_fm = "---" + "\n".join(fm_lines) + "\n---\n\n"
    
    # 2. Extract metadata from top lines of body
    rel_path = file_path.relative_to(ROOT_DIR)
    rel_parts = rel_path.parts # e.g. ('qmd', '01_equities', 'ko', 'exchanges', 'krx.qmd')
    
    is_korean = "/ko/" in str(rel_path) or "_ko." in str(rel_path) or "/ko" in str(rel_path)
    
    domain_key = rel_parts[1] if len(rel_parts) > 1 else 'reference'
    domain_info = DOMAIN_LABELS.get(domain_key, ('글로벌 리서치', 'Global Research'))
    domain_label = domain_info[0] if is_korean else domain_info[1]
    
    cat_label = ""
    for p in rel_parts:
        if p in CATEGORY_LABELS:
            cat_info = CATEGORY_LABELS[p]
            cat_label = cat_info[0] if is_korean else cat_info[1]
            break
            
    if not cat_label:
        if "overview" in file_path.name:
            cat_label = "개요" if is_korean else "Overview"
        elif "comparative" in file_path.name:
            cat_label = "비교분석" if is_korean else "Comparative Analysis"
        elif "glossary" in file_path.name:
            cat_label = "용어집" if is_korean else "Glossary"
        elif "final_review" in file_path.name:
            cat_label = "종합 벤치마킹" if is_korean else "Benchmarking"
        else:
            cat_label = "상세 리포트" if is_korean else "Detail Report"
            
    # Extract date & tier from blockquote
    date_val = "2026-04-17"
    tier_val = ""
    
    body_lines = body.splitlines()
    cleaned_body_lines = []
    in_meta_block = True
    
    for idx, line in enumerate(body_lines):
        if in_meta_block:
            # Look for date
            m_date = re.search(r'(?:최종 (?:수정일|업데이트)|Date)\s*:\s*\*?\*?\s*([0-9]{4}-[0-9]{2}-[0-9]{2})', line, re.IGNORECASE)
            if m_date:
                date_val = m_date.group(1)
            
            # Look for tier
            m_tier = re.search(r'(?:조사 등급|Tier)\s*:\s*\*?\*?\s*(Tier\s*[1-3]|T[1-3])', line, re.IGNORECASE)
            if m_tier:
                tier_val = m_tier.group(1).upper()
                
            if line.strip().startswith('>') or line.strip() == '---' or line.strip() == '':
                continue
            else:
                in_meta_block = False
                cleaned_body_lines.append(line)
        else:
            cleaned_body_lines.append(line)
            
    # Counterpart link
    counterpart_url = get_counterpart_url(rel_path)
    
    # Build premium meta header HTML
    header_html = ['```{=html}', '<div class="doc-header-card">', '  <div class="doc-header-left">']
    
    badge_bread = f'<span class="doc-badge category">📁 {domain_label} &gt; {cat_label}</span>'
    header_html.append(f'    {badge_bread}')
    
    if tier_val:
        tier_text = f"⭐ {tier_val} 공식자료 기반" if is_korean else f"⭐ {tier_val} Primary Source"
        header_html.append(f'    <span class="doc-badge tier">{tier_text}</span>')
    else:
        doc_type_text = "📑 심층 분석 리포트" if is_korean else "📑 In-Depth Research"
        header_html.append(f'    <span class="doc-badge tier">{doc_type_text}</span>')
        
    date_text = f"📅 {date_val}"
    header_html.append(f'    <span class="doc-badge date">{date_text}</span>')
    header_html.append('  </div>')
    
    if counterpart_url:
        lang_btn_text = "🌐 Read in English" if is_korean else "🇰🇷 한국어 리포트 보기"
        header_html.append('  <div class="doc-header-right">')
        header_html.append(f'    <a href="{counterpart_url}" class="doc-lang-btn">{lang_btn_text}</a>')
        header_html.append('  </div>')
        
    header_html.append('</div>')
    header_html.append('```\n\n')
    
    new_content = new_fm + "\n".join(header_html) + "\n".join(cleaned_body_lines) + "\n"
    file_path.write_text(new_content, encoding="utf-8")

def main():
    count = 0
    for root, _, files in os.walk(QMD_DIR):
        for f in files:
            if f.endswith('.qmd'):
                p = Path(root) / f
                process_qmd_file(p)
                count += 1
    print(f"Successfully enhanced {count} detail QMD files with premium header cards and language toggles!")

if __name__ == '__main__':
    main()
