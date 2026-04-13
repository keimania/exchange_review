# Taiwan Stock Exchange (TWSE)

> **Last Updated:** 2026-04-06
> **Research Tier:** Tier 3
> **Domain:** Equities

---

## 1. Overview & Profile

| Item | Details |
|------|---------|
| Official Name | Taiwan Stock Exchange Corporation (TWSE; èºç£è­å¸äº¤ææ) |
| Abbreviation | TWSE |
| Website | https://www.twse.com.tw/en/ |
| Year Established | 1961 (October 23); trading commenced February 9, 1962 |
| Country / City | Taiwan / Taipei (headquartered in Taipei 101) |
| Ownership Structure | Private corporation (not publicly listed). Originally established as a non-profit organization; transformed into a corporation in 1994. Shareholders include government-linked financial institutions and securities firms. At least one-third of board directors and supervisors are appointed by the securities authority (FSC) to represent public interest [unverified â exact shareholder breakdown not publicly disclosed in English sources] |
| Parent Company / Group | N/A â TWSE is an independent corporation, not part of a holding group |
| Regulatory Authority | Financial Supervisory Commission (FSC; éèç£ç£ç®¡çå§å¡æ) |
| Market Capitalization (listed companies) | ~NT$94 trillion (~USD 2.9 trillion) at end of 2025; rose to ~NT$99.6 trillion by early January 2026. Taiwan ranked 7th globally by equity market cap |
| Total Listed Instruments | ~1,045 listed companies (as of mid-2025); plus ETFs, ETNs, TDRs, warrants, and convertible bonds |
| Average Daily Trading Volume | Not separately disclosed in available English sources [unverified] |
| Average Daily Trading Value | Record average daily turnover of NT$416 billion (~USD 13 billion) in 2025; total annual trading value ~NT$100 trillion in 2024 |

### Key Historical Milestones
- **1961:** Taiwan Stock Exchange Corporation established on October 23 as a non-profit organization
- **1962:** Trading commenced on February 9 with 18 listed companies
- **1985:** TAIEX (Taiwan Capitalization Weighted Stock Index) launched as the primary market benchmark
- **1993:** Fully Automated Securities Trading (FAST) system launched in November, replacing floor trading
- **1994:** TWSE transformed from a non-profit organization into a corporation
- **2003:** Foreign investor daily investment limit abolished; FINI/FIDI registration system introduced
- **2014:** Second-generation FAST system rolled out in August â tripled order throughput capacity from 6.5 million to 20 million transactions daily; reduced latency from ~50 ms to <3 ms
- **2015:** Daily price fluctuation limit widened from Â±7% to Â±10% (effective June 1)
- **2019:** Banqiao proximity data center opened in August, offering colocation services
- **2020:** Transition from periodic call auction to continuous trading on March 23; new order types (Market Order, IOC, FOK) introduced simultaneously
- **2020:** Intraday odd-lot trading system launched on October 26
- **2022:** Intraday odd-lot matching interval shortened from 3 minutes to 1 minute (December 19)
- **2024:** Intraday odd-lot matching interval shortened from 1 minute to 5 seconds (December 2)
- **2025:** TAIEX reached historic peak; total market cap surpassed NT$94 trillion; 45 new IPO applications (highest since 2008); all 1,029 listed companies submitted sustainability reports by August 31 deadline
- **2026:** ESG Evaluation system launched, replacing the former Corporate Governance Evaluation

### Key Indices
| Index | Description |
|-------|-------------|
| **TAIEX** (Taiwan Capitalization Weighted Stock Index) | Primary benchmark; market-cap-weighted index of all common shares listed on TWSE. Heavily influenced by TSMC, which accounts for ~30%+ of total index weight |
| TWSE Taiwan 50 Index | Top 50 companies by market cap (basis for the 0050 ETF) |
| TWSE Taiwan Mid-Cap 100 Index | Next 100 companies by market cap |
| Taiwan Semiconductor Index | Sector-specific index for semiconductor companies |

