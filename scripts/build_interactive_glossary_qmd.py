#!/usr/bin/env python3
"""
Generates interactive QMD glossary pages (qmd/reference/glossary_ko.qmd & glossary_en.qmd)
from md/_common/glossary_ko.md & md/_common/glossary_en.md with:
- Real-time search input + match highlighting + clear button
- Category filter pills with counts
- KRX/Korea-related terms quick toggle
- A-Z alphabetical filter bar
- Click-to-copy term & definition toast
"""

from pathlib import Path

ROOT = Path("/Users/jamin/Library/CloudStorage/GoogleDrive-jamingoo83@gmail.com/My Drive/Code/Antigravity/exchange_review")

EXPLORER_CSS_AND_JS = """```{=html}
<style>
.glossary-explorer-panel {
  position: sticky;
  top: 60px;
  z-index: 90;
  background: var(--bg-card);
  border: 1px solid var(--border-color);
  border-radius: var(--radius-md);
  padding: 1rem 1.25rem;
  margin-bottom: 1.75rem;
  box-shadow: 0 6px 20px rgba(15, 23, 42, 0.07);
}
.g-search-row {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  gap: 0.65rem;
  margin-bottom: 0.8rem;
}
.g-search-wrap {
  flex: 1;
  min-width: 240px;
  position: relative;
}
.g-search-input {
  width: 100%;
  padding: 0.6rem 2.4rem 0.6rem 2.35rem;
  border: 1.5px solid #cbd5e1;
  border-radius: 10px;
  font-size: 0.92rem;
  font-weight: 500;
  background: var(--bg-page);
  color: var(--text-main);
  outline: none;
  transition: var(--transition);
}
.g-search-input:focus {
  border-color: var(--primary-light);
  background: var(--bg-card);
  box-shadow: 0 0 0 3px rgba(37, 99, 235, 0.16);
}
.g-search-icon {
  position: absolute;
  left: 0.8rem;
  top: 50%;
  transform: translateY(-50%);
  font-size: 0.95rem;
  pointer-events: none;
}
.g-clear-btn {
  position: absolute;
  right: 0.6rem;
  top: 50%;
  transform: translateY(-50%);
  border: none;
  background: #e2e8f0;
  color: #475569;
  width: 22px;
  height: 22px;
  border-radius: 50%;
  font-size: 0.75rem;
  font-weight: 800;
  cursor: pointer;
  display: none;
  align-items: center;
  justify-content: center;
}
.g-krx-toggle {
  padding: 0.55rem 0.95rem;
  border-radius: 10px;
  border: 1.5px solid #93c5fd;
  background: var(--primary-subtle);
  color: #1e40af;
  font-size: 0.84rem;
  font-weight: 700;
  cursor: pointer;
  transition: var(--transition);
  white-space: nowrap;
}
.g-krx-toggle.active {
  background: #2563eb;
  border-color: #1d4ed8;
  color: #ffffff;
}
.g-count-badge {
  font-size: 0.83rem;
  font-weight: 700;
  color: var(--text-muted);
  padding: 0.45rem 0.8rem;
  background: var(--bg-page);
  border: 1px solid var(--border-color);
  border-radius: 8px;
  white-space: nowrap;
}
.g-cat-row {
  display: flex;
  flex-wrap: wrap;
  gap: 0.4rem;
  margin-bottom: 0.65rem;
}
.g-cat-chip {
  padding: 0.3rem 0.75rem;
  border-radius: 9999px;
  border: 1px solid var(--border-color);
  background: var(--bg-page);
  color: var(--text-muted);
  font-size: 0.8rem;
  font-weight: 700;
  cursor: pointer;
  transition: var(--transition);
}
.g-cat-chip:hover {
  border-color: #93c5fd;
  color: var(--primary-light);
}
.g-cat-chip.active {
  background: #1e3a8a;
  border-color: #1e3a8a;
  color: #ffffff;
}
.g-az-row {
  display: flex;
  flex-wrap: wrap;
  gap: 3px;
  padding-top: 0.5rem;
  border-top: 1px dashed var(--border-color);
}
.g-az-btn {
  min-width: 27px;
  height: 26px;
  padding: 0 5px;
  border-radius: 5px;
  border: 1px solid transparent;
  background: transparent;
  color: var(--text-muted);
  font-size: 0.76rem;
  font-weight: 800;
  cursor: pointer;
  transition: var(--transition);
}
.g-az-btn:hover:not(:disabled) {
  background: var(--primary-subtle);
  color: var(--primary-light);
}
.g-az-btn.active {
  background: #2563eb;
  color: #ffffff;
}
.g-az-btn:disabled {
  opacity: 0.28;
  cursor: not-allowed;
}
mark.glossary-hl {
  background: #fef08a;
  color: #0f172a;
  padding: 0 2px;
  border-radius: 3px;
  font-weight: 700;
}
.g-empty-state {
  display: none;
  text-align: center;
  padding: 3rem 1.5rem;
  background: var(--bg-card);
  border: 1px dashed var(--border-color);
  border-radius: var(--radius-md);
  margin: 1.5rem 0;
}
.g-copy-toast {
  position: fixed;
  bottom: 24px;
  left: 50%;
  transform: translateX(-50%) translateY(20px);
  background: #0f172a;
  color: #ffffff;
  padding: 0.6rem 1.2rem;
  border-radius: 9999px;
  font-size: 0.85rem;
  font-weight: 700;
  box-shadow: 0 10px 25px rgba(0,0,0,0.25);
  opacity: 0;
  pointer-events: none;
  transition: all 0.22s ease;
  z-index: 2000;
}
.g-copy-toast.show {
  opacity: 1;
  transform: translateX(-50%) translateY(0);
}
#quarto-document-content table tbody tr {
  cursor: pointer;
}
@media (max-width: 768px) {
  .glossary-explorer-panel {
    position: static;
    padding: 0.85rem;
  }
}
</style>

<div class="glossary-explorer-panel" id="glossaryExplorer">
  <div class="g-search-row">
    <div class="g-search-wrap">
      <span class="g-search-icon">🔍</span>
      <input type="text" id="gSearchInput" class="g-search-input" placeholder="__SEARCH_PLACEHOLDER__">
      <button type="button" id="gClearBtn" class="g-clear-btn" title="Clear">✕</button>
    </div>
    <button type="button" id="gKrxToggle" class="g-krx-toggle">__KRX_BTN_LABEL__</button>
    <span id="gCountBadge" class="g-count-badge">420 / 420</span>
  </div>
  <div class="g-cat-row" id="gCatRow"></div>
  <div class="g-az-row" id="gAzRow"></div>
</div>

<div class="g-empty-state" id="gEmptyState">
  <div style="font-size:2rem; margin-bottom:0.5rem;">🔎</div>
  <div style="font-weight:800; font-size:1.05rem; margin-bottom:0.35rem;">__EMPTY_TITLE__</div>
  <div style="font-size:0.88rem; color:var(--text-muted); margin-bottom:1rem;">__EMPTY_DESC__</div>
  <button type="button" class="g-krx-toggle active" id="gResetAllBtn">__RESET_LABEL__</button>
</div>
<div class="g-copy-toast" id="gCopyToast">📋 __TOAST_LABEL__</div>

<script>
(function() {
  const IS_KO = __IS_KO__;
  let activeCat = 'ALL';
  let activeLetter = 'ALL';
  let krxOnly = false;

  function initGlossaryExplorer() {
    const main = document.getElementById('quarto-document-content');
    if (!main) return;

    const sections = Array.from(main.querySelectorAll('section.level2'));
    if (!sections.length) return;

    const searchInput = document.getElementById('gSearchInput');
    const clearBtn = document.getElementById('gClearBtn');
    const krxBtn = document.getElementById('gKrxToggle');
    const catRow = document.getElementById('gCatRow');
    const azRow = document.getElementById('gAzRow');
    const countBadge = document.getElementById('gCountBadge');
    const emptyState = document.getElementById('gEmptyState');
    const resetAllBtn = document.getElementById('gResetAllBtn');
    const toast = document.getElementById('gCopyToast');

    // Index all rows and preserve original HTML for clean highlighting
    const allItems = [];
    const catMeta = [];

    sections.forEach((sec, sIdx) => {
      const h2 = sec.querySelector('h2');
      const catName = h2 ? h2.textContent.trim() : ('Category ' + (sIdx + 1));
      const rows = Array.from(sec.querySelectorAll('table tbody tr'));
      catMeta.push({ id: 'cat-' + sIdx, name: catName, count: rows.length, section: sec });

      rows.forEach(tr => {
        const cells = Array.from(tr.querySelectorAll('td'));
        const origHtml = cells.map(td => td.innerHTML);
        const fullText = tr.textContent.toLowerCase();
        const firstTerm = (cells[0] ? cells[0].textContent.trim() : '');
        const firstChar = firstTerm ? firstTerm[0].toUpperCase() : '';
        const letter = /^[A-Z]$/.test(firstChar) ? firstChar : '0-9';
        const isKrx = /(krx|한국거래소|nextrade|nxt|넥스트레이드|ksd|예탁결제원|koscom|코스콤|코스피|코스닥|kospi|kosdaq|자본시장법|전자증권법|동시호가|단일가매매|접속매매|최유리|최우선|스톱지정가|중간가호가|nsds)/i.test(fullText);

        tr.title = IS_KO ? '클릭하면 용어와 정의를 복사합니다' : 'Click to copy term & definition';
        tr.addEventListener('click', function() {
          if (window.getSelection && window.getSelection().toString().length > 0) return;
          const copyStr = cells.map(c => c.textContent.trim()).filter(Boolean).join(' — ');
          if (navigator.clipboard) {
            navigator.clipboard.writeText(copyStr).then(() => {
              toast.classList.add('show');
              setTimeout(() => toast.classList.remove('show'), 1800);
            });
          }
        });

        allItems.push({
          tr, cells, origHtml, fullText, letter, isKrx,
          catId: 'cat-' + sIdx, section: sec
        });
      });
    });

    const totalCount = allItems.length;

    // Render Category Pills
    const allLabel = IS_KO ? `전체 (${totalCount})` : `All (${totalCount})`;
    let catHtml = `<button type="button" class="g-cat-chip active" data-cat="ALL">${allLabel}</button>`;
    catMeta.forEach(c => {
      const shortName = c.name.replace(/\\s*\\([^)]*\\)/, '');
      catHtml += `<button type="button" class="g-cat-chip" data-cat="${c.id}">${shortName} (${c.count})</button>`;
    });
    catRow.innerHTML = catHtml;

    catRow.querySelectorAll('.g-cat-chip').forEach(btn => {
      btn.addEventListener('click', function() {
        activeCat = this.getAttribute('data-cat');
        catRow.querySelectorAll('.g-cat-chip').forEach(b => b.classList.remove('active'));
        this.classList.add('active');
        applyGlossaryFilter();
      });
    });

    // Render A-Z Bar
    const letters = ['ALL', '0-9', ...'ABCDEFGHIJKLMNOPQRSTUVWXYZ'.split('')];
    azRow.innerHTML = letters.map(l =>
      `<button type="button" class="g-az-btn ${l === 'ALL' ? 'active' : ''}" data-letter="${l}">${l}</button>`
    ).join('');

    azRow.querySelectorAll('.g-az-btn').forEach(btn => {
      btn.addEventListener('click', function() {
        activeLetter = this.getAttribute('data-letter');
        azRow.querySelectorAll('.g-az-btn').forEach(b => b.classList.remove('active'));
        this.classList.add('active');
        applyGlossaryFilter();
      });
    });

    function escapeRegExp(s) {
      return s.replace(/[.*+?^${}()|[\\]\\\\]/g, '\\\\$&');
    }

    function highlightHtml(html, q) {
      if (!q) return html;
      const rx = new RegExp('(' + escapeRegExp(q) + ')', 'gi');
      // Only highlight text outside HTML tags
      return html.replace(/(>[^<]*<|^[^<]*<|>[^<]*$|^[^<]*$)/g, function(seg) {
        return seg.replace(rx, '<mark class="glossary-hl">$1</mark>');
      });
    }

    function applyGlossaryFilter() {
      const q = (searchInput.value || '').trim().toLowerCase();
      clearBtn.style.display = q ? 'inline-flex' : 'none';

      // Update available letters under current cat + krx + query
      const availLetters = new Set(['ALL']);
      allItems.forEach(item => {
        if ((activeCat === 'ALL' || item.catId === activeCat) &&
            (!krxOnly || item.isKrx) &&
            (!q || item.fullText.includes(q))) {
          availLetters.add(item.letter);
        }
      });
      azRow.querySelectorAll('.g-az-btn').forEach(btn => {
        const l = btn.getAttribute('data-letter');
        btn.disabled = !availLetters.has(l) && l !== activeLetter;
      });

      let visibleCount = 0;
      const secVisibleCounts = {};

      allItems.forEach(item => {
        const matchCat = activeCat === 'ALL' || item.catId === activeCat;
        const matchKrx = !krxOnly || item.isKrx;
        const matchLetter = activeLetter === 'ALL' || item.letter === activeLetter;
        const matchQ = !q || item.fullText.includes(q);

        if (matchCat && matchKrx && matchLetter && matchQ) {
          item.tr.style.display = '';
          visibleCount++;
          secVisibleCounts[item.catId] = (secVisibleCounts[item.catId] || 0) + 1;
          item.cells.forEach((td, i) => {
            td.innerHTML = q ? highlightHtml(item.origHtml[i], q) : item.origHtml[i];
          });
        } else {
          item.tr.style.display = 'none';
        }
      });

      catMeta.forEach(c => {
        c.section.style.display = (secVisibleCounts[c.id] > 0) ? '' : 'none';
      });

      countBadge.textContent = IS_KO
        ? `${visibleCount} / ${totalCount}개 표시`
        : `${visibleCount} / ${totalCount} terms`;

      emptyState.style.display = visibleCount === 0 ? 'block' : 'none';
    }

    searchInput.addEventListener('input', applyGlossaryFilter);
    clearBtn.addEventListener('click', function() {
      searchInput.value = '';
      applyGlossaryFilter();
      searchInput.focus();
    });
    krxBtn.addEventListener('click', function() {
      krxOnly = !krxOnly;
      this.classList.toggle('active', krxOnly);
      applyGlossaryFilter();
    });
    resetAllBtn.addEventListener('click', function() {
      searchInput.value = '';
      activeCat = 'ALL';
      activeLetter = 'ALL';
      krxOnly = false;
      krxBtn.classList.remove('active');
      catRow.querySelectorAll('.g-cat-chip').forEach((b, i) => b.classList.toggle('active', i === 0));
      azRow.querySelectorAll('.g-az-btn').forEach((b, i) => b.classList.toggle('active', i === 0));
      applyGlossaryFilter();
    });

    applyGlossaryFilter();
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initGlossaryExplorer);
  } else {
    initGlossaryExplorer();
  }
})();
</script>
```
"""

