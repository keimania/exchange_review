# Comparative Analysis of Global Equities Exchanges

> **Last Updated:** 2026-04-13
> **Scope:** 23 exchanges across Americas, EMEA, and Asia-Pacific (including KRX)
> **Author:** Exchange Research Project

---

## 1. Trading System Technology Comparison

| Exchange | System Name | Vendor / In-house | Launch Year | Latency (round-trip) | Capacity (orders/sec) | Technology Stack |
|----------|-----------|-------------------|-------------|---------------------|----------------------|------------------|
| NYSE | Pillar | In-house (ICE) | 2017-2023 | ~34 us (binary, P50) | Not disclosed (handles 10B+ shares/day peaks) | Binary/FIX gateways, UDP multicast, deterministic matching |
| NASDAQ | INET / Eqlipse | In-house (Nasdaq) | 2006 / 2024 | ~14 us (door-to-door fastest); ~20 us (order ack) | Millions/sec (estimated) | OUCH/FIX/ITCH, FPGA-accelerated, microservices, AWS hybrid |
| LSE | Millennium Exchange | In-house (MillenniumIT) | 2011 | ~126 us (native) | Tens of thousands/sec | C++/Linux, MITCH/FIX 5.0, commodity x86 |
| JPX (TSE) | arrowhead 4.0 | Co-developed (Fujitsu) | 2024 (4th gen) | Microsecond-level (in-memory) | Not disclosed | 462 Fujitsu PRIMERGY servers, triple-redundancy |
| HKEX | OTP-C / OCG-C | In-house (HKEX) | 2018 | Sub-millisecond (estimated) | 60,000 orders/sec | Open systems, SDNet/3 network |
| SGX | REACH (Nasdaq) | Nasdaq (licensed) | 2019 (upgraded) | Sub-90 us | Not disclosed | Nasdaq Financial Framework, OUCH/ITCH/FIX |
| Euronext | Optiq | In-house (Euronext) | 2018 | ~15 us average | 1,000,000 msgs/sec | SBE/FIX 5.0, UDP multicast, Apache Kafka |
| Deutsche Borse | T7 | In-house (Deutsche Borse) | 2017 (Xetra) | ~5 us median (co-located) | Hundreds of thousands/sec per partition | Partition-based, ETI/FIX, event-driven |
| ASX | ASX Trade (Genium INET) | Nasdaq (licensed) | 2010 | ~300 us (at launch) | 100,000+ orders/sec | Genium INET (C/C++), OUCH/ITCH/FIX |
| TMX (TSX) | Quantum XA | In-house (TMX) | 2013-2014 | Not disclosed | Not disclosed | FIX/STAMP protocols, co-located Markham DC |
| SIX Swiss | SWXess (X-stream INET) | Nasdaq (licensed) | 2012 | ~10.6 us average | Not disclosed | X-stream INET, SwissAtMid MPOB |
| SSE | 4th-gen (self-developed) | In-house | ~2023 | 20x reduction vs prior gen | 2.5x increase vs prior gen | Self-developed, Chinese crypto standards |
| SZSE | Proprietary | In-house | 2016 (upgrade) | ~1.1 ms (matching engine) | 300,000 orders/sec | Self-developed, STEP protocol |
| NSE India | NEAT+ | In-house | 2010s | ~100 us (pre-Apr 2026) | 5-6 million TPS | Custom-built, planned nanosecond upgrade Apr 2026 |
| BSE India | BOLT Plus | Licensed (Deutsche Borse T7) | 2013-2014 | ~200 us (at launch) | 500,000 orders/sec | T7 architecture, FIX/FAST, NFCAST |
| TWSE | FAST (2nd gen) | In-house | 2014 | <3 ms (door-to-door) | 20 million transactions/day | Proprietary TMP/FIX |
| Nasdaq Nordic | INET Nordic / Genium INET | In-house (Nasdaq) | 2010s | Sub-100 us | >1,000,000 msgs/sec | OUCH/ITCH/FIX, nanosecond timestamps |
| Borsa Italiana | Optiq (Euronext) | In-house (Euronext) | 2023 | ~15 us average | 1,000,000 msgs/sec | SBE/FIX 5.0, Bergamo data centre |
| BME (Spain) | SIBE-Smart | In-house (BME) | 2012 (upgrade) | Sub-millisecond | Tripled from prior gen | FIX/native binary |
| Tadawul | X-Stream INET | Nasdaq (licensed) | 2015 | <40 us | 40,000 orders/sec | Nasdaq X-Stream INET |
| JSE | Millennium Exchange | LSEG Technology | 2012 | ~124 us (platform spec) | Tens of thousands/sec | C++/Linux, FAST/ITCH, FIX |
| Bursa Malaysia | BTS2 (X-Stream INET) | Nasdaq (licensed) | 2013 | Sub-millisecond | 10x prior capacity | Nasdaq X-Stream INET, FIX |
| **KRX** | **Exture 3.0** | **In-house (KRX/KOSCOM)** | **2023** | **~49 us (estimated, 30% improvement over EXTURE+ 70 us)** | **100,000+ TPS (EXTURE+ baseline)** | **Linux x86, FIX/FAST, memory-based order book** |