**Semiconductor Concentration:** TSMC (2330.TW) alone contributed an estimated 3,813 points to the TAIEX in 2025. The semiconductor sector dominates the exchange, reflecting Taiwan's central role in the global chip supply chain.

---

## 2. Market Structure

### 2.1 Market Segments
| Segment | Description | Listing Requirements (Summary) |
|---------|-------------|-------------------------------|
| **Main Board (TWSE)** | Primary market for established companies meeting quantitative listing criteria | Profitability requirements, minimum paid-in capital, track record, public float requirements. Companies must meet financial thresholds for revenue, net income, and shareholder equity |
| **Taiwan Innovation Board (TIB)** | Launched for innovative technology companies; lighter listing requirements [unverified â limited English-language detail available] | Targeted at biotech, technology, and innovative companies with relaxed profitability requirements |

**Note:** The Taipei Exchange (TPEx/GTSM) operates separately from TWSE as Taiwan's secondary board for smaller/growth companies, and is not covered in this document. The Emerging Stock Board (ESB) under TPEx serves as a pre-listing market.

### 2.2 Trading Sessions
| Session | Local Time (TST, UTC+8) | UTC | Description |
|---------|--------------------------|-----|-------------|
| Pre-open Order Entry | 08:30 â 09:00 | 00:30 â 01:00 | Orders accepted and queued; no matching occurs |
| Opening Auction | 09:00 | 01:00 | Opening price determined by call auction |
| Continuous Trading | 09:00 â 13:25 | 01:00 â 05:25 | Continuous matching with price-time priority |
| Closing Auction | 13:25 â 13:30 | 05:25 â 05:30 | Closing price determined by call auction |
| After-hours Odd-Lot Trading | 13:40 â 14:30 | 05:40 â 06:30 | Odd-lot orders (< 1,000 shares); matched by call auction |
| After-hours Fixed-Price Trading | 14:00 â 14:30 | 06:00 â 06:30 | Orders submitted at closing price; executed at 14:30 via computer matching |
| Block Trading | 09:00 â 17:00 | 01:00 â 09:00 | Negotiated large-block transactions; tick increment of NT$0.01 |

**Notes:**
- Total regular trading hours: 4.5 hours per day (09:00 â 13:30). This is notably shorter than most major Asian exchanges (JPX: 5.5 hours, HKEX: 5.5 hours, SGX: 7 hours).
- No lunch break â continuous single session from open to close.
- Intraday odd-lot trading also operates from 09:00 â 13:30 during regular hours, with first match at 09:10 and subsequent matches every 5 seconds (as of December 2, 2024).
- Market closed on Saturdays, Sundays, and national holidays.

### 2.3 Tick Sizes
| Price Range (NT$) | Tick Size (NT$) |
|--------------------|-----------------|
| Below 10 | 0.01 |
| 10 to below 50 | 0.05 |
| 50 to below 100 | 0.10 |
| 100 to below 500 | 0.50 |
| 500 to below 1,000 | 1.00 |
| 1,000 and above | 5.00 |

**ETF tick sizes:** NT$0.01 for units priced below NT$50; NT$0.05 for units priced NT$50 and above.

### 2.4 Lot Sizes
- **Standard trading unit:** 1,000 shares (one board lot)
- **Odd-lot trading:** Orders of 1â999 shares; available in both intraday (09:10â13:30, matched every 5 seconds) and after-hours (13:40â14:30) sessions
- **Block trades:** Minimum size requirements apply; settled T+2

### 2.5 Market Maker / Liquidity Provider Programs
- **Stock Market Making Mechanism:** Introduced in June 2021 to enhance trading volume and liquidity for less-liquid stocks
- **ETF Liquidity Provider Program:** Securities firms act as liquidity providers for ETFs to maintain tight spreads [unverified â limited detail on program specifics]

---

## 3. Trading Mechanism

