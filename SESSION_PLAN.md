# Session Execution Plan — Global Exchange Research

> **총 14세션** (준비 1 + 영어 조사 6 + 한국어 번역 3 + 용어집/DB 1 + 최종 검토 1 + DOCX 1 + 웹 퍼블리싱 1)
> 각 세션은 독립적으로 실행 가능하며, 순서대로 진행을 권장한다.

---

## 핵심 원칙: 참조 자료 우선 (Reference-First Research)

> `00_references/` 폴더에 거래소별 공식 자료(규정, 규칙, 시행세칙, 기술문서 등)가 사전에 업로드되어 있다.
> **이 자료를 1차 자료(primary source)로 우선 활용**하고, 웹 검색은 보충 자료로 사용한다.

### 참조 자료 디렉토리 구조

```
00_references/
├── krx/                         # 한국거래소 (예시 — 현재 업로드 완료)
│   ├── 유가증권시장 업무규정_전문_20260129.txt
│   ├── 유가증권시장 업무규정 시행세칙_전문_20260401.txt
│   ├── 유가증권시장 상장규정_전문_20250710.txt
│   ├── 유가증권시장 상장규정 시행세칙_전문_20251111.txt
│   ├── 유가증권시장 공시규정_전문_20250801.txt
│   ├── 유가증권시장 공시규정 시행세칙_전문_20250801.txt
│   ├── 파생상품시장 업무규정_전문_20250609.txt
│   ├── 파생상품시장 업무규정 시행세칙_전문_20251027.txt
│   ├── 증권시장 청산결제 업무규정_전문_20260304.txt
│   └── 증권시장 청산결제 업무규정 시행세칙_전문_20250304.txt
├── jpx/                         # JPX (규칙 업로드 시)
├── hkex/                        # HKEX (규칙 업로드 시)
├── cme/                         # CME Group
└── ...                          # 기타 거래소
```

### 참조 자료 활용 규칙

1. **참조 자료가 있는 거래소 → 자동 Tier 1 (Deep Dive) 격상**
   - 참조 자료가 없더라도 Tier 1인 거래소는 웹 검색으로 Tier 1 수준 유지
   - 참조 자료가 있는 Tier 2/3 거래소는 해당 참조 범위 내에서 Tier 1 깊이로 조사
2. **조사 우선순위:** 참조 자료 읽기 → 웹 검색으로 보충 → 교차 검증
3. **인용 형식:** 참조 자료 인용 시 `[Source: {파일명}, Article/조항 XX]` 형식 사용
4. **원어 용어 보존:** 참조 자료가 해당 거래소의 현지어인 경우, 핵심 용어는 원어를 그대로 사용
   - 예: KRX 규정의 동시호가, 접속매매, 정적VI, 동적VI, 손해배상공동기금
   - 예: JPX 규칙의 板寄せ (이타요세), ザラバ (자라바)

---

## Phase 0: 사전 준비 (1세션)

#### Session P0 — 환경 설정 및 참조 자료 확인
- **작업 디렉토리:** `exchange_review/` (루트)
- **지시 프롬프트:**
```
STEP 1: Verify project structure exists:
  _common/ (RESEARCH_GUIDE.md, TEMPLATE_*.md, TRANSLATION_GUIDE.md, glossary_*.md)
  01_equities/, 02_derivatives/, 03_clearing/ (각각 en/, ko/, CLAUDE.md)
  00_references/ (거래소별 서브 디렉토리)
Create any missing directories.

STEP 2: Scan 00_references/ and inventory all available reference materials.
Create/update 00_references/INVENTORY.md listing:
  - Exchange/organization name
  - Files available
  - Language
  - Coverage (equities, derivatives, clearing, or multiple)
  - Date of document

STEP 3: Based on the inventory, determine Tier assignments:
  - Any exchange with reference materials → Tier 1 depth for covered areas
  - Update each domain's CLAUDE.md to reflect adjusted Tier assignments

STEP 4: Initialize glossary files and overview templates if not already present.

STEP 5: Create _common/glossary.db (SQLite with FTS5) if not present.
```
- **예상 산출물:** `00_references/INVENTORY.md`, 디렉토리 구조 확인, Tier 배정 조정
- **상태:** ⬜ Not started

---

## Phase 1: 영어 조사 (6세션)