**Key Observations:**
- Deutsche Borse T7 (~5 us) and Nasdaq INET (~14 us door-to-door) lead in raw latency among major exchanges
- Euronext Optiq (~15 us) demonstrates that in-house platforms can rival vendor solutions
- Chinese exchanges (SSE, SZSE) have pivoted to fully self-developed systems aligned with national technology independence policy
- NSE India is targeting a transformative upgrade to nanosecond-level latency with 100 million TPS by April 2026
- Nasdaq technology (INET/Genium/X-Stream) powers the most exchanges globally: ASX, SGX, SIX, Tadawul, Bursa Malaysia, Nasdaq Nordic, and more

---

## 2. Market Structure Comparison

| Exchange | Market Type | Auction Types | Trading Hours (Local) | Trading Hours (UTC) | Lunch Break | Tick Size Approach | Standard Lot |
|----------|-----------|--------------|----------------------|--------------------|-----------|--------------------|-------------|
| NYSE | Hybrid (order + DMM floor) | Open, Close, LULD halt | 9:30-16:00 ET | 14:30-21:00 | No | Fixed ($0.01/>=$1) | 100 shares (variable from Nov 2025) |
| NASDAQ | Order-driven + competing MMs | Opening Cross, Closing Cross | 9:30-16:00 ET | 14:30-21:00 | No | Fixed ($0.01/>=$1) | 100 shares |
| LSE | Order-driven (SETS) / Hybrid (SETSqx) | Open, Close, Volatility, Intraday (SETSqx) | 08:00-16:30 GMT | 08:00-16:30 | No | MiFID II RTS 11 (price+liquidity) | 1 share |
| JPX (TSE) | Order-driven (Zaraba) | Itayose (open/close), Special Quote | 09:00-15:30 JST | 00:00-06:30 | Yes (1 hr) | Tiered by price (TOPIX 500 finer) | 100 shares |
| HKEX | Order-driven | POS, CAS (random close) | 09:30-16:00 HKT | 01:30-08:00 | Yes (1 hr) | Tiered by price (11 bands) | Varies (100-10,000) |
| SGX | Order-driven | Open, Mid-day, Close (randomized) | 09:00-17:00 SGT | 01:00-09:00 | Yes (1 hr) | Tiered by price (3 bands) | 100 shares |
| Euronext | Order-driven | Open, Close, Volatility | 09:00-17:30 CET | 08:00-16:30 | No | MiFID II RTS 11 | 1 share |
| Deutsche Borse | Order-driven + Designated Sponsors | Open, Close, Intraday, Volatility | 09:00-17:30 CET | 08:00-16:30 | No | MiFID II RTS 11 | 1 share |
| ASX | Order-driven (CLOB + dark) | Open, CSPA, Post-close | 10:00-16:00 AEST | 00:00-06:00 | No | Tiered by price (3 bands) | 1 share |
| TMX (TSX) | Order-driven + Registered Traders | MOO, MOC (with PME) | 09:30-16:00 ET | 14:30-21:00 | No | Fixed (C$0.01/>=$0.50) | 100/500/1000 (by price) |
| SIX Swiss | Order-driven + SwissAtMid | Open, Close, Volatility | 09:00-17:20 CET | 08:00-16:20 | No | MiFID II-aligned (non-EU) | 1 share |
| SSE | Order-driven | Opening call, Closing call | 09:30-15:00 CST | 01:30-07:00 | Yes (1.5 hrs) | Uniform (RMB 0.01) | 100 shares |
| SZSE | Order-driven | Opening call, Closing call | 09:30-15:00 CST | 01:30-07:00 | Yes (1.5 hrs) | Uniform (CNY 0.01) | 100 shares |
| NSE India | Order-driven | Pre-open call auction | 09:15-15:30 IST | 03:45-10:00 | No | Tiered by price (6 bands, from Apr 2025) | 1 share |
| BSE India | Order-driven | Pre-open call auction | 09:15-15:30 IST | 03:45-10:00 | No | Fixed (INR 0.05) | 1 share |
| TWSE | Order-driven (continuous since 2020) | Opening call, Closing call | 09:00-13:30 TST | 01:00-05:30 | No | Tiered by price (6 bands) | 1,000 shares |
| Nasdaq Nordic | Order-driven | Open, Close, Volatility, Auction-only | 09:00-17:25 CET | 08:00-16:25 | No | MiFID II RTS 11 | 1 share |
| Borsa Italiana | Order-driven | Open, Close, Volatility | 09:00-17:25 CET | 08:00-16:25 | No | MiFID II RTS 11 | 1 share |
| BME (Spain) | Order-driven | Open, Close, Volatility | 09:00-17:30 CET | 08:00-16:30 | No | MiFID II RTS 11 | 1 share |
| Tadawul | Order-driven | Open (random), Close (random) | 10:00-15:00 AST | 07:00-12:00 | No | Tiered by price (6 bands) | 1 share |
| JSE | Order-driven | Open, Close, Intraday, Volatility | 09:00-17:00 SAST | 07:00-15:00 | No | Flat (1 cent minimum) | 1 share |
| Bursa Malaysia | Order-driven | Open (AM/PM), Close | 09:00-17:00 MYT | 01:00-09:00 | Yes (1.5 hrs) | Tiered by price (2 bands) | 100 shares |
| **KRX (KOSPI)** | **Order-driven + LP/MM** | **Open call, Close call, VI auction** | **09:00-15:30 KST (08:00-18:00 incl. off-hours)** | **00:00-06:30 (23:00-09:00 incl. off-hours)** | **No** | **Tiered by price (7 bands)** | **1 share** |