### 3.1 Auction Mechanisms
- **Opening Auction (Call Auction):** At 09:00, all orders accumulated during the pre-open period (08:30â09:00) are matched via a single-price call auction to determine the opening price
- **Closing Auction (Call Auction):** During 13:25â13:30, orders are matched via call auction to determine official closing prices
- **Intraday Odd-Lot Auction:** Odd-lot orders matched every 5 seconds by call auction during regular trading hours (first match at 09:10)

### 3.2 Continuous Trading

**Historical Evolution:**
1. **Pre-2013:** Pure call auction system with 20-second matching intervals
2. **2013â2014:** Call auction interval progressively shortened â from 20 seconds to 15 seconds (July 1, 2013), then 10 seconds (February 24, 2014), then 5 seconds (December 29, 2014)
3. **March 23, 2020:** Full transition to continuous trading for stocks, ETFs, ETNs, and TDRs

**Current Mechanism (post-March 2020):**
- **Order-driven** market with **price-time priority**
- Orders are matched continuously on a real-time basis during the regular session (09:00â13:25)
- Trading price, volume, and best 5 bid/ask prices and volumes are disclosed in real time
- A "5-second snapshot" of market information is also provided for data dissemination purposes

### 3.3 Price Discovery
- Opening and closing prices are determined via call auction, providing a transparent aggregation of supply and demand
- Intraday prices are discovered through continuous matching under price-time priority
- The **intraday price stabilization mechanism** (dynamic circuit breaker) pauses matching for 2 minutes if a potential execution price deviates more than Â±3.5% from the reference price, preventing excessive short-term volatility while allowing orders to accumulate

---

## 4. Order Types

### 4.1 Standard Order Types
| Order Type | Description |
|-----------|-------------|
| Limit Order | Specify maximum buy or minimum sell price; the primary and most common order type |
| Market Order | Executed at the best available price; introduced with continuous trading on March 23, 2020 |

### 4.2 Advanced Order Types
| Order Type | Description |
|-----------|-------------|
| â | Advanced order types such as stop orders, iceberg orders, and pegged orders are not available on TWSE [unverified] |

### 4.3 Time-in-Force Options
| TIF | Description |
|-----|-------------|
| ROD (Rest of Day) | Standard day order; remains active until end of session or execution |
| IOC (Immediate or Cancel) | Execute immediately at best available price; unfilled portion cancelled. Introduced March 23, 2020 |
| FOK (Fill or Kill) | Execute in full immediately or cancel entirely. Introduced March 23, 2020 |

### 4.4 Order Modification / Cancellation
- Limit orders (ROD) may be cancelled or have volume amended during trading sessions
- Price amendments are not permitted; must cancel and re-enter at new price [unverified]
- During the intraday price stabilization pause (2 minutes), order placing, cancelling, and volume amendment of ROD orders are still accepted

---

## 5. Trading System (Technology)

| Item | Details |
|------|---------|
| System Name | FAST (Fully Automated Securities Trading) |
| Vendor / In-house | In-house / proprietary development |
| Architecture | Centralized matching engine |
| Matching Engine | Proprietary; price-time priority continuous matching (post-2020) |
| Round-trip Latency | <3 milliseconds (door-to-door order latency, as of 2nd gen FAST in 2014) |
| Order Processing Capacity | 20 million transactions per day (2nd gen FAST) |
| Messages Per Second | Not publicly disclosed [unverified] |
| Launch Year | 1st gen: 1993; 2nd gen: 2014 |

### System History
| Period | System | Notes |
|--------|--------|-------|
| Pre-1993 | Floor trading / manual | Open-outcry trading system |
| 1993 | FAST 1st Generation | Fully electronic trading introduced; call auction matching |
| 2014 | FAST 2nd Generation | 3x capacity increase (to 20M orders/day); 17x latency reduction (to <3 ms); 2x system efficiency improvement |
| 2020 | FAST with Continuous Trading | Software upgrade to support continuous matching, new order types (Market, IOC, FOK); same hardware platform |