> 각 세션의 프롬프트에는 다음 공통 지시가 적용된다:
> - `00_references/` 내 해당 거래소의 참조 자료를 **먼저 읽고** 1차 자료로 활용
> - 참조 자료가 없는 거래소는 웹 검색만으로 조사
> - 참조 자료의 구체적 조항/조문 번호를 인용에 포함

### ━━━ Equities (유가증권시장) ━━━

#### Session E1 — Equities Tier 1 (Part 1)
- **작업 디렉토리:** `01_equities/`
- **대상:** NYSE, NASDAQ, LSE + **참조 자료가 있는 거래소 (해당 시)**
- **지시 프롬프트:**
```
Read CLAUDE.md and ../_common/RESEARCH_GUIDE.md first.
Check ../00_references/ for any reference materials related to the target exchanges.

Research the following exchanges IN PARALLEL using subagents:
1. NYSE (New York Stock Exchange)
2. NASDAQ
3. LSE (London Stock Exchange)

For each exchange:
- **FIRST** read any files in ../00_references/{exchange}/ if they exist
  → These are PRIMARY sources. Extract specific data: article numbers, exact thresholds,
    exact rules, fee schedules, trading hours, order types, circuit breaker parameters.
  → If the reference is in a non-English language, preserve key terms in original language
    and provide English translation.
- THEN search the web for supplementary info (annual reports, technical specs, recent updates)
- Use the template from ../_common/TEMPLATE_EXCHANGE.md
- Fill ALL 11 sections thoroughly — especially Section 5 (Trading System) and Section 8 (Risk Controls)
- Save to en/exchanges/{exchange_name}.md
- Include specific numbers: latency, throughput, market cap, trading volume
- Cite reference files as: [Source: {filename}, Article XX] or [Source: {filename}, Section X.X]

After all are done:
- Update ../_common/glossary_en.md with any new terms found
- Update en/01_overview.md status to "Completed" for these exchanges
```
- **예상 산출물:** 3+ 거래소 파일
- **상태:** ⬜ Not started

---

#### Session E2 — Equities Tier 1 (Part 2)
- **작업 디렉토리:** `01_equities/`
- **대상:** JPX (TSE), HKEX, SGX + **참조 자료가 있는 거래소 (해당 시)**
- **지시 프롬프트:**
```
Read CLAUDE.md and ../_common/RESEARCH_GUIDE.md first.
Check ../00_references/ for any reference materials related to the target exchanges.

Research the following exchanges IN PARALLEL using subagents:
1. JPX / Tokyo Stock Exchange
2. HKEX (Hong Kong Exchanges)
3. SGX (Singapore Exchange)

For each exchange:
- **FIRST** read any files in ../00_references/{exchange}/ if they exist
  → PRIMARY sources. Extract specific rules, thresholds, article numbers.
  → Preserve key terms in original language (日本語, 中文) with English translation.
- THEN search the web for supplementary info
- Use ../_common/TEMPLATE_EXCHANGE.md
- Fill ALL 11 sections thoroughly
- Save to en/exchanges/{exchange_name}.md
- Note Asia-specific features (lunch break, price limits, etc.)

After all are done:
- Update ../_common/glossary_en.md with any new terms found
- Update en/01_overview.md status
```
- **예상 산출물:** 3+ 거래소 파일
- **상태:** ⬜ Not started

---