**Key Observations:**
- Five Asian exchanges maintain lunch breaks: JPX (1 hr), HKEX (1 hr), SGX (1 hr), SSE/SZSE (1.5 hrs), and Bursa Malaysia (1.5 hrs)
- EU exchanges uniformly apply MiFID II RTS 11 tick sizes; Chinese exchanges use a simple uniform tick
- TWSE has the shortest trading hours among major exchanges at 4.5 hours; SGX has the longest continuous session at 7 hours
- The lot size of 1 share is now the global standard for most Western exchanges; Asian exchanges (TWSE: 1,000; HKEX: variable; SSE/SZSE: 100) retain larger board lots
- Randomized auction endings are widespread (HKEX, SGX, Euronext, BME, Tadawul, Nasdaq Nordic) to prevent manipulation

---

## 3. Circuit Breaker Mechanisms

| Exchange | Mechanism Name | Trigger Levels | Halt Duration | Static vs Dynamic | Index vs Stock Level |
|----------|---------------|---------------|--------------|-------------------|---------------------|
| NYSE / NASDAQ | LULD (Limit Up-Limit Down) | 5%/10%/20% bands (varies by tier/time) | 5-minute pause per stock | Dynamic (reference price updated) | Stock-level |
| NYSE / NASDAQ | Market-Wide Circuit Breaker (MWCB) | S&P 500: -7% (L1), -13% (L2), -20% (L3) | 15 min (L1/L2); remainder of day (L3) | Static (previous close) | Index-level |
| LSE | Dynamic + Static Circuit Breaker | ~8% static (FTSE 100); dynamic varies | Volatility auction (variable) | Both | Stock-level |
| JPX (TSE) | Special Quote (Tokubetsu Kehai) | Renewal price range (varies by price) | Stepwise display until balance or daily limit | Dynamic | Stock-level |
| JPX (TSE) | Daily Price Limits | Varies by price level (tiered) | Trading continues within limits | Static (previous close) | Stock-level |
| HKEX | Volatility Control Mechanism (VCM) | +/-10% (HSI/HSCEI stocks) | 5-minute cooling-off | Dynamic (last 5-min reference) | Stock-level (index constituents only) |
| SGX | Circuit Breaker | +/-10% from reference price | 5-minute cooling-off (trading continues within band) | Dynamic | Stock-level |
| Euronext | Dynamic + Static Collars | ~2-5% dynamic; ~8-10% static | ~5-minute reservation (volatility auction) | Both | Stock-level |
| Deutsche Borse (Xetra) | Volatility Interruption | Dynamic + static price corridors | ~2-minute auction + random end | Both | Stock-level |
| ASX | ETR (Extreme Trade Range) | Stock-specific bands | 2-minute trading pause | Dynamic | Stock-level |
| ASX | AOT (Anomalous Order Threshold) | +/-10% from 2-min VWAP | Order rejected (not halt) | Dynamic | Stock-level (pre-trade) |
| TMX (TSX) | Single Stock Circuit Breaker (SSCB) | Not publicly specified | 5-minute halt across all Canadian venues | Dynamic | Stock-level |
| SIX Swiss | Stop Trading Range | Dynamic + static thresholds | ~5-minute volatility auction | Both | Stock-level |
| SSE / SZSE | Daily Price Limits | +/-10% Main Board; +/-20% STAR/ChiNext | No halt; orders beyond limit rejected | Static (previous close) | Stock-level |
| SSE / SZSE | Market-wide CB (suspended) | CSI 300: -5%, -7% (SUSPENDED Jan 2016) | Was 15 min / rest of day | Static | Index-level (SUSPENDED) |
| NSE / BSE India | Market-Wide CB | Sensex/Nifty: -10%, -15%, -20% | 15 min to remainder of day (time-dependent) | Static (previous close) | Index-level |
| NSE / BSE India | Individual Price Bands | 2%/5%/10%/20% (varies by security) | No halt; orders beyond band rejected | Static | Stock-level |
| TWSE | Daily Price Limit | +/-10% | Orders beyond limit rejected | Static (previous close) | Stock-level |
| TWSE | Intraday Price Stabilization | +/-3.5% from last trade | 2-minute matching pause | Dynamic | Stock-level |
| Nasdaq Nordic | Volatility Guards | Dynamic + static thresholds | 60-180 second volatility auction | Both | Stock-level |
| BME (Spain) | Static + Dynamic Range | Per-security volatility-based | 5-minute volatility auction + 30s random end | Both | Stock-level |
| Tadawul | Volatility Interruption | +/-10% from previous close | 5-minute call auction | Static | Stock-level |
| JSE | Dynamic + Static CB | ~2% dynamic; ~5% static | Volatility auction | Both | Stock-level |
| Bursa Malaysia | Market-Wide CB | FBM KLCI: -10%, -15%, -20% | 1 hour to remainder of day | Static (previous close) | Index-level |
| **KRX** | **Market-Wide CB (SAPI)** | **KOSPI: -8% (L1), -15% (L2), -20% (L3)** | **20 min (L1/L2); remainder of day (L3)** | **Static (previous close)** | **Index-level** |
| **KRX** | **Volatility Interruption (VI)** | **Static: 3%/6% from reference; Dynamic: 10% from last trade** | **2-minute call auction + 30-sec random end** | **Both (static + dynamic)** | **Stock-level** |
| **KRX** | **Sidecar (Program Trading)** | **KOSPI 200 futures: +/-5%** | **5-minute program order suspension** | **Dynamic** | **Market-level (program trades only)** |
| **KRX** | **Daily Price Limits** | **+/-30% (standard); +300%/-60% (IPO day)** | **Orders beyond limit rejected** | **Static (previous close)** | **Stock-level** |