### Technology Stack
- Proprietary trading system developed in-house by TWSE
- FIX protocol support available as alternative to proprietary TMP (Transaction Message Protocol) for broker connectivity
- Market information transmission via dedicated protocols (see TWSE Market Information Transmission Operation Manual)

### Disaster Recovery / Business Continuity
- Banqiao Data Center (opened August 2019) serves as the primary facility; TIA-942 Tier 4 compliant
- 10-story building (7 above ground, 3 underground) in Banqiao District, New Taipei City
- Backup/DR arrangements not publicly detailed in available English sources [unverified]

---

## 6. Market Data

### 6.1 Data Feed Protocols
| Protocol | Description | Use Case |
|----------|-------------|----------|
| TWSE Market Information Transmission | Proprietary protocol | Real-time market data dissemination to information vendors |
| FIX | Available for order routing | Broker connectivity (optional alternative to TMP) |

### 6.2 Data Levels
- **Real-time disclosure:** Trading price, volume, best 5 bid/ask price and volume
- **5-second snapshot:** Periodic aggregated market data snapshot
- **Full depth:** Not publicly described in available sources [unverified]

### 6.3 Distribution Infrastructure
- Licensed information vendors distribute TWSE market data
- Colt is the only foreign licensed market data vendor and Network Service Provider (NSP) in Taiwan
- Pico provides connectivity and local services via CHT Taipei IDC

### 6.4 Historical Data
- TWSE provides historical trading data through its website (daily trading value/volume by individual security)
- TWSE Fact Book published annually with comprehensive market statistics

---

## 7. Connectivity & Access

### 7.1 Membership / Participation
- Trading conducted through licensed securities firms (brokers)
- As of 2025, there are multiple securities firms with TWSE trading access
- Foreign investors must register as FINI (Foreign Institutional Investor) or FIDI (Foreign Individual Investor) with TWSE before investing

### 7.2 Connection Methods
| Method | Description |
|--------|-------------|
| TMP (Transaction Message Protocol) | TWSE proprietary order routing protocol; primary connection method for brokers |
| FIX Protocol | Alternative connection method for order routing |
| Dedicated leased lines | For securities firms connecting to TWSE systems |

### 7.3 Co-location / Proximity Services
- **Location:** Banqiao Data Center, Banqiao District, New Taipei City
- **Offerings:** Rack space, hardware hosting, and low-latency connectivity within 100 meters of TWSE/TAIFEX matching engines
- **Providers:** Colt (rack space, hosting, connectivity, market data); Pico (connectivity, Intellihands service)
- Colocation services available for TWSE, TAIFEX (futures), and TPEx from the same facility

### 7.4 API Protocols
| Protocol | Use Case |
|----------|----------|
| FIX | Order routing (alternative to TMP) |
| TMP (proprietary) | Primary order routing |
| REST/WebSocket | Not publicly documented [unverified] |

### 7.5 Certification / Testing
- Brokers must complete certification testing before accessing TWSE systems [unverified â specific testing requirements not detailed in available English sources]

---

## 8. Risk Controls & Circuit Breakers

### 8.1 Price Limits
| Type | Threshold | Action |
|------|-----------|--------|
| **Daily price limit** | Â±10% of previous closing price | Orders beyond the limit are rejected; price cannot exceed the upper/lower limit for the day |
| **Bonds** | Â±5% of reference price | Same mechanism as stocks but narrower band |

**Note:** The daily price limit was widened from Â±7% to Â±10% on June 1, 2015. Applies to stocks, ETFs, ETNs, TDRs, convertible bonds, and beneficiary certificates.

### 8.2 Circuit Breakers
| Type | Trigger | Action |
|------|---------|--------|
| **Intraday Price Stabilization Mechanism** | Potential execution price deviates Â±3.5% from the last traded price (reference price) | Matching is postponed for 2 minutes; during the pause, order entry, cancellation, and volume amendment of ROD orders continue; after 2 minutes, trading resumes via call auction |