#### Session E3 — Equities Tier 2 + Tier 3 + Systems + Regulations + Comparative
- **작업 디렉토리:** `01_equities/`
- **대상:** Tier 2/3 거래소 + 시스템 분석 + 규제 분석 + 비교분석
- **지시 프롬프트:**
```
Read CLAUDE.md and ../_common/RESEARCH_GUIDE.md first.
Check ../00_references/ for any reference materials — exchanges with references get Tier 1 depth.

STEP 1: Research Tier 2 exchanges IN PARALLEL (5 exchanges):
- Euronext, Deutsche Borse (Xetra), ASX, TMX, SIX Swiss Exchange
- For any with files in ../00_references/{exchange}/, read those FIRST as primary sources
  and upgrade to Tier 1 depth for the areas covered by the references.
- Use ../_common/TEMPLATE_EXCHANGE.md
- Standard depth (or Tier 1 if references available) — all sections
- Save to en/exchanges/

STEP 2: Research Tier 3 exchanges IN PARALLEL (remaining exchanges):
- SSE, SZSE, BSE, NSE India, TWSE, Borsa Italiana, BME, Nasdaq Nordic, Tadawul, JSE, Bursa Malaysia
- Same rule: check ../00_references/ first, upgrade depth if references available
- Overview depth (unless references available) — focus on Sections 1, 2, 3, 5, 8, 9
- Save to en/exchanges/

STEP 3: Create trading system deep-dive files in en/systems/ using ../_common/TEMPLATE_SYSTEM.md.
Create one file per major trading platform:
- pillar.md (NYSE), inet.md (NASDAQ), millennium.md (LSE), arrowhead.md (JPX)
- orion.md (HKEX), titan.md (SGX), optiq.md (Euronext), t7.md (Deutsche Borse)
- PLUS any additional system files for exchanges with reference materials
  (e.g., exture_3.md for KRX if KRX references exist)
For each: architecture, performance specs, technology stack, evolution history.
Use reference materials as primary source where available.

STEP 4: Create regional regulation comparison files in en/regulations/:
- us_equities_regulation.md — Reg NMS, SEC/FINRA, SRO model, LULD/MWCB
- eu_equities_regulation.md — MiFID II/MiFIR, ESMA, transparency
- asia_equities_regulation.md — Japan, HK, Singapore, Korea, others with references
For exchanges with reference materials: cite specific articles/provisions.

STEP 5: Create en/02_comparative_analysis.md
- Compare ALL researched exchanges (including those from reference materials)
- Include rows for EVERY exchange in all comparison tables — no exchange should be missing
- Dimensions: trading system tech, market structure, circuit breakers, market data,
  co-location, fee models, regulatory framework

STEP 6: Complete en/01_overview.md with actual data (market cap rankings, trading volumes, etc.)

After done:
- Update ../_common/glossary_en.md
- Update en/01_overview.md status for all exchanges
```
- **예상 산출물:** Tier 2/3 거래소 파일 + 시스템 파일 + 규제 파일 + 비교분석 + 개요
- **상태:** ⬜ Not started

---

### ━━━ Derivatives (파생상품시장) ━━━

#### Session D1 — Derivatives Tier 1
- **작업 디렉토리:** `02_derivatives/`
- **대상:** CME Group, Eurex + **참조 자료가 있는 거래소 (해당 시)**
- **지시 프롬프트:**
```
Read CLAUDE.md and ../_common/RESEARCH_GUIDE.md first.
Check ../00_references/ for any reference materials related to derivatives exchanges.

Research the following exchanges IN PARALLEL using subagents:
1. CME Group (CME, CBOT, NYMEX, COMEX)
2. Eurex
3. [Any additional exchanges with derivatives-related reference materials in ../00_references/]

For each exchange:
- **FIRST** read any files in ../00_references/{exchange}/ if they exist
  → PRIMARY sources for: contract specifications, margin methodology, position limits,
    block trading rules, trading hours, circuit breakers, fee schedules
  → Extract specific article numbers, exact thresholds, exact rules
  → Preserve key terms in original language where applicable
- THEN search the web for supplementary info
- Use ../_common/TEMPLATE_EXCHANGE.md adapted for derivatives
- Fill ALL 11 sections PLUS derivatives-specific items from CLAUDE.md:
  * Product catalog (futures, options by underlying)
  * Key contract specifications (top 5 products by volume)
  * Margin framework (methodology details from reference materials if available)
  * Position limits
  * Block trading / EFP / EFS rules
- Save to en/exchanges/

After done:
- Update ../_common/glossary_en.md (margin/derivatives terms)
- Update en/01_overview.md status
```
- **예상 산출물:** 2+ 거래소 파일
- **상태:** ⬜ Not started

---

