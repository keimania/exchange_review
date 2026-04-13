# Korea Exchange (KRX)

> **Last Updated:** 2026-04-13
> **Research Tier:** Tier 1
> **Domain:** Equities

---

## 1. Overview & Profile

| Item | Details |
|------|---------|
| Official Name | Korea Exchange (한국거래소) |
| Abbreviation | KRX |
| Website | https://www.krx.co.kr / https://global.krx.co.kr |
| Year Established | 1956 (Korea Stock Exchange); 2005 (merged as KRX) |
| Country / City | South Korea / Busan (headquarters), Seoul (equities operations) |
| Ownership Structure | Private enterprise; owned by ~44 financial and government entities; removed from direct state control in 2015; supervised by FSC as public-service-related organization |
| Parent Company / Group | Korea Exchange (sole entity; no parent) |
| Regulatory Authority | Financial Services Commission (FSC) / Financial Supervisory Service (FSS) |
| Market Capitalization (listed companies) | ~KRW 4,277 trillion (~USD 2.95 trillion) (January 2026) |
| Total Listed Instruments | ~2,901 companies (KOSPI ~954, KOSDAQ ~1,700+, KONEX ~129) plus ETFs, ETNs, ELWs, REITs, bonds |
| Average Daily Trading Volume | ~USD 20.7 billion (KOSPI, February 2026) |
| Average Daily Trading Value | ~KRW 32.23 trillion (KOSPI, February 2026) |

[Source: Wikipedia — Korea Exchange, accessed 2026-04-13]
[Source: Social News XYZ, "KOSPI's Average Daily Trading Volume Exceeds $20.7 Billion in Feb", 2026-03-01]

### Key Historical Milestones
- **1956:** Korea Stock Exchange established in Busan (Daehan Stock Exchange)
- **1963:** Reorganized as Korea Stock Exchange (KSE) under government oversight
- **1988:** Electronic trading introduced (parallel with open outcry, inspired by TSE CATS)
- **1996:** KOSDAQ market launched for technology and growth companies
- **1997 (September):** Fully automated trading; trading floor eliminated
- **2005 (January 27):** Korea Exchange (KRX) formed by merger of KSE, KOSDAQ market, and Korea Futures Exchange (KOFEX)
- **2009 (March):** EXTURE trading system launched, consolidating three legacy systems
- **2013 (July):** KONEX market launched for startups and SMEs
- **2014:** EXTURE+ launched (sub-70 us latency, first Linux x86 in Korean capital markets)
- **2015:** KRX removed from direct state control; became private enterprise
- **2023 (January):** Exture 3.0 Phase 1 launched (trading + information distribution)
- **2023 (October):** Exture 3.0 Phase 2 launched (clearing & settlement)
- **2025 (March):** Nextrade (NXT) launched as Korea's first alternative exchange, ending KRX monopoly
- **2025 (December):** KRX introduces maker-taker fee model (first fee change in 20 years)
- **2026 (February):** KOSPI reaches 6,000 milestone

---

## 2. Market Structure

### 2.1 Market Segments
| Segment | Description | Listing Requirements (Summary) |
|---------|-------------|-------------------------------|
| **KOSPI (Main Board)** | Large-cap blue-chip market; Korea's primary equities market | Equity KRW 30B+; 3+ years operations; 500+ shareholders; 25%+ public float; clean audit opinion; financial performance (5 alternative paths including revenue KRW 100B+ or market cap KRW 1T+) [상장규정 Art. 29] |
| **KOSDAQ** | Growth market for technology, venture, and mid-cap companies | Lower thresholds than KOSPI; targets innovative and growth companies |
| **KONEX** | Third-tier market for startups and SMEs | Lowest thresholds; pre-KOSDAQ stage companies; viability questioned (only 129 listed as of Jan 2024, 1 new listing in 2024) |

**Listed instrument types on KOSPI** [상장규정]:
- Common shares (보통주권), Preferred/class shares (종류주권)
- Foreign shares and DRs (외국주권/예탁증권)
- SPAC shares (기업인수목적회사주권)
- ETFs (상장지수펀드), Foreign ETFs
- ETNs (상장지수증권)
- ELWs (주식워런트증권)
- REITs (부동산투자회사주권)
- Debt securities (채무증권 — corporate bonds, government bonds, ABS, covered bonds)
- Beneficiary certificates (수익증권)
- Subscription rights certificates (신주인수권증권/증서)
- Investment company shares, Ship investment company shares