**Note:** Taiwan does not employ a market-wide index-based circuit breaker mechanism like the U.S. or China. Instead, it relies on individual-security-level intraday price stabilization combined with daily price limits.

### 8.3 Pre-trade Risk Controls
- **Daily price limit enforcement:** Orders priced beyond the Â±10% band are automatically rejected
- **Margin maintenance ratio:** Set at 130% for margin trading accounts (adjusted May 2015)
- **Short selling volume limit:** Daily short selling of borrowed securities cannot exceed 30% of average daily trading volume over the previous 30 sessions (temporarily reduced to 3% during periods of extreme volatility, e.g., April 2025)
- **Fat-finger checks:** Specific mechanisms not publicly detailed [unverified]
- **Order size limits:** Block trade minimum thresholds apply [unverified â specific limits not found in English sources]

### 8.4 Kill Switch
- Not publicly documented in available English sources [unverified]

---

## 9. Regulatory Framework

### 9.1 Supervising Authority
- **Financial Supervisory Commission (FSC)** â the primary regulator of Taiwan's securities, banking, and insurance markets. The Securities and Futures Bureau (SFB) under the FSC directly supervises securities market activities
- **TWSE** also performs self-regulatory functions, including market surveillance, listing review, and enforcement of trading rules

### 9.2 Key Regulations
| Regulation | Description |
|------------|-------------|
| **Securities and Exchange Act (è­å¸äº¤ææ³)** | The principal legislation governing securities issuance, trading, and market participants in Taiwan |
| **Securities and Exchange Act Enforcement Rules** | Detailed implementation rules under the main act |
| **TWSE Operating Rules** | Exchange-specific rules governing trading, listing, disclosure, and member conduct |
| **Regulations Governing Investment in Securities by Overseas Chinese and Foreign Nationals** | Governs FINI/FIDI registration, investment scope, and reporting obligations |
| **Regulations Governing Securities Firms** | Licensing, capital requirements, and operational rules for broker-dealers |
| **Regulations Governing Margin Trading** | Rules for margin purchases and short sales by securities firms and investors |

### 9.3 Market Surveillance
- TWSE operates a market surveillance system under the "Taiwan Stock Exchange Corporation Rules Governing Implementation of the Stock Market Surveillance System"
- Monitors for insider trading, market manipulation, and abnormal trading patterns
- Surveillance Operations Oversight Committee can resolve to suspend margin purchases and short sales for specific securities showing abnormal activity
- Cooperation with SFB/FSC for enforcement actions

### 9.4 Reporting Requirements
- Listed companies must file periodic financial reports (quarterly, semi-annual, annual)
- Material information must be disclosed immediately via the Market Observation Post System (MOPS)
- All 1,029 TWSE-listed companies required to submit annual sustainability reports (as of 2025)
- Foreign investors (FINI/FIDI) must report holdings and transactions per FSC regulations

### 9.5 Foreign Investor Rules (FINI / FIDI)
| Item | Details |
|------|---------|
| **Registration** | Foreign institutional investors (FINIs) and foreign individual investors (FIDIs) must register with TWSE and obtain a Foreign Investor Investment ID (FID) before investing |
| **Custodian requirement** | FINIs must appoint a qualified custodian in Taiwan to hold securities and cash proceeds |
| **Ownership limits** | Generally no individual or aggregate foreign ownership limits (removed in 2003), except for certain sectors (e.g., telecom, media) that retain statutory caps |
| **Investment scope** | TWSE-listed stocks, bonds, ETFs, warrants, and other FSC-approved securities |
| **Repatriation** | No restrictions on repatriation of capital or profits |
| **Foreign ownership share** | Foreign investors held 45.41% of total TWSE market capitalization by end of 2024, with market value exceeding NT$33 trillion |
| **Recent development** | Since August 2023, FINIs may use Taiwan-listed stocks as collateral for offshore investment activities |

