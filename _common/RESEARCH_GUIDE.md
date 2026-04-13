# Global Exchange Research Guide

This document defines the scope, methodology, and standards for researching global exchanges across three domains: Equities Markets, Derivatives Markets, and Clearing & Settlement.

---

## 1. Research Scope

### 1.1 Target Exchanges

#### Equities Markets (01_equities)
| Region | Exchanges |
|--------|-----------|
| North America | NYSE, NASDAQ, TMX (Toronto Stock Exchange) |
| Europe | London Stock Exchange (LSE), Euronext, Deutsche Borse (Xetra), SIX Swiss Exchange, Borsa Italiana, BME (Bolsas y Mercados Espanoles), Nasdaq Nordic |
| Asia-Pacific | Japan Exchange Group (JPX/TSE), Hong Kong Exchanges (HKEX), Singapore Exchange (SGX), Australian Securities Exchange (ASX), Shanghai Stock Exchange (SSE), Shenzhen Stock Exchange (SZSE), Bombay Stock Exchange (BSE), National Stock Exchange of India (NSE), Taiwan Stock Exchange (TWSE), Bursa Malaysia |
| Middle East & Africa | Saudi Exchange (Tadawul), Johannesburg Stock Exchange (JSE) |

#### Derivatives Markets (02_derivatives)
| Region | Exchanges |
|--------|-----------|
| North America | CME Group (CME/CBOT/NYMEX/COMEX), Cboe Global Markets, ICE Futures U.S., Montreal Exchange (MX) |
| Europe | Eurex, ICE Futures Europe, Euronext Derivatives, Nasdaq Nordic Derivatives |
| Asia-Pacific | Osaka Exchange (JPX), HKEX Derivatives, SGX Derivatives, ASX Derivatives, China Financial Futures Exchange (CFFEX), Dalian Commodity Exchange (DCE), Shanghai Futures Exchange (SHFE), National Stock Exchange of India (NSE F&O), Taiwan Futures Exchange (TAIFEX) |
| Middle East & Africa | Dubai Mercantile Exchange (DME) |

#### Clearing & Settlement (03_clearing)
| Region | Organizations |
|--------|---------------|
| North America | DTCC (DTC/NSCC/FICC), Options Clearing Corporation (OCC), CME Clearing, ICE Clear U.S., Canadian Depository for Securities (CDS) |
| Europe | LCH (LCH Ltd / LCH SA), Eurex Clearing, EuroCCP, SIX x-clear, Euroclear, Clearstream |
| Asia-Pacific | Japan Securities Clearing Corporation (JSCC), HKSCC / HKCC / SEOCH, Central Depository Pte (CDP, Singapore), ASX Clear / ASX Settlement, China Securities Depository and Clearing (CSDC), Clearing Corporation of India (CCIL) |
| Middle East | Muqassa (Saudi Exchange CCP) |

### 1.2 Research Priority
- **Tier 1 (Deep dive):** NYSE, NASDAQ, CME, Eurex, LSE, JPX, HKEX, SGX, DTCC, LCH, OCC
- **Tier 2 (Standard):** Euronext, Deutsche Borse, ASX, ICE, Cboe, JSCC, Eurex Clearing
- **Tier 3 (Overview):** Remaining exchanges

---

## 2. Research Items per Exchange

Every exchange/organization file MUST cover the following sections. Use the templates in `TEMPLATE_EXCHANGE.md` or `TEMPLATE_SYSTEM.md`.

### 2.1 For Equities & Derivatives Exchanges

1. **Overview & Profile**
   - Official name, abbreviation, website
   - Year established, key historical milestones
   - Ownership structure (public/private, parent company, mergers)
   - Regulatory authority / governing body
   - Market capitalization (for equities) or notional volume (for derivatives)
   - Number of listed instruments

2. **Market Structure**
   - Market segments and tiers (e.g., Main Board, Growth Board)
   - Trading sessions and hours (pre-market, continuous, closing auction, after-hours)
   - Tick sizes / price increments
   - Lot sizes and minimum order sizes
   - Market maker / liquidity provider programs

3. **Trading Mechanism**
   - Auction types (opening, closing, intraday, volatility)
   - Continuous trading (order-driven vs quote-driven vs hybrid)
   - Price discovery process
   - Order priority rules (price-time, price-size-time, pro-rata)

4. **Order Types**
   - Standard order types (market, limit, stop, stop-limit)
   - Advanced/special order types (iceberg, pegged, midpoint, etc.)
   - Order validity / time-in-force options (DAY, GTC, IOC, FOK, GTD)
   - Order modification and cancellation rules