**Key Observations:**
- Most exchanges use stock-level circuit breakers; only the US, India, China (suspended), and Bursa Malaysia have active index-level market-wide halts
- China's failed 2016 circuit breaker experiment (suspended after 4 days due to "magnet effect") remains a cautionary case study
- European exchanges uniformly use dynamic+static dual-threshold systems feeding into volatility auctions
- US LULD is unique in its tiered percentage bands based on security classification

---

## 4. Market Data Protocols

| Exchange | Primary Protocol | Data Levels Available | Delivery Method |
|----------|-----------------|----------------------|----------------|
| NYSE | NYSE Pillar (XDP binary) | L1, L2, Full Depth | UDP multicast |
| NASDAQ | TotalView-ITCH 5.0 | L1, L2, Full Depth (order-by-order) | UDP multicast (MoldUDP64) |
| LSE | MITCH (ITCH variant) | L1, L2 (full depth) | UDP multicast |
| JPX (TSE) | arrowhead FLEX (ITCH-based) | L1, L2, Full Depth | UDP multicast |
| HKEX | OMD-C (Orion Market Data) | L1, L2 (40 price queues) | UDP multicast |
| SGX | ITCH | L1, L2, Full Depth | UDP multicast |
| Euronext | Optiq MDG (SBE binary) | L1, L2 (MBP 10 / MBO 10) | UDP multicast |
| Deutsche Borse | T7 EOBI (Enhanced Order Book Interface) | L1, L2, Full Depth | UDP multicast |
| ASX | ASX ITCH | L1, L2, Full Depth | UDP multicast |
| TMX (TSX) | TMX Quantum Feed | L1, L2, Full Depth | Multicast |
| SIX Swiss | ITCH (via X-stream INET) | L1, L2, Full Depth | UDP multicast |
| SSE | FAST (L1); Binary (L2) | L1 (5-level MBP), L2 (10 MBP + 50 MBO) | Dedicated feeds |
| SZSE | STEP / Binary | L1, L2 | Dedicated feeds |
| NSE India | Proprietary TCP/IP feed | L1, L2 (5 best), L3 (20 best) | TCP/colocation direct |
| BSE India | NFCAST (UDP multicast) | L1, L2 (market depth) | UDP multicast / leased line |
| TWSE | Proprietary (TWSE Market Info) | Real-time (5 bid/ask), 5-sec snapshot | Dedicated feeds |
| Nasdaq Nordic | TotalView-ITCH | L1, L2, Full Depth (with attribution) | UDP multicast (MoldUDP64) |
| Tadawul | Market Data Feed (Nasdaq) | L1, L2 (5 levels), Premium (full depth) | Direct / vendors |
| JSE | FAST/ITCH | L1, L2 | Multicast |
| Bursa Malaysia | FIX / Proprietary | L1, L2 | Dedicated feeds |
| **KRX** | **FIX/FAST + KRX proprietary** | **L1, L2, Full Depth** | **KOSCOM STOCK-NET (dedicated network) + internet** |

**Key Observations:**
- ITCH-based protocols (and variants like MITCH, OUCH) dominate globally for low-latency market data
- UDP multicast is the universal delivery method for production-grade exchange feeds
- Chinese exchanges have the most restricted data architecture, with proprietary protocols and no standard ITCH/FIX feeds
- Nasdaq Nordic's TotalView-ITCH uniquely includes market participant attribution in full-depth data

---

## 5. Co-location Offerings

| Exchange | Co-lo Location | Availability | Network Connectivity |
|----------|---------------|--------------|---------------------|
| NYSE | Equinix NY11, Carteret, NJ | Full rack, partial rack, cross-connect | 10G/40G fiber; DR at Equinix CH4 Chicago |
| NASDAQ | Equinix NY11, Carteret, NJ | Full rack, cross-connect | 10G/40G; 40G Express Connect (<35 ns switching) |
| LSE | Interxion LON1 / Equinix LD4, London area | Proximity hosting, cross-connect | LSE Extranet, third-party networks |
| JPX (TSE) | Primary DC, Tokyo metropolitan area | Co-location with equal-length cables | arrowhead co-location service |
| HKEX | Tseung Kwan O (TKO), Hong Kong | Proximity hosting via SDNet/3 | Dedicated SDNet/3 network |
| SGX | SGX co-location facility, Singapore | Full rack, cross-connect | Equal-length cross-connects |
| Euronext | Aruba IT3, Bergamo, Italy | Full/partial rack | Data centre carriers, direct cross-connect |
| Deutsche Borse | Equinix FR2, Frankfurt | Co-location, proximity | T7 proximity services |
| ASX | Australian Liquidity Centre (ALC), Gore Hill, Sydney | Full rack, equal-length cross-connects | ASX Net dark fibre network |
| TMX (TSX) | Markham, Ontario | Co-location at TMX DC | Direct cross-connects |
| SIX Swiss | Zurich area | Co-location, cross-connect | Dedicated network |
| SSE | Shanghai data center | Co-location for members | Dedicated lines |
| SZSE | Shenzhen data center (5,000 cabinets) | Co-location for members | Dedicated lines |
| NSE India | Mumbai (BKC area) | 2,000+ racks (expanding to 4,500) | Colocation direct feed |
| BSE India | Mumbai (NTT/Netmagic) | Rack space, cross-connects | Leased lines |
| TWSE | Banqiao Data Center, New Taipei City | Rack space, <100m from matching engines | Colt / Pico connectivity |
| Nasdaq Nordic | Vasby, Stockholm | Full rack, cross-connect | DR at Equinix SK2 |
| Tadawul | Riyadh (not confirmed) | Not confirmed | Not confirmed |
| JSE | JSE premises, Sandton + Teraco (Colo 2.0) | Rack space, cross-connect | TNS, IPC, Beeks |
| Bursa Malaysia | Not publicly disclosed | Available | BDA gateway connectivity |
| **KRX** | **Seoul DC (equities primary) + Busan DC (derivatives primary / KOSCOM IDC)** | **Rack space, proximity hosting, cross-connects** | **KOSCOM STOCK-NET; IPC/Itiviti connectivity; ICE Global Network** |