### 2.2 Trading Sessions
| Session | Local Time (KST) | UTC | Description |
|---------|-----------------|-----|-------------|
| Pre-market block/basket trading | 08:00 - 09:00 | 23:00 - 00:00 | Off-hours block, basket, and competitive block trades |
| Pre-market closing-price trading (시간외종가매매) | 08:30 - 08:40 | 23:30 - 23:40 | Trades at previous day's closing price |
| Pre-open order collection | 08:30 - 09:00 | 23:30 - 00:00 | Orders accumulated for opening call auction |
| **Opening Call Auction (개시 동시호가)** | ~09:00 | ~00:00 | Single-price determination for opening price |
| **Continuous Trading (접속매매)** | 09:00 - 15:20 | 00:00 - 06:20 | Price-time priority matching |
| Closing auction order collection | 15:20 - 15:30 | 06:20 - 06:30 | Orders accumulated for closing call auction |
| **Closing Call Auction (장종료 동시호가)** | ~15:30 | ~06:30 | Single-price determination for closing price |
| Post-market closing-price trading | 15:30 - 16:00 | 06:30 - 07:00 | Trades at closing price [업무규정 시행세칙 Art. 11] |
| Post-market single-price trading (시간외단일가매매) | 16:00 - 18:00 | 07:00 - 09:00 | Call auction at 10-minute intervals; +/-10% of closing price [업무규정 Art. 34의2] |
| Post-market block/basket trading | 15:40 - 18:00 | 06:40 - 09:00 | Off-hours block and basket trades |

**Total trading window:** 08:00 - 18:00 KST (10 hours including off-hours sessions)

[Source: 유가증권시장 업무규정 Art. 4; 업무규정 시행세칙 Art. 8, 11]

### 2.3 Tick Sizes

**Equities (주권), Foreign DRs, Subscription Rights, Beneficiary Certificates** [시행세칙 Art. 32(2)]:

| Price Range (KRW) | Tick Size (KRW) |
|--------------------|-----------------|
| Below 2,000 | 1 |
| 2,000 ~ < 5,000 | 5 |
| 5,000 ~ < 20,000 | 10 |
| 20,000 ~ < 50,000 | 50 |
| 50,000 ~ < 200,000 | 100 |
| 200,000 ~ < 500,000 | 500 |
| 500,000 and above | 1,000 |

**ETFs and ETNs:**

| Price Range (KRW) | Tick Size (KRW) |
|--------------------|-----------------|
| Below 2,000 | 1 |
| 2,000 and above | 5 |

**ELWs:** KRW 5 (flat)

### 2.4 Lot Sizes
- **Standard lot:** 1 share (no board lot requirement) [시행세칙 Art. 33]
- **ETF/ETN:** 1 unit
- **ELW:** 10 units
- **Odd lot trading:** Supported

### 2.5 Market Maker / Liquidity Provider Programs

**A. Liquidity Provider (유동성공급회원, LP)** [업무규정 Art. 20의2 ~ 20의8]:
- Eligible for: Stocks, ETFs, ETNs, ELWs
- Must be a settlement member (결제회원) with 투자매매업 license
- **Spread obligation:** Must submit quotes within 5 minutes when spread exceeds contractual threshold:
  - Stocks: within 3% spread ratio
  - ETF/ETN (domestic underlying): within 2%; (foreign underlying): within 3%
- **NAV tracking:** ETF/ETN deviation must not exceed 3% (domestic) / 6% (foreign)
- LP position limit: Quote obligation exempted when holdings exceed 2% of listed shares
- Performance evaluated by KRX; compensation from ETF trading fee pool

**B. Market Maker (시장조성자)** [업무규정 Art. 20의9 ~ 20의11; 시행세칙 Art. 31-12 ~ 31-22]:
- For low-liquidity stocks (저유동성종목) designated by KRX
- Continuous two-sided quoting obligation
- Must maintain minimum quote maintenance amount within contractual spread
- Start quoting within 3 minutes of market open
- Quarterly evaluation; penalty points for non-compliance can lead to 1-year suspension
- Compensation from KRX trading fee revenue on designated stocks
- Buy obligation exempted when position exceeds 0.2% of listed shares or KRW 100M

---

## 3. Trading Mechanism