5. **Trading System (Technology)**
   - System name and vendor/in-house
   - Architecture overview (matching engine design)
   - Latency (round-trip, order-to-acknowledgment)
   - Throughput / capacity (messages per second, orders per second)
   - System history (past platforms, migration timeline)
   - Technology stack (if publicly known)
   - Disaster recovery / business continuity

6. **Market Data**
   - Real-time data feed protocols (ITCH, OUCH, FIX, FAST, proprietary)
   - Levels of data (L1, L2, full depth)
   - Market data distribution infrastructure
   - Historical data availability

7. **Connectivity & Access**
   - Member/participant access requirements
   - Connection methods (dedicated line, VPN, internet)
   - Co-location / proximity hosting services
   - API protocols (FIX, binary, REST/WebSocket for retail)
   - Certification / conformance testing process

8. **Risk Controls & Circuit Breakers**
   - Price limits (static/dynamic)
   - Circuit breaker mechanism and thresholds
   - Fat-finger / erroneous trade prevention
   - Pre-trade risk checks
   - Kill switch capabilities

9. **Regulatory Framework**
   - Supervising authority
   - Key regulations and rules
   - Market surveillance approach
   - Reporting requirements
   - Cross-border regulatory arrangements

10. **Fees & Revenue Model**
    - Trading fees structure (maker-taker, flat, tiered)
    - Listing fees
    - Market data fees
    - Connectivity / co-location fees

11. **Recent Developments**
    - System upgrades or migrations (last 5 years)
    - New products or market segments
    - Regulatory changes
    - Strategic initiatives (ESG, digital assets, cloud migration, etc.)

### 2.2 For Clearing & Settlement Organizations

1. **Overview & Profile** (same as above, adapted for CCPs/CSDs)
2. **Clearing Model**
   - CCP vs bilateral clearing
   - Novation process
   - Products cleared (equities, derivatives, fixed income, OTC)
   - Clearing membership tiers and requirements
3. **Risk Management**
   - Margin methodology (SPAN, PRISMA, VaR-based, etc.)
   - Initial margin and variation margin
   - Default waterfall structure
   - Default fund / guarantee fund
   - Stress testing and back-testing
   - Recovery and resolution planning
4. **Settlement**
   - Settlement cycle (T+1, T+2, etc.)
   - DVP (Delivery versus Payment) model
   - CSD linkages
   - Settlement finality
   - Securities lending / borrowing facility
5. **Technology & Infrastructure**
   - System name and architecture
   - Processing capacity
   - STP (Straight-Through Processing) rate
   - Interface protocols (SWIFT, ISO 20022, proprietary)
6. **Regulatory Framework** (same as above)
7. **Interoperability** - Links with other CCPs/CSDs
8. **Recent Developments** (same as above)

---

## 3. Research Standards

### 3.1 Source Priority
1. **Primary:** Official exchange websites, technical specifications, rulebooks, annual reports
2. **Secondary:** WFE statistics, IOSCO reports, BIS/CPMI publications, FIA surveys
3. **Tertiary:** Industry publications (e.g., Waters Technology, The TRADE), academic papers

### 3.2 Citation Format
All factual claims must include a source citation:
```
[Source: NYSE Official Website, "Market Model", accessed 2026-04-03]
[Source: WFE Annual Statistics Guide 2025]
[Source: BIS CPMI Red Book, 2024 edition]
```

### 3.3 Data Recency
- Prefer data from the most recent full year available
- For statistics, note the reference year/date
- Mark any data older than 3 years as `[data as of YYYY]`

### 3.4 Uncertainty Handling
- If information cannot be verified from primary sources: mark as `[unverified]`
- If information is estimated or approximate: mark as `[estimated]`
- If information is unavailable: explicitly state "Information not publicly available" rather than omitting

### 3.5 File Naming Convention
- Lowercase with underscores: `nyse.md`, `cme_group.md`, `lch_ltd.md`
- No spaces, no special characters
- Use commonly recognized abbreviations

---

## 4. Glossary Management

- All new technical terms encountered during research must be added to `glossary_en.md`
- Terms should be categorized (Trading, Clearing, Settlement, Technology, Regulation)
- Korean translations are maintained separately in `glossary_ko.md`
- When a term has a KRX equivalent concept, note it in the Korean glossary

---

## 5. Quality Checklist

Before finalizing any exchange file, verify:
- [ ] All 11 sections (or 8 for clearing) are addressed
- [ ] Sources cited for key facts
- [ ] New terms added to glossary
- [ ] Consistent formatting with template
- [ ] No placeholder text remaining
- [ ] File name follows convention
