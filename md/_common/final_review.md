# Final Review: Global Exchange Research — Cross-Domain Analysis & KRX Benchmarking

> **Date:** 2026-04-13
> **Scope:** 23 equity exchanges, 17 derivatives exchanges, 20 clearing/settlement organizations
> **Total Documents:** 90+ English research files across 3 domains

---

## Table of Contents

1. [Cross-Domain Comparative Analysis](#1-cross-domain-comparative-analysis)
2. [KRX Benchmarking](#2-krx-benchmarking)
3. [Quality Check](#3-quality-check)

---

## 1. Cross-Domain Comparative Analysis

### 1.1 Master Comparison — Exchange Infrastructure Ecosystem

The global exchange ecosystem operates as an interconnected chain: **Trading (Exchange) → Clearing (CCP) → Settlement (CSD)**. The following table maps these relationships across all researched jurisdictions.

#### North America

| Exchange (Trading) | Trading System | CCP (Clearing) | Margin Method | CSD (Settlement) | Cycle |
|---|---|---|---|---|---|
| NYSE | Pillar (ICE, in-house) | NSCC (DTCC) | VaR-based | DTC (DTCC) | T+1 |
| NASDAQ | Eqlipse/INET (in-house) | NSCC (DTCC) | VaR-based | DTC (DTCC) | T+1 |
| CME/CBOT/NYMEX/COMEX | Globex (in-house) | CME Clearing | SPAN → SPAN 2 (HVaR) | CME settlement | T+0/T+1 |
| Cboe | Titanium (in-house) | OCC | STANS (Monte Carlo) | DTC (DTCC) | T+1 |
| ICE Futures | ICE Platform (in-house) | ICE Clear US/Europe/Credit | IRM 2 (FHS VaR) | — | T+0/T+1 |
| TMX (TSX) | Quantum XA (in-house) | CDS Canada | Collateral-based | CDS (CDSX) | T+1 |
| Montreal Exchange | SOLA (in-house) | CDCC | SPAN | CDS (CDSX) | T+1 |

#### Europe

| Exchange (Trading) | Trading System | CCP (Clearing) | Margin Method | CSD (Settlement) | Cycle |
|---|---|---|---|---|---|
| LSE | Millennium (LSEG/MillenniumIT) | LCH Ltd | PAIRS (ES-based) | Euroclear UK & Ireland | T+2 |
| Euronext (7 countries) | Optiq (in-house) | Euronext Clearing (ex-LCH SA) | VaR-based | Euroclear | T+2 |
| Deutsche Borse / Xetra | T7 (in-house) | Eurex Clearing | PRISMA (FHS) | Clearstream | T+2 |
| Eurex (derivatives) | T7 (in-house) | Eurex Clearing | PRISMA (FHS) | Clearstream | T+2 |
| SIX Swiss | SWXess/X-stream (Nasdaq) | SIX x-clear | Monte Carlo VaR | SIX SIS | T+2 |
| Borsa Italiana | Optiq (Euronext) | LCH Ltd → Euronext Clearing | VaR-based | Monte Titoli / Euroclear | T+2 |
| BME (Spain) | SIBE-Smart (in-house) | BME Clearing | VaR-based | Iberclear | T+2 |
| Nasdaq Nordic | Genium INET (Nasdaq) | Eurex Clearing | PRISMA | Euroclear Finland/Sweden | T+2 |

#### Asia-Pacific

| Exchange (Trading) | Trading System | CCP (Clearing) | Margin Method | CSD (Settlement) | Cycle |
|---|---|---|---|---|---|
| JPX / TSE | arrowhead 4.0 (Fujitsu co-dev) | JSCC | VaR (99%) | JASDEC | T+2 |
| Osaka Exchange (JPX deriv) | J-GATE 3.0 (Genium INET) | JSCC | VaR (migrated from SPAN) | JASDEC | T+2 |
| HKEX (equities) | OTP-C / Orion (in-house) | HKSCC | Cover 2 | HKSCC (integrated) | T+2 |
| HKEX (derivatives) | HKATS (Genium INET) | HKCC / SEOCH | PRiME (VaR) | HKSCC | T+1 |
| SGX (equities) | REACH (Nasdaq) | CDP | Risk-based (99%+) | CDP (integrated) | T+2 |
| SGX (derivatives) | Titan DT (Genium INET) | SGX-DC | IRM (SPAN-like) | SGX-DC | T+0 |
| ASX (equities) | ASX Trade (Genium INET) | ASX Clear | VaR-based | ASX Settlement (CHESS) | T+1 |
| ASX (derivatives) | ASX 24 NTP (Nasdaq) | ASX Clear (Futures) | SPAN-based | ASX Settlement | T+1 |
| SSE (Shanghai) | 4th-gen (in-house) | ChinaClear | Fixed-percentage | CSDC | T+1 |
| SZSE (Shenzhen) | Self-developed (in-house) | ChinaClear | Fixed-percentage | CSDC | T+1 |
| NSE India (equities) | NEAT+ (in-house) | NSCCL | SPAN | NSDL / CDSL | T+1 |
| NSE India (F&O) | NEAT+ (in-house) | NSE Clearing (NCL) | SPAN (100% peak) | NSDL / CDSL | T+1 |
| BSE India | BOLT Plus (T7 licensed) | ICCL | VaR-based | CDSL | T+1 |
| TWSE | FAST 2nd-gen (in-house) | Taiwan CCDC | VaR-based | TDCC | T+2 |
| TAIFEX | 6th-gen (in-house) | TAIFEX Clearing | Scenario-based | TDCC | T+0/T+1 |
| Bursa Malaysia | BTS2/X-stream (Nasdaq) | Bursa Malaysia Clearing | Risk-based | Bursa Malaysia Depository | T+2 |
| **KRX (equities)** | **Exture 3.0 (in-house)** | **KRX Clearing** | **KRX-SPAN (scenario-based)** | **KSD** | **T+2** |
| **KRX (derivatives)** | **Exture 3.0 (in-house)** | **KRX Clearing** | **KRX-SPAN (scenario-based)** | **KSD** | **T+0/T+1** |

#### Middle East & Africa

| Exchange (Trading) | Trading System | CCP (Clearing) | Margin Method | CSD (Settlement) | Cycle |
|---|---|---|---|---|---|
| Tadawul (Saudi) | X-stream INET (Nasdaq) | Muqassa | Portfolio-based | Edaa | T+2 |
| JSE (South Africa) | Millennium (LSEG) | JSE Clear | VaR-based | Strate | T+3 |
| DME (Dubai) | CME Globex (hosted) | CME Clearing | SPAN / SPAN 2 | — | T+0/T+1 |

---

### 1.2 Common Technology Vendors Across Exchanges

The global exchange technology market is dominated by a small number of platform providers:

#### Nasdaq Technology (INET / Genium INET / X-stream INET)

The most widely deployed exchange technology globally, powering **10+ exchanges**:

| Platform Variant | Exchanges | Domain |
|---|---|---|
| INET / Eqlipse (4th gen) | NASDAQ | Equities |
| Genium INET | ASX, Nasdaq Nordic, SGX (REACH), Bursa Malaysia, SIX Swiss | Equities |
| Genium INET (derivatives) | HKEX Derivatives (HKATS), SGX Derivatives (Titan DT), Osaka Exchange (J-GATE) | Derivatives |
| X-stream INET | Tadawul, Bursa Malaysia (BTS2) | Equities |

**Key characteristics:** OUCH/ITCH/FIX protocols; modular architecture; sub-100 microsecond latency; configurable matching algorithms.

#### LSEG / MillenniumIT (Millennium Exchange)

| Exchanges | Domain |
|---|---|
| LSE | Equities |
| JSE (South Africa) | Equities |
| Borsa Italiana (migrated to Optiq 2023-24) | Equities (former) |
| 40+ other exchanges globally | Various |

**Key characteristics:** C++/Linux; ~126 microsecond latency; widely deployed in emerging markets.

#### Deutsche Borse (T7 Platform)

| Exchanges | Domain |
|---|---|
| Deutsche Borse / Xetra | Equities |
| Eurex | Derivatives |
| BSE India (BOLT Plus, T7 licensed) | Equities |

**Key characteristics:** ~5 microsecond median latency (fastest major platform); partition-based architecture; shared equities/derivatives platform; C/C++/Linux.

#### In-House Proprietary Systems

| Exchange | System | Notable Feature |
|---|---|---|
| NYSE | Pillar | Unified 7 venues; 34 microsecond binary |
| CME Group | Globex | Google Cloud migration 2026-2028 |
| Euronext | Optiq | Unified 7 countries; ~15 microsecond; Kafka persistence |
| HKEX (equities) | OTP-C / Orion | SDNet/3 network |
| SSE, SZSE | Self-developed | Technology independence policy |
| NSE India | NEAT+ | Nanosecond upgrade planned Apr 2026 |
| TMX | Quantum XA | — |
| TWSE | FAST 2nd-gen | <3 ms |
| BME | SIBE-Smart | — |
| ICE | ICE Platform | Sub-millisecond |
| Cboe | Titanium | Sub-100 microsecond |
| KRX | Exture 3.0 | Unified equities + derivatives; ~49 us est.; Phase 1 Jan 2023 |

#### Technology Vendor Summary

| Vendor | Equities | Derivatives | Clearing Systems | Total Footprint |
|---|---|---|---|---|
| **Nasdaq Tech** | 7 exchanges | 4 exchanges | — | 11+ exchanges |
| **LSEG/MillenniumIT** | 2+ exchanges | — | — | 40+ globally |
| **Deutsche Borse T7** | 2 exchanges (incl. BSE license) | 1 exchange | Eurex C7 | 3+ |
| **In-House** | 11 exchanges | 10 exchanges | All CCPs | Majority |

**Key insight:** While Nasdaq technology has the broadest global deployment, the largest exchanges (NYSE, CME, Euronext, HKEX equities, Chinese exchanges) use in-house systems. The trend is toward in-house development for Tier 1 exchanges and licensed technology for Tier 2/3.

---

### 1.3 Clearing Relationship Map — Which CCP Clears for Which Exchange

#### Global CCP-Exchange Relationships

```
DTCC (NSCC/DTC/FICC)
  ├── NYSE
  ├── NASDAQ
  ├── Cboe (equities)
  └── All U.S. equity venues + U.S. Treasuries

CME Clearing
  ├── CME / CBOT / NYMEX / COMEX
  ├── DME (Dubai Mercantile Exchange)
  └── Cross-margin with FICC (Treasuries)

OCC (Options Clearing Corporation)
  ├── All U.S. equity options exchanges (Cboe, NYSE Arca, NASDAQ, ISE, etc.)
  └── Cross-margin with NSCC/FICC/DTC

LCH Ltd (UK)
  ├── LSE (EquityClear)
  ├── Global OTC IRS (SwapClear — $779T H1 2024)
  ├── RepoClear
  └── Interoperability: SIX x-clear, Cboe Clear Europe

Euronext Clearing (ex-LCH SA, migrated Sept 2024)
  ├── Euronext (Paris, Amsterdam, Brussels, Lisbon, Dublin, Oslo, Milan)
  └── Borsa Italiana (migrating)

Eurex Clearing
  ├── Eurex (derivatives)
  ├── Xetra / Deutsche Borse (equities)
  ├── Nasdaq Nordic
  └── OTC IRS clearing

JSCC (Japan)
  ├── TSE / JPX (equities)
  ├── Osaka Exchange (derivatives)
  └── OTC IRS (TONA), CDS

HKEX Clearing (HKSCC / HKCC / SEOCH)
  ├── HKEX (equities via HKSCC)
  ├── HKEX (futures via HKCC)
  ├── HKEX (stock options via SEOCH)
  └── Stock Connect (cross-border with ChinaClear)

SGX-DC / CDP
  ├── SGX (equities via CDP)
  ├── SGX (derivatives via SGX-DC)
  └── GIFT Connect with NSE India

ICE Clear (US / Europe / Credit)
  ├── ICE Futures U.S.
  ├── ICE Futures Europe
  └── ICE Clear Credit (CDS — $2T+ OI)

ASX Clear / ASX Clear (Futures)
  ├── ASX (equities)
  └── ASX 24 (derivatives)

ChinaClear (CSDC)
  ├── SSE (Shanghai)
  ├── SZSE (Shenzhen)
  └── Stock Connect (cross-border with HKSCC)

NSE Clearing (NCL) / ICCL
  ├── NSE India (equities + F&O)
  └── BSE India (via ICCL)

KRX Clearing (Korea)
  ├── KRX (equities — KOSPI, KOSDAQ)
  ├── KRX (derivatives — KOSPI 200, KTB, FX, commodity)
  └── OTC IRS/CRS clearing (mandated)

KSD (Korea Securities Depository)
  ├── KRX (all exchange-traded equities, bonds, ETFs)
  ├── Government bond settlement (BOK central bank money)
  └── Cross-border links: Euroclear, Clearstream, DTC
```

#### Cross-Border Clearing Arrangements

| Arrangement | Type | Participants | Status |
|---|---|---|---|
| Stock Connect | Cross-border equity access | HKSCC ↔ ChinaClear | Operational (2014-) |
| GIFT Connect | Cross-border derivatives | SGX-DC ↔ NSE India | Operational (2023-) |
| Swap Connect | Cross-border IRS | OTC Clear (HK) ↔ CFETS | Northbound operational (2023-) |
| CME-FICC Cross-Margin | Cross-CCP margin offset | CME Clearing ↔ FICC | Operational (2024-) |
| CCP Interoperability | Multi-CCP clearing | LCH Ltd ↔ SIX x-clear ↔ Cboe Clear Europe | Operational |
| CME-OCC Cross-Margin | Portfolio margin offset | CME Clearing ↔ OCC | Operational |
| JSCC-CFTC | Regulatory recognition | JSCC ↔ U.S. persons | JPY-IRS client clearing (2025-) |

---

### 1.4 Global Settlement Cycle Transition Status

| Settlement Cycle | Jurisdictions | Date Achieved/Target |
|---|---|---|
| **T+1 (achieved)** | USA, Canada | May 2024 |
| **T+1 (achieved)** | India | January 2023 |
| **T+1 (achieved)** | China (equities) | Ongoing (same-day sell restriction) |
| **T+1 (achieved)** | Australia | Late 2024 |
| **T+2 (T+1 target)** | EU (28 countries) | Target: October 2027 |
| **T+2 (T+1 target)** | UK | Target: ~2027 |
| **T+2 (under review)** | Japan, Hong Kong, Singapore, Taiwan | Under discussion |
| **T+2 (active review)** | Korea (KRX/KSD) | Under active review; KSD split-settlement reform underway (KRW 1B units from Apr 2026) |
| **T+3 (outlier)** | South Africa (JSE) | No announced timeline |

---

### 1.5 Margin Methodology Convergence

The global clearing industry is transitioning from scenario-based (SPAN) to VaR-based methodologies:

| Generation | Methodology | CCPs Using | Key Feature |
|---|---|---|---|
| **1st Gen** | Fixed-percentage | CFFEX, DCE, SHFE | Regulatory discretion; used as policy tool |
| **2nd Gen** | SPAN (scenario-based) | CDCC, ASX Clear (Futures), NSE Clearing, SGX-DC (IRM) | 16 standardized scenarios |
| **3rd Gen** | Historical VaR | JSCC, HKSCC, ICE Clear (IRM 2), CME (SPAN 2) | Filtered historical simulation |
| **3rd Gen** | PRISMA (FHS + ES) | Eurex Clearing | 750 filtered + 250 stress scenarios; portfolio-based |
| **3rd Gen** | PAIRS (ES-based) | LCH | Expected Shortfall 99.7%; 5-day holding period |
| **3rd Gen** | STANS (Monte Carlo) | OCC | 10,000+ scenarios; 99% ES |
| **2nd Gen** | KRX-SPAN (scenario-based) | KRX | Modified SPAN; evaluating VaR transition (following JSCC 2023 precedent) |
| **Transitional** | SPAN → SPAN 2 | CME Clearing | HVaR + ES; phased rollout 2023-2025 |

---

## 2. KRX Benchmarking

### 2.1 KRX Profile Summary

Korea Exchange (KRX) operates as an integrated exchange covering equities (KOSPI/KOSDAQ/KONEX), derivatives, and bonds. Key infrastructure:

- **Equities Trading System:** Exture 3.0 (Phase 1: Jan 2023, Phase 2: Oct 2023; in-house developed)
- **Derivatives Trading System:** Exture 3.0 (unified platform)
- **CCP:** KRX acts as CCP for all exchange-traded products
- **CSD:** Korea Securities Depository (KSD)
- **Regulators:** Financial Services Commission (FSC), Financial Supervisory Service (FSS), Bank of Korea (BOK — systemic oversight)
- **Settlement Cycle:** T+2 (equities), T+1 (government bonds), T+0/T+1 (derivatives margin)
- **Market Cap:** ~KRW 4,277 trillion (~USD 2.95 trillion, January 2026)
- **Listed Companies:** ~2,901 (KOSPI ~954, KOSDAQ ~1,700+, KONEX ~129)
- **Daily Trading Value:** ~KRW 32.23 trillion (~USD 20.7 billion, February 2026 average)

---

### 2.2 KRX Equities Market vs Global Peers

#### Trading System Comparison

| Metric | KRX (Exture+) | NYSE (Pillar) | NASDAQ (Eqlipse) | Deutsche Borse (T7) | JPX (arrowhead 4.0) |
|---|---|---|---|---|---|
| **Latency** | ≤70 us worst-case (EXTURE+); ~49 us est. (Exture 3.0, 30% improvement) | ~34 microseconds | ~14 microseconds | ~5 microseconds | Microsecond-level |
| **Architecture** | In-house (Linux x86, memory-based order book) | In-house (ICE) | In-house (4th gen) | In-house | Co-dev (Fujitsu) |
| **Launch** | Jan 2023 (Exture 3.0 Phase 1) | 2016-2023 | 2024 | 2012/2017 | Nov 2024 |
| **Unified** | Equities + Derivatives + Clearing/Settlement | 7 NYSE venues | Multiple markets | Equities + Derivatives | Equities only |

**Assessment:**
- **Competitive:** Exture 3.0 latency (~49 us estimated worst-case) is competitive with most exchanges but behind the leaders (T7 at ~5 us, NASDAQ at ~14 us)
- **Strength:** Exture 3.0 is a recently upgraded system (Jan/Oct 2023), with unified platform extending low-latency scope to clearing/settlement — broader coverage than most peers
- **Strength:** Unified platform for equities, derivatives, and clearing/settlement — more efficient than separate systems (like JPX with arrowhead + J-GATE + JSCC)
- **Gap:** Official Exture 3.0 latency/throughput not publicly disclosed — the ~49 us figure is an estimate based on KRX's stated 30% improvement over EXTURE+ (≤70 us)

#### Market Structure Comparison

| Feature | KRX | NYSE | NASDAQ | LSE | JPX | HKEX |
|---|---|---|---|---|---|---|
| **Market cap** | ~$2.95T (KRW 4,277T, Jan 2026) | $28.0T | $42.2T | $5.9T | $8.1T | $6.2T |
| **Opening auction** | Yes (call auction) | Yes | Yes (cross) | Yes | Yes | Yes |
| **Closing auction** | Yes | Yes (D-Limit) | Yes (cross) | Yes | Yes (since Nov 2024) | Yes |
| **Lunch break** | No (removed 2000) | No | No | No | Yes (11:30-12:30) | Yes (12:00-13:00) |
| **Price limits** | ±30% (IPO +300%/-60%) | LULD (5-20%) | LULD (5-20%) | None (dynamic CB) | ±30% (1st day none) | None |
| **DMM/Market makers** | LP program | Designated MMs | Registered MMs | Voluntary MMs | Voluntary MMs | Voluntary MMs |
| **Dark trading** | Minimal | ~15% of volume | ~15% of volume | ~10% | Minimal | Minimal |

**Assessment:**
- **KRX leads:** Removal of lunch break (since 2000) — ahead of all Asian peers. Price limit system (+/-30%) well-calibrated
- **KRX lags:** Limited dark pool/alternative venue ecosystem; extended hours limited to 16:00-18:00 off-hours (NYSE planning 22-hour trading); Nextrade (NXT) ATS approval pending

#### Settlement Comparison

| Feature | KRX/KSD | DTCC (US) | LCH/Euroclear (EU) | JSCC/JASDEC (JP) | HKSCC (HK) |
|---|---|---|---|---|---|
| **Cycle** | T+2 | T+1 | T+2 | T+2 | T+2 |
| **DVP Model** | DVP Model 1 | DVP Model 2 | DVP Model 1 (T2S) | DVP Model 3 | DVP Model 1 |
| **Central bank money** | BOK (KRW) | Fed (Fedwire) | ECB (T2S for EUR) | BOJ | HKMA (RTGS) |
| **T+1 plans** | Under review | Achieved (May 2024) | Target Oct 2027 | Under discussion | Readiness by 2025 |

**Assessment:**
- **Gap:** T+2 settlement when US/Canada/India/Australia have moved to T+1. T+1 migration should be a priority
- **Strength:** DVP Model 1 with BOK settlement provides robust settlement finality

---

### 2.3 KRX Derivatives Market vs Global Peers

#### Volume and Product Comparison

| Exchange | 2024 Volume (contracts) | Product Breadth | Key Products |
|---|---|---|---|
| NSE India (F&O) | ~92-108B [estimated] | Equity index, single stock, FX, commodity | Nifty 50, Bank Nifty |
| CME Group | ~6.2B (28.1M ADV) | Multi-asset (6+ classes) | E-mini S&P, Treasuries, WTI, Gold |
| Eurex | ~2.1B | Multi-asset (8+ classes) | Euro-Bund, EURO STOXX 50, DAX |
| KRX | ~1.5B (2024; 8th globally by value) | Equity index (KOSPI 200, Mini, Weekly, KOSDAQ 150, Sector), single stock (~274 futures, ~64 options), FX (USD/JPY/EUR/CNY), commodity (gold, lean hog), interest rate (3Y/10Y/30Y KTB), volatility (V-KOSPI 200) | KOSPI 200 options/futures, Mini KOSPI 200 |
| Cboe | ~4.5B (18.4M ADV options) | Equity/index options | SPX, VIX |
| HKEX Deriv | ~334M | Equity index, FX, commodity | HSI, H-shares |
| SGX Deriv | ~329M | Asian equity index, FX, commodity | FTSE China A50, Nikkei 225 |

**Assessment:**
- **KRX leads:** Historically the world's most active single-product derivatives exchange (KOSPI 200 options; peak 3.93B contracts in 2011). After 2012 multiplier increase (KRW 100K → 500K), volume normalized to ~1.5B (2024). KRX ranked 8th globally by derivatives trading value
- **KRX lags:** Product breadth improving but still concentrated on KOSPI 200. CME and Eurex offer vastly broader product catalogs. Commodity coverage minimal (gold, lean hog only). V-KOSPI 200 futures exist but with limited liquidity
- **Opportunity:** Night session expansion (10 products from June 2025); commodity derivatives development; environmental/ESG derivatives; Weekly options expansion

#### Margin Methodology Comparison

| Feature | KRX | CME (SPAN 2) | Eurex (PRISMA) | OCC (STANS) | LCH (PAIRS) |
|---|---|---|---|---|---|
| **Methodology** | KRX-SPAN (modified SPAN, scenario-based) | Historical VaR + ES | Filtered Historical Sim | Monte Carlo VaR | Expected Shortfall |
| **Confidence** | Not publicly disclosed | 99%+ | 99%/99.5% | 99% | 99.7% |
| **Holding period** | Not publicly disclosed | 1-2 days (ETD) | 2 days (ETD) | 2 days | 5 days (SwapClear) |
| **Cross-margining** | Spread margins (calendar/inter-commodity); OTC IRS/CRS clearing (mandated) | Comprehensive (futures-IRS, CME-OCC) | Comprehensive (ETD-OTC, cross-asset) | Portfolio margining | Cross-service |
| **Anti-procyclicality** | Not publicly disclosed; evaluating VaR transition | Stress VaR floors | Stress buffers | Margin floors | Volatility buffers |

**Assessment:**
- **Update:** KRX uses KRX-SPAN (modified SPAN, scenario-based) — 2nd generation methodology. KRX is evaluating transition to VaR-based approach following JSCC's 2023 precedent
- **Gap:** Cross-margining limited to spread margins and mandated OTC IRS/CRS clearing. No cross-CCP arrangements or comprehensive ETD-OTC portfolio margining like CME or Eurex
- **Gap:** Margin methodology confidence level and holding period not publicly disclosed — transparency improvement recommended
- **Opportunity:** VaR transition would bring KRX in line with global 3rd-gen standards; develop comprehensive cross-margining between equities, derivatives, and bonds

---

### 2.4 KRX/KSD Clearing & Settlement vs Global Peers

#### CCP Comparison

| Feature | KRX (CCP) | DTCC/NSCC | CME Clearing | LCH | Eurex Clearing |
|---|---|---|---|---|---|
| **Model** | Integrated exchange-CCP | Standalone CCP (utility) | Exchange-CCP (CME Group) | Multi-exchange CCP | Exchange-CCP (DBAG) |
| **Products cleared** | Equities, derivatives, bonds | Equities, Treasuries, MBS | Futures, options, OTC IRS/FX | OTC IRS, repos, equities, FX, CDS | ETD, equities, OTC IRS |
| **Default waterfall** | Sequential: (1) Defaulter margin → (2) Defaulter clearing deposit → (3) Joint Compensation Fund (~KRW 100B est.) → (4) KRX own capital (SITG) → (5) Non-defaulting members' additional contributions | Sequential with assessment powers | Sequential with guaranty fund | Sequential with reserve fund | Sequential with reserve fund |
| **SITG (Skin-in-the-Game)** | Present (Layer 4, before non-defaulting members); amount not publicly disclosed | Material | Material | Material | Material |
| **Cover standard** | Not explicitly disclosed; PFMI largely observant (IMF FSAP) | Cover 1-2 | Cover 2 | Cover 2 | Cover 2 |
| **PFMI compliance** | Largely observant (FSAP assessed) | Full | Full | Full | Full |
| **Recovery tools** | Assessment powers on surviving members; asset liquidation; netting. No dedicated CCP R&R regime (as of 2026) | Assessment, VMGH | Assessment, tear-up | VMGH, tear-up, forced allocation, auction | VMGH, cash calls, position allocation |
| **Resolution authority** | FSC/FSS (no dedicated CCP R&R regime; gap noted) | FDIC (Title II) | FDIC (Title II) | Bank of England | SRB + BaFin |

**Assessment:**
- **Strength:** Integrated exchange-CCP model (like CME, Eurex) provides operational efficiency and risk visibility
- **Strength:** PFMI largely observant (IMF FSAP); SITG positioned correctly before non-defaulting members
- **Strength:** Joint Compensation Fund uses fixed + variable model for dynamic adequacy
- **Gap:** No dedicated CCP recovery and resolution regime (similar gap in Japan, Hong Kong, Singapore) — contrast with EU CCP RRR (2021/23) and US Dodd-Frank Title II
- **Gap:** Default waterfall layer sizes and SITG amount not publicly disclosed — global best practice (CPMI-IOSCO PQD) calls for detailed disclosure
- **Gap:** No CCP interoperability arrangements — contrast with European model (LCH ↔ SIX x-clear ↔ Cboe Clear Europe)
- **Gap:** Recovery tools limited to assessment powers and asset liquidation — no VMGH or forced allocation tools documented

#### CSD Comparison (KSD vs Peers)

| Feature | KSD | DTC (DTCC) | Euroclear | JASDEC | CSDC (China) |
|---|---|---|---|---|---|
| **Type** | National CSD | National CSD | ICSD + National CSDs | National CSD | National CSD |
| **Assets under custody** | KRW 3,149T (~$2.4T, 2014; likely significantly higher by 2026) | $100T+ | EUR 42.5T | ~$5T [estimated] | RMB 11.05 quadrillion |
| **ISO 20022** | Adopted (CSD connections, transfer agents, global fund platforms) | Target Q3 2027 | Adopted | Progressing | Proprietary protocols |
| **DLT initiatives** | Security Token Framework (mandatory KSD registration; law effective Jan 2027) | Project Ion | — | — | — |
| **T2S equivalent** | N/A (single market) | N/A | T2S (EUR settlement) | N/A | N/A |

**Assessment:**
- **Strength:** KSD has already adopted ISO 20022 — ahead of DTC (target Q3 2027) and JASDEC (in progress)
- **Strength:** Security Token Framework legislation passed; KSD positioned as mandatory central registry for ALL security tokens (effective Jan 2027) — proactive approach
- **Strength:** Split settlement reform (KRW 1B units from Apr 2026) reduces member deposit requirements
- **On par:** KSD functions well as a national CSD with BOK central bank money settlement for government bonds
- **Gap:** AUC figure outdated (KRW 3,149T from 2014); current figures should be published

---

### 2.5 KRX Strengths and Gaps Summary

#### Areas Where KRX Leads

| Area | Description |
|---|---|
| **No lunch break** | Removed in 2000 — ahead of JPX, HKEX, SGX, SSE/SZSE which all still have lunch breaks |
| **Integrated exchange** | Single exchange for equities + derivatives + bonds (like Deutsche Borse Group model) — operationally efficient |
| **Derivatives heritage** | Historically world's most active single-product derivatives exchange (KOSPI 200 options; peak 3.93B contracts, 2011); ranked 8th globally by value (2024) |
| **PFMI compliance** | Largely observant, confirmed by IMF FSAP assessment |
| **Unified Exture 3.0** | Recently upgraded (2023) unified platform extending low-latency scope to clearing/settlement |
| **Technology independence** | In-house developed system — not dependent on foreign vendors |
| **ISO 20022** | KSD adopted ISO 20022 — ahead of DTC and JASDEC |
| **Security Token** | KSD designated as mandatory central registry for all security tokens (law effective Jan 2027) |
| **OTC clearing** | Mandated central clearing for KRW IRS and CRS through KRX |
| **LP/MM programs** | Comprehensive LP and Market Maker programs for equities, ETFs, ETNs, ELWs, and derivatives |

#### Areas Where KRX Lags

| Area | Gap | Priority | Global Leaders |
|---|---|---|---|
| **Trading system transparency** | Official Exture 3.0 latency/throughput not publicly disclosed | Medium | T7, NASDAQ, Optiq (public specs) |
| **Settlement cycle** | T+2 when US/Canada/India/Australia at T+1 | High | DTCC (T+1, May 2024), India (T+1, Jan 2023) |
| **Margin methodology** | KRX-SPAN (2nd gen) while peers moving to VaR/ES (3rd gen) | Medium-High | CME (SPAN 2), Eurex (PRISMA), OCC (STANS) |
| **Product breadth (derivatives)** | Improving but concentrated on KOSPI 200; minimal commodity coverage | Medium | CME (6+ asset classes), Eurex (8+ product categories) |
| **CCP R&R regime** | No dedicated CCP recovery and resolution regime | Medium-High | EU CCP RRR (2021/23), US Dodd-Frank Title II |
| **Default waterfall transparency** | Waterfall layer sizes and SITG amount not publicly disclosed | Medium | DTCC, CME, LCH, Eurex (detailed PQD reports) |
| **Cross-margining** | Limited to spread margins and mandated OTC IRS/CRS; no cross-CCP arrangements | Medium | CME-FICC, Eurex PRISMA (comprehensive ETD/OTC) |
| **CCP recovery tools** | No VMGH or forced allocation documented; only assessment powers | Medium | LCH (VMGH, tear-up, auction), Eurex (VMGH, cash calls) |
| **Dark pool/alternative venues** | Minimal; Nextrade (NXT) ATS approval pending | Low | US (15%+ dark), EU (10%+ dark/SI) |
| **Extended trading hours** | Off-hours 16:00-18:00 only; night session for derivatives from June 2025 | Low-Medium | NYSE (22-hour planned), CME Globex (~23 hours) |
| **Cloud migration** | No announced plans | Low | CME (Google Cloud 2026-28), LCH (AWS), Eurex (Google Cloud) |

#### Recommended Priority Actions for KRX

1. **High Priority — T+1 Settlement Migration**
   - US/Canada completed May 2024; EU targeting Oct 2027
   - Korea risks falling behind if not aligned with regional peers (HKEX readiness by 2025)
   - Requires coordination with KSD, BOK, and market participants

2. **High Priority — CCP Recovery and Resolution Framework**
   - No dedicated CCP R&R regime — gap shared with Japan, Hong Kong, Singapore
   - EU CCP RRR (Regulation 2021/23) provides a model framework
   - Should include: VMGH, forced allocation, tear-up, and partial property transfer tools
   - SITG amount and waterfall details should be publicly disclosed per CPMI-IOSCO PQD best practice

3. **Medium Priority — Derivatives Product Diversification**
   - Expand commodity derivatives, interest rate products, volatility products
   - Consider micro/mini contracts for retail participation
   - Environmental/ESG derivatives (growing global trend)

4. **Medium-High Priority — Margin Methodology Modernization**
   - KRX-SPAN is 2nd-generation; global peers transitioning to VaR/ES (3rd gen)
   - JSCC completed SPAN → VaR transition in 2023 — a model for KRX
   - Develop comprehensive cross-margining between equities, derivatives, and bonds (beyond current spread margins)

5. **Medium Priority — Transparency & Disclosure**
   - Publish CPMI-IOSCO PQD reports with detailed default waterfall data
   - Enhance CCP recovery and resolution planning documentation
   - Align with global best practices on margin methodology transparency

---

## 3. Quality Check

### 3.1 Document Completeness

#### Equities Domain (01_equities)

| Category | Expected | Delivered | Status |
|---|---|---|---|
| Exchange profiles | 23 | 23 (including KRX) | Complete |
| System deep-dives | 9 | 9 (Pillar, INET, Millennium, arrowhead, Orion, Titan, Optiq, T7, Exture 3.0) | Complete |
| Regulatory analyses | 3 | 3 (US, EU, Asia) | Complete |
| Overview | 1 | 1 | Complete |
| Comparative analysis | 1 | 1 | Complete |
| **Total English files** | **37** | **37** | **Complete** |

#### Derivatives Domain (02_derivatives)

| Category | Expected | Delivered | Status |
|---|---|---|---|
| Exchange profiles | 17 | 17 (including KRX Derivatives) | Complete |
| System deep-dives | 3 | 3 (Globex, Genium INET, T7 Derivatives) | Complete |
| Regulatory analyses | 3 | 3 (US, EU, Asia) | Complete |
| Overview | 1 | 1 | Complete |
| Comparative analysis | 1 | 1 | Complete |
| **Total English files** | **25** | **25** | **Complete** |

#### Clearing Domain (03_clearing)

| Category | Expected | Delivered | Status |
|---|---|---|---|
| Organization profiles | 20 | 20 (add KRX Clearing + KSD) | Complete |
| System deep-dives | 3 | 3 (DTCC Systems, LCH Systems, Eurex PRISMA) | Complete |
| Regulatory analyses | 3 | 3 (US, EU, Asia) | Complete |
| Overview | 1 | 1 | Complete |
| Comparative analysis | 1 | 1 | Complete |
| **Total English files** | **28** | **28** | **Complete** |

#### Overall

| Item | Count |
|---|---|
| Total English research files | 90 |
| Korean translations | 90 (mirrored) |
| English DOCX exports | 90 |
| Korean DOCX exports | 90 |
| **Grand Total** | **360+ files** |

---

### 3.2 [Unverified] Items Summary

**Total [unverified] tags across all domains: ~215 instances in 50 files**

#### Distribution by Domain

| Domain | [unverified] | [estimated] | TBD/TODO |
|---|---|---|---|
| Equities | ~61 | ~24 | 0 |
| Derivatives | ~57 | ~1 | 2 |
| Clearing | ~97 | ~3 | 3 |
| **Total** | **~215** | **~28** | **5** |

#### Top Files by [unverified] Count

| File | Count | Primary Areas |
|---|---|---|
| `02_derivatives/en/exchanges/sgx_derivatives.md` | 32 | Product specs, tick sizes, settlement methods |
| `01_equities/en/systems/arrowhead.md` | 15 | Hardware specs, programming languages |
| `03_clearing/en/organizations/jscc.md` | 14 | Margin methodology details, MPOR values |
| `03_clearing/en/regulations/eu_clearing_regulation.md` | 12 | KRX comparison points, DLT initiatives |
| `01_equities/en/regulations/us_equities_regulation.md` | 11 | SIFMU definitions (tagged as [estimated]) |
| `03_clearing/en/regulations/us_clearing_regulation.md` | 8 | Security-based swap clearing status |
| `03_clearing/en/systems/dtcc_systems.md` | 7 | Legacy tech stack, netting efficiency |
| `01_equities/en/systems/pillar.md` | 7 | OS, programming languages, DR config |

#### [Unverified] Categories

| Category | % of Total | Typical Examples |
|---|---|---|
| Technical specifications (latency, capacity, programming languages) | ~35% | arrowhead C++ [unverified], T7 FPGA details [unverified] |
| KRX comparison points | ~20% | KRX margin methodology [unverified], KRX settlement model [unverified] |
| Product/contract specifications | ~15% | SGX tick values [unverified], contract sizes [unverified] |
| Regulatory details | ~15% | Security-based swap mandate [unverified], T+1 timelines [unverified] |
| Organizational/operational | ~15% | Employee counts [unverified], revenue figures [unverified] |

**Assessment:** The [unverified] tagging is appropriately used per RESEARCH_GUIDE.md standards. Most tags apply to secondary details (programming languages, exact hardware counts) or KRX-specific comparisons that require internal KRX documentation to verify. Core exchange mechanics, market structures, and regulatory frameworks are well-sourced.

---

### 3.3 Consistency Check

#### Naming Conventions
- All files follow lowercase_underscore convention per RESEARCH_GUIDE.md
- Directory structure consistent across all 3 domains: `en/exchanges/`, `en/systems/`, `en/regulations/`
- Korean translations mirror English structure: `ko/exchanges/`, `ko/systems/`, `ko/regulations/`

#### Template Adherence
- Equities: All 23 exchange files follow TEMPLATE_EXCHANGE.md (11 sections)
- Derivatives: All 17 exchange files follow TEMPLATE_EXCHANGE.md adapted for derivatives
- Clearing: All 20 organization files follow TEMPLATE_CLEARING.md (8-9 sections)
- System files follow TEMPLATE_SYSTEM.md

#### Source Citation
- Primary sources (exchange websites, annual reports) used consistently
- Source format follows `[Source: Name, "Document", accessed YYYY-MM-DD]` pattern
- All three domains use identical citation standards

#### Cross-Domain Terminology
- Terms used consistently across domains (e.g., "DVP Model 1/2/3", "PFMI", "SPAN")
- No conflicting definitions found between domains

---

### 3.4 Glossary Completeness

| Metric | English (glossary_en.md) | Korean (glossary_ko.md) |
|---|---|---|
| **Total terms** | 355 | 374 |
| **Categories covered** | Trading, Clearing, Settlement, Technology, Regulation, Derivatives, Market Segments | Same + KRX-specific terms |
| **EN terms missing from KO** | 3 (Exchange for Physical, Exchange for Swap, Pro-Rata Matching) | — |
| **KO-only terms** | — | ~22 (additional KRX/Korean market terms) |

**Assessment:** Glossaries are 99%+ aligned. The 3 missing Korean translations should be added for completeness:
- Exchange for Physical (EFP) → 실물교환거래
- Exchange for Swap (EFS) → 스왑교환거래
- Pro-Rata Matching → 비례배분 체결

#### Suggested Additional Terms (currently absent from both glossaries)

| Term | Category | Relevance |
|---|---|---|
| 0DTE (Zero Days to Expiration) | Derivatives | 59% of SPX volume in 2025 |
| Active Account Requirement (AAR) | Regulation | EMIR 3.0 key provision |
| DORA (Digital Operational Resilience Act) | Regulation | EU mandatory from Jan 2025 |
| Swap Connect | Cross-border | HK-China IRS connectivity |
| GIFT Connect | Cross-border | SGX-NSE India connectivity |
| Consolidated Tape Provider (CTP) | Market Data | EU MiFIR Refit initiative |

---

### 3.5 Known Gaps and Follow-Up Items

#### Documentation Gaps (Not Critical)

1. **System deep-dives limited to major platforms only:** Only 14 system files created (8 equities + 3 derivatives + 3 clearing). Tier 2/3 exchange systems (Quantum XA, SIBE-Smart, NEAT+, Chinese systems) do not have dedicated system files — by design per SESSION_PLAN.md

2. **Middle East/Africa regulation:** No dedicated regulation file for Middle East or Africa. Covered briefly within exchange-level documents (Tadawul, JSE, DME)

3. **OTC derivatives clearing:** Limited detail on bilateral vs. cleared OTC markets beyond major CCPs (LCH SwapClear, CME OTC, Eurex OTC)

#### Items Requiring KRX Internal Verification

The following items remain [unverified] after KRX deep-dive research and require access to internal KRX documentation:

1. Exture 3.0 official latency and throughput specifications (KRX has not published; ~49 us is estimated from 30% improvement claim)
2. KRX SITG (Skin-in-the-Game) exact amount (confirmed present at Layer 4, amount not disclosed)
3. Joint Compensation Fund exact size (estimated ~KRW 100B)
4. KRX-SPAN confidence level and holding period parameters (not specified in public materials)
5. Cover standard (not explicitly stated as Cover 1 or Cover 2)
6. KSD current assets under custody (KRW 3,149T figure is from 2014)
7. KRX extended trading hours plans beyond current off-hours session
8. KRX T+1 settlement migration timeline (under active review)

---

## Appendix: Research Statistics

| Metric | Value |
|---|---|
| **Total exchanges/organizations researched** | 60 (23 equities + 17 derivatives + 20 clearing) |
| **Total English research documents** | 90 |
| **Total Korean translations** | 90 |
| **Total DOCX exports** | 180 (90 EN + 90 KO) |
| **Grand total files** | 360+ |
| **Research period** | 2026-04-03 to 2026-04-13 |
| **Sessions executed** | 15 (E1-E3, D1-D3, C1-C3, T1-T3, K1-K3) |
| **Glossary terms (EN)** | 355 |
| **Glossary terms (KO)** | 374 |
| **[unverified] tags** | ~215 across 50 files |
| **[estimated] tags** | ~28 across 7 files |
| **TBD/placeholder items** | 5 |
| **Jurisdictions covered** | 20+ |
| **Trading systems analyzed** | 25+ distinct platforms |
| **CCPs/CSDs profiled** | 20 organizations |
| **Regulatory frameworks** | 9 regional analyses (3 per domain) |

---

*Document generated: 2026-04-13*
*Project: Global Exchange Research for KRX IT Department*
*Status: Phase 5 — KRX Deep-Dive Complete*
