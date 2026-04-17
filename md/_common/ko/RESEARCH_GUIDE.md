# 글로벌 거래소 리서치 가이드 (Global Exchange Research Guide)

본 문서는 주식시장, 파생상품시장, 청산 및 결제의 세 가지 도메인(domain)에 걸친 글로벌 거래소 조사의 범위, 방법론 및 기준을 정의한다.

---

## 1. 조사 범위 (Research Scope)

### 1.1 대상 거래소 (Target Exchanges)

#### 주식시장 (01_equities)
| 지역 | 거래소 |
|------|--------|
| 북미 | NYSE, NASDAQ, TMX (Toronto Stock Exchange) |
| 유럽 | London Stock Exchange (LSE), Euronext, Deutsche Borse (Xetra), SIX Swiss Exchange, Borsa Italiana, BME (Bolsas y Mercados Espanoles), Nasdaq Nordic |
| 아시아태평양 | Japan Exchange Group (JPX/TSE), Hong Kong Exchanges (HKEX), Singapore Exchange (SGX), Australian Securities Exchange (ASX), Shanghai Stock Exchange (SSE), Shenzhen Stock Exchange (SZSE), Bombay Stock Exchange (BSE), National Stock Exchange of India (NSE), Taiwan Stock Exchange (TWSE), Bursa Malaysia |
| 중동 및 아프리카 | Saudi Exchange (Tadawul), Johannesburg Stock Exchange (JSE) |

#### 파생상품시장 (02_derivatives)
| 지역 | 거래소 |
|------|--------|
| 북미 | CME Group (CME/CBOT/NYMEX/COMEX), Cboe Global Markets, ICE Futures U.S., Montreal Exchange (MX) |
| 유럽 | Eurex, ICE Futures Europe, Euronext Derivatives, Nasdaq Nordic Derivatives |
| 아시아태평양 | Osaka Exchange (JPX), HKEX Derivatives, SGX Derivatives, ASX Derivatives, China Financial Futures Exchange (CFFEX), Dalian Commodity Exchange (DCE), Shanghai Futures Exchange (SHFE), National Stock Exchange of India (NSE F&O), Taiwan Futures Exchange (TAIFEX) |
| 중동 및 아프리카 | Dubai Mercantile Exchange (DME) |

#### 청산 및 결제 (03_clearing)
| 지역 | 기관 |
|------|------|
| 북미 | DTCC (DTC/NSCC/FICC), Options Clearing Corporation (OCC), CME Clearing, ICE Clear U.S., Canadian Depository for Securities (CDS) |
| 유럽 | LCH (LCH Ltd / LCH SA), Eurex Clearing, EuroCCP, SIX x-clear, Euroclear, Clearstream |
| 아시아태평양 | Japan Securities Clearing Corporation (JSCC), HKSCC / HKCC / SEOCH, Central Depository Pte (CDP, Singapore), ASX Clear / ASX Settlement, China Securities Depository and Clearing (CSDC), Clearing Corporation of India (CCIL) |
| 중동 | Muqassa (Saudi Exchange CCP) |

### 1.2 조사 우선순위 (Research Priority)
- **Tier 1 (심층 조사):** NYSE, NASDAQ, CME, Eurex, LSE, JPX, HKEX, SGX, DTCC, LCH, OCC
- **Tier 2 (표준 조사):** Euronext, Deutsche Borse, ASX, ICE, Cboe, JSCC, Eurex Clearing
- **Tier 3 (개요 수준):** 나머지 거래소

---

## 2. 거래소별 조사 항목 (Research Items per Exchange)

모든 거래소/기관 파일은 반드시 다음 섹션을 포함해야 한다. `TEMPLATE_EXCHANGE.md` 또는 `TEMPLATE_SYSTEM.md`의 템플릿(template)을 사용한다.

### 2.1 주식 및 파생상품 거래소 (For Equities & Derivatives Exchanges)