### 9.6 Cross-border Arrangements
- Taiwan participates in international regulatory cooperation through FSC bilateral MOUs with other jurisdictions
- Stock Connect or mutual market access mechanisms with mainland China do not exist due to political considerations [unverified]
- TWSE actively promotes international index inclusion (e.g., FTSE TWSE Taiwan Index Series, MSCI Taiwan Index)

---

## 10. Fees & Revenue Model

### 10.1 Trading Fees
| Fee Type | Structure | Rate |
|----------|-----------|------|
| Brokerage commission | Charged by securities firms; ceiling set by FSC | Maximum 0.1425% of trading value (buy and sell); most firms offer discounts |
| Securities transaction tax | Government tax on seller | 0.30% of transaction value for stocks; 0.10% for ETF beneficiary certificates, warrants, and TDRs |
| TWSE trading fee | Charged to securities firms | Specific schedule per TWSE fee criteria [unverified â exact rates not found in English sources] |

### 10.2 Other Fees
- **Listing fees:** Initial listing fees and annual listing maintenance fees apply (schedule published by TWSE)
- **Market data fees:** Charged to information vendors for real-time market data redistribution
- **Co-location fees:** Charged for rack space and connectivity at Banqiao Data Center

---

## 11. Recent Developments

### System Upgrades (Last 5 Years)
- **2020:** Continuous trading launched (March 23); intraday odd-lot trading launched (October 26)
- **2022:** Odd-lot matching interval shortened from 3 minutes to 1 minute (December 19)
- **2024:** Odd-lot matching interval shortened from 1 minute to 5 seconds (December 2)

### New Products / Segments
- Expansion of ETF and ETN offerings
- Taiwan Innovation Board for innovative technology companies [unverified â launch details limited]
- Intraday odd-lot trading broadened retail investor access

### Regulatory Changes
- **2025:** FSC temporarily tightened short selling limits (30% to 3% daily cap) during April 2025 market volatility
- **2025:** All listed companies required to submit sustainability reports
- **2026:** ESG Evaluation system replaces Corporate Governance Evaluation with 75 indicators across E, S, and G dimensions
- **2026:** Independent directors limited to no more than three consecutive terms under new evaluation criteria

### Strategic Initiatives
- **ESG / Sustainability:** Integration of SASB metrics into ESG Genplus platform; mandatory sustainability reporting for all listed companies
- **Internationalization:** Promotion of FTSE TWSE index series; efforts to attract international capital through improved ESG disclosure and governance standards
- **Retail Investor Access:** Progressive shortening of odd-lot matching intervals (20s -> 15s -> 10s -> 5s -> 1min -> 5s) to lower investment thresholds
- **Market Maker Programs:** Stock market making mechanism (2021) and ETF liquidity provider programs to improve market depth

---

## KRX Comparison Notes

| Item | TWSE | KRX (KOSPI) |
|------|------|-------------|
| Trading hours | 09:00-13:30 (4.5 hrs) | 09:00-15:30 (6.5 hrs) |
| Trading mechanism | Continuous (since 2020) | Continuous with opening/closing auctions |
| Daily price limit | Â±10% | Â±30% |
| Standard lot | 1,000 shares | 1 share |
| Intraday volatility control | Â±3.5% dynamic price stabilization (2-min pause) | VI (Volatility Interruption): static Â±10% / dynamic Â±3-6% (2-min auction) |
| Transaction tax (seller) | 0.30% | 0.18% (effective 2026 planned) [unverified] |
| Market cap (2025) | ~USD 2.9 trillion | ~USD 1.6 trillion |
| Semiconductor concentration | Very high (~30%+ TSMC alone) | Moderate (~20%+ Samsung Electronics) |

---

## Sources