#### Session D2 — Derivatives Tier 1 (Part 2) + Tier 2/3 + Systems + Regulations + Comparative
- **작업 디렉토리:** `02_derivatives/`
- **대상:** 나머지 거래소 + 시스템 + 규제 + 비교분석
- **지시 프롬프트:**
```
Read CLAUDE.md and ../_common/RESEARCH_GUIDE.md first.
Check ../00_references/ for any reference materials.

STEP 1: Research Tier 1 Part 2 IN PARALLEL:
- HKEX Derivatives, SGX Derivatives, Cboe, ICE Futures, Osaka Exchange
- Check ../00_references/ for each; upgrade depth if references available
- Save to en/exchanges/

STEP 2: Research Tier 2/3 IN PARALLEL:
- Euronext Derivatives, ASX Derivatives, Montreal Exchange, CFFEX, DCE, SHFE,
  NSE F&O, TAIFEX, DME
- Check ../00_references/ for each; upgrade depth if references available
- Save to en/exchanges/

STEP 3: Create system deep-dive files in en/systems/:
- globex.md (CME), t7_derivatives.md (Eurex), genium_inet.md (Nasdaq/Nordic)
- PLUS any additional systems for exchanges with reference materials
For each: architecture, matching algorithm, performance, spread engine.

STEP 4: Create regulation files in en/regulations/:
- us_derivatives_regulation.md, eu_derivatives_regulation.md, asia_derivatives_regulation.md
Use reference materials for specific regulatory provisions where available.

STEP 5: Create en/02_comparative_analysis.md
- Include ALL exchanges (including reference-based) in every comparison table
- Dimensions: product coverage, trading tech, margin methodology, fees, trading hours,
  position limits, regulatory framework

STEP 6: Complete en/01_overview.md

After done:
- Update ../_common/glossary_en.md
- Update en/01_overview.md status
```
- **예상 산출물:** 전체 거래소 파일 + 시스템 파일 + 규제 파일 + 비교분석 + 개요
- **상태:** ⬜ Not started

---

### ━━━ Clearing & Settlement (청산결제) ━━━

#### Session C1 — Clearing Tier 1
- **작업 디렉토리:** `03_clearing/`
- **대상:** DTCC, LCH, OCC, CME Clearing, Eurex Clearing + **참조 자료가 있는 기관 (해당 시)**
- **지시 프롬프트:**
```
Read CLAUDE.md and ../_common/RESEARCH_GUIDE.md first.
Check ../00_references/ for any reference materials related to clearing organizations.

Research the following organizations IN PARALLEL using subagents:
1. DTCC (DTC/NSCC/FICC)
2. LCH (Ltd & SA)
3. OCC
4. CME Clearing
5. Eurex Clearing
6. [Any additional CCPs/CSDs with reference materials in ../00_references/]

For each:
- **FIRST** read any files in ../00_references/{organization}/ if they exist
  → PRIMARY sources for: default waterfall, margin methodology, clearing membership,
    settlement cycle, DVP model, recovery tools, assessment powers
  → Extract specific article numbers, KRW/USD figures, exact thresholds
  → Preserve key terms in original language where applicable
- THEN search the web for supplementary info (CPMI-IOSCO PQD, annual reports, rulebooks)
- Use ../_common/TEMPLATE_CLEARING.md
- Fill ALL 9 sections, especially:
  * Default waterfall with actual amounts where available
  * Margin methodology — detailed technical description
  * Recovery & resolution tools
  * Settlement finality
  * Interoperability arrangements
- Save to en/organizations/

After done:
- Update ../_common/glossary_en.md (clearing/settlement terms)
- Update en/01_overview.md status
```
- **예상 산출물:** 5+ 기관 파일
- **상태:** ⬜ Not started

---

#### Session C2 — Clearing Tier 2/3 + Systems + Regulations + Comparative
- **작업 디렉토리:** `03_clearing/`
- **대상:** 나머지 기관 + 시스템 + 규제 + 비교분석
- **지시 프롬프트:**
```
Read CLAUDE.md and ../_common/RESEARCH_GUIDE.md first.
Check ../00_references/ for any reference materials.

STEP 1: Research Tier 2 organizations IN PARALLEL:
- JSCC, HKEX Clearing (HKSCC/HKCC/SEOCH), CDP, EuroCCP, ICE Clear, ASX Clear
- Check ../00_references/ for each; upgrade depth if references available
- Save to en/organizations/

STEP 2: Research Tier 3 organizations IN PARALLEL:
- SIX x-clear, Euroclear, Clearstream, CSDC, CCIL, CDS Canada, Muqassa
- Plus any CSDs with reference materials (e.g., KSD if KRX references exist)
- Check ../00_references/ for each; upgrade depth if references available
- Save to en/organizations/

STEP 3: Create system deep-dive files in en/systems/:
- dtcc_systems.md, lch_systems.md, eurex_clearing_prisma.md
- PLUS any additional systems for organizations with reference materials
For each: architecture, capacity, STP rates, protocols, DR/BCP.

STEP 4: Create regulation files in en/regulations/:
- us_clearing_regulation.md, eu_clearing_regulation.md, asia_clearing_regulation.md
Use reference materials for specific regulatory provisions where available.

STEP 5: Create en/02_comparative_analysis.md
- Include ALL organizations (including reference-based) in every comparison table
- Dimensions: default waterfall, margin methodology, settlement cycle, DVP model,
  interoperability, PFMI compliance, technology, regulatory framework, fees

STEP 6: Complete en/01_overview.md

After done:
- Update ../_common/glossary_en.md
- Update en/01_overview.md status
```
- **예상 산출물:** 전체 기관 파일 + 시스템 파일 + 규제 파일 + 비교분석 + 개요
- **상태:** ⬜ Not started