---

## 6. Fee Models

| Exchange | Fee Model Type | Approximate Rate Range |
|----------|---------------|----------------------|
| NYSE | Maker-taker (tiered) | Maker rebate ~$0.0020-0.0030/share; taker fee ~$0.0030/share |
| NASDAQ | Maker-taker (tiered) | Maker rebate ~$0.0020-0.0032/share; taker fee ~$0.0030/share |
| LSE | Ad valorem (value-based) | ~0.45 bps of trade value |
| JPX (TSE) | Flat per-trade + value-based | Trading participation fee; access fee per session |
| HKEX | Ad valorem + flat | ~0.00565% trading fee; HK$0.50 CCASS stock fee per side |
| SGX | Ad valorem (tiered) | Clearing fee varies by value tier |
| Euronext | Ad valorem | 0.50 bps per trade; min EUR 0.70 |
| Deutsche Borse (Xetra) | Ad valorem (tiered) | Varies by volume tier; Designated Sponsor discounts |
| ASX | Ad valorem (tiered) | ~0.15-0.28 bps per side |
| TMX (TSX) | Maker-taker | Varies by venue and tier |
| SIX Swiss | Ad valorem | Varies by volume tier |
| SSE | Ad valorem + stamp duty | ~0.00487% handling fee; 0.05% stamp duty (seller) |
| SZSE | Ad valorem + stamp duty | ~0.00487% handling fee; 0.05% stamp duty (seller) |
| NSE India | Flat per traded value | ~INR 3.22 per lakh; STT: 0.1% delivery |
| BSE India | Per-trade (tiered) | Competitive with NSE |
| TWSE | Commission + transaction tax | Max 0.1425% commission; 0.30% transaction tax (seller) |
| Nasdaq Nordic | Ad valorem (tiered) | Value-based + possible fixed per-trade |
| BME (Spain) | Ad valorem (tiered) | Varies by volume |
| Tadawul | Ad valorem | ~10.5 bps exchange commission + 3 bps CMA fee |
| JSE | Ad valorem + STT | 0.25% Securities Transfer Tax; Strate fee 0.005787% |
| Bursa Malaysia | Commission + clearing + stamp duty | Max 0.7% brokerage; 0.03% clearing; RM1/RM1,000 stamp duty |
| **KRX** | **Maker-taker (since Dec 2025; previously ad valorem flat)** | **Maker: 0.00134%; Taker: 0.00182% (total ~0.0036% incl. clearing fee); + 0.23% Securities Transaction Tax (seller)** |

**Key Observations:**
- US exchanges (NYSE, NASDAQ) are unique in their maker-taker rebate model, incentivizing passive liquidity provision
- Asian markets (China, India, Taiwan, Malaysia) layer government taxes (stamp duty, STT) on top of exchange fees
- EU exchanges generally use straightforward ad valorem models with volume tiers
- Tadawul has among the highest explicit exchange fee rates at ~10.5 bps

---

## 7. Regulatory Framework Comparison

### 7.1 Americas

| Item | United States (NYSE/NASDAQ) | Canada (TMX) |
|------|---------------------------|-------------|
| Regulator | SEC (federal) | OSC (lead) + CSA (provincial harmonization) |
| Key Regulation | Securities Exchange Act 1934, Reg NMS, Reg SHO | Securities Act (provincial), UMIR |
| SRO Model | Exchanges are SROs; FINRA oversees broker-dealers | CIRO (formed 2023 from IIROC+MFDA merger) |
| Short Selling | Reg SHO: locate requirement; alternative uptick rule | UMIR short selling rules; locate requirement |
| Foreign Access | Broker-dealer registration or exemptions | Remote access via approved intermediaries |
| Settlement Cycle | T+1 (since May 2024) | T+1 (since May 2024) |

### 7.2 Europe