### 3.1 Auction Mechanisms

**Opening Auction (개시 동시호가)** [업무규정 Art. 23]:
- Call auction (단일가격에 의한 개별경쟁매매) at market open (~09:00)
- Orders collected 08:30-09:00; executed at single equilibrium price
- Price determination: the price where aggregate sell volume equals aggregate buy volume (합치가격)
- If multiple match prices exist, select the price closest to previous close [Art. 23④⑤]

**Closing Auction (장종료 동시호가)** [업무규정 Art. 23]:
- Orders collected 15:20-15:30; executed at single closing price
- 조건부지정가호가 (conditional limit orders) convert to market orders for closing auction

**Volatility Interruption Auction** [업무규정 Art. 26의2]:
- Triggered when VI conditions are met (see Section 8)
- 2-minute call auction with random end within 30 seconds [시행세칙 Art. 35(1)(4)]

**Off-Hours Single-Price Trading (시간외단일가매매)** [업무규정 Art. 34의2]:
- Call auctions at 10-minute intervals from 16:00 to 18:00
- Price range: +/-10% of the day's closing price, within daily price limits

### 3.2 Continuous Trading
- **Order-driven** market with price-time priority (가격-시간 우선원칙)
- Continuous matching (접속매매 / 복수가격에 의한 개별경쟁매매) [업무규정 Art. 24]
- Execution price = the earlier (선행) order's price when lowest ask meets highest bid

### 3.3 Price Discovery

**Priority rules** [업무규정 Art. 22②]:

| Priority | Rule | Detail |
|----------|------|--------|
| 1. Price priority (가격우선) | Art. 22②1 | Lower sell price > higher sell price; Higher buy price > lower buy price; Market orders have priority over limit orders |
| 2. Time priority (시간우선) | Art. 22②2 | Same price: earlier submission takes priority |
| 3. Simultaneous order rules | Art. 22③ | For call auctions: orders at limit-up (buys) or limit-down (sells) during price determination treated as simultaneous |

---

## 4. Order Types

### 4.1 Standard Order Types
| Order Type | Korean | Description | Article |
|-----------|--------|-------------|---------|
| Limit Order | 지정가호가 | Specify issue, quantity, and price | Art. 2④1 |
| Market Order | 시장가호가 | Specify issue and quantity; price determined by matching | Art. 2④2 |
| Conditional Limit | 조건부지정가호가 | Limit order during continuous session; converts to market at closing auction | Art. 2④3 |
| Best Limit (opposite-side) | 최유리지정가호가 | Auto-priced at best opposing quote (sell at best bid, buy at best ask) | Art. 2④4 |
| Best Priority (own-side) | 최우선지정가호가 | Auto-priced at own-side best quote (sell at best ask, buy at best bid) | Art. 2④5 |

### 4.2 Advanced Order Types
| Order Type | Korean | Description | Article |
|-----------|--------|-------------|---------|
| Competitive Block Order | 경쟁대량매매호가 | For VWAP/block trades; minimum KRW 500M based on base price | Art. 2④6 |
| **Mid-Price Order** | 중간가호가 | **NEW (2025.2.5)** — Priced at midpoint of best bid/ask | Art. 2④7 |
| **Stop Limit Order** | 스톱지정가호가 | **NEW (2025.2.5)** — Limit order activated when stop price is triggered | Art. 2④8 |
| Target Price Order | 목표가주문 | Client-level VWAP-targeting order | Art. 2⑤6 |

### 4.3 Time-in-Force Options
| TIF | Description | Article |
|-----|-------------|---------|
| DAY | Default; valid for the trading day | |
| IOC (Immediate or Cancel) | Execute available quantity immediately, cancel remainder | 시행세칙 Art. 108(12) |
| FOK (Fill or Kill) | Execute entire quantity or cancel all | 시행세칙 Art. 108(12) |

**Restrictions:**
- Market/conditional limit orders prohibited for: short-selling, LP/MM quotes, treasury stock, off-hours sessions
- Mid-price orders prohibited during: call auctions, all off-hours sessions, LP/MM quotes, short-selling
- Stop limit orders prohibited during: call auctions, all off-hours sessions

