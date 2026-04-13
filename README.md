# Global Exchange Infrastructure Research

KRX IT 부서를 위한 글로벌 거래소 인프라 비교 조사 프로젝트.
주식, 파생상품, 청산/결제 3개 도메인에 걸쳐 60개 기관을 분석하고, 벤치마킹을 수행한다.

> **A comprehensive, bilingual (English/Korean) research project analyzing 60 exchanges, CCPs, and CSDs across 20+ jurisdictions — with deep-dive benchmarking powered by official reference materials.**

---

## Project Overview

| Item | Detail |
|------|--------|
| **Scope** | 23 equity exchanges, 17 derivatives exchanges, 20 clearing/settlement organizations |
| **Jurisdictions** | 20+ (North America, Europe, Asia-Pacific, Middle East, Africa) |
| **Languages** | English (primary research) + Korean (full translation) |
| **Total Files** | 360+ (90 EN research + 90 KO translations + 180 DOCX exports) |
| **Glossary** | 403 terms (EN/KO bilingual, SQLite FTS indexed) |
| **Research Period** | 2026-04-03 ~ 2026-04-13 |

---

## Reference-First Research

이 프로젝트의 핵심 방법론은 **참조 자료 우선 조사(Reference-First Research)** 이다.

`00_references/` 폴더에 거래소별 공식 자료(규정, 규칙, 시행세칙, 기술문서 등)를 사전에 업로드하고, 이를 **1차 자료(primary source)로 우선 활용**한다. 웹 검색은 보충 자료로 사용한다.

```
00_references/
├── krx/                    # 한국거래소 — 규정 원문 10개 (현재 업로드 완료)
│   ├── 유가증권시장 업무규정_전문_20260129.txt
│   ├── 파생상품시장 업무규정_전문_20250609.txt
│   ├── 증권시장 청산결제 업무규정_전문_20260304.txt
│   └── ... (7 more)
├── jpx/                    # JPX — 규칙 업로드 시
├── hkex/                   # HKEX
├── cme/                    # CME Group
└── ...                     # 기타 거래소
```

### 참조 자료의 효과

| | 참조 자료 없음 (웹 검색만) | 참조 자료 있음 |
|---|---|---|
| **조사 깊이** | Tier에 따라 차등 | 참조 범위 내 자동 Tier 1 격상 |
| **정확도** | `[unverified]` 태그 다수 | 조항 번호 인용, 정확한 임계치 |
| **용어 품질** | 영어 번역 의존 | 원어 용어 보존 (동시호가, 접속매매 등) |
| **2차 작업** | 별도 심층 조사 필요 가능 | 불필요 — 한 번에 완료 |

---

## Repository Structure

```
exchange_review/
├── _common/                          # Shared resources
│   ├── final_review.md               # Cross-domain analysis & benchmarking
│   ├── glossary_en.md                # English glossary (403 terms)
│   ├── glossary_ko.md                # Korean glossary (403 terms)
│   ├── glossary.db                   # SQLite FTS-indexed glossary database
│   ├── RESEARCH_GUIDE.md             # Research methodology & standards
│   ├── TRANSLATION_GUIDE.md          # EN→KO translation rules
│   ├── TEMPLATE_EXCHANGE.md          # Exchange profile template (11 sections)
│   ├── TEMPLATE_SYSTEM.md            # System deep-dive template
│   ├── TEMPLATE_CLEARING.md          # Clearing org template
│   ├── ko/                           # Korean translations of common files
│   └── docx/                         # DOCX exports (en/, ko/)
│
├── 00_references/                    # 거래소별 공식 참조 자료 (PRIMARY SOURCES)
│   └── {exchange}/                   # 거래소별 서브 디렉토리
│
├── 01_equities/                      # Equities / Securities Markets
│   ├── en/
│   │   ├── 01_overview.md            # Domain overview & research roadmap
│   │   ├── 02_comparative_analysis.md # 23-exchange comparative analysis
│   │   ├── exchanges/                # 23 exchange profiles
│   │   ├── systems/                  # 9 trading system deep-dives
│   │   ├── regulations/              # 3 regulatory analyses (US, EU, Asia)
│   │   └── docx/                     # DOCX exports
│   └── ko/                           # Korean translations (mirror structure)
│
├── 02_derivatives/                   # Derivatives Markets
│   ├── en/
│   │   ├── exchanges/                # 17 exchange profiles
│   │   ├── systems/                  # 3 system deep-dives
│   │   ├── regulations/              # 3 regulatory analyses
│   │   └── docx/
│   └── ko/
│
├── 03_clearing/                      # Clearing & Settlement
│   ├── en/
│   │   ├── organizations/            # 20 CCP/CSD profiles
│   │   ├── systems/                  # 3 system deep-dives
│   │   ├── regulations/              # 3 regulatory analyses
│   │   └── docx/
│   └── ko/
│
├── SESSION_PLAN.md                   # Research session plan (13 sessions)
└── README.md
```