---

## Phase 2: 한국어 번역 (3세션)

> 번역 시 참조 자료 원어 용어 보존 규칙:
> - 참조 자료가 한국어인 거래소(KRX 등): 규정 원문의 한국어 용어를 그대로 사용, 역번역 금지
> - 참조 자료가 일본어인 거래소(JPX 등): 일본어 원어 병기 가능
> - glossary_ko.md의 KRX 참고사항 열에 기재된 용어를 우선 사용

#### Session T1 — Equities 번역
- **작업 디렉토리:** `01_equities/`
- **지시 프롬프트:**
```
Read ../_common/TRANSLATION_GUIDE.md and ../_common/glossary_ko.md first.

Translate ALL files in en/ to Korean and save to ko/ with the same directory structure.

Rules:
1. Follow TRANSLATION_GUIDE.md strictly
2. Use glossary_ko.md for consistent terminology
3. Keep exchange names, system names, protocol names in English
4. Korean reading in parentheses on first mention: e.g., "NYSE (뉴욕증권거래소)"
5. Section headings with English: e.g., "## 5. 매매시스템 (Trading System)"
6. 한다체 (formal written style)
7. Preserve all tables, source citations, and formatting
8. For exchanges with Korean-language reference materials (e.g., KRX):
   use the ORIGINAL Korean terminology from 규정 원문 — do NOT re-translate
   (e.g., 동시호가, 접속매매, 정적VI, 동적VI)

Use parallel subagents — one per file.

After translation:
- Update ../_common/glossary_ko.md with any new terms

DOCX EXPORT:
- Use python-docx to convert all md files to docx
- English: en/docx/   Korean: ko/docx/
- Preserve tables, headings, formatting
```
- **예상 산출물:** `ko/` 전체 번역 + `en/docx/` + `ko/docx/`
- **상태:** ⬜ Not started

---

#### Session T2 — Derivatives 번역
- **작업 디렉토리:** `02_derivatives/`
- **지시 프롬프트:** (T1과 동일한 규칙, 디렉토리만 다름)
```
Read ../_common/TRANSLATION_GUIDE.md and ../_common/glossary_ko.md first.

Translate ALL files in en/ to Korean and save to ko/.
(Same rules as T1 — especially: preserve original-language terms from reference materials)

Use parallel subagents — one per file.

After translation:
- Update ../_common/glossary_ko.md

DOCX EXPORT:
- English: en/docx/   Korean: ko/docx/
```
- **예상 산출물:** `ko/` 전체 번역 + `en/docx/` + `ko/docx/`
- **상태:** ⬜ Not started

---

#### Session T3 — Clearing 번역
- **작업 디렉토리:** `03_clearing/`
- **지시 프롬프트:**
```
Read ../_common/TRANSLATION_GUIDE.md and ../_common/glossary_ko.md first.

Translate ALL files in en/ to Korean and save to ko/.
(Same rules as T1/T2 — preserve original-language terms from reference materials)

Use parallel subagents — one per file.

After translation:
- Update ../_common/glossary_ko.md
```
- **예상 산출물:** `ko/` 전체 번역
- **상태:** ⬜ Not started

---

## Phase 3: 용어집 정리 및 DB 구축 (1세션)

#### Session G1 — Glossary Finalization + DB + DOCX
- **작업 디렉토리:** `exchange_review/` (루트)
- **지시 프롬프트:**
```
STEP 1: Glossary cleanup
- Review _common/glossary_en.md — alphabetize within each category, remove duplicates,
  ensure all definitions are clear
- Review _common/glossary_ko.md — ensure all English terms have Korean translations,
  ensure KRX 참고사항 column is populated where relevant
- Cross-check: every term in EN should exist in KO and vice versa

STEP 2: Build/update _common/glossary.db (SQLite)
- Create table: terms (id, english_term, abbreviation, korean_term, category_en,
  category_ko, definition_en, definition_ko, krx_note, created_at, updated_at)
- Create FTS5 virtual table for full-text search
- Import all terms from glossary_en.md and glossary_ko.md
- Verify row count matches term count in md files

STEP 3: Generate glossary DOCX files
- _common/docx/en/glossary_en.docx
- _common/docx/en/glossary_ko.docx (Korean glossary in EN docx folder for reference)
- _common/docx/ko/glossary_ko.docx
```
- **예상 산출물:** 정리된 용어집 MD + glossary.db + glossary DOCX 3개
- **상태:** ⬜ Not started