### 4.4 Order Modification / Cancellation
- Orders may be modified or cancelled before execution
- Modification allowed for: price, quantity (decrease only or change), order type conditions
- **Kill switch (접속해제 호가취소):** Members may pre-register for automatic mass cancellation if connectivity is severed [업무규정 Art. 13의2]
- **Bulk cancellation (일괄호가취소):** HFT traders can cancel all orders by HFT ID within a security type [시행세칙 Art. 17-2]
- **Account-level kill switch:** Cancel all orders or block new orders for specific algo accounts; 10-minute cooldown before reactivation [시행세칙 Art. 130-2]
- **Self-trade prevention:** Required for HFT; 3 modes (cancel resting, cancel incoming, cancel both) [시행세칙 Art. 13-2]

---

## 5. Trading System (Technology)

| Item | Details |
|------|---------|
| System Name | Exture 3.0 (엑스처 3.0) |
| Vendor / In-house | In-house (KRX) with KOSCOM as primary technology partner |
| Architecture | Memory-based order book; layered/tiered architecture; flexible, expandable with market-specific multi-matching capabilities |
| Matching Engine | Zero-latency design goal; memory-based matching |
| Round-trip Latency | ~49 us [estimated] (30% improvement over EXTURE+ worst-case 70 us) |
| Order Processing Capacity | 100,000+ TPS (inherited from EXTURE+ baseline) |
| Messages Per Second | Not publicly disclosed; derivative bandwidth expanded from 45 Mbps to 100 Mbps |
| Launch Year | 2023 (Phase 1: January 25; Phase 2: October 4) |

[Source: Seoul Finance, "Exture 3.0 Launch", 2023-01-25]
[Source: KRX Global — EXTURE+ Trading System]
[Source: CEO Score Daily, "Exture 3.0 Phase 2", 2023-09-26]

### System History
| Period | System | Notes |
|--------|--------|-------|
| 1956-1988 | Manual / Open Outcry | Physical trading floor in Busan |
| 1988-1997 | Computer-assisted trading | Electronic trading introduced; parallel with open outcry |
| 1997-2009 | Fully automated (legacy) | Trading floor eliminated September 1997; separate systems for KSE, KOSDAQ, KOFEX |
| 2009-2014 | EXTURE | Launched March 2009; consolidated 3 exchange systems; ~20 ms latency; 250 TPS; 40M quotes/day |
| 2014-2023 | EXTURE+ | Sub-70 us worst-case latency; 20,000+ TPS matching; 100,000+ TPS throughput; first Linux x86 in Korean capital markets; FIX/FAST protocol support; DMA support |
| 2023-present | **Exture 3.0** | 30% faster than EXTURE+; low-latency extended to entire system (info distribution, clearing/settlement); Phase 1: trading + data; Phase 2: clearing + settlement; unified clearing/settlement UI (on-exchange + OTC integrated); integrated real-time risk calculation and simulation |

### Technology Stack
- **Platform:** Linux-based x86 servers
- **Architecture:** Memory-based order book with layered design
- **Protocols:** FIX/FAST for order entry and market data
- **DMA:** Supported
- **Algorithmic trading:** Supported with HFT registration requirement

### Disaster Recovery / Business Continuity
- **Primary DC (equities):** Seoul area
- **Primary DC (derivatives):** Busan
- **DR architecture:** Seoul and Busan interchangeable failover backup
- **Backup system (예비시스템):** Can be activated if primary system fails [시행세칙 Art. 42(4)]
- **System failure threshold:** Trading hours may be changed when failures affect firms responsible for 75%+ of total trading volume [시행세칙 Art. 8(2)]

---

## 6. Market Data

### 6.1 Data Feed Protocols
| Protocol | Description | Use Case |
|----------|-------------|----------|
| FIX/FAST | Standard financial protocols supported by EXTURE+ and Exture 3.0 | Order entry and market data |
| KRX proprietary | Direct market data feed via KOSCOM infrastructure | Real-time production data |
| STOCK-NET | KOSCOM's dedicated high-speed financial network | Connects KRX, securities firms, KOFIA, institutional investors |

### 6.2 Data Levels
- **Level 1:** Best bid/ask, last trade price, volume
- **Level 2:** Depth of book (multiple price levels)
- **Full depth:** Available through KRX real-time market data products

### 6.3 Distribution Infrastructure
- **Primary distributor:** KOSCOM (Korea Securities Computing Corporation)
- **Distribution methods:**
  - Real-time via dedicated high-speed network (STOCK-NET)
  - Real-time via internet
  - FTP batch (end-of-day)