1. **개요 및 프로필 (Overview & Profile)**
   - 공식 명칭, 약어, 웹사이트
   - 설립 연도, 주요 연혁
   - 지배구조 (상장/비상장, 모회사, 합병 이력)
   - 감독기관 / 관할기구
   - 시가총액(주식시장의 경우) 또는 명목거래량(파생상품의 경우)
   - 상장 상품 수

2. **시장 구조 (Market Structure)**
   - 시장 세그먼트(segment) 및 시장 단계 (예: 본시장, 성장시장)
   - 매매 세션 및 거래시간 (프리마켓, 접속매매, 종가단일가, 시간외거래)
   - 호가 단위 / 가격 증분(tick size)
   - 매매 단위 및 최소 주문 수량
   - 시장조성자(market maker) / 유동성공급자(liquidity provider) 프로그램

3. **매매 메커니즘 (Trading Mechanism)**
   - 단일가매매 유형 (시가, 종가, 장중, 변동성 완화)
   - 접속매매 (주문주도형 vs 호가주도형 vs 혼합형)
   - 가격발견 과정
   - 주문 우선순위 규칙 (가격-시간, 가격-수량-시간, 비례배분)

4. **주문 유형 (Order Types)**
   - 표준 주문 유형 (시장가, 지정가, 역지정가, 역지정가-지정가)
   - 고급/특수 주문 유형 (iceberg, pegged, midpoint 등)
   - 주문 유효기간 / TIF(Time-in-Force) 옵션 (DAY, GTC, IOC, FOK, GTD)
   - 주문 정정 및 취소 규칙

5. **매매 시스템 (Trading System / Technology)**
   - 시스템 명칭 및 개발 방식 (자체 개발/외부 벤더)
   - 아키텍처(architecture) 개요 (체결엔진 설계)
   - 지연시간(latency) (왕복 지연시간, 주문~확인 응답 시간)
   - 처리용량 / 수용능력 (초당 메시지 수, 초당 주문 수)
   - 시스템 이력 (과거 플랫폼, 전환 일정)
   - 기술 스택(technology stack) (공개된 경우)
   - 재해복구(DR) / 업무연속성계획(BCP)

6. **시장 데이터 (Market Data)**
   - 실시간 데이터 피드 프로토콜(protocol) (ITCH, OUCH, FIX, FAST, 자체 프로토콜)
   - 데이터 수준 (L1, L2, 전체 호가창)
   - 시장 데이터 배포 인프라
   - 과거 데이터 이용 가능 여부

7. **접속 및 참가 (Connectivity & Access)**
   - 회원/참가자 자격 요건
   - 접속 방식 (전용선, VPN, 인터넷)
   - 코로케이션(co-location) / 근접 호스팅(proximity hosting) 서비스
   - API 프로토콜 (FIX, binary, REST/WebSocket(리테일용))
   - 인증 / 적합성 테스트 절차

8. **리스크 관리 및 서킷브레이커 (Risk Controls & Circuit Breakers)**
   - 가격제한 (정적/동적)
   - 서킷브레이커(circuit breaker) 메커니즘 및 발동 기준
   - 오주문(fat-finger) / 착오거래 방지 장치
   - 사전 리스크 점검(pre-trade risk check)
   - 킬스위치(kill switch) 기능

9. **규제 체계 (Regulatory Framework)**
   - 감독기관
   - 주요 규정 및 규칙
   - 시장감시 접근방식
   - 보고 의무
   - 국경간 규제 협력 체계

10. **수수료 및 수익 모델 (Fees & Revenue Model)**
    - 매매 수수료 구조 (maker-taker, 정액제, 차등제)
    - 상장 수수료
    - 시장 데이터 수수료
    - 접속 / 코로케이션 수수료

11. **최근 동향 (Recent Developments)**
    - 시스템 업그레이드 또는 전환 (최근 5년)
    - 신규 상품 또는 시장 세그먼트
    - 규제 변경사항
    - 전략적 이니셔티브(initiative) (ESG, 디지털 자산, 클라우드 전환 등)

### 2.2 청산 및 결제 기관 (For Clearing & Settlement Organizations)