---

## Phase 4: 최종 검토 (1세션)

#### Session R1 — Final Review & Benchmarking
- **작업 디렉토리:** `exchange_review/` (루트)
- **지시 프롬프트:**
```
Review the complete research output across all 3 domains.

1. Cross-domain comparative analysis:
   - Create a master comparison document covering all domains
   - Map: Exchange (Trading) → CCP (Clearing) → CSD (Settlement) for all jurisdictions
   - Include ALL exchanges in tables — especially those researched from reference materials
   - Identify common technology vendors
   - Map CCP-exchange clearing relationships
   - Global settlement cycle transition status
   - Margin methodology convergence trends

2. Benchmarking for exchanges with reference materials:
   - For each exchange that had reference materials in 00_references/:
     * Compare vs global peers across all dimensions
     * Replace any remaining [estimated]/[unverified] tags with verified data from references
     * Identify strengths, gaps, and recommended priority actions
   - KRX-specific (if KRX references present):
     * Equities vs NYSE, NASDAQ, JPX, HKEX, etc.
     * Derivatives vs CME, Eurex, Cboe, etc.
     * Clearing vs DTCC, LCH, Eurex Clearing, etc.

3. Quality check:
   - Verify consistency across all documents
   - Count and categorize remaining [unverified] items
   - Ensure glossary completeness
   - Template adherence check

Save to: _common/final_review.md
Translate to: _common/ko/final_review.md
```
- **예상 산출물:** `_common/final_review.md` + `_common/ko/final_review.md`
- **상태:** ⬜ Not started

---

## Phase 5: DOCX 최종 일괄 생성 (1세션)

#### Session X1 — Final DOCX Export
- **작업 디렉토리:** `exchange_review/` (루트)
- **지시 프롬프트:**
```
Generate DOCX files for ALL remaining/updated files:

1. final_review.md (EN + KO) → _common/docx/en/, _common/docx/ko/
2. Any files updated during R1 that need DOCX regeneration
3. Verify ALL md files have corresponding docx files:
   - 01_equities/en/docx/, 01_equities/ko/docx/
   - 02_derivatives/en/docx/, 02_derivatives/ko/docx/
   - 03_clearing/en/docx/, 03_clearing/ko/docx/
   - _common/docx/en/, _common/docx/ko/

Use the existing _convert_to_docx.py pattern or the md_to_docx function.
Report final file counts.
```
- **예상 산출물:** 전체 DOCX 파일 검증 및 보완
- **상태:** ⬜ Not started

---

## Quick Reference: Session Order

```
사전 준비
  P0 (환경 설정 + 참조 자료 인벤토리)

영어 조사 (순서대로 권장, 시장 간에는 병행 가능)
  E1 → E2 → E3    (Equities)
  D1 → D2           (Derivatives)
  C1 → C2           (Clearing)
  * 참조 자료가 있는 거래소는 해당 세션에서 자동 Tier 1 격상

한국어 번역 (해당 시장 영어 조사 완료 후)
  T1 (E3 완료 후)
  T2 (D2 완료 후)
  T3 (C2 완료 후)

용어집 정리 (모든 번역 완료 후)
  G1

최종 검토 (G1 완료 후)
  R1

DOCX 최종 (R1 완료 후)
  X1

웹 퍼블리싱 (X1 완료 후, 또는 번역 완료 후 언제든)
  Q1 (MD→QMD 변환 + Quarto HTML 빌드 + GitHub Pages 배포 준비)
  → bash scripts/build_html.sh  (이후 재빌드 시 동일 명령)
```

### 의존성 요약

```
P0 ──→ E1 ──→ E2 ──→ E3 ──→ T1 ──┐
P0 ──→ D1 ──→ D2 ──────────→ T2 ──┤
P0 ──→ C1 ──→ C2 ──────────→ T3 ──┼──→ G1 ──→ R1 ──→ X1 ──→ Q1
                                    │
       (E/D/C 시장 간에는 순서 무관 — 병행 가능)
       (Q1은 X1 이후 권장, 번역 완료 후 언제든 실행 가능)
```