- **Recipients:** Securities/futures firms, domestic/foreign institutional investors, information providers, media
- **International access:** ICE Global Network provides access to KRX native data feed and execution services

[Source: KOSCOM — Market Data Service]
[Source: ICE Developer — Korea Exchange]

### 6.4 Historical Data
- **KRX Data Marketplace:** Official data portal at data.krx.co.kr
- Both free and paid tiers available
- Historical daily data, corporate actions, indices, and reference data

---

## 7. Connectivity & Access

### 7.1 Membership / Participation
- **회원 (Member):** Governed by 회원관리규정; must be licensed financial institution [업무규정 Art. 2①]
- **결제회원 (Settlement/Clearing Member):** Settles trades in own name [Art. 2②]
- **매매전문회원 (Trading-only Member):** Trades in own name but delegates settlement to clearing member [Art. 2③]
- Foreign participants access via licensed Korean broker-dealers or registered QFI framework

### 7.2 Connection Methods
| Method | Description |
|--------|-------------|
| Dedicated line | KOSCOM STOCK-NET high-speed financial network |
| Co-location | Proximity hosting at KOSCOM data centers |
| Internet | Available for lower-speed access and retail platforms |
| DMA | Direct Market Access supported since EXTURE+ |

### 7.3 Co-location / Proximity Services
- **Seoul DC:** Primary for equities (KOSPI, KOSDAQ) co-location
- **Busan DC (KOSCOM):** Primary for derivatives market co-location and proximity hosting
- **Services:** Rack space, cross-connects, proximity hosting
- **International connectivity:** IPC (Itiviti) connected to KOSCOM Busan facility; ICE Global Network provides access
- **Equal-length cross-connects:** Standard practice for fair-access co-location

[Source: KOSCOM — STOCK-NET; WatersTechnology, "IPC connects to KOSCOM Busan facility"]

### 7.4 API Protocols
| Protocol | Use Case |
|----------|----------|
| FIX | International standard order entry; supported by EXTURE+ and Exture 3.0 |
| FAST | Market data compression protocol |
| KRX Native/Binary | Proprietary high-performance protocol for co-located participants |

### 7.5 Certification / Testing
- Detailed technical specifications governed by 「회원시스템 접속 등에 관한 지침」 (Member System Connection Guidelines)
- Members must disclose: order generation entity, location, input device, transmission medium, pre-trade check method, and geographic location of check system [시행세칙 Art. 104-2]
- HFT systems require connectivity tests before registration and annually [시행세칙 Art. 131-4]

---

## 8. Risk Controls & Circuit Breakers

### 8.1 Price Limits

**Daily price limits** [업무규정 Art. 20]:

| Type | Threshold | Notes |
|------|-----------|-------|
| Standard equities | **+/- 30%** of base price (기준가격) | Art. 20② |
| Leveraged ETF/ETN | 30% x leverage multiple (e.g., 2x = +/-60%) | Art. 20② |
| IPO first trading day | **+300% / -60%** of base price | 시행세칙 Art. 31(3) |
| Delisting trading (정리매매) | **No price limit** | Art. 20③ |
| Off-hours single-price trading | **+/- 10%** of closing price (within daily limits) | Art. 34의2③ |

### 8.2 Circuit Breakers

**Market-Wide Circuit Breaker (SAPI, 시장전체 매매거래중단)** [업무규정 Art. 25; 시행세칙 Art. 39]:

| Level | Trigger | Halt Duration | Conditions |
|-------|---------|---------------|------------|
| Level 1 | KOSPI drops **8%+** from previous close, sustained **1 minute** | **20-minute halt** (then 10-min call auction to resume) | Once per day; not triggered after 14:50 |
| Level 2 | KOSPI drops **15%+** from previous close AND 1%+ further from Level 1 halt, sustained 1 min | **20-minute halt** | Once per day; not triggered after 14:50 |
| Level 3 | KOSPI drops **20%+** from previous close AND 1%+ further from Level 2 halt, sustained 1 min | **Trading halted for remainder of day** | Applies even after 14:50 |

**Program Trading Sidecar (프로그램매매호가 효력정지)** [업무규정 Art. 16; 시행세칙 Art. 20]:
- Trigger: KOSPI 200 front-month futures price rises/falls **5%+** from base price, sustained 1 minute
- Effect: Program trading orders suspended for **5 minutes**
- Applied **once per day**; not triggered after 14:50