1. **개요 및 프로필 (Overview & Profile)** (상기와 동일, CCP/CSD에 맞게 조정)
2. **청산 모델 (Clearing Model)**
   - CCP 방식 vs 쌍무 청산
   - 채무인수(novation) 과정
   - 청산 대상 상품 (주식, 파생상품, 채권, OTC)
   - 청산회원 등급 및 자격 요건
3. **리스크 관리 (Risk Management)**
   - 증거금 산출 방법론 (SPAN, PRISMA, VaR 기반 등)
   - 개시증거금 및 변동증거금
   - 손실분담 구조(default waterfall)
   - 공동기금 / 보증기금(default fund / guarantee fund)
   - 스트레스 테스트(stress testing) 및 사후검증(back-testing)
   - 회복 및 정리 계획(recovery and resolution planning)
4. **결제 (Settlement)**
   - 결제 주기 (T+1, T+2 등)
   - DVP(Delivery versus Payment) 모델
   - CSD 연계
   - 결제 완결성(settlement finality)
   - 증권 대차(securities lending/borrowing) 제도
5. **기술 및 인프라 (Technology & Infrastructure)**
   - 시스템 명칭 및 아키텍처
   - 처리 용량
   - STP(Straight-Through Processing) 비율
   - 인터페이스 프로토콜 (SWIFT, ISO 20022, 자체 프로토콜)
6. **규제 체계 (Regulatory Framework)** (상기와 동일)
7. **상호운용성 (Interoperability)** - 타 CCP/CSD와의 연계
8. **최근 동향 (Recent Developments)** (상기와 동일)

---

## 3. 조사 기준 (Research Standards)

### 3.1 출처 우선순위 (Source Priority)
1. **1차 출처:** 거래소 공식 웹사이트, 기술 사양서, 규정집, 연차보고서
2. **2차 출처:** WFE 통계, IOSCO 보고서, BIS/CPMI 발간물, FIA 조사
3. **3차 출처:** 업계 간행물 (예: Waters Technology, The TRADE), 학술 논문

### 3.2 인용 형식 (Citation Format)
모든 사실 기반 주장에는 반드시 출처를 명시해야 한다:
```
[Source: NYSE Official Website, "Market Model", accessed 2026-04-03]
[Source: WFE Annual Statistics Guide 2025]
[Source: BIS CPMI Red Book, 2024 edition]
```

### 3.3 데이터 최신성 (Data Recency)
- 가능한 한 가장 최근 완결 연도의 데이터를 사용한다
- 통계의 경우, 기준 연도/일자를 명기한다
- 3년 이상 경과한 데이터는 `[data as of YYYY]`로 표시한다

### 3.4 불확실성 처리 (Uncertainty Handling)
- 1차 출처에서 검증할 수 없는 정보: `[unverified]`로 표시한다
- 추정 또는 근사치인 정보: `[estimated]`로 표시한다
- 이용 불가능한 정보: 생략하지 않고 "정보가 공개되지 않음(Information not publicly available)"으로 명시한다

### 3.5 파일 명명 규칙 (File Naming Convention)
- 소문자와 밑줄 사용: `nyse.md`, `cme_group.md`, `lch_ltd.md`
- 공백 및 특수문자 사용 금지
- 널리 알려진 약어를 사용한다

---

## 4. 용어집 관리 (Glossary Management)

- 조사 중 새로 접한 기술 용어는 모두 `glossary_en.md`에 추가해야 한다
- 용어는 범주별(매매, 청산, 결제, 기술, 규제)로 분류한다
- 한국어 번역은 `glossary_ko.md`에 별도로 관리한다
- KRX에 대응하는 개념이 있는 경우, 한국어 용어집에 이를 명기한다

---

## 5. 품질 점검표 (Quality Checklist)

거래소 파일을 최종 확정하기 전에 다음 사항을 확인한다:
- [ ] 11개 섹션(청산 기관의 경우 8개) 모두 작성 완료
- [ ] 주요 사실에 대한 출처 명시
- [ ] 신규 용어를 용어집에 추가
- [ ] 템플릿과 일관된 서식
- [ ] 임시 텍스트(placeholder) 잔존 여부 확인
- [ ] 파일명이 명명 규칙을 준수