| Item | UK (LSE) | EU (Euronext/Xetra/BME/Borsa Italiana) | Switzerland (SIX) | Nordics (Nasdaq Nordic) |
|------|---------|----------------------------------------|-------------------|----------------------|
| Regulator | FCA | AMF/BaFin/CNMV/CONSOB (College of Regulators for Euronext) | FINMA | Finansinspektionen (SE), FIN-FSA (FI), Finanstilsynet (DK) |
| Key Regulation | UK MiFID (onshored), UK MAR, FSMA 2000 | MiFID II/MiFIR, MAR, Prospectus Reg | FMIA (Financial Market Infrastructure Act) | MiFID II/MiFIR, MAR |
| SRO Model | LSE as RIE; FCA direct oversight | Exchange as regulated market; national regulator oversight | SIX Exchange Regulation (SER) as SRO | Exchange entities supervised by national regulators |
| Short Selling | UK Short Selling Regulation; 0.2%/0.5% thresholds | EU Short Selling Regulation; 0.1%/0.5% thresholds | Swiss regulations (FMIA-aligned) | EU Short Selling Regulation |
| Foreign Access | FCA recognition for overseas firms | MiFID II passporting (EEA); third-country equivalence | FINMA recognition | MiFID II passporting |
| Settlement Cycle | T+2 (T+1 targeted 2027) | T+2 (T+1 targeted 2027) | T+2 | T+2 |

### 7.3 Asia-Pacific

| Item | Japan (JPX) | Hong Kong (HKEX) | Singapore (SGX) | China (SSE/SZSE) | India (NSE/BSE) | Taiwan (TWSE) | Saudi Arabia (Tadawul) | **Korea (KRX)** |
|------|------------|-----------------|----------------|-----------------|----------------|-------------|---------------------|----------------|
| Regulator | JFSA / SESC | SFC | MAS | CSRC | SEBI | FSC (SFB) | CMA | **FSC / FSS** |
| Key Regulation | FIEA | SFO | SFA | Securities Law of PRC (2020) | SEBI Act 1992, SCRA 1956 | Securities and Exchange Act | Capital Market Law 2003 | **FSCMA (자본시장법)** |
| SRO Model | JPX-R (self-regulatory subsidiary) | HKEX as frontline regulator | SGX RegCo (independent subsidiary) | SSE/SZSE as frontline SROs under CSRC | Exchanges conduct surveillance; SEBI oversight | TWSE performs self-regulatory functions | Saudi Exchange under CMA | **KRX as SRO (market surveillance, delisting authority)** |
| Short Selling | Permitted with restrictions; uptick rule | Permitted; designated securities only | Permitted with rules | Restricted; securities lending only; naked shorts prohibited | Permitted; daily reporting | Permitted; volume limits (30% daily cap, temporarily 3%) | Limited | **Permitted with uptick rule; naked shorts prohibited; overheated stock bans** |
| Foreign Access | Relatively open; no investor registration | Open; Stock Connect for mainland | Open; FPI framework | QFI scheme + Stock Connect; direct access limited | FPI registration via custodians | FINI/FIDI registration required | Barrier-free since Feb 2026 (QFI abolished) | **QFI scheme (quota abolished); via licensed Korean broker-dealers** |
| Settlement Cycle | T+2 | T+2 | T+2 | T+1 (unique: cannot sell same-day purchase) | T+1 (since Jan 2023) | T+2 | T+2 | **T+2 (T+1 under study)** |

### 7.4 Africa & Middle East

| Item | South Africa (JSE) | Saudi Arabia (Tadawul) |
|------|-------------------|---------------------|
| Regulator | FSCA (market conduct) + SARB Prudential Authority | CMA |
| Key Regulation | Financial Markets Act 2012, FSR Act 2017 | Capital Market Law 2003 |
| SRO Model | JSE as frontline regulator (Twin Peaks model) | Saudi Exchange under CMA |
| Short Selling | Permitted with JSE/FSCA oversight | Limited |
| Foreign Access | Open via FSCA-licensed members | Barrier-free since Feb 2026 |
| Settlement Cycle | T+3 (JSE) | T+2 |

---

## 8. Market Size Rankings

### 8.1 By Market Capitalization (listed companies, approximate, as of early 2026)

| Rank | Exchange | Market Cap (USD, approx.) |
|------|---------|--------------------------|
| 1 | NYSE | ~$28.0 trillion |
| 2 | NASDAQ | ~$42.2 trillion (Nov 2025) |
| 3 | SSE | ~$8.9 trillion |
| 4 | JPX (TSE) | ~$8.1 trillion |
| 5 | HKEX | ~$6.2 trillion |
| 6 | Euronext (combined) | ~$7.5 trillion (EUR 6.8T) |
| 7 | LSE | ~$5.9 trillion |
| 8 | NSE India | ~$5.1 trillion |
| 9 | BSE India | ~$5.0 trillion |
| 10 | SZSE | ~$5.1 trillion |
| 11 | **KRX (KOSPI+KOSDAQ)** | **~$2.95 trillion (KRW 4,277T)** |
| 12 | TWSE | ~$2.9 trillion |
| 13 | Tadawul | ~$2.7 trillion |
| 14 | Deutsche Borse | ~$2.3 trillion (EUR 2.1T) |
| 15 | TMX (TSX) | ~$4.3 trillion (C$5.8T) |
| 16 | ASX | ~$2.2 trillion |
| 17 | Nasdaq Nordic | ~$2.2 trillion (EUR 2.0T) |
| 18 | SIX Swiss | ~$2.0 trillion (CHF 1.8T) |
| 19 | JSE | ~$1.5 trillion |
| 20 | BME (Spain) | ~$1.3 trillion (EUR 1.2T) |
| 21 | Borsa Italiana | ~$1.2 trillion (EUR 1.04T) |
| 22 | SGX | ~$0.8 trillion |
| 23 | Bursa Malaysia | ~$0.4 trillion |

