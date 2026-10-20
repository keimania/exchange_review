#!/usr/bin/env python3
"""
scripts/format_index_qmd.py
Wraps raw HTML blocks in index.qmd inside ```{=html} ``` blocks
so Pandoc does not misinterpret indentations as <pre><code>.
"""

from pathlib import Path
import re

ROOT_DIR = Path(__file__).resolve().parent.parent
INDEX_FILE = ROOT_DIR / "index.qmd"

def main():
    content = INDEX_FILE.read_text(encoding="utf-8")
    
    # Split frontmatter
    parts = content.split("---", 2)
    if len(parts) < 3:
        print("Frontmatter split failed")
        return
    
    frontmatter = f"---{parts[1]}---\n\n"
    body = parts[2].strip()
    
    # We want to format body into clean blocks:
    # 1. Hero & Quick Actions & Filter (raw html)
    # 2. panel-tabset with 4 tabs
    # Each tab has its heading (## ...) followed by ```{=html} <content> ```
    
    # Let's inspect headings in body
    # Headings are:
    # ::: {.panel-tabset}
    # ## 📈 주식시장 (Equities)
    # ...
    # ## ⚡ 파생상품 (Derivatives)
    # ...
    # ## 🛡️ 청산·결제 (Clearing)
    # ...
    # ## 📚 벤치마킹 & 용어집 (Reference)
    # ...
    # :::
    
    # Let's split by '## '
    sections = re.split(r'\n(?=## )', body)
    
    top_part = sections[0]
    tab_sections = sections[1:]
    
    # In top_part, isolate ::: {.hero-container} to before ::: {.panel-tabset}
    top_clean = top_part.replace("::: {.hero-container}", '<div class="hero-container">').replace(":::\n\n<div class=\"quick-action-bar\">", '</div>\n\n<div class="quick-action-bar">')
    
    # If there is ::: {.panel-tabset} in top_part, split it
    tabset_marker = "::: {.panel-tabset}"
    if tabset_marker in top_clean:
        pre_tabset, post_tabset = top_clean.split(tabset_marker, 1)
    else:
        pre_tabset = top_clean
        post_tabset = ""
    
    formatted_body = []
    
    # Top raw html
    formatted_body.append("```{=html}\n" + pre_tabset.strip() + "\n```\n\n")
    formatted_body.append("::: {.panel-tabset}\n\n")
    
    for sec in tab_sections:
        # First line is ## Tab Title
        sec_lines = sec.split("\n", 1)
        tab_title = sec_lines[0].strip()
        sec_body = sec_lines[1] if len(sec_lines) > 1 else ""
        
        # Check if ::: (end of tabset) is at the end of the last section
        end_tabset = False
        if "\n:::" in sec_body:
            sec_body, after_tabset = sec_body.split("\n:::", 1)
            end_tabset = True
        else:
            after_tabset = ""
            
        formatted_body.append(f"{tab_title}\n\n")
        formatted_body.append("```{=html}\n" + sec_body.strip() + "\n```\n\n")
        
        if end_tabset:
            formatted_body.append(":::\n\n")
            if after_tabset.strip():
                formatted_body.append("```{=html}\n" + after_tabset.strip() + "\n```\n\n")
                
    full_output = frontmatter + "".join(formatted_body)
    INDEX_FILE.write_text(full_output, encoding="utf-8")
    print("Successfully reformatted index.qmd with ```{=html} blocks!")

if __name__ == "__main__":
    main()
