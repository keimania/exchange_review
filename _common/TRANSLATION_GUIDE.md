# Translation Guide (English → Korean)

This document defines standards for translating exchange research documents from English to Korean.

---

## 1. General Principles

1. **Accuracy over fluency:** Technical accuracy takes priority over natural-sounding Korean.
2. **Consistent terminology:** Always use `glossary_ko.md` for term translations. Never translate the same term differently across documents.
3. **Preserve structure:** Maintain the same heading structure, table format, and section numbering as the English original.
4. **Keep proper nouns in English:** Exchange names, system names, protocol names, and organization names remain in English with Korean reading in parentheses on first mention.
   - Example: "NYSE (뉴욕증권거래소)" on first mention, then "NYSE" thereafter
5. **Technical terms:** Use the established Korean financial term if one exists. If no standard Korean term exists, use the English term with a Korean explanation in parentheses.

---

## 2. Term Translation Rules

### 2.1 Terms to Keep in English (Do Not Translate)
- System names: Exigo, Optiq, INET, Genium, etc.
- Protocol names: FIX, ITCH, OUCH, FAST, SWIFT, ISO 20022
- Technical abbreviations: API, STP, DMA, HFT, FPGA
- Acronyms widely used in Korean finance: ETF, ETN, ELS, DLS, CCP, CSD, DVP

### 2.2 Terms to Translate to Korean
- General financial concepts: market, order, trade, settlement, clearing
- Descriptions and explanations
- Section headings (but keep English in parentheses)
  - Example: "## 5. 매매시스템 (Trading System)"

### 2.3 Hybrid Approach for Specialized Terms
Format: **Korean Term (English Term)**
- Example: 중앙청산소 (Central Counterparty, CCP)
- Example: 가격제한폭 (Price Limit)
- Example: 호가단위 (Tick Size)

---

## 3. Style Guidelines

### 3.1 Sentence Style
- Use formal written Korean (합니다체 or 한다체 — use 한다체 for research documents)
- Avoid overly long sentences; break into shorter units
- Use bullet points and tables where appropriate

### 3.2 Numbers and Units
- Use Arabic numerals for all numbers
- Currency: Use original currency with KRW equivalent where helpful
  - Example: "100억 USD (약 13조 원)"
- Percentages: 5% (maintain as-is)
- Time: Convert to KST where relevant, but always show original timezone
  - Example: "09:30 EST (23:30 KST)"

### 3.3 Dates
- Use YYYY-MM-DD format (same as English version)
- For historical dates in prose: YYYY년 MM월

### 3.4 Tables
- Translate column headers to Korean
- Keep data cells in their original language if they are proper nouns or technical terms
- Translate descriptive content in cells

---

## 4. Document-Specific Guidelines

### 4.1 Exchange Profile Documents
- Translate all descriptive content
- Keep exchange names, system names in English
- Translate table headers
- Add KRX comparison notes where relevant (in a separate subsection, not inline)

### 4.2 System/Technology Documents
- Keep most technical specifications in English (latency numbers, protocol names)
- Translate architectural descriptions
- Translate section headings with English in parentheses

### 4.3 Regulatory Documents
- Use official Korean translations of foreign regulations if they exist
- For regulation names, keep English with Korean description
  - Example: "Regulation NMS (전미시장제도규정)"

---

## 5. Quality Checklist for Translation

- [ ] All terms consistent with glossary_ko.md
- [ ] Exchange/system proper nouns kept in English
- [ ] Korean reading provided on first mention of each proper noun
- [ ] Table structure matches English original
- [ ] Numbers and units properly formatted
- [ ] No machine-translation artifacts (unnatural phrasing)
- [ ] KRX context notes added where valuable
- [ ] Source citations preserved as-is (do not translate URLs or source names)

---

## 6. Workflow

1. Read the complete English document first
2. Check glossary_ko.md for all terms in the document
3. Add any missing terms to both glossary_en.md and glossary_ko.md
4. Translate section by section, preserving structure
5. Review against quality checklist
6. Final read-through for natural Korean flow