*Note: Rankings are approximate and vary by date and methodology. NASDAQ's figure includes all listed companies; NYSE's figure covers NYSE-listed equities only. Euronext is an aggregate across 7 markets.*

### 8.2 By Average Daily Trading Value (approximate, 2025)

| Rank | Exchange | ADV (USD, approx.) |
|------|---------|-------------------|
| 1 | NASDAQ | ~$300-400 billion |
| 2 | NYSE | ~$80 billion |
| 3 | SSE | ~$50-100 billion (varies) |
| 4 | SZSE | ~$50-70 billion |
| 5 | JPX (TSE) | ~$45 billion (JPY 6.7T) |
| 6 | **KRX (KOSPI)** | **~$20.7 billion (KRW 32.2T, Feb 2026)** |
| 7 | HKEX | ~$30 billion (HK$230B) |
| 8 | Euronext (combined) | ~$13 billion (EUR 12B) |
| 9 | TWSE | ~$13 billion (NT$416B record) |
| 10 | NSE India | ~$8-9 billion |
| 11 | LSE | ~$5-6 billion (GBP 4-4.5B) |
| 12 | Deutsche Borse (Xetra) | ~$5-6 billion (EUR 4.5-5.5B) |
| 13 | TMX (TSX) | ~$5.5 billion (C$7.4B) |
| 14 | SIX Swiss | ~$4 billion (CHF 3.5B) |
| 15 | Nasdaq Nordic | ~$3.5 billion (EUR 3.2B) |
| 16 | ASX | ~$3.5 billion (AUD 4.7B) |
| 17 | Tadawul | ~$1.2 billion (SAR 4.6B) |
| 18 | SGX | ~$1.0 billion (SGD 1.3-1.8B) |
| 19 | Bursa Malaysia | ~$0.6 billion (RM 2.5-3B) |

### 8.3 By Number of Listed Companies (approximate, 2025-2026)

| Rank | Exchange | Listed Companies |
|------|---------|-----------------|
| 1 | BSE India | ~5,936 |
| 2 | TMX (TSX + TSXV) | ~3,400+ |
| 3 | JPX (TSE) | ~3,945 |
| 4 | NASDAQ | ~4,075 |
| 5 | Deutsche Borse (all segments) | ~3,500+ |
| 6 | SZSE | ~2,879 |
| 7 | **KRX (KOSPI+KOSDAQ+KONEX)** | **~2,901** |
| 8 | HKEX | ~2,673 |
| 9 | NYSE | ~2,400+ |
| 9 | SSE | ~2,302 |
| 10 | ASX | ~2,241 |
| 11 | Euronext (combined) | ~1,900+ |
| 12 | LSE | ~1,900+ |
| 13 | Nasdaq Nordic + Baltic | ~1,119 |
| 14 | TWSE | ~1,045 |
| 15 | Bursa Malaysia | ~1,051 |
| 16 | BME (Spain) | ~655 |
| 17 | SGX | ~622 |
| 18 | JSE | ~431 |
| 19 | Borsa Italiana | ~375+ |
| 20 | Tadawul | ~390+ |
| 21 | SIX Swiss | ~250+ |

---

## 9. Key Observations and Trends

### 9.1 Technology Convergence and Divergence

The global exchange landscape exhibits a clear technology stratification. At the top tier, Deutsche Borse T7 (~5 us), Nasdaq INET (~14 us), and Euronext Optiq (~15 us) deliver single-digit to low double-digit microsecond latencies. A second tier includes NYSE Pillar (~34 us), SGX REACH (sub-90 us), and Nasdaq-powered exchanges like Tadawul (<40 us) and SIX (~10.6 us). Notably, Chinese exchanges (SSE, SZSE) have diverged from the global technology ecosystem entirely, building proprietary systems aligned with national technology self-sufficiency mandates. This creates a bifurcated landscape: Western/global exchanges converging on a handful of platform families (Nasdaq INET, Millennium, Optiq, T7), while China's exchanges operate in a largely opaque, domestically developed environment.

### 9.2 Platform Consolidation

Nasdaq technology (across INET, Genium INET, and X-Stream INET variants) powers the most exchanges globally -- at least 8 of the 22 exchanges reviewed, plus 130+ other marketplaces. LSEG's Millennium Exchange powers at least 3 exchanges (LSE, JSE, and until recently Borsa Italiana). This concentration of exchange technology in a few vendors creates both efficiency (shared development costs, proven platforms) and systemic risk (a vulnerability in one platform could affect multiple markets simultaneously).

### 9.3 Market Structure Modernization

Several exchanges are undergoing significant market structure reforms:
- **TWSE** transitioned from call auction to continuous trading only in 2020, among the last major exchanges to do so
- **HKEX** is reducing tick sizes in phases (2025-2026), narrowing the gap with Western peers
- **JPX** extended trading hours and introduced a closing auction in 2024 (arrowhead 4.0)
- **ASX** unified its opening auction and introduced post-close trading in 2025 (SR15 reforms)
- **NSE India** is implementing the most aggressive tick size reform, moving from a uniform INR 0.05 to a 6-tier price-dependent structure

### 9.4 Settlement Cycle Acceleration