**Volatility Interruption (VI, 종목별 매매계약체결방법 변경)** [업무규정 Art. 26의2; 시행세칙 Art. 41-2]:

| Type | Trigger | Duration |
|------|---------|----------|
| **Static VI** — KOSPI 200 constituents | **3%** from last call auction price (reference price) | 2-minute call auction + random 30-sec close |
| **Static VI** — Other stocks/ETF/ETN | **6%** from reference price | 2-minute call auction + random 30-sec close |
| **Static VI** — During closing auction | Thresholds halved: 2% (KOSPI 200) / 4% (others); **1%** on derivatives last trading day | 2-minute call auction |
| **Dynamic VI** — All equities/ETF/ETN | **10%** from last trade price | 2-minute call auction + random 30-sec close |

**VI Exceptions:** Delisting trading, short-term overheated stocks, abnormal surge stocks, cautionary stocks, IPO day stocks, prices within 3 tick sizes of prior price for stocks below KRW 1,000.

### 8.3 Pre-trade Risk Controls

**Order validation checks (회원의 호가 사전통제의무)** [업무규정 Art. 11의2; 시행세칙 Art. 12-2]:
- Members **must** validate orders before submission to KRX system
- Required checks:
  1. Account validation (account number, type)
  2. Instrument validation (security code, trading suspension status)
  3. **Quantity limits** by market cap tier:
     - Market cap >= KRW 10T: max KRW 100B / base price per order
     - Market cap KRW 100B ~ 10T: max 1% of listed shares
     - Market cap KRW 20B ~ 100B: max KRW 1B / base price
     - Market cap < KRW 20B: max 5% of listed shares
  4. Price validation (tick size, price limit compliance)
  5. Order type validation per session
  6. Margin requirements
  7. HFT account validation

**Algorithm trading controls** [업무규정 Art. 104의2]:
- Algo trading accounts must be registered with KRX
- Members must identify and manage algo trading risks
- Account-level kill switch available for emergencies

**High-frequency trading (HFT) controls** [업무규정 Art. 104의3-4]:
- HFT participants must be **registered** with KRX before trading
- Require: system adequacy, sufficient knowledge/experience
- HFT accounts separately registered
- KRX may revoke registration with 6-month re-registration ban
- Members must refuse orders from unregistered HFT participants
- Record retention: 10 years for all HFT-related records

### 8.4 Kill Switch
- **Disconnect kill switch (접속해제 호가취소):** Automatic mass cancellation when member-exchange connection is severed [업무규정 Art. 13의2]
- **Bulk order cancellation (일괄호가취소):** HFT traders cancel all orders by HFT ID [시행세칙 Art. 17-2]
- **Account-level kill switch (계좌단위호가처리):** Cancel all orders or block new orders for specific algo accounts; 10-minute cooldown [시행세칙 Art. 130-2]

**Erroneous trade relief** [업무규정 Art. 28, 28의2]:
- KRX may correct erroneous trade executions
- Large erroneous trade relief (대규모착오매매 구제) available for trades risking settlement failure and market disruption

**Short selling controls** [업무규정 Art. 17, 18]:
- Naked short selling prohibited
- Covered short selling permitted with uptick rule: cannot sell below last trade price unless last price was an uptick
- KRX may restrict short selling on specific stocks per 시행세칙 criteria
- **Overheated stock rules** [시행세칙 Art. 24-3]: When price drops 5-10% AND short ratio is 3x market average AND short volume is 6x 40-day average, 1-day short selling ban applies

**Short-term overheated stock (단기과열종목) designation** [시행세칙 Art. 133-134]:
- Triggers: Price up 130%+ vs 40-day avg, turnover 600%+ vs 40-day avg, volatility 150%+ vs 40-day avg
- Effect: 3 trading days of 30-minute interval single-price auction (extendable)

---

## 9. Regulatory Framework

### 9.1 Supervising Authority
- **FSC (Financial Services Commission, 금융위원회):** Highest financial authority; policy formulation, licensing, and approval
- **FSS (Financial Supervisory Service, 금융감독원):** FSC's enforcement arm; examinations, investigations, sanctions across all financial sectors