---

## 이전 실행 이력

> 아래는 이 프로젝트의 최초 실행(2026-04-03 ~ 2026-04-13) 기록이다.
> 당시에는 00_references/ 참조 자료 없이 웹 검색만으로 조사 후, KRX 규정 업로드 후 K1-K3를 추가 수행하였다.

| Session | Date | Description | Status |
|---------|------|-------------|--------|
| E1 | 2026-04-03 | NYSE, NASDAQ, LSE | ✅ |
| E2 | 2026-04-06 | JPX, HKEX, SGX | ✅ |
| E3 | 2026-04-06 | Tier 2/3 (16) + Systems (8) + Regulations (3) + Comparative | ✅ |
| D1 | 2026-04-06 | CME Group, Eurex | ✅ |
| D2 | 2026-04-06 | HKEX Deriv, SGX Deriv, Cboe, ICE, Osaka | ✅ |
| D3 | 2026-04-07 | Tier 2/3 (9) + Systems (3) + Regulations (3) + Comparative | ✅ |
| C1 | 2026-04-07 | DTCC, LCH | ✅ |
| C2 | 2026-04-07 | OCC, CME Clearing, Eurex Clearing | ✅ |
| C3 | 2026-04-07 | Tier 2/3 (13) + Systems (3) + Regulations (3) + Comparative | ✅ |
| T1 | 2026-04-10 | Equities 한국어 번역 + DOCX | ✅ |
| T2 | 2026-04-10 | Derivatives 한국어 번역 + DOCX | ✅ |
| T3 | 2026-04-10 | Clearing 한국어 번역 + DOCX + 용어집 정리 | ✅ |
| R1 | 2026-04-10 | Final Review + KRX Benchmarking | ✅ |
| K1 | 2026-04-12 | KRX 유가증권 + Exture 3.0 (규정 기반 심층 조사) | ✅ |
| K2 | 2026-04-12 | KRX 파생상품 + 청산결제 (규정 기반 심층 조사) | ✅ |
| K3 | 2026-04-13 | KRX 번역 + Final Review 업데이트 + 용어집 + DOCX | ✅ |

### 교훈 (Lessons Learned)

1. **참조 자료는 처음부터 준비하라:** K1-K3가 별도 필요했던 이유는 KRX 규정을 나중에 업로드했기 때문이다. 참조 자료를 사전에 준비하면 한 번의 조사로 동일 품질을 달성할 수 있다.
2. **참조 자료가 있는 거래소는 품질이 현저히 높다:** KRX 파일은 규정 원문의 구체적 조항 인용, 정확한 임계치, 원어 용어 보존 덕분에 웹 검색만으로 작성된 다른 거래소 파일보다 품질이 높다.
3. **원어 용어 보존이 중요하다:** 동시호가, 접속매매 등 규정 원문의 용어를 그대로 사용하면 번역 품질과 실무 활용도가 크게 향상된다.
4. **비교분석 테이블에는 모든 거래소를 포함하라:** 초기에 KRX 행이 누락되어 R1 이후 전면 보완이 필요했다. 처음부터 전체 대상을 테이블에 포함해야 한다.

---

## Phase 6: Quarto 웹 퍼블리싱 (1세션)