---

## Exchanges & Organizations Covered

### Equities (23 exchanges)

| Tier | Exchanges |
|------|-----------|
| **Tier 1** | NYSE, NASDAQ, LSE, JPX, HKEX, SGX, **KRX** |
| **Tier 2** | Euronext, Deutsche Borse, ASX, TMX, SIX Swiss |
| **Tier 3** | SSE, SZSE, BSE, NSE India, TWSE, Borsa Italiana, BME, Nasdaq Nordic, Tadawul, JSE, Bursa Malaysia |

> **Note:** 참조 자료가 있는 거래소는 Tier에 관계없이 해당 범위 내에서 Tier 1 깊이로 조사된다.

### Derivatives (17 exchanges)

CME Group, Eurex, Cboe, ICE Futures, Osaka Exchange, HKEX Derivatives, SGX Derivatives, **KRX Derivatives**, CFFEX, Montreal Exchange, TAIFEX, DCE, Euronext Derivatives, DME, ASX Derivatives, SHFE, NSE F&O

### Clearing & Settlement (20 organizations)

DTCC, LCH, OCC, Eurex Clearing, CME Clearing, **KRX Clearing**, **KSD**, JSCC, HKEX Clearing, SIX x-clear, CDS Canada, CSDC, EuroCCP, Euroclear, CDP, Muqassa, ICE Clear, CCIL, Clearstream, ASX Clear

---

## Benchmarking (KRX)

`_common/final_review.md` Section 2에서 KRX를 글로벌 동류 기관과 비교 분석한다.

> 이 벤치마킹은 `00_references/krx/`의 규정 원문 10개 파일을 1차 자료로 활용하여 작성되었다.

### Strengths
- 통합 거래소 (주식 + 파생 + 채권) — Deutsche Borse 모델과 유사
- Exture 3.0 (2023) 최근 업그레이드 완료, 청산/결제까지 저지연 범위 확장
- KOSPI 200 옵션 — 역사적으로 세계 최다 거래 단일 파생상품
- KSD ISO 20022 채택 — DTC, JASDEC보다 앞서 있음
- 보안토큰 법제화 (2027.1 시행) — KSD 의무등록

### Key Gaps
- T+2 결제 (미국/캐나다/인도/호주는 T+1 완료)
- KRX-SPAN (2세대) → VaR 기반 (3세대) 전환 필요
- CCP 회복 및 정리 체계 부재
- 손해배상공동기금 규모/SITG 미공개

---

## Research Methodology

1. **Reference-First:** `00_references/{거래소}/` 의 공식 자료를 1차 자료로 우선 활용, 웹 검색은 보충용
2. **Structured Templates:** 모든 기관을 동일한 11-section 템플릿으로 분석 (`TEMPLATE_EXCHANGE.md`)
3. **Source-Based:** 인용 형식 `[Source: {파일명}, Article XX]` (참조 자료) 또는 `[Source: Name, "Document", accessed YYYY-MM-DD]` (웹)
4. **Verification Tags:** 미검증 정보에 `[unverified]`, 추정치에 `[estimated]` 태그 부착
5. **Bilingual:** 영문 조사 완료 후 `TRANSLATION_GUIDE.md` 기준으로 한국어 전문 번역
6. **Native Terminology:** 참조 자료의 현지어 핵심 용어를 그대로 보존 (동시호가, 접속매매, 정적VI, 동적VI, 損害賠償共同基金 등)