def build_glossary_qmd(md_path: Path, qmd_path: Path, is_ko: bool):
    lines = md_path.read_text(encoding="utf-8").splitlines()
    title = lines[0].lstrip("# ").strip()
    # Skip header & blockquote & ---
    body_start = 0
    for i, l in enumerate(lines):
        if l.startswith("## "):
            body_start = i
            break
    body = "\n".join(lines[body_start:])

    fm = f"""---
title: "{title}"
subtitle: "{'참고자료' if is_ko else 'Reference'}"
date: "2026-11-24"
lang: {'ko' if is_ko else 'en'}
toc: true
toc-depth: 3
number-sections: false
format:
  html:
    theme: cosmo
    toc: true
    self-contained: false
---

```{{=html}}
<div class="doc-header-card">
  <div class="doc-header-left">
    <span class="doc-badge category">📁 {'참고자료 &gt; 용어집' if is_ko else 'Reference &gt; Glossary'}</span>
    <span class="doc-badge tier">📖 {'420개 한·영 전문 용어집' if is_ko else '420 Bilingual Terms'}</span>
    <span class="doc-badge date">📅 2026-11-24</span>
  </div>
  <div class="doc-header-right">
    <a href="{'glossary_en.html' if is_ko else 'glossary_ko.html'}" class="doc-lang-btn">{'🌐 Read in English' if is_ko else '🇰🇷 한국어 용어집 보기'}</a>
  </div>
</div>
```

"""
    ui_block = (
        EXPLORER_CSS_AND_JS
        .replace("__IS_KO__", "true" if is_ko else "false")
        .replace("__SEARCH_PLACEHOLDER__",
                 "영문·국문 용어, 약어(SOR, OIO, VI), 정의, KRX 규정 실시간 검색... (단축키: / )"
                 if is_ko else
                 "Search terms, abbreviations (SOR, OIO, VI), definitions, KRX notes... (Press / )")
        .replace("__KRX_BTN_LABEL__", "🇰🇷 한국(KRX·NXT·KSD) 핵심 용어만" if is_ko else "🇰🇷 Korea / KRX / NXT Only")
        .replace("__EMPTY_TITLE__", "검색 조건과 일치하는 용어가 없습니다." if is_ko else "No matching glossary terms found.")
        .replace("__EMPTY_DESC__", "검색어나 카테고리·알파벳 필터를 초기화해 보세요." if is_ko else "Try clearing your search query or active category/letter filters.")
        .replace("__RESET_LABEL__", "필터 전체 초기화" if is_ko else "Reset All Filters")
        .replace("__TOAST_LABEL__", "클립보드에 용어와 정의가 복사되었습니다!" if is_ko else "Copied term & definition to clipboard!")
    )

    qmd_path.write_text(fm + ui_block + "\n" + body + "\n", encoding="utf-8")
    print("Generated interactive glossary:", qmd_path.relative_to(ROOT))

if __name__ == "__main__":
    build_glossary_qmd(ROOT / "md/_common/glossary_ko.md", ROOT / "qmd/reference/glossary_ko.qmd", is_ko=True)
    build_glossary_qmd(ROOT / "md/_common/glossary_en.md", ROOT / "qmd/reference/glossary_en.qmd", is_ko=False)