The global move toward shorter settlement is accelerating:
- **T+1 achieved:** US (May 2024), Canada (May 2024), India (Jan 2023), China (T+1 with unique same-day sale restriction)
- **T+1 planned:** EU (targeting 2027), UK (targeting 2027), Australia (post-CHESS replacement, likely 2029+)
- **T+2 standard:** Most of Europe, Japan, Hong Kong, Singapore, Australia, Saudi Arabia currently on T+2

### 9.5 Foreign Investor Liberalization

The trend toward barrier-free foreign investor access continues:
- **Tadawul** abolished the QFI regime entirely in February 2026, granting barrier-free access
- **China** expanded Stock Connect scope and abolished QFI quotas, though structural barriers (T+1, capital controls) remain
- **India** simplified FPI registration and expanded GIFT City international access
- **TWSE** has eliminated most foreign ownership limits (45% foreign ownership at end of 2024)

### 9.6 ESG and Sustainability Integration

ESG reporting and sustainability are becoming universal exchange requirements:
- **TWSE:** All 1,029 listed companies submitted sustainability reports by August 2025; ESG Evaluation system launched 2026
- **Tadawul:** Launched ESG Disclosure Guidelines (2021); 29 Unified ESG Metrics across GCC exchanges
- **HKEX:** Enhanced ESG reporting aligned with ISSB standards
- **Euronext:** Bergamo data center powered by green energy
- **LSEG:** Launched Sustainability Ratings and Data (March 2026)

### 9.7 24-Hour Trading Ambitions

Multiple exchanges are exploring extended or round-the-clock trading:
- **NASDAQ:** Plans for 24/5 trading (pending SEC approval, H2 2026 target)
- **NYSE Arca:** SEC approved 22-hour trading; implementation targeted late 2026
- **JSE:** Reported to be considering 24-hour trading (July 2025)
- This trend reflects the globalization of capital flows and competition from crypto markets that trade 24/7

---

## 10. KRX Positioning

Korea Exchange (KRX) serves as the reference benchmark for this research project. Based on the comparative analysis above, KRX's positioning relative to global peers can be characterized as follows:

### 10.1 Market Size
- **Market capitalization:** KRX KOSPI is approximately USD 1.6 trillion, placing it in the middle tier globally -- comparable to JSE (~$1.5T) and larger than BME, Borsa Italiana, or SGX, but smaller than TWSE (~$2.9T), Tadawul (~$2.7T), or ASX (~$2.2T)
- **Listed companies:** KOSPI + KOSDAQ combined total approximately 2,500+ companies, comparable to NYSE or HKEX

### 10.2 Trading System
- KRX operates the Exture+ trading system. Compared to global peers, its latency and capacity specifications should be benchmarked against:
  - **Top tier:** Deutsche Borse T7 (~5 us), Nasdaq INET (~14 us), Euronext Optiq (~15 us)
  - **Peer tier:** HKEX OTP-C (60K orders/sec), SGX REACH (sub-90 us), ASX Trade (100K+ orders/sec)

### 10.3 Market Structure
- **Trading hours:** KOSPI trades 09:00-15:30 KST (6.5 hours continuous, no lunch break since 2000), longer than TWSE (4.5 hrs), JPX (5.5 hrs), and SSE/SZSE (4 hrs), but shorter than SGX (7 hrs)
- **Daily price limits:** KRX uses +/-30% limits (since 2015), among the widest in Asia (vs. TWSE +/-10%, SSE/SZSE +/-10-20%, HKEX no daily limit)
- **Lot size:** KRX uses 1 share as the standard lot, aligned with global best practice
- **Circuit breakers:** KRX employs both stock-level Volatility Interruption (VI) and market-wide SAPI mechanisms, consistent with the dual-layer approach used by most sophisticated exchanges

### 10.4 Settlement and Access
- **Settlement:** T+2 (Korea is not yet on T+1, unlike the US, Canada, and India)
- **Foreign access:** Relatively open with foreign investor registration; foreign ownership limits apply per company. No Stock Connect-style mechanism exists, though MSCI EM inclusion has long been a goal (Korea remains in MSCI EM, with discussions about potential DM reclassification contingent on FX market reforms)

### 10.5 Regulatory Framework
- KRX operates under the Financial Services Commission (FSC) and Financial Supervisory Service (FSS), with KRX performing SRO functions -- a structure similar to JPX-R (Japan), SGX RegCo (Singapore), and JSE (South Africa)
- The regulatory framework is well-developed and IOSCO-aligned, comparable to other advanced Asian markets

### 10.6 Areas of Relative Strength
- Continuous trading without lunch break (eliminated in 2000, ahead of many Asian peers)
- Wide daily price limits (+/-30%) allowing efficient price discovery
- Strong derivatives market (world-class options volume)
- Well-developed electronic infrastructure

### 10.7 Areas for Potential Enhancement
- T+1 settlement adoption (behind US, Canada, India)
- MSCI DM reclassification (requires FX market liberalization)
- Extended trading hours consideration (23-hour trading trend)
- Enhanced international connectivity mechanisms (no Stock Connect equivalent)

---

## Sources

This comparative analysis is derived from detailed exchange research files covering 22 exchanges. Individual source citations are documented in each exchange file located in `/01_equities/en/exchanges/` and system files in `/01_equities/en/systems/`. Key regulatory analysis files are in `/01_equities/en/regulations/`.