---

## Session Plan

연구는 13개 세션으로 구성되며, `SESSION_PLAN.md`에 전체 계획이 기술되어 있다.

```
P0   사전 준비 (참조 자료 인벤토리 + Tier 배정)

E1 → E2 → E3   Equities 영어 조사
D1 → D2         Derivatives 영어 조사    ← 참조 자료 있는 거래소는 자동 Tier 1
C1 → C2         Clearing 영어 조사

T1, T2, T3      한국어 번역 + DOCX (도메인별)
G1              용어집 정리 + DB 구축
R1              최종 검토 + 벤치마킹
X1              DOCX 최종 일괄 생성
```

### 의존성

```
P0 ──→ E1 → E2 → E3 → T1 ──┐
P0 ──→ D1 → D2 ──────→ T2 ──┤
P0 ──→ C1 → C2 ──────→ T3 ──┼──→ G1 → R1 → X1
                              │
      (E/D/C 시장 간에는 순서 무관 — 병행 가능)
```

---

## Glossary Database

`_common/glossary.db`는 SQLite FTS5 인덱스를 갖춘 용어집 데이터베이스이다.

```sql
-- 용어 검색 예시
SELECT english_term, korean_term, category_ko, krx_note
FROM terms WHERE terms MATCH 'margin' ORDER BY rank;

-- 카테고리별 용어 수
SELECT category_en, COUNT(*) FROM terms GROUP BY category_en ORDER BY COUNT(*) DESC;
```

| Category | Terms |
|----------|-------|
| Trading | 59 |
| Derivatives | 55 |
| Clearing | 48 |
| Settlement | 36 |
| Technology | 34 |
| Regulation | 44 |
| Market Segments | 23 |
| **Total** | **403** |

---

## How to Use

### Browse Research
각 도메인 디렉토리의 `en/` (영문) 또는 `ko/` (한국어)에서 Markdown 파일을 열어 확인한다.
DOCX 파일은 `en/docx/` 및 `ko/docx/`에 위치한다.

### Cross-Domain Analysis
`_common/final_review.md`에서 3개 도메인을 관통하는 비교 분석과 벤치마킹 결과를 확인한다.

### Search Terms
```bash
# SQLite 용어 검색
sqlite3 _common/glossary.db "SELECT english_term, korean_term FROM terms WHERE terms MATCH 'margin' ORDER BY rank;"

# 파일 내 검색
grep -r "KOSPI 200" 01_equities/en/ 02_derivatives/en/
```

### Add New Exchange References
새로운 거래소의 참조 자료를 추가하려면:
1. `00_references/{거래소명}/` 디렉토리를 생성
2. 규정, 규칙, 기술문서 등을 업로드
3. `SESSION_PLAN.md`의 P0 세션을 실행하여 인벤토리 갱신 및 Tier 재배정
4. 해당 도메인 세션(E/D/C)을 실행하면 참조 자료를 1차 자료로 활용하여 Tier 1 깊이로 조사

---

## File Formats

| Format | Count | Description |
|--------|-------|-------------|
| `.md` | 198 | Markdown 원본 (EN 90 + KO 90 + templates/guides 18) |
| `.docx` | 196 | Word 문서 변환본 (EN 90 + KO 90 + glossary/common 16) |
| `.db` | 1 | SQLite 용어집 데이터베이스 |
| `.txt` | 10 | 거래소 규정 원문 (00_references/) |
| `.py` | 2 | MD→DOCX 변환 스크립트 |

---

## Tech Stack

- **Research & Writing:** Claude (Anthropic) — AI-assisted research with human verification
- **Document Conversion:** python-docx (MD → DOCX)
- **Glossary:** SQLite 3 with FTS5 full-text search
- **Source Data:** 거래소별 공식 자료 (00_references/), 웹 검색 (보충)

---

## License

This research is prepared for internal use by KRX IT Department. All data is sourced from publicly available materials (exchange websites, annual reports, regulatory filings). Reference materials in `00_references/` are copyrighted by their respective exchanges.

---

*Generated: 2026-04-13*