### 9.2 Key Regulations
- **Financial Investment Services and Capital Markets Act (자본시장법, FSCMA):** Primary securities law; function-based regulation (same activities = same rules regardless of entity type); covers stocks, bonds, collective investment schemes, derivatives
- **유가증권시장 업무규정:** KRX KOSPI Market Business Regulations (trading rules, order types, circuit breakers)
- **유가증권시장 상장규정:** KRX KOSPI Market Listing Regulations (listing requirements, delisting criteria)
- **유가증권시장 공시규정:** KRX KOSPI Market Disclosure Regulations (timely, periodic, fair, query disclosure)
- **회원관리규정:** KRX Member Management Regulations

### 9.3 Market Surveillance
- **KRX as SRO:** Self-regulatory functions including market surveillance, listed company supervision, market manipulation prevention, delisting authority
- **Market Surveillance Committee:** Prevents market manipulation; investigates abnormal transactions
- May impose sanctions including delisting or trading suspensions
- Refers cases to FSS for further enforcement

### 9.4 Reporting Requirements
- **Disclosure types:** Timely (수시공시), Periodic (정기공시), Fair (공정공시), Query (조회공시), Voluntary (자율공시), Clarification (해명공시) [공시규정 Art. 7-28]
- **Material event triggers:** Same-day disclosure required for events exceeding 5% of revenue, 5% of equity capital, 10% of equity capital, etc. (thresholds halved for large-cap companies with KRW 2T+ total assets) [공시규정 Art. 7]
- **Settlement results:** 30% YoY change in revenue/operating income/net income triggers disclosure (15% for large-cap)
- **English-language disclosure:** Mandatory for companies with total assets >= KRW 10T (unless foreign ownership < 5%) or >= KRW 2T with >= 30% foreign ownership; deadline 3 trading days [공시규정 Art. 48]
- **Penalty system:** Demerit points (벌점) for violations; max KRW 1 billion monetary penalty; unfaithful disclosure designation with ticker marking
- **Trading halts on disclosure:** 30-minute halt for material disclosures; full-day halt for serious infractions [공시규정 Art. 40]

### 9.5 Cross-border Arrangements
- QFI (Qualified Foreign Investor) scheme for foreign institutional access (quota limits abolished)
- Foreign companies may list on KOSPI under modified requirements [상장규정 Art. 53]
  - Fast-track for large foreign companies: 5+ years listed overseas, market cap KRW 2T+, revenue KRW 2T+
  - Must appoint Korean listing agent and disclosure agent
  - Accepted accounting standards: K-IFRS, IFRS, or US GAAP
- Settlement cycle: **T+2** (standard) [업무규정 Art. 7]

---

## 10. Fees & Revenue Model

### 10.1 Trading Fees

**Exchange fees (as of March 2025):**

| Fee Type | Structure | Rate |
|----------|-----------|------|
| Exchange trading fee (거래수수료) | Ad valorem | 0.0022763% of trade value |
| Clearing fee (결제수수료) | Ad valorem | 0.0013633% of trade value |
| **Total** | | **0.0036396%** (~0.036 bps) |
| Short selling fee | Ad valorem | 0.00329% total |

[Source: Mirae Asset Securities — fee schedule, accessed 2026-04-13]

**New Maker-Taker Fee Structure (December 2025):**

| Type | Rate | Change vs. Old Single Rate (0.0023%) |
|------|------|--------------------------------------|
| Maker | 0.00134% | -41.7% |
| Taker | 0.00182% | -20.9% |

First fee structure change in 20 years; initially a 2-month trial, introduced in response to competition from Nextrade (NXT).

[Source: KED Global, "Korea Exchange cuts fees", 2025-10-02]

### 10.2 Other Fees
- **Listing eligibility review fee:** KRW 5,000,000
- **Initial listing fees (상장수수료):** Graduated by market cap range; detailed schedule in 상장규정 시행세칙 별표 10
- **Annual listing fees (연부과금):** Graduated by market cap range; paid annually while listed
- **Market data fees (시세정보이용료):** Available through KRX Data Marketplace (data.krx.co.kr) with free and paid tiers; detailed schedule via KOSCOM
- **Brokerage commissions (위탁수수료):** Set freely by member firms; must be filed with KRX and publicly disclosed [업무규정 Art. 100]
- **ESG bond fee exemption:** Available through December 31, 2025 [상장규정 시행세칙 별표10-4]
- **Auction commission (경매위탁수수료):** Up to KRW 100M: 0.3%; KRW 100M-500M: 0.2%; above KRW 500M: 0.1% [시행세칙 Art. 141]

