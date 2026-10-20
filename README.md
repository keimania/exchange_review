# Global Exchange Infrastructure Research

KRX IT 부서를 위한 글로벌 거래소 인프라 비교 조사 프로젝트.
주식, 파생상품, 청산/결제 3개 도메인에 걸쳐 60개 기관을 분석하고, 벤치마킹을 수행한다.

> **A comprehensive, bilingual (English/Korean) research project analyzing 60 exchanges, CCPs, and CSDs across 20+ jurisdictions — with deep-dive benchmarking powered by official reference materials.**

> 🌐 **웹 포털 (PC 및 모바일 브라우저 즉시 접속):** [https://keimania.github.io/exchange_review/](https://keimania.github.io/exchange_review/)  
> *반응형 웹 UI, 실시간 전문 검색(Search), 180+ 심층 리포트 및 403개 용어집 포함*

---

## Project Overview

| Item | Detail |
|------|--------|
| **Scope** | 23 equity exchanges, 17 derivatives exchanges, 20 clearing/settlement organizations |
| **Jurisdictions** | 20+ (North America, Europe, Asia-Pacific, Middle East, Africa) |
| **Languages** | English (primary research) + Korean (full translation) |
| **Glossary** | 403 terms (EN/KO bilingual, SQLite FTS indexed) |
| **Research Period** | 2026-04-03 ~ 2026-04-17 |

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

| | 참조 자료 없음 (웹 검색만) | 참조 자료 있음 |
|---|---|---|
| **조사 깊이** | Tier에 따라 차등 | 참조 범위 내 자동 Tier 1 격상 |
| **정확도** | `[unverified]` 태그 다수 | 조항 번호 인용, 정확한 임계치 |
| **용어 품질** | 영어 번역 의존 | 원어 용어 보존 (동시호가, 접속매매 등) |

---

## Repository Structure

```
exchange_review/
│
├── md/                               # Markdown 원본 소스
│   ├── 01_equities/                  # Equities
│   │   ├── en/
│   │   │   ├── 01_overview.md
│   │   │   ├── 02_comparative_analysis.md
│   │   │   ├── exchanges/            # 23개 거래소 프로파일
│   │   │   ├── systems/              # 9개 매매시스템 심층분석
│   │   │   └── regulations/          # 3개 규제 분석 (US, EU, Asia)
│   │   ├── ko/                       # 한국어 번역 (동일 구조)
│   │   └── CLAUDE.md
│   ├── 02_derivatives/               # Derivatives
│   │   ├── en/ exchanges/ systems/ regulations/
│   │   ├── ko/
│   │   └── CLAUDE.md
│   ├── 03_clearing/                  # Clearing & Settlement
│   │   ├── en/ organizations/ systems/ regulations/
│   │   ├── ko/
│   │   └── CLAUDE.md
│   └── _common/                      # 공용 리소스
│       ├── final_review.md           # 최종 검토 & KRX 벤치마킹
│       ├── glossary_en.md            # 영어 용어집 (403 terms)
│       ├── glossary_ko.md            # 한국어 용어집 (403 terms)
│       ├── glossary.db               # SQLite FTS5 용어집 DB
│       ├── RESEARCH_GUIDE.md
│       ├── TRANSLATION_GUIDE.md
│       ├── TEMPLATE_EXCHANGE.md
│       ├── TEMPLATE_SYSTEM.md
│       ├── TEMPLATE_CLEARING.md
│       └── ko/                       # 한국어 번역본
│
├── 00_references/                    # 거래소별 공식 참조 자료 (PRIMARY SOURCES)
│   └── {exchange}/
│
│─ ─ ─ ─ ─ ─ ─ ─  생성물 (Generated Outputs)  ─ ─ ─ ─ ─ ─ ─ ─
│
├── qmd/                              # Quarto 소스 (MD → QMD 변환본)
│   ├── 01_equities/en/ko/...         # 동일 계층 구조
│   ├── 02_derivatives/en/ko/...
│   ├── 03_clearing/en/ko/...
│   └── reference/                    # 용어집 + 최종리뷰 QMD
│       ├── glossary_en.qmd
│       ├── glossary_ko.qmd
│       ├── final_review.qmd
│       └── ko/final_review.qmd
│
├── docx/                             # Word 문서 (MD → DOCX 변환본)
│   ├── 01_equities/en/ko/
│   ├── 02_derivatives/en/ko/
│   ├── 03_clearing/en/ko/
│   └── _common/en/ko/
│
├── docs/                             # HTML 웹사이트 (GitHub Pages 배포)
│   └── ... (185개 HTML 파일)
│
│─ ─ ─ ─ ─ ─ ─ ─  프로젝트 파일  ─ ─ ─ ─ ─ ─ ─ ─
│
├── scripts/                          # 빌드 & 변환 스크립트
│   ├── build_html.sh                 # 전체 빌드 자동화 (MD→QMD→HTML)
│   ├── convert_md_to_qmd.py          # MD → QMD 변환 (YAML 헤더 추가)
│   ├── convert_md_to_docx.py         # MD → DOCX 변환
│   └── generate_quarto_yml.py        # _quarto.yml 자동 생성
│
├── _quarto.yml                       # Quarto 웹사이트 설정
├── index.qmd                         # 웹사이트 인덱스 페이지
├── SESSION_PLAN.md                   # 연구 세션 계획 (14세션)
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

### Derivatives (17 exchanges)

CME Group, Eurex, Cboe, ICE Futures, Osaka Exchange, HKEX Derivatives, SGX Derivatives, **KRX Derivatives**, CFFEX, Montreal Exchange, TAIFEX, DCE, Euronext Derivatives, DME, ASX Derivatives, SHFE, NSE F&O

### Clearing & Settlement (20 organizations)

DTCC, LCH, OCC, Eurex Clearing, CME Clearing, **KRX Clearing**, **KSD**, JSCC, HKEX Clearing, SIX x-clear, CDS Canada, CSDC, EuroCCP, Euroclear, CDP, Muqassa, ICE Clear, CCIL, Clearstream, ASX Clear

---

## KRX Benchmarking

`md/_common/final_review.md` Section 2에서 KRX를 글로벌 동류 기관과 비교 분석한다.
KRX 규정 원문 10개 파일(`00_references/krx/`)을 1차 자료로 활용하였다.

### Strengths
- 통합 거래소 (주식 + 파생 + 채권) — Deutsche Borse 모델과 유사
- Exture 3.0 (2023) 최근 업그레이드 완료
- KOSPI 200 옵션 — 역사적으로 세계 최다 거래 단일 파생상품
- KSD ISO 20022 채택 — DTC, JASDEC보다 앞서 있음

### Key Gaps
- T+2 결제 (미국/캐나다/인도/호주는 T+1 완료)
- KRX-SPAN (2세대) → VaR 기반 (3세대) 전환 필요
- CCP 회복 및 정리 체계 부재

---

## File Formats & Counts

| 위치 | 포맷 | 수량 | 설명 |
|------|------|------|------|
| `md/` | `.md` | ~180 | Markdown 원본 소스 |
| `qmd/` | `.qmd` | 184 | Quarto 변환본 (YAML 헤더 포함) |
| `docx/` | `.docx` | 195 | Word 문서 변환본 |
| `docs/` | `.html` | 185 | HTML 웹사이트 |
| `md/_common/` | `.db` | 1 | SQLite 용어집 DB (FTS5) |
| `00_references/krx/` | `.txt` | 10 | KRX 규정 원문 |

---

## How to Build

### HTML 웹사이트 빌드 (전체 자동)
```bash
bash scripts/build_html.sh
```
> Quarto CLI 필요: `brew install --cask quarto`

### 개별 스크립트
```bash
# MD → QMD 변환만
python3 scripts/convert_md_to_qmd.py

# MD → DOCX 변환만
python3 scripts/convert_md_to_docx.py

# _quarto.yml 재생성만
python3 scripts/generate_quarto_yml.py

# Quarto 렌더링만
quarto render
```

### GitHub Pages 배포
```bash
git add docs/ && git commit -m "Build: Quarto HTML" && git push
# → GitHub: Settings → Pages → Branch: main, /docs → Save
```

### 로컬 미리보기
```bash
quarto preview
```

---

## How to Use

### 콘텐츠 탐색
- **Markdown 원본:** `md/01_equities/en/`, `md/02_derivatives/en/`, `md/03_clearing/en/`
- **한국어 번역:** 동일 경로의 `ko/` 디렉토리
- **Word 문서:** `docx/` (도메인별 정리)
- **웹 브라우저:** `docs/index.html` 또는 GitHub Pages URL

### 용어집 검색
```bash
# SQLite 전문 검색
sqlite3 md/_common/glossary.db \
  "SELECT english_term, korean_term FROM terms WHERE terms MATCH 'margin' ORDER BY rank;"
```

### 새 거래소 참조 자료 추가
1. `00_references/{거래소명}/` 디렉토리 생성
2. 규정, 규칙, 기술문서 업로드
3. `SESSION_PLAN.md`의 P0 세션 실행 (인벤토리 갱신 + Tier 재배정)
4. 해당 도메인 세션 실행 (참조 자료 기반 Tier 1 조사)

---

## Research Methodology

1. **Reference-First:** `00_references/{거래소}/`의 공식 자료를 1차 자료로 우선 활용
2. **Structured Templates:** 11-section 표준 템플릿 (`md/_common/TEMPLATE_EXCHANGE.md`)
3. **Source Citation:** `[Source: {파일명}, Article XX]` (참조 자료) / URL + 접근일 (웹)
4. **Verification Tags:** 미검증 정보 `[unverified]`, 추정치 `[estimated]`
5. **Bilingual:** `md/_common/TRANSLATION_GUIDE.md` 기준 한국어 전문 번역
6. **Native Terminology:** 현지어 핵심 용어 보존 (동시호가, 접속매매, 정적VI, 板寄せ 등)

---

## Session Plan

연구는 14개 세션으로 구성되며, `SESSION_PLAN.md`에 전체 계획이 기술되어 있다.

```
P0            사전 준비 (참조 자료 인벤토리 + Tier 배정)
E1 → E2 → E3  Equities 영어 조사
D1 → D2       Derivatives 영어 조사
C1 → C2       Clearing 영어 조사
T1, T2, T3    한국어 번역 + DOCX
G1            용어집 정리 + DB 구축
R1            최종 검토 + 벤치마킹
X1            DOCX 최종 일괄 생성
Q1 ✅         Quarto 웹 퍼블리싱 (bash scripts/build_html.sh)
```

---

## Tech Stack

| 역할 | 도구 |
|------|------|
| Research & Writing | Claude (Anthropic) — AI 보조 조사 |
| 웹사이트 빌드 | Quarto (qmd → HTML) |
| DOCX 변환 | python-docx (md → docx) |
| 용어집 DB | SQLite 3 + FTS5 |
| 소스 관리 | Git / GitHub Pages |

---

## License

This research is prepared for internal use by KRX IT Department. All data is sourced from publicly available materials (exchange websites, annual reports, regulatory filings). Reference materials in `00_references/` are copyrighted by their respective exchanges.

---

*최종 업데이트: 2026-04-17*
