# 번역 가이드 (Translation Guide) (영어 → 한국어)

본 문서는 거래소 조사 문서를 영어에서 한국어로 번역할 때의 기준을 정의한다.

---

## 1. 일반 원칙 (General Principles)

1. **유창성보다 정확성 우선:** 자연스러운 한국어 표현보다 기술적 정확성을 우선한다.
2. **용어 일관성:** 용어 번역 시 항상 `glossary_ko.md`를 참조한다. 동일한 용어를 문서마다 다르게 번역하지 않는다.
3. **구조 유지:** 영문 원본과 동일한 제목 구조, 표 형식, 섹션 번호를 유지한다.
4. **고유명사는 영문 유지:** 거래소명, 시스템명, 프로토콜명, 기관명은 영문을 유지하되, 최초 언급 시 괄호 안에 한국어 독음을 병기한다.
   - Example: "NYSE (뉴욕증권거래소)" on first mention, then "NYSE" thereafter
5. **기술 용어:** 확립된 한국어 금융 용어가 있으면 해당 용어를 사용한다. 표준 한국어 용어가 없는 경우 영문 용어를 사용하고 괄호 안에 한국어 설명을 병기한다.

---

## 2. 용어 번역 규칙 (Term Translation Rules)

### 2.1 영문 유지 용어 (Terms to Keep in English) — 번역하지 않는다
- 시스템명: Exigo, Optiq, INET, Genium 등
- 프로토콜명: FIX, ITCH, OUCH, FAST, SWIFT, ISO 20022
- 기술 약어: API, STP, DMA, HFT, FPGA
- 한국 금융계에서 널리 사용되는 약어: ETF, ETN, ELS, DLS, CCP, CSD, DVP

### 2.2 한국어로 번역하는 용어 (Terms to Translate to Korean)
- 일반 금융 개념: market(시장), order(주문), trade(매매), settlement(결제), clearing(청산)
- 설명 및 해설 내용
- 섹션 제목 (단, 괄호 안에 영문을 병기한다)
  - Example: "## 5. 매매시스템 (Trading System)"

### 2.3 전문 용어의 혼용 표기 (Hybrid Approach for Specialized Terms)
형식: **한국어 용어 (English Term)**
- Example: 중앙청산소 (Central Counterparty, CCP)
- Example: 가격제한폭 (Price Limit)
- Example: 호가단위 (Tick Size)

---

## 3. 스타일 가이드라인 (Style Guidelines)

### 3.1 문체 (Sentence Style)
- 공식 문어체 한국어를 사용한다 (합니다체 또는 한다체 — 조사 문서에는 한다체를 사용한다)
- 지나치게 긴 문장은 지양하고, 짧은 단위로 분리한다
- 적절한 경우 불릿 포인트와 표를 활용한다

### 3.2 숫자 및 단위 (Numbers and Units)
- 모든 숫자는 아라비아 숫자를 사용한다
- 통화: 원화 환산액이 도움이 되는 경우 원래 통화와 함께 표기한다
  - Example: "100억 USD (약 13조 원)"
- 백분율: 5% (그대로 유지한다)
- 시간: 관련성이 있는 경우 KST로 변환하되, 원래 시간대를 항상 병기한다
  - Example: "09:30 EST (23:30 KST)"

### 3.3 날짜 (Dates)
- YYYY-MM-DD 형식을 사용한다 (영문 버전과 동일)
- 본문 중 역사적 날짜: YYYY년 MM월

### 3.4 표 (Tables)
- 열 머리글은 한국어로 번역한다
- 데이터 셀이 고유명사 또는 기술 용어인 경우 원어를 유지한다
- 셀 내 설명적 내용은 번역한다

---

## 4. 문서 유형별 가이드라인 (Document-Specific Guidelines)

### 4.1 거래소 개요 문서 (Exchange Profile Documents)
- 모든 설명적 내용을 번역한다
- 거래소명, 시스템명은 영문을 유지한다
- 표 머리글을 번역한다
- 관련성이 있는 경우 KRX 비교 사항을 추가한다 (본문 내 삽입이 아닌 별도 하위 섹션으로 작성한다)

### 4.2 시스템/기술 문서 (System/Technology Documents)
- 대부분의 기술 사양은 영문을 유지한다 (지연시간 수치, 프로토콜명 등)
- 아키텍처 설명은 번역한다
- 섹션 제목은 괄호 안에 영문을 병기하여 번역한다

### 4.3 규제 문서 (Regulatory Documents)
- 외국 규정의 공식 한국어 번역이 존재하는 경우 해당 번역을 사용한다
- 규정명은 영문을 유지하고 한국어 설명을 병기한다
  - Example: "Regulation NMS (전미시장제도규정)"

---

## 5. 번역 품질 체크리스트 (Quality Checklist for Translation)

- [ ] 모든 용어가 glossary_ko.md와 일치하는가
- [ ] 거래소/시스템 고유명사가 영문으로 유지되었는가
- [ ] 각 고유명사의 최초 언급 시 한국어 독음이 병기되었는가
- [ ] 표 구조가 영문 원본과 일치하는가
- [ ] 숫자 및 단위가 올바른 형식으로 표기되었는가
- [ ] 기계번역 흔적(부자연스러운 표현)이 없는가
- [ ] 유용한 경우 KRX 맥락 참고사항이 추가되었는가
- [ ] 출처 인용이 원문 그대로 유지되었는가 (URL 및 출처명은 번역하지 않는다)

---

## 6. 작업 흐름 (Workflow)

1. 영문 문서 전체를 먼저 통독한다
2. 문서 내 모든 용어에 대해 glossary_ko.md를 확인한다
3. 누락된 용어가 있으면 glossary_en.md와 glossary_ko.md 양쪽에 추가한다
4. 구조를 유지하면서 섹션별로 번역한다
5. 품질 체크리스트에 따라 검토한다
6. 자연스러운 한국어 흐름을 위해 최종 통독한다