1. [TWSE Official Website â Trading Mechanism Introduction](https://www.twse.com.tw/en/products/system/trading.html)
2. [TWSE â 2025 Guide to Investing in Taiwan](https://www.twse.com.tw/en/about/company/guide.html)
3. [TWSE â Continuous Trading](https://www.twse.com.tw/en/page/products/trading/information13.html)
4. [TWSE â Timeline / History](https://www.twse.com.tw/en/about/company/history.html)
5. [TWSE â Co-Location Service](https://www.twse.com.tw/en/products/colo/colo.html)
6. [TWSE â Foreign Investment](https://www.twse.com.tw/en/products/education/foreign/other/free.html)
7. [TWSE Market Insights â 2025 Thrived Amid Challenges, 2026 Poised for Greater Heights](https://www.twse.com.tw/market_insights/en/detail/8a8216d69bde495d019c033cfb3400a7)
8. [TWSE Market Insights â Setting Sail from 2024 Milestones](https://www.twse.com.tw/market_insights/en/detail/8a8216d69517ec0c019527a7005a0062)
9. [Focus Taiwan â Taiwan stock market sets six records in 2025](https://focustaiwan.tw/business/202601080012)
10. [Taiwan Stock Exchange â Wikipedia](https://en.wikipedia.org/wiki/Taiwan_Stock_Exchange)
11. [Finextra â Taiwan Stock Exchange rolls out trading system (2014)](https://www.finextra.com/pressarticle/56470/taiwan-stock-exchange-rolls-out-trading-system)
12. [The TRADE â Taiwan Stock Exchange to launch new trading system](https://www.thetradenews.com/taiwan-stock-exchange-to-launch-new-trading-system-by-end-2012/)
13. [Lee, Tsai & Partners â From Call Auction to Continuous Trading (Taiwan)](https://www.leetsai.com/ltp-special-column/from-call-auction-to-continuous-trading-taiwan)
14. [Traders Magazine â A Closer Look at Trading Curbs in Asia Markets](https://www.tradersmagazine.com/featured_articles/a-closer-look-at-trading-curbs-in-asia-markets/)
15. [Colt â Full hosting capability for three Taiwan exchanges](https://www.colt.net/resources/insights/colt-provides-full-hosting-capability-to-three-taiwan-exchanges-in-response-to-the-growing-demand-for-twse-implementing-continuous-trading)
16. [Chambers & Partners â Investing In Taiwan 2026](https://practiceguides.chambers.com/practice-guides/investing-in-2026/taiwan/trends-and-developments)
17. [Law.asia â Short selling and securities lending in Taiwan](https://law.asia/short-selling-securities-lending-taiwan-fini-regulations-market/)
18. [Securities and Exchange Act â Laws & Regulations Database of Taiwan](https://law.moj.gov.tw/ENG/LawClass/LawAll.aspx?pcode=G0400001)
19. [SFB/FSC â Number of TWSE Listed Companies](https://www.sfb.gov.tw/en/home.jsp?id=272&parentpath=0,7,92)
20. [SFB/FSC â Intraday Odd Lot Matching Interval Shortened (Dec 2024)](https://www.sfb.gov.tw/en/home.jsp?id=78&parentpath=0&mcustomize=multimessage_view.jsp&dataserno=202407300001&dtable=News)
21. [TWSE Intraday Odd-Lot Trading â Market Insights](https://www.twse.com.tw/market_insights/en/detail/8a8216d6933460a401936c8d0e8401a8)
22. [Interactive Brokers â Taiwan Stock Exchange Fees](https://www.interactivebrokers.com/en/accounts/fees/TAIWAN-StkFees.php)
23. [DataCenterDynamics â Taiwan Stock Exchange opens modern data center](https://www.datacenterdynamics.com/en/news/taiwan-stock-exchange-opens-modern-data-center/)
24. [TWSE CGC â ESG Evaluation 2026](https://cgc.twse.com.tw/pressReleases/promoteNewsArticleEn/4549)
25. [Baker McKenzie â Taiwan Regulatory Sources](https://resourcehub.bakermckenzie.com/en/resources/global-financial-services-regulatory-guide/asia-pacific/taiwan/topics/what-are-the-main-sources-of-regulatory-laws-in-your-jurisdiction)