[Source: Baker McKenzie — Cross-Border Listings Guide: South Korea]

---

## 11. Recent Developments

### System Upgrades (Last 5 Years)
- **2023 (January):** Exture 3.0 Phase 1 — trading and information distribution systems; 30% latency improvement; extended low-latency to entire market system
- **2023 (October):** Exture 3.0 Phase 2 — clearing and settlement systems; unified UI for on-exchange + OTC; integrated real-time risk calculation
- **2025 (February):** New order types introduced — Mid-Price Order (중간가호가) and Stop Limit Order (스톱지정가호가)
- **2025:** Quote price unit improvement — max 0.5% reduced to 0.25% for stocks and stock futures

### New Products / Segments
- **2024 (September):** Korea Value-up Index launched (100 best-practice companies for corporate governance)
- **2025 (March):** Nextrade (NXT) launched as Korea's first alternative exchange with 12-hour trading (08:00-20:00); captured 30%+ market share by July
- **2025 (April):** KRX contract to supply clearing/settlement system to Thai Stock Exchange
- **Crypto ETFs:** Under consideration

### Regulatory Changes
- **2024 (February):** Corporate Value-up Program announced to address "Korea discount"
- **2025 (March):** Short selling restrictions lifted; all listed stocks available for shorting
- **2025 (December):** Maker-taker fee model introduced (first fee change in 20 years)
- **Self-trade prevention:** Made mandatory for HFT participants

### Strategic Initiatives
- **Extended trading hours:** Plan for 12-hour trading; pre-market 07:00-08:00, after-hours 16:00-20:00; targeting 24-hour trading by December 2027
- **ETF pre/after-market trading:** September 2026 launch for KRX; November for NXT
- **T+1 settlement study:** KRX inspecting North America's T+1 experience (WFE CLEAR 2026 conference, Toronto); concerns about foreign investor time zone challenges
- **KOSPI milestones:** 3,549 (Oct 2025), 4,000 (Oct 2025), 5,000 (Jan 2026), 6,000 (Feb 2026)

[Source: Korea Herald — KRX extended hours; Seoul Economic Daily — T+1 settlement; KED Global — Nextrade, fee cuts, Value-up]

---

## Sources
1. [KRX Global Website](https://global.krx.co.kr) — EXTURE+ Trading System specifications
2. [Wikipedia — Korea Exchange](https://en.wikipedia.org/wiki/Korea_Exchange) — Overview and history
3. [KOSCOM](https://www.koscom.co.kr/eng/main/contents.do?menuNo=300005) — Trading system and market data
4. [Seoul Finance](https://www.seoulfn.com/news/articleView.html?idxno=477662) — Exture 3.0 Phase 1 launch
5. [CEO Score Daily](https://m.ceoscoredaily.com/page/view/2023092616475531974) — Exture 3.0 Phase 2 launch
6. [KED Global](https://www.kedglobal.com) — Fee changes, Nextrade, Value-up Index
7. [Chambers Practice Guides](https://practiceguides.chambers.com/practice-guides/financial-services-regulation-2025/south-korea) — Regulatory framework
8. [Mirae Asset Securities](https://securities.miraeasset.com/imf/200/imf606.do) — Fee schedule
9. [Baker McKenzie — Cross-Border Listings Guide](https://resourcehub.bakermckenzie.com) — Listing fees
10. [Korea Herald](https://www.koreaherald.com/article/10548345) — Extended trading hours
11. [Seoul Economic Daily](https://en.sedaily.com) — T+1 settlement, ETF trading hours
12. 유가증권시장 업무규정 (전문, 2026.01.29) — KRX KOSPI Business Regulations
13. 유가증권시장 업무규정 시행세칙 (전문, 2026.04.01) — Business Regulations Enforcement Rules
14. 유가증권시장 상장규정 (전문, 2025.07.10) — KOSPI Listing Regulations
15. 유가증권시장 상장규정 시행세칙 (전문, 2025.11.11) — Listing Regulations Enforcement Rules
16. 유가증권시장 공시규정 (전문, 2025.08.01) — KOSPI Disclosure Regulations
17. 유가증권시장 공시규정 시행세칙 (전문, 2025.08.01) — Disclosure Regulations Enforcement Rules
