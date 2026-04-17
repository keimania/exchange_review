# Genium INET — Nasdaq Technology

> **최종 수정일:** 2026-04-07
> **시스템 분류:** 매매시스템 (Trading System)

---

## 1. 시스템 개요 (System Overview)

| 항목 | 상세 |
|------|---------|
| 시스템명 | Genium INET |
| 운영 주체 | Nasdaq, Inc. (구 NASDAQ OMX Group); 전 세계 40개 이상의 거래소에 라이선스 제공 |
| 목적 | 파생상품, 주식, 채권, 상품, 외환을 위한 멀티에셋 매매 및 청산 플랫폼 |
| 출시 연도 | 2010년 (Nordic 파생상품용 Genium INET); 플랫폼 계보는 1980년대 OM/CLICK까지 거슬러 올라감 |
| 현재 버전 | Genium INET 8.0.0.0 (2025년 6월 릴리스); 후속 플랫폼 Nasdaq Eqlipse 2025년 출시 |
| 벤더 | Nasdaq, Inc. — Market Technology 사업부 (스톡홀름 기반 개발) |

[Source: Nasdaq IR, "NASDAQ OMX Launches World's Fastest Trading System for Its Nordic Derivatives Markets", October 2010](https://ir.nasdaq.com/news-releases/news-release-details/nasdaq-omx-launches-worlds-fastest-trading-system-its-nordic)
[Source: Nasdaq, "Genium INET Upgrade 8.0.0.0", 2025](https://www.nasdaq.com/solutions/genium-inet-upgrade-to-version-8.0.0.0)

### 시스템 발전 과정 (System Evolution)

| 기간 | 시스템명 | 주요 변경사항 |
|--------|-------------|-------------|
| 1980년대~1990년대 | OM CLICK / CLICK Trade | OM AB (스웨덴 옵션 시장 운영사)가 파생상품용 CLICK 전자매매시스템을 개발; Nordic 거래소 및 기타 거래소에 광범위하게 라이선스 제공 |
| 1990년대 후반~2003 | SAXESS | OMX가 NOREX Alliance (스톡홀름, 헬싱키, 코펜하겐, 오슬로, 아이슬란드, 탈린, 리가)의 공통 주식 매매 플랫폼으로 SAXESS를 개발; Nordic/발틱 현물주식 매매 통합 |
| 2003~2007 | Genium (독립형) | OMX Technology가 CLICK과 SAXESS의 교훈을 반영한 차세대 멀티에셋 매매 및 청산 시스템으로 Genium 플랫폼을 개발 |
| 2007~2008 | NASDAQ OMX 합병 | NASDAQ이 OMX Group을 인수 (2007), NASDAQ의 INET 매매체결엔진 기술과 OMX의 Genium/CLICK 파생상품 플랫폼 유산을 결합 |
| 2010 | **Genium INET** 출시 | 2010년 10월 25일 NASDAQ OMX Nordic 현물 및 채권 파생상품용 통합 플랫폼 출시; 100 마이크로초 미만의 지연시간으로 "세계 최고속 매매시스템"으로 마케팅 |
| 2011~2013 | 글로벌 배포 | SGX가 Genium INET 도입 ("SGX Reach/Titan"); HKEX가 HKATS/DCASS를 Genium INET으로 업그레이드 (2013년 10월); ASX가 파생상품용으로 도입 (ASX Trade24); Borsa Istanbul (BISTECH)도 도입 |
| 2014~2024 | 성숙기 | 지속적인 버전 업그레이드 (v4.x~v8.x); NLX (런던, 2013~2015), Montreal Exchange (검토) 및 다수의 기타 거래소에 배포; Pre-trade Risk Management (PRM/TradeGuard) 통합 |
| 2025~현재 | **Nasdaq Eqlipse** (4세대) | 후속 플랫폼 발표; 매매, 청산, CSD, 데이터 인텔리전스를 아우르는 통합 스위트; 마이크로서비스 아키텍처; 클라우드 대응; "에버그린" 분기별 업그레이드 모델; 기존 배포에서 Genium INET은 전환 기간 동안 운영 지속 |

[Source: Nasdaq, "SAXESS trading platform launched successfully at Helsinki, Tallinn and Riga stock exchanges"](https://www.nasdaq.com/about/press-center/saxess-trading-platform-launched-successfully-helsinki-tallinn-and-riga-stock)
[Source: HKEX, "HKEx Upgrades its Derivatives Trading and Clearing Systems to Genium INET", October 2013](https://www.hkex.com.hk/News/News-Release/2013/131016news?sc_lang=en)
[Source: Nasdaq Newsroom, "Nasdaq Launches Eqlipse, Fourth Generation of its Marketplace Technology Platform", 2025](https://www.nasdaq.com/newsroom/nasdaq-launches-eqlipse-fourth-generation-its-marketplace-technology-platform)

---

## 2. 아키텍처 (Architecture)

### 2.1 상위 수준 설계 (High-Level Design)

Genium INET은 단일 통합 플랫폼 내에서 여러 자산군(파생상품, 주식, 채권, 상품)을 지원하도록 설계된 **모듈형, 이벤트 구동 아키텍처(modular, event-driven architecture)**를 따른다. 순수 속도에 최적화된 단일 스레드 방식의 INET 주식 매매체결엔진과 달리, Genium INET은 파생상품 시장에 필요한 풍부한 기능(내재가격, 복합 전략, pro-rata 매칭, 청산 통합)과 성능 간의 균형을 맞춘다.

**설계 원칙:**
- **멀티에셋, 멀티마켓** — 단일 플랫폼 인스턴스가 여러 상품, 시장, 자산군을 동시에 지원 가능
- **매매-청산 통합** — 매매 + 청산 통합 솔루션으로 설계 (청산이 별도인 많은 주식 시스템과 차별화)
- **구성 가능한 매칭 로직** — 상품별로 다중 매칭 알고리즘(가격-시간 우선, pro-rata, 하이브리드 구성) 지원
- **실시간 리스크 관리** — 주문 처리 경로에 사전거래 및 거래 시점 리스크 제어가 내장
- **고가용성** — 보조 사이트에 핫 스탠바이를 갖춘 액티브-스탠바이 아키텍처

**데이터 흐름 (간략화):**
1. 주문이 TCP를 통해 게이트웨이(FIX, OUCH 또는 OMnet API)로 도착
2. 사전거래 리스크 검증 적용 (PRM/TradeGuard: 가격 한도, 수량 한도, 신용 검사)
3. 주문이 적절한 매매체결엔진 파티션(상품/시장별)으로 라우팅
4. 매매체결엔진이 구성된 매칭 알고리즘(가격-시간, pro-rata, 또는 하이브리드) 실행
5. 파생상품의 경우: 내재가격 엔진이 전략 조합으로부터의 잠재적 내재 주문을 평가
6. 체결 보고서가 참가자에게 반환; 매매 데이터가 청산 엔진(DCASS 또는 동등 시스템)으로 전달
7. 시장데이터 업데이트가 ITCH (multicast/unicast) 및 AMD (Advanced Market Data)를 통해 발행

### 2.2 핵심 구성요소 (Core Components)

| 구성요소 | 기능 | 상세 |
|-----------|----------|---------|
| **매매체결엔진** | 구성 가능한 알고리즘을 사용한 핵심 주문 매칭; 가격-시간 우선, pro-rata, 하이브리드 매칭 지원; 개장/폐장 경매, 연속 거래, RFQ(호가요청) 세션 처리 | 신규 주문, 정정, 취소를 처리; 매매를 생성; 호가장 상태를 관리; 파생상품 전략에 대한 내재가격 지원 |
| **주문 게이트웨이** | 참가자로부터의 인바운드 주문 수신 및 검증; 프로토콜 변환; 세션 관리 및 인증 | FIX (업계 표준), OUCH (고성능 네이티브 바이너리), OMnet API (Nasdaq 독자) 지원; 모든 연결 애플리케이션에 적합성 테스트 필수 |
| **시장데이터 엔진** | 매매체결엔진 이벤트로부터 실시간 시장데이터를 생성 및 배포 | ITCH 프로토콜 (바이너리, 주문별 호가 잔량); AMD (Advanced Market Data) 파생/요약 데이터용; MoldUDP64 multicast 전달 |
| **청산 엔진 (DCASS/Genium INET Clearing)** | 통합 사후거래 청산, 포지션 관리, 증거금 계산 | 실시간 청산 지원; 포지션 네팅; 증거금 계산 (고객 거래소에서 일반적으로 SPAN 기반); 결제 처리 |
| **리스크 엔진 (PRM / TradeGuard)** | 사전거래 리스크 관리; 매매체결엔진에 도달하기 전 구성 가능한 한도에 대해 주문 검증 | Fat-finger 가격 검사; 최대 주문 수량 검사; 누적 금액 한도; 순/총 포지션 한도; 사실상 추가 지연시간 제로; ESMA 가이드라인 준수 지원 |
| **감시 인터페이스 (SMARTS)** | 모든 주문 및 매매 활동의 실시간 피드를 Nasdaq SMARTS 감시 플랫폼에 제공 | 전 세계 50개 이상의 거래소와 170개 이상의 은행/브로커가 사용; 호가장 재생 기능; AI 기반 이상탐지; 시장 조작 및 내부자 거래 탐지 |
| **내재가격 엔진** | 전략 다리 조합으로부터 파생된 내재 매수/매도 가격 계산 | 캘린더 스프레드, 상품간 스프레드 및 기타 전략 유형에 대한 implied-in 및 implied-out 가격 생성; 아웃라이트와 전략 호가장을 연결하여 유동성 증대 |
| **Mass Quote 처리기** | 마켓 메이커를 위한 효율적 대량 호가 관리 | 마켓 메이커가 다수의 양방향 호가를 동시에 제출 및 업데이트 가능; 구성 가능한 호가 업데이트 쓰로틀링 지원 |
| **전략/복합주문 엔진** | 다중 다리 파생상품 전략(스프레드, 스트래들, 스트랭글 등) 관리 | 사전 정의 및 사용자 정의 전략; 전략 생성 및 검증; 다중 다리 매칭; 내재가격 통합 |
| **기준정보 서버** | 종목 마스터 데이터, 계약 사양, 매매 일정 배포 | 파생상품 호가장 디렉토리, 상품 정의, 만기일, 호가 단위 표, 증거금 파라미터 포함 |
| **Drop Copy 서버** | 참가자에게 체결 및 주문 상태의 실시간 복사본 제공 | FIX Drop Copy 프로토콜; 복사된 메시지에 CopyMsgIndicator (797)="Y" 태그; 컴플라이언스, 대사, 백오피스 통합에 사용 |
| **프론트엔드 애플리케이션** | 레퍼런스 클라이언트로 제공되는 GUI 기반 매매 워크스테이션 | CLICK Trade (파생상품 매매 GUI); TradeGuard (리스크 관리 GUI); 거래소 브랜딩 커스터마이징 가능 |

[Source: Nasdaq, "Technical Information - Genium INET Trading and Clearing Platform"](https://www.nasdaq.com/solutions/technical-information-genium-inet-trading-and-clearing-platform)
[Source: Nasdaq, "Genium INET Front Ends"](https://www.nasdaq.com/solutions/genium-inet-front-ends)
[Source: Nasdaq, "Nasdaq Market Surveillance (SMARTS) Features"](https://www.nasdaq.com/solutions/nasdaq-market-surveillance/features)
[Source: Nasdaq, "Pre-Trade Risk Management"](https://www.nasdaq.com/solutions/pre-trade-risk-management)

### 2.3 기술 스택 (Technology Stack)

| 계층 | 기술 |
|-------|-----------|
| **프로그래밍 언어** | C/C++ (매매체결엔진 핵심 및 핵심 경로); Java (애플리케이션 레이어, 프론트엔드 구성요소) [unverified] |
| **운영체제** | Linux (범용 x86 서버; 저지연 운영을 위해 커널 튜닝) |
| **네트워킹** | 표준 TCP/IP; 시장데이터 배포용 UDP multicast; 최고 성능 배포를 위한 후기 버전에서 커널 바이패스 네트워킹 가능 |
| **전송 프로토콜** | SoupBinTCP (OUCH/ITCH 유니캐스트용 신뢰성 있는 점대점); MoldUDP64 (재전송을 갖춘 비신뢰성 multicast 시장데이터용); FIX 및 OMnet용 표준 TCP |
| **미들웨어** | OMnet 미들웨어 버스 — Genium INET 구성요소를 연결하는 독자 메시지 버스; 시스템 구성요소 간 신뢰성 있고 순서 보장된 메시지 전달 제공 |
| **애플리케이션 프로토콜** | OUCH (주문 입력), ITCH (시장데이터), FIX 5.0 SP2 (주문 입력, drop copy, 기준정보), OMnet API (독자), AMD (Advanced Market Data) |
| **하드웨어** | 범용 x86 Linux 서버; 필수 FPGA 가속 없음 (INET 주식과 달리); 소프트웨어를 통한 성능 최적화 |
| **플랫폼 아키텍처** | 모듈형 모놀리스 — 통합되었으나 구성 가능; 개별 모듈(매칭, 청산, 리스크, 감시)을 다양한 조합으로 배포 가능 |
| **후속 아키텍처** | Nasdaq Eqlipse: 마이크로서비스 기반; 컨테이너화; 클라우드 대응 (하이브리드 온프레미스/클라우드); 표준화된 API 스위트; "에버그린" 분기별 업그레이드 전달 |

---

## 3. 성능 사양 (Performance Specifications)

| 지표 | 수치 | 조건 |
|--------|-------|------------|
| **평균 지연시간** | < 100 마이크로초 | 2010년 출시 시 Genium INET 벤치마크; 평균 운영 왕복시간 |
| **SGX 벤치마크** | < 90 마이크로초 | Singapore Exchange 배포에서 측정된 door-to-door 지연시간 |
| **HKEX 배포** | 서브밀리초 | 이전 HKATS 시스템의 ~20 ms에서 Genium INET (2013)의 서브밀리초로 대폭 개선 |
| **처리량** | > 1,000,000 메시지/초 | Genium INET 배포 전반의 지속 처리 속도 |
| **이전 시스템 대비** | ~200배 개선 | HKEX: 평균 ~10 ms에서 서브밀리초로; Nordic: CLICK/SAXESS 대비 유사한 수준의 개선 |

**참고:** 성능은 배포별로 크게 다르다. 각 거래소는 자사의 상품 구성, 시장 구조, 리스크 요구사항, 하드웨어 선택에 따라 Genium INET을 다르게 구성한다. 공개된 벤치마크는 참조 구성을 나타내며, 실제 운영 성능은 다음에 따라 달라진다:
- 거래 상품의 수 및 복잡성
- 매칭 알고리즘 선택 (가격-시간이 pro-rata보다 빠름)
- 내재가격 엔진 활성화 (파생상품에 대한 연산 오버헤드 추가)
- 리스크 검사 구성 깊이
- 거래소 데이터센터의 하드웨어 및 네트워크 인프라
- 시장데이터 배포 부하

### 성능 이력 (Performance History)

| 연도 | 배포 | 지연시간 | 비고 |
|------|-----------|---------|-------|
| 2010년 이전 | CLICK / SAXESS | ~10~20 ms | 레거시 OMX 기술; 당시에는 적합했으나 전자거래 성장으로 점차 한계에 도달 |
| 2010 | Nasdaq Nordic (파생상품) | 평균 < 100 μs | 출시 시 "세계 최고속 매매시스템"; 최초의 Genium INET 운영 배포 |
| 2011 | SGX (파생상품) | door-to-door < 90 μs | Singapore Exchange; 이전 시스템 대비 대폭적인 지연시간 감소 |
| 2013 | HKEX (HKATS 파생상품) | 서브밀리초 | 레거시 HKATS에서 업그레이드; 2013년 10월 예정보다 앞서 출시 |
| 2013 | NLX (런던) | < 100 μs | Genium INET과 Equinix 코로케이션을 활용한 Nasdaq의 런던 파생상품 거래소 (2013~2015 운영) |
| 2025 | Genium INET v8.0.0.0 | 비공개 | 최신 버전; 지속적 최적화 |

[Source: Nasdaq IR, "NASDAQ OMX Launches World's Fastest Trading System for Its Nordic Derivatives Markets", 2010](https://ir.nasdaq.com/news-releases/news-release-details/nasdaq-omx-launches-worlds-fastest-trading-system-its-nordic)
[Source: Nasdaq IR, "NASDAQ OMX to Deliver World's Fastest Trading Platform to Singapore Exchange"](https://ir.nasdaq.com/news-releases/news-release-details/nasdaq-omx-deliver-worlds-fastest-trading-platform-singapore)
[Source: Finextra, "HKEx moves derivatives clearing and trading platforms to Genium Inet", 2013](https://www.finextra.com/pressarticle/52257/hkex-moves-derivatives-clearing-and-trading-platforms-to-genium-inet)
[Source: A-Team Insight, "NLX Leverages Genium Inet, Equinix For Low Latency"](https://a-teaminsight.com/blog/nlx-leverages-genium-inet-equinix-for-low-latency/)

---

## 4. 인터페이스 및 프로토콜 (Interfaces & Protocols)

### 4.1 주문 입력 (Order Entry)

| 프로토콜 | 유형 | 전송 | 설명 | 사용 사례 |
|----------|------|-----------|-------------|----------|
| **OUCH** | 네이티브 바이너리 | SoupBinTCP | 단순하고 고성능의 주문 입력 프로토콜; 주문 입력, 정정, 취소 및 체결 수신 지원; 최소한의 오버헤드; 독자 매매시스템 통합을 위해 설계 | 최저 지연시간을 추구하는 HFT 회사 및 알고리즘 트레이더 |
| **FIX (5.0 SP2)** | 업계 표준 | TCP | Genium INET에 맞게 조정된 Financial Information Exchange 프로토콜; 주문 관리를 위한 표준 FIX 시맨틱스; OUCH보다 폭넓은 메시지 세트 | 기존 FIX 인프라를 보유한 기관 참가자, 브로커 및 회사 |
| **OMnet API** | 독자 바이너리 | OMnet 미들웨어 | Nasdaq의 네이티브 독자 API; 고급 기능을 포함한 Genium INET 전체 기능에 대한 완전한 접근 제공; OMnet Gateway Process가 API 클라이언트의 연결을 관리 | 전체 기능이 필요한 참가자; 거래소 운영자 애플리케이션 |

**주요 주문 입력 기능:**
- 복합/전략 주문 입력 (다중 다리 스프레드, 스트래들 등)
- 마켓 메이커를 위한 mass quote 입력 및 유지
- RFQ(호가요청) 제출
- 주문 정정 (가격 및 수량 변경)
- 연결 해제 시 취소(cancel-on-disconnect) 기능
- Kill switch (모든 미체결 주문 취소)
- 모든 연결 애플리케이션에 운영 접속 전 적합성 테스트 필수

[Source: Nasdaq, "Genium INET Protocol Specifications"](https://www.nasdaq.com/solutions/genium-inet-protocol-specifications)
[Source: Nasdaq, "Genium INET OMnet Application Programmer's Interface Manual"](https://www.nasdaq.com/docs/omnet_api_nordic_va2393_0.pdf)

### 4.2 시장데이터 (Market Data)

| 프로토콜 | 유형 | 전송 | 설명 |
|----------|------|-----------|-------------|
| **ITCH (Genium INET ITCH)** | 네이티브 바이너리 | MoldUDP64 (multicast) | 자동 매칭 시장의 모든 공개 주문 및 매매를 표시하는 직접 데이터 피드; 주문별 전체 호가 잔량 뷰; 아웃바운드 전용 (주문 입력 미지원); 가변 길이 바이너리 메시지; 배포별로 버전 상이 (일부 거래소에서 ITCH 2.0) |
| **AMD (Advanced Market Data)** | 파생 데이터 | MoldUDP64 / SoupBinTCP | 파생/집계된 시장데이터 뷰 (BBO, 매매 요약) 제공; ITCH 원시 주문별 피드를 보완 |
| **Glimpse** | 스냅샷 | SoupBinTCP (유니캐스트) | 온디맨드 전체 호가장 스냅샷 서비스; 초기 상태 복구 또는 갭 보충에 사용; 점대점 요청/응답 |

**ITCH 주요 메시지 유형 (파생상품):**
- **Derivative Order Book Directory** — 계약 사양, 상품 파라미터, 내재가격 플래그
- **System Event** — 시장 개장/폐장, 매매 세션 시작/종료
- **Add Order** — 호가장에 새 주문 추가
- **Order Executed** — 부분 또는 전체 체결
- **Order Delete** — 호가장에서 주문 제거
- **Trade** — 체결된 매매 정보
- **Equilibrium Price** — 경매 균형가격 업데이트
- **Implied Price** — 전략 조합으로부터 파생된 내재 매수/매도 가격

**데이터 인코딩:**
- 바이너리 인코딩 메시지
- 메시지 유형에 따른 가변 길이
- 갭 탐지 및 복구를 위한 시퀀스 메시지
- 나노초 정밀도 타임스탬프

[Source: Nasdaq, "Genium INET ITCH Protocol Specification NFX"](https://www.nasdaq.com/docs/ITCH%20Reference%20Data.pdf)
[Source: OnixS, "ITCH Protocol Usage"](https://www.onixs.biz/insights/itch-protocol-usage)

### 4.3 Drop Copy

| 프로토콜 | 기능 | 설명 |
|----------|----------|-------------|
| **FIX Drop Copy** | 실시간 체결 및 주문 상태 복사 | FIX 프로토콜 기반; 모든 주문 활동(입력, 정정, 체결, 취소)의 복사본을 지정된 drop copy 세션에 제공; 모든 복사된 메시지에 CopyMsgIndicator (797)="Y" 적용; OMnet을 통해 입력된 주문의 경우 Drop 세션에 Execution Report 전송; 교차 프로토콜 가시성 활성화 |

[Source: Borsa Istanbul, "Genium INET FIX Drop Copy Protocol Specification"](https://www.borsaistanbul.com/files/genium-inet-fix-drop-copy-protocol-specification.pdf)

### 4.4 기준정보 (Reference Data)

| 데이터 유형 | 배포 방식 | 설명 |
|-----------|-------------------|-------------|
| **FIX 기준정보** | FIX 5.0 SP2 | 계약 사양, 상품 정의, 매매 일정; FIX Application Sequencing 기반; Resend Request는 지원되나 Sequence Reset gap fill로 응답; 애플리케이션 시퀀싱을 통한 메시지 복구 |
| **ITCH 기준정보** | ITCH 시스템/디렉토리 메시지 | 시장 개장 전 Derivative Order Book Directory 메시지 방송; 호가 단위 표, 거래 단위, 매매 상태, 내재가격 파라미터 포함 |
| **OMnet 기준정보** | OMnet API 방송 | OMnet 미들웨어를 통한 전체 기준정보 접근; API 클라이언트가 대기열 방송을 폴링 |

[Source: Borsa Istanbul, "Genium INET FIX Reference Data Protocol Specification"](https://borsaistanbul.com/files/genium-inet-fix-reference-data-protocol-specification.pdf)
[Source: Nasdaq, "FIX for Genium INET for NASDAQ Nordic 2.0"](https://www.nasdaq.com/docs/2023/05/31/Genium_INET_FIX_Protocol_Specification-6.0.0240_v228.pdf)

---

## 5. 복원력 및 업무연속성 (Resilience & Business Continuity)

### 5.1 아키텍처 (Architecture)

| 항목 | 상세 |
|--------|---------|
| **배포 모델** | 주 사이트 (액티브) + 보조 사이트 (핫 스탠바이); 중앙 시스템 구성요소가 주 사이트에서 실행되며 보조 사이트로 실시간 상태 복제 |
| **페일오버 모델** | 주 사이트 장애 시 보조 사이트의 매매체결엔진이 주 모드로 승격; 보조 사이트의 ITCH 포트는 매매체결엔진이 주 역할을 인수한 후에만 활성화 |
| **하트비트 모니터링** | 주 및 보조 시스템이 정기적인 상태 신호를 교환; 장애 감지 시 사전 정의된 페일오버 절차 작동 |
| **게이트웨이 이중화** | 다수의 주문 입력 및 시장데이터 게이트웨이; 참가자가 주 및 백업 인프라 모두에 연결 유지 |
| **네트워크 이중화** | 주 사이트와 보조 사이트 간 이중 네트워크 경로; 다양한 물리적 케이블 경로 |
| **데이터 무결성** | 실시간 상태 복제로 페일오버 시 최소한의 데이터 손실 보장; 복제된 로그로부터 호가장 상태 복구 가능 |

### 5.2 배포별 구성 (Deployment-Specific Configurations)

Genium INET을 배포하는 각 거래소는 자체적인 업무연속성 계획을 구성한다. 예시:

- **Nasdaq Nordic:** 핫 스탠바이를 갖춘 주 및 보조 데이터센터; 회원에게 상세한 BCP 공개; 정기적 DR 페일오버 테스트 실시
- **HKEX:** Genium INET 기반 HKATS는 홍콩 내 주 사이트와 DR 사이트에서 운영; HKEX는 Nasdaq의 표준 구성과 독립적으로 자체 BCP를 유지
- **SGX:** Singapore Exchange는 Genium INET 기반 시스템으로 별도의 주 시설과 DR 시설을 유지

### 5.3 운영 복원력 (Operational Resilience)

- **적합성 테스트:** Genium INET에 연결하는 모든 애플리케이션은 운영 접속 전에 적합성 테스트를 통과해야 하며, 이를 통해 페일오버 시나리오, 시장 상태 변경, 오류 상황을 올바르게 처리하는지 확인한다
- **테스트 환경:** 참가자 연결 테스트, 적합성 인증, 재해복구 시뮬레이션을 위한 전용 Genium INET 테스트 시스템 제공
- **용량 계획:** 정상 운영 거래량을 크게 상회하는 여유를 갖추도록 시스템을 설계; 정기적 스트레스 테스트 실시

[Source: NASDAQ OMX Nordic, "Business Continuity Plan Description"](https://docplayer.net/7172713-Nasdaq-omx-nordic-business-continuity-plan-description.html)
[Source: Nasdaq, "Genium INET Test Systems"](https://www.nasdaq.com/solutions/genium-inet-test-systems)
[Source: Nasdaq, "Genium INET Conformance"](https://business.nasdaq.com/trade/trade-management/technical-information/genium-inet/conformance.html)

---

## 6. 주요 기술 특징 (Notable Technical Features)

### 6.1 멀티에셋 지원 (Multi-Asset Support)
Genium INET은 주식, 주식파생상품, 채권, 채권파생상품, 상품(에너지 및 농산물 포함), 외환파생상품, 지수상품을 단일 통합 시스템 내에서 지원하는 진정한 멀티에셋 플랫폼이다. 이는 자산군별로 별도의 시스템을 필요로 하는 많은 거래소 기술 플랫폼과 대비된다. 이 플랫폼의 유연성은 전체 상품군을 위한 단일 기술 솔루션을 찾는 거래소들에게 매력적인 요소가 되었다.

### 6.2 유연한 매칭 알고리즘 (Flexible Matching Algorithms)
일반적으로 가격-시간 우선만을 사용하는 순수 주식 플랫폼과 달리, Genium INET은 파생상품 시장에 필수적인 다중 구성 가능 매칭 알고리즘을 지원한다:
- **가격-시간 우선 (FIFO):** 최우선 가격의 주문이 먼저 매칭되고, 동일 가격 수준에서는 시간 우선으로 처리되는 표준 알고리즘; 대부분의 주식 및 유동성 높은 파생상품에 사용
- **가격 Pro-Rata (PPR):** 최우선 가격에 우선순위가 부여되지만, 마지막 매칭 가격 수준에서 거래량이 대기 주문 크기에 비례하여 배분; 마켓 메이커 인센티브가 중요한 금리 선물 및 옵션에 흔히 사용
- **하이브리드 구성:** 거래소가 최소 배분 크기 및 최우선호가 우선순위 조정을 포함하여 상품별 알고리즘 파라미터를 구성 가능

[Source: Nasdaq, "Genium INET - Pro-Rata Matching"](https://www.nasdaq.com/solutions/genium-inet-pro-rata-matching)

### 6.3 복합주문 / 전략 지원 (Complex Order / Strategy Support)
파생상품 거래를 위해 Genium INET은 포괄적인 전략 주문 관리를 제공한다:
- **사전 정의 전략:** 캘린더 스프레드, 상품간 스프레드, 스트래들, 스트랭글, 기타 표준 전략 유형
- **사용자 정의 전략:** 참가자가 거래소 정의 규칙에 따라 맞춤형 다중 다리 조합 생성 가능
- **전략 매칭:** 네이티브 전략 매칭 엔진이 다중 다리 체결을 원자적으로 처리
- **전략-아웃라이트 상호작용:** 전략 주문이 내재가격 엔진을 통해 아웃라이트 호가장과 상호작용 가능

### 6.4 내재가격 (Implied Pricing)
내재가격 엔진은 Genium INET의 가장 정교한 파생상품 전용 기능 중 하나이다:
- **Implied-in:** 아웃라이트 다리 주문의 조합으로부터 내재 전략 주문을 생성
- **Implied-out:** 전략 주문과 다른 아웃라이트 주문의 조합으로부터 내재 아웃라이트 주문을 생성
- **다중 수준 내재:** 여러 관련 상품에 걸친 내재가격 체인 지원
- **유동성 강화:** 내재가격은 아웃라이트와 전략 호가장을 효과적으로 연결하여 가시적 유동성을 증가시키고 스프레드를 축소
- **구성 가능:** 거래소가 상품별로 내재가격을 활성화 또는 비활성화하고 내재 깊이를 구성 가능

### 6.5 마켓 메이커를 위한 Mass Quote (Mass Quote for Market Makers)
mass quoting 기능을 통한 효율적인 마켓 메이커 지원:
- 단일 거래에서 여러 상품에 걸쳐 양방향 호가의 동시 제출 및 업데이트 가능
- mass quote 거래별 최대 주문 수량 검사 수행
- 거래당 최대 호가 항목 수 구성 가능
- 메시지 트래픽 관리를 위한 호가 업데이트 쓰로틀링
- 기존 호가의 효율적 수정을 위한 델타 호가 업데이트

### 6.6 감시 통합 (SMARTS) (Surveillance Integration — SMARTS)
Genium INET은 Nasdaq의 SMARTS 감시 플랫폼과의 네이티브 통합을 제공한다:
- 모든 주문 및 매매 데이터의 SMARTS로의 실시간 피드
- 조사를 위한 전체 호가장 재생 기능 — 임의 기간에 걸쳐 전체 호가장 재구성
- 모든 Genium INET 연결 시장에 걸친 교차 시장 감시
- 시장 조작, 내부자 거래, 스푸핑에 대한 AI 기반 이상탐지
- 전 세계 50개 이상의 거래소와 170개 이상의 은행/브로커가 사용
- 생성형 AI 기능 (~2024 도입)이 조사 절차를 간소화

[Source: Nasdaq, "Nasdaq Market Surveillance (SMARTS) Features"](https://www.nasdaq.com/solutions/nasdaq-market-surveillance/features)

### 6.7 사전거래 리스크 관리 (PRM / TradeGuard) (Pre-Trade Risk Management — PRM / TradeGuard)
사실상 추가 지연시간 영향이 없는 통합 사전거래 리스크 제어:
- **Fat Finger 가격 검사:** 수신 주문 가격을 참조 가격과 비교
- **최대 주문 수량:** 참가자별 및 상품별 구성 가능
- **누적 금액 한도:** 구성 가능한 시간 창에 걸친 총 주문 금액 추적 및 제한
- **포지션 한도:** 순 및 총 포지션 한도 적용
- **스폰서드 액세스 제어:** GCM (General Clearing Member) / NCM (Non-Clearing Member) 리스크 관계 지원
- **DMA 제어:** 저지연 Direct Market Access 검증
- **ESMA 준수:** EU MiFID II / ESMA의 자동 매매 제어 요건을 충족하도록 설계

[Source: Nasdaq, "PRE-TRADE RISK MANAGEMENT Product Sheet"](https://www.nasdaq.com/docs/prm-genium-inet-product-sheet.pdf)
[Source: Nasdaq, "NASDAQ NORDIC Genium INET Pre-trade Risk Management Service Guide"](https://www.nasdaq.com/docs/nasdaq-nordic-genium-inet-prm-service-guide-2.2.pdf)

### 6.8 주요 글로벌 배포 (파생상품 중심) (Key Global Deployments — Derivatives Focus)

| 거래소 | 시스템명 | 가동 시점 | 자산군 | 비고 |
|----------|------------|------------|---------------|-------|
| **Nasdaq Nordic / OMX** | Genium INET | 2010년 10월 | 주식파생상품, 채권파생상품, 상품 | 최초 배포; CLICK/SAXESS 대체; Nasdaq 자체 Nordic 파생상품 시장 |
| **HKEX** | HKATS (Genium INET 기반) | 2013년 10월 | 주가지수 선물/옵션, 개별주식 옵션, 통화 선물, 금리 선물, 상품 선물 | 레거시 HKATS 대체; 청산(DCASS)도 Genium INET으로 업그레이드; 예정보다 앞서 출시 |
| **SGX** | SGX Titan / Reach | 2011 | 주식파생상품, 외환파생상품, 상품파생상품, 금리파생상품 | Singapore Exchange; 90 μs 미만 벤치마크 지연시간 |
| **ASX** | ASX Trade24 | 2010~2011 | 주식파생상품, 금리파생상품, 에너지파생상품, 상품파생상품 | Australian Securities Exchange 파생상품 플랫폼 |
| **Borsa Istanbul** | BISTECH | 2013~2015 | 주식, 파생상품, 채권 | 전체 멀티에셋 배포; ITCH, OUCH, FIX 프로토콜 사용 |
| **NLX** | NLX | 2013~2015 | 금리파생상품 | Nasdaq의 런던 기반 파생상품 거래소 (이후 폐쇄); Eurex/Liffe에 대한 경쟁 거래소 |
| **NFX** | Nasdaq Futures (NFX) | 2015~2020 | 에너지 및 상품파생상품 | Nasdaq의 미국 선물 거래소; ITCH/OUCH 프로토콜로 Genium INET 사용 |
| **Montreal Exchange** | — | 검토 | 주식 및 금리파생상품 | MX가 매매 플랫폼 현대화를 위해 Genium INET을 검토 [unverified] |

[Source: HKEX, "HKEx Upgrades its Derivatives Trading and Clearing Systems to Genium INET", 2013](https://www.hkex.com.hk/News/News-Release/2013/131016news?sc_lang=en)
[Source: Nasdaq IR, "ASX Launches Next Generation Trading Platform Powered by NASDAQ OMX's Genium INET"](https://ir.nasdaq.com/news-releases/news-release-details/asx-launches-next-generation-trading-platform-powered-nasdaq)
[Source: The Trade News, "Nasdaq OMX Nordic installs INET for derivatives"](https://www.thetradenews.com/nasdaq-omx-nordic-installs-inet-for-derivatives/)

---

## 7. 비교 참고사항 (Comparison Notes)

### vs. KRX 시스템 (Exture+)

| 항목 | Genium INET | KRX Exture+ |
|--------|------------|-------------|
| **시스템 유형** | 라이선스형 상용 플랫폼 (Nasdaq 벤더) | 자체 개발 (KRX + KOSCOM) |
| **출시 연도** | 2010 (파생상품) | 2014 (2009년 원래 Exture 대체) |
| **매칭 지연시간** | 평균 < 100 μs (참조); SGX에서 < 90 μs | ≤ 70 μs (전 자산군) |
| **자산 범위** | 멀티에셋 (파생상품, 주식, 채권, 상품) | 올인원: 주식 (KOSPI, KOSDAQ), 채권, 선물, 옵션, ETF를 단일 플랫폼에서 지원 |
| **매칭 알고리즘** | 구성 가능: 가격-시간, pro-rata, 상품별 하이브리드 | 가격-시간 우선; 선별 종목에 대한 LP (Liquidity Provider) 제도 |
| **내재가격** | 있음 — 전략 간 다중 수준 implied-in 및 implied-out | 제한적; 주로 아웃라이트 매칭 [unverified] |
| **청산 통합** | 단일 플랫폼 내 매매 + 청산 통합 (DCASS) | 별도 청산 시스템; KSD (한국예탁결제원)가 결제 담당 |
| **리스크 관리** | PRM/TradeGuard로 거의 제로 지연시간 영향; ESMA 준수 | 통합된 사전거래 리스크 검사; KRX 특화 규제 체계 |
| **감시** | SMARTS 감시 네이티브 통합; AI 기반 | KOSCOM 개발 도구를 사용한 KRX 시장감시 |
| **시장데이터 프로토콜** | MoldUDP64를 통한 ITCH (바이너리, 주문별) | Solace PubSub+ 하드웨어 어플라이언스; 독자 바이너리 프로토콜 |
| **주문 입력 프로토콜** | FIX, OUCH, OMnet API | FIX 기반; KOSCOM 게이트웨이를 통한 KRX 독자 프로토콜 |
| **글로벌 배포** | 전 세계 40개 이상의 거래소 | 주로 KRX; KOSCOM을 통해 일부 신흥시장에 수출 |
| **업그레이드 모델** | 주요 버전 릴리스 (현재 Eqlipse "에버그린" 분기별로 전환 중) | 다년 주기의 주요 버전 업그레이드 |
| **전략 지원** | 포괄적: 사전 정의 + 사용자 정의 전략; 네이티브 전략 매칭 | 표준 전략 주문 지원; 거래소 정의 전략 유형 |
| **클라우드 전략** | Eqlipse 후속 플랫폼은 클라우드 대응 (하이브리드 온프레미스/클라우드) | 온프레미스; 핵심 매매에 대한 퍼블릭 클라우드 전략 없음 [unverified] |

### 주요 차별화 요소 (Key Differentiators)

**Genium INET의 강점:**
- **광범위한 배포 및 실전 검증:** 아메리카, 유럽, 아시아태평양, 중동의 40개 이상의 거래소 배포가 광범위한 운영 실적과 다양한 사용 사례로부터의 지속적 개선을 제공한다
- **모듈형 및 구성 가능한 설계:** 거래소가 자사의 특정 시장 구조에 맞게 매칭 알고리즘, 리스크 파라미터, 상품 구성, 프로토콜 조합을 선택할 수 있다 — 다양한 상품 유형을 가진 파생상품 시장에서 중요한 이점이다
- **검증된 아시아태평양 파생상품 실적:** HKEX, SGX, ASX에서의 주요 파생상품 배포가 복잡한 상품 구성을 가진 대량 아시아 파생상품 시장에 대한 플랫폼의 적합성을 입증한다
- **매매-청산 통합:** 통합 매매 + 청산 솔루션이 연동 복잡성을 줄이고 매매 수명주기 전반에 걸쳐 일관된 리스크 관리를 제공한다
- **풍부한 파생상품 기능:** 내재가격, pro-rata 매칭, 복합주문 지원, mass quoting, 유연한 전략 정의는 OM/CLICK 유산으로부터 수십 년에 걸쳐 정제된 파생상품 전용 기능을 나타낸다
- **감시 생태계:** 네이티브 SMARTS 통합이 관할권 간 규제 준수에 중요한 세계적 수준의 감시 역량을 제공한다

**KRX Exture+의 강점:**
- **더 빠른 원시 매칭:** Exture+의 ≤ 70 μs는 많은 Genium INET 배포와 경쟁적이거나 더 빠르며, 이는 단일 시장에 대한 집중 최적화를 반영한다
- **통합 단일 시장 플랫폼:** 모든 KRX 자산군이 하나의 시스템에 있어 교차 시스템 조율 복잡성을 제거한다
- **완전한 국내 통제:** 자체 개발이 벤더 의존성 없이 기술 결정, 업그레이드 시기, 커스터마이징에 대한 완전한 주권을 제공한다
- **Solace 하드웨어 메시징:** 전용 메시징 어플라이언스가 보장되고 결정론적인 데이터 전달을 제공한다
- **총비용 투명성:** 외부 벤더에 대한 라이선스 비용 없음; 개발 비용은 전적으로 KRX/KOSCOM이 부담

**아키텍처 철학 차이:**
- Genium INET은 **유연성과 글로벌 이식성**에 최적화되어 있다 — 다양한 시장 구조, 규제 요건, 상품 구성을 가진 다양한 거래소를 서비스하도록 설계되어 구성 가능성과 멀티에셋 지원이 최우선시된다
- KRX Exture+는 **단일 국내 시장의 포괄적 커버리지**에 최적화되어 있다 — 모든 자산군, 모든 매칭 로직, 모든 리스크 제어가 일반화의 오버헤드 없이 한국 시장에 특화되어 맞춤 구성되어 있다

---

## 출처 (Sources)

- [Source: Nasdaq IR, "NASDAQ OMX Launches World's Fastest Trading System for Its Nordic Derivatives Markets", October 2010](https://ir.nasdaq.com/news-releases/news-release-details/nasdaq-omx-launches-worlds-fastest-trading-system-its-nordic)
- [Source: Nasdaq IR, "NASDAQ OMX to Deliver World's Fastest Trading Platform to Singapore Exchange"](https://ir.nasdaq.com/news-releases/news-release-details/nasdaq-omx-deliver-worlds-fastest-trading-platform-singapore)
- [Source: Nasdaq IR, "ASX Launches Next Generation Trading Platform Powered by NASDAQ OMX's Genium INET"](https://ir.nasdaq.com/news-releases/news-release-details/asx-launches-next-generation-trading-platform-powered-nasdaq)
- [Source: Nasdaq, "Technical Information - Genium INET Trading and Clearing Platform"](https://www.nasdaq.com/solutions/technical-information-genium-inet-trading-and-clearing-platform)
- [Source: Nasdaq, "Genium INET Protocol Specifications"](https://www.nasdaq.com/solutions/genium-inet-protocol-specifications)
- [Source: Nasdaq, "Genium INET Front Ends"](https://www.nasdaq.com/solutions/genium-inet-front-ends)
- [Source: Nasdaq, "Genium INET - Pro-Rata Matching"](https://www.nasdaq.com/solutions/genium-inet-pro-rata-matching)
- [Source: Nasdaq, "Pre-Trade Risk Management"](https://www.nasdaq.com/solutions/pre-trade-risk-management)
- [Source: Nasdaq, "PRE-TRADE RISK MANAGEMENT Product Sheet"](https://www.nasdaq.com/docs/prm-genium-inet-product-sheet.pdf)
- [Source: Nasdaq, "NASDAQ NORDIC Genium INET Pre-trade Risk Management Service Guide 2.2"](https://www.nasdaq.com/docs/nasdaq-nordic-genium-inet-prm-service-guide-2.2.pdf)
- [Source: Nasdaq, "Genium INET Upgrade 8.0.0.0"](https://www.nasdaq.com/solutions/genium-inet-upgrade-to-version-8.0.0.0)
- [Source: Nasdaq, "Genium INET Test Systems"](https://www.nasdaq.com/solutions/genium-inet-test-systems)
- [Source: Nasdaq, "Genium INET Conformance"](https://business.nasdaq.com/trade/trade-management/technical-information/genium-inet/conformance.html)
- [Source: Nasdaq, "Nasdaq Market Surveillance (SMARTS) Features"](https://www.nasdaq.com/solutions/nasdaq-market-surveillance/features)
- [Source: Nasdaq Newsroom, "Nasdaq Launches Eqlipse, Fourth Generation of its Marketplace Technology Platform"](https://www.nasdaq.com/newsroom/nasdaq-launches-eqlipse-fourth-generation-its-marketplace-technology-platform)
- [Source: Nasdaq, "Capital Market Technology & Business Solutions - Nasdaq Eqlipse"](https://www.nasdaq.com/solutions/fintech/nasdaq-eqlipse)
- [Source: Nasdaq, "SAXESS trading platform launched successfully at Helsinki, Tallinn and Riga stock exchanges"](https://www.nasdaq.com/about/press-center/saxess-trading-platform-launched-successfully-helsinki-tallinn-and-riga-stock)
- [Source: Nasdaq, "Genium INET OMnet Application Programmer's Interface Manual"](https://www.nasdaq.com/docs/omnet_api_nordic_va2393_0.pdf)
- [Source: Nasdaq, "FIX for Genium INET for NASDAQ Nordic 2.0, Revision 2.28"](https://www.nasdaq.com/docs/2023/05/31/Genium_INET_FIX_Protocol_Specification-6.0.0240_v228.pdf)
- [Source: Nasdaq, "Genium INET ITCH Protocol Specification NFX"](https://www.nasdaq.com/docs/ITCH%20Reference%20Data.pdf)
- [Source: HKEX, "HKEx Upgrades its Derivatives Trading and Clearing Systems to Genium INET", October 2013](https://www.hkex.com.hk/News/News-Release/2013/131016news?sc_lang=en)
- [Source: HKEX, "HKATS User's Guide Genium INET CLICK Trade", July 2017](https://www.hkex.com.hk/-/media/HKEX-Market/Services/Trading/Derivatives/Infrastructure/HKATS/HKATS-User_s-Guide/genium-user-guide.pdf)
- [Source: Borsa Istanbul, "Genium INET FIX Drop Copy Protocol Specification"](https://www.borsaistanbul.com/files/genium-inet-fix-drop-copy-protocol-specification.pdf)
- [Source: Borsa Istanbul, "Genium INET FIX Reference Data Protocol Specification"](https://borsaistanbul.com/files/genium-inet-fix-reference-data-protocol-specification.pdf)
- [Source: Finextra, "HKEx moves derivatives clearing and trading platforms to Genium Inet", 2013](https://www.finextra.com/pressarticle/52257/hkex-moves-derivatives-clearing-and-trading-platforms-to-genium-inet)
- [Source: The Trade News, "Nasdaq OMX Nordic installs INET for derivatives"](https://www.thetradenews.com/nasdaq-omx-nordic-installs-inet-for-derivatives/)
- [Source: A-Team Insight, "NLX Leverages Genium Inet, Equinix For Low Latency"](https://a-teaminsight.com/blog/nlx-leverages-genium-inet-equinix-for-low-latency/)
- [Source: A-Team Insight, "SGX Reaches for Lower Latency"](https://a-teaminsight.com/blog/sgx-reaches-for-lower-latency/?brand=tti)
- [Source: Markets Media, "Nasdaq Pushes Technology"](https://www.marketsmedia.com/nasdaq-pushes-technology/)
- [Source: Markets Media, "Nasdaq Reaches 'New Base Camp' with Eqlipse"](https://www.marketsmedia.com/nasdaq-reaches-new-base-camp-with-eqlipse/)
- [Source: OnixS, "ITCH Protocol Usage"](https://www.onixs.biz/insights/itch-protocol-usage)
- [Source: Databento, "What is the ITCH protocol?"](https://databento.com/microstructure/itch)
- [Source: NASDAQ OMX Nordic, "Business Continuity Plan Description"](https://docplayer.net/7172713-Nasdaq-omx-nordic-business-continuity-plan-description.html)
- [Source: Data Center Dynamics, "NASDAQ OMX to supply Genium Inet platform to Hong Kong stock exchange"](https://www.datacenterdynamics.com/en/news/nasdaq-omx-to-supply-genium-inet-platform-to-hong-kong-stock-exchange/)
- [Source: Wikipedia, "Nasdaq Nordic", accessed 2026-04-07](https://en.wikipedia.org/wiki/Nasdaq_Nordic)
- [Source: Wikipedia, "Nasdaq, Inc.", accessed 2026-04-07](https://en.wikipedia.org/wiki/Nasdaq,_Inc.)