#### Session Q1 — MD → QMD 변환 + HTML 빌드 + GitHub Pages 배포 준비
- **작업 디렉토리:** `exchange_review/` (루트)
- **지시 프롬프트:**
```
STEP 1: MD → QMD 변환
- 프로젝트 내 모든 콘텐츠 md 파일(01_equities/, 02_derivatives/, 03_clearing/, _common/ 내
  en/ 및 ko/ 하위의 모든 .md)을 .qmd 파일로 변환한다.
- 각 .qmd 파일 상단에 YAML 헤더를 삽입한다:
  ---
  title: "{적절한 제목 — 원본 파일의 H1 또는 파일명 기반}"
  subtitle: "{도메인 > 카테고리 — 예: Equities > Exchanges}"
  date: "{원본 파일의 최종 수정일 또는 오늘 날짜}"
  lang: "{en 또는 ko}"
  toc: true
  toc-depth: 3
  number-sections: true
  format:
    html:
      theme: cosmo
      code-fold: true
      self-contained: false
  ---
- 본문의 수식($...$, $$...$$)이 Quarto에서 올바르게 렌더링되도록 확인한다.
  특히 파이프(|) 등이 테이블과 충돌하지 않도록 \lvert \rvert 등으로 이스케이프한다.
- 본문의 Markdown 테이블이 Quarto에서 정상 렌더링되는지 확인한다.
  필요시 pipe table → grid table 등으로 변환한다.
- 변환된 .qmd 파일은 원본 .md와 동일한 디렉토리에 저장한다 (예: en/exchanges/nyse.qmd).
- SESSION_PLAN.md, README.md, CLAUDE.md 등 프로젝트 관리용 파일은 변환 대상에서 제외한다.

STEP 2: Quarto 프로젝트 설정 + 빌드 스크립트 생성
- 프로젝트 루트에 _quarto.yml 파일을 생성한다:
  project:
    type: website
    output-dir: docs
  website:
    title: "Global Exchange Research"
    navbar:
      left:
        - text: "Equities"
          menu: [equities 하위 qmd 목록]
        - text: "Derivatives"
          menu: [derivatives 하위 qmd 목록]
        - text: "Clearing"
          menu: [clearing 하위 qmd 목록]
        - text: "용어집 (Glossary)"
          href: glossary 경로
    sidebar:
      - title: "Equities"
        contents: [en/ko 별 exchanges, systems, regulations 파일 목록]
      - title: "Derivatives"
        contents: [동일 구조]
      - title: "Clearing"
        contents: [동일 구조]
  format:
    html:
      theme: cosmo
      toc: true
- 프로젝트 루트에 index.qmd를 생성한다:
  - 프로젝트 전체 소개
  - 도메인별(Equities, Derivatives, Clearing) 섹션으로 구분
  - 각 섹션 내 EN/KO 문서 링크 목록 (exchanges, systems, regulations, comparative)
  - 용어집(EN/KO) 링크
  - 최종 리뷰 문서 링크
- build_html.sh 스크립트를 생성한다:
  #!/bin/bash
  # Quarto가 설치되어 있는지 확인
  command -v quarto >/dev/null 2>&1 || { echo "Quarto CLI 필요: https://quarto.org/docs/get-started/"; exit 1; }
  # HTML 빌드
  quarto render
  echo "HTML 출력: docs/"
  echo "로컬 미리보기: quarto preview"

STEP 3: HTML 빌드 실행
- quarto render 명령을 실행하여 docs/ 디렉토리에 HTML을 생성한다.
- 빌드 오류가 있으면 수정 후 재빌드한다.
- docs/ 내 index.html이 정상적으로 모든 문서에 대한 네비게이션을 제공하는지 확인한다.
- GitHub Pages 배포를 위해:
  - docs/.nojekyll 파일을 생성한다 (빈 파일).
  - .gitignore에 docs/를 추가하지 않는다 (docs/가 커밋되어야 함).
  - README.md에 GitHub Pages 설정 안내를 추가한다:
    "Settings → Pages → Source: Deploy from a branch → Branch: main, /docs"
```
- **예상 산출물:** 전체 `.qmd` 파일 + `_quarto.yml` + `index.qmd` + `build_html.sh` + `docs/` (HTML 출력) + `.nojekyll`
- **상태:** ✅ Completed (2026-04-17)
- **사전 조건:** X1 완료 후 (또는 번역 완료 후 언제든 실행 가능)
- **참고:** Quarto CLI 사전 설치 필요 (`brew install --cask quarto`)
- **산출물 요약:**
  - `md/` — MD 원본 소스 (`md/01_equities/`, `md/02_derivatives/`, `md/03_clearing/`, `md/_common/`)
  - `qmd/` — 184개 `.qmd` 파일 (YAML 헤더 포함, `md/` 구조 미러링)
  - `docx/` — 195개 `.docx` 파일 (도메인별 계층 구조로 통합)
  - `docs/` — 185개 HTML 파일 (GitHub Pages 배포 준비 완료, `.nojekyll` 포함)
  - `scripts/` — 4개 스크립트 (convert_md_to_qmd.py, convert_md_to_docx.py, generate_quarto_yml.py, build_html.sh)
  - `_quarto.yml` — navbar + 8개 도메인별 sidebar (qmd/ 경로 기반)
  - `index.qmd` — 전체 문서 인덱스 (루트)
