# LCH Clearing Platforms & Margin Engines

> **Last Updated:** 2026-04-07
> **System Category:** Clearing System

---

## 1. System Overview

| Item | Details |
|------|---------|
| System Name | LCH Clearing Platforms (multiple) |
| Operated By | LCH Ltd (London) / LCH SA (Paris), subsidiaries of LSEG |
| Purpose | CCP clearing, margin calculation, risk management, and settlement across multiple asset classes (OTC IRS, FX, repos, equities, CDS, energy, digital assets) |
| Launch Year | SwapClear: 1999; EquityClear MCCP: 2020; Collateral Management on AWS: 2025 |
| Current Version | Millennium Clearing & Risk (MCCP) for EquityClear; Murex MX.3 for SwapClear/SwapAgent; bespoke platforms for CDSClear, RepoClear |
| Vendor / In-house | Hybrid -- LSEG Technology (Millennium platform, in-house), Murex (MX.3 for OTC derivatives processing), proprietary risk engines (PAIRS), AWS/Azure cloud infrastructure |

### System Evolution

| Period | System / Milestone | Key Changes |
|--------|--------------------|-------------|
| 1999 | SwapClear launch | First CCP for OTC interest rate swaps; bespoke clearing platform |
| 2003 | LCH.Clearnet merger | Integration of London Clearing House and Paris-based Clearnet SA systems |
| 2009 | CDSClear launch | Dedicated CDS clearing platform built for LCH SA |
| ~2012 | ForexClear launch | NDF clearing platform with proprietary API connectivity |
| 2016-2020 | LSEG Technology MCCP rollout | Millennium Clearing & Risk platform developed; EquityClear went live March 2020 [Source: FinTech Futures, Finance Magnates] |
| ~2017 | SwapClear platform upgrade | Trade registration and margining platform upgraded; Murex MX.3 integration for SwapAgent [Source: Murex] |
| 2022 | LSEG-Microsoft 10-year partnership | Strategic partnership for cloud migration to Azure; Microsoft equity investment in LSEG [Source: Microsoft News] |
| 2024 | DigitalAssetClear launch (LCH SA) | New clearing service for digital asset derivatives (GFO-X partnership) |
| 2025 (Q2) | Collateral Management System migrated to AWS | First core LCH clearing service to run on public cloud; multi-region architecture with 2-hour RTO and zero RPO [Source: AWS re:Invent 2025, AWS Industries Blog] |
| 2025 | LSEG-AWS collaboration extended | AWS named preferred cloud provider for Markets, Risk Intelligence, and FTSE Russell divisions; multicloud strategy with 1,300+ AWS accounts [Source: LSEG Press Release] |

---

## 2. Architecture

### 2.1 High-Level Design

LCH operates a **heterogeneous, service-oriented architecture** in which each clearing service runs on a platform best suited to its asset class. The overall design is:

- **Hybrid cloud / on-premise:** Core clearing and risk engines remain on-premise in LCH data centers, with progressive migration of supporting services (collateral management, reporting, analytics) to public cloud (AWS primary, Azure for data/analytics).
- **Service-per-asset-class model:** Each clearing service (SwapClear, ForexClear, RepoClear, CDSClear, EquityClear, etc.) operates as a logically independent clearing unit with its own margin model, default fund, and technology stack, though sharing common infrastructure for connectivity, collateral management, and member portals.
- **Event-driven + batch hybrid:** Real-time trade registration, intraday margin monitoring, and position updates are event-driven; end-of-day margin recalculation, default fund resizing, and reporting use batch processing.
- **Straight-through processing (STP):** Near-100% STP for standard products with zero-touch automated workflows from trade submission through novation, margining, and settlement. [Source: LSEG Technology]

### 2.2 Core Components

#### SwapClear -- World's Largest OTC IRS Clearing Service

| Item | Details |
|------|---------|
| Asset Class | OTC interest rate derivatives (IRS, OIS, FRAs, basis swaps, zero-coupon swaps, inflation swaps) |
| Scope | 28 currencies; tenors up to 51 years in USD/GBP/EUR; dozens of benchmark rates |
| Market Share | ~95% of vanilla OTC IRS globally; 99.4% in EMEA [Source: Clarus FT] |
| Volume | $779 trillion notional cleared in H1 2024 (up 15% YoY); cumulative cleared > 65 million trades [Source: LSEG, Clarus FT] |
| Initial Margin Held | ~$240 billion (GBP 192 billion) as of Q4 2024 [Source: Clarus FT Q4 2024 PQD] |
| Technology Platform | Murex MX.3 for trade processing and valuation; manages peak volumes exceeding 30,000 trades/day [Source: Murex] |
| Margin Engine | **PAIRS** (Portfolio Approach to Interest Rate Scenarios) -- see Section 6 for deep-dive |
| Trade Registration | Real-time (~10 seconds from submission to novation); supported by dedicated GBP 600 million RTTR default fund component [Source: RBA Assessment 2020] |
| Operating Hours | 06:00 UK time to 19:00 New York time |
| Connectivity | ClearLink API (FpML-based) over MQ messaging; middleware integration via MarkitWire/OSTTRA |
| Compression | Proprietary compression + OSTTRA triReduce multilateral compression; cumulative compressed notional exceeds $7,000 trillion (>$1 quadrillion) [Source: LeapRate, Finance Magnates] |

#### ForexClear -- FX Derivatives Clearing

| Item | Details |
|------|---------|
| Asset Class | OTC FX derivatives: NDFs (25 currency pairs), NDOs (9 pairs), deliverable FX (spot, forwards, options -- 8 pairs) |
| Launch | 2012 |
| Initial Margin Held | $10.7 billion (Q2 2024 record, up 32% YoY) [Source: LCH ForexClear Factsheet] |
| Members | ~30 direct clearing members; 92 clients [Source: LCH ForexClear Factsheet] |
| Margin Engine | PAIRS (shared methodology with SwapClear, calibrated for FX risk factors) |
| Operating Hours | Trade registration 24 hours/day, 5.5 days/week |
| Connectivity | ForexClear API (proprietary); direct venue connectivity; trade submission via approved trade sources including 24 Exchange [Source: Securities Finance Times] |
| Settlement | Physical settlement via CLS for deliverable FX; cash variation margin via Protected Payments System (PPS) |
| Notable Feature | "FX Smart Clearing" in partnership with Quantile -- optimizes which trades to clear for maximum margin efficiency [Source: LSEG Press Release 2023] |

#### RepoClear -- Fixed Income Repo Clearing

| Item | Details |
|------|---------|
| Entities | RepoClear Ltd (London) -- UK gilts and other markets; RepoClear SA (Paris) -- 13 eurozone government bond markets |
| Asset Class | Repos, reverse repos, cash government bond trades |
| RepoClear SA IM | EUR 1.9 billion gross notional unsettled cash bonds (Q4 2024) [Source: Clarus FT] |
| Margin Engine | RepoClear SA uses a historical simulation-based margin model with volatility scaling (similar principles to PAIRS but calibrated for fixed income/repo risk) [Source: LCH SA Margin Model Overview, May 2024] |
| Settlement | T+0 to T+2 depending on instrument; DVP via CREST (UK), Euroclear, Clearstream |
| Connectivity | LCAP gateway (LCH SA); FIX protocol and proprietary messaging |

#### EquityClear -- Cash Equities & Equity Derivatives

| Item | Details |
|------|---------|
| Entity | EquityClear Ltd (London) |
| Asset Class | Cash equities for LSE, SIX Swiss Exchange, Cboe Europe, Aquis, and other European venues |
| Platform | **Millennium Clearing & Risk (MCCP)** -- LSEG Technology's flagship post-trade platform, live since March 2020 [Source: FinTech Futures] |
| Capacity | 20 million trades (40 million trade sides) per day; throughput of 1,600 trades/second [Source: LSEG Technology] |
| Peak Volume | Nearly 80 million trade sides cleared in first 5 days of operation (March 2020, COVID market volatility) [Source: FinanceFeeds] |
| Venues Connected | 16 trading venues |
| CSD Connections | 19 depositories across Europe |
| Participants | ~250 global participants |
| Operating Hours | 24x6.5 |
| Interoperability | Interoperable with SIX x-clear and Cboe Clear Europe |
| Key Technology | GPU-accelerated parallel real-time risk processing; zero-touch STP; trade-by-trade exposure and margin recalculation [Source: LSEG Technology, WatersTechnology AFTAs 2020] |
| Impact | Significantly reduced end-of-day processing time compared to predecessor platform [Source: Securities Finance Times] |

#### CDSClear -- Credit Default Swaps

| Item | Details |
|------|---------|
| Entity | LCH SA (Paris) |
| Asset Class | CDS indices (iTraxx, CDX) and single-name CDS |
| Members | 28 members (20 GCMs) as of 2024 [Source: Risk.net] |
| Volume | EUR 5,437 billion total notional cleared in 2024 (up 9% YoY); client notional EUR 426 billion in H1 2024 (up 88%) [Source: Risk.net] |
| Initial Margin Held | ~$10.2 billion (EUR 9.8 billion) Q4 2024 [Source: Clarus FT Q4 2024] |
| Margin Engine | Historical simulation with scaled returns; Expected Shortfall at 99.7% confidence; 5-day holding period; lookback from April 2007 (includes GFC) [Source: LCH SA CDSClear Risk Management] |
| Connectivity | ClearLink API; CDSClear PMC and Reporting API; LCAP access gateway supporting MMTP (real-time) and SFTP (file) protocols [Source: LCH SA Connectivity Guide] |
| Settlement | Cash-settled variation margin daily; credit event settlement per ISDA protocols |

#### EnClear -- Energy & Commodities (Historical / Limited)

| Item | Details |
|------|---------|
| Divisions | Energy Division, Freight Division, Precious Metals Division |
| Energy Products | OTC emissions spot/forward/options (EUA, CER contracts); OTC power transactions (Dutch electricity via Endex) [Source: Global Custodian] |
| Freight Products | Forward Freight Agreements (FFAs), Container Freight Swaps, iron ore swaps, steel swaps, fertilizer swaps, coal swaps/options |
| Status | Largely wound down or transferred following Euronext migration; LCH SA closed CommodityClear in 2024; remaining energy/commodity clearing minimal [Source: Euronext Press Release 2024] |

#### DigitalAssetClear (LCH SA) -- New 2024

| Item | Details |
|------|---------|
| Asset Class | Bitcoin index futures and options |
| Partner | GFO-X (regulated digital asset derivatives exchange) |
| Launch | 2024 |
| Status | Early stage; replaces former EquityClear SA/CommodityClear SA capacity at LCH SA |
| Connectivity | LCAP gateway [Source: LCH SA Connectivity Guide] |

#### PAIRS Margin Engine

See Section 6 for full technical deep-dive. Summary:

| Item | Details |
|------|---------|
| Full Name | Portfolio Approach to Interest Rate Scenarios |
| Applied To | SwapClear, ForexClear, Listed Rates |
| Model Type | Expected Shortfall (ES) based on filtered historical simulation with EWMA volatility scaling |
| Confidence Level | 99.7% |
| Holding Period | 5 days (members); 7 days (clients) |
| Lookback | 10 years of daily market data |
| Anti-procyclicality Floor | Unscaled 10-year lookback + 2.5-year GFC window (2007-2009) |

#### SPAN-like Models for Listed Derivatives

| Item | Details |
|------|---------|
| Applied To | Listed Rates (FMX SOFR futures and options cleared by LCH Ltd) |
| Approach | PAIRS methodology extended to listed interest rate derivatives; portfolio margining between listed futures and OTC IRS positions [Source: Coalition Greenwich] |
| Portfolio Margining | LCH's Portfolio Margining Service allows cross-margining between FMX Futures Exchange listed positions and SwapClear IRS portfolios; first client enabled September 2025 via Marex [Source: Marex Press Release] |

### 2.3 Technology Stack

| Layer | Technology | Details |
|-------|-----------|---------|
| Programming Languages | Java (primary), C++ (performance-critical components) | Java Spring Boot for services; C++ for matching and risk engines [Source: AWS re:Invent 2025; unverified for specific LCH components] |
| Clearing Platform | Millennium Clearing & Risk (MCCP) | LSEG Technology in-house platform; GPU-accelerated risk computations [Source: LSEG Technology] |
| OTC Derivatives Processing | Murex MX.3 | Trade processing, valuation, and margining for SwapClear and SwapAgent [Source: Murex] |
| Risk Engine | PAIRS (proprietary) | In-house developed Expected Shortfall engine |
| Cloud Infrastructure (Primary) | AWS | Amazon EKS (containers), Oracle RDS (database), S3 (storage), FSx for NetApp ONTAP (file systems); multi-region deployment [Source: AWS re:Invent 2025] |
| Cloud Infrastructure (Analytics) | Microsoft Azure | Synapse, Fabric, Purview for data analytics; Copilot integration; part of 10-year LSEG-Microsoft partnership [Source: Microsoft News] |
| Private Cloud | Dell Technologies | Private cloud platform build-out for on-premise workloads [Source: The TRADE] |
| Infrastructure as Code | Terraform | Standardized IaC with verified modules for security/policy compliance [Source: AWS re:Invent 2025] |
| Containerization | Amazon EKS (Kubernetes) | Containerized microservices for cloud-migrated components |
| Database | Oracle (RDS and EC2) | Primary database for clearing and collateral systems |
| Messaging / Middleware | IBM MQ, FpML (ClearLink) | MQ for ClearLink API connectivity; FpML messaging standard for OTC trade submission |
| Network Connectivity | CMC (Customer Managed Connectivity) | Secure IP network between CMC City PoPs and LCH Data Centres; members connect via dedicated "Last Mile" connections [Source: LCH SA Connectivity Guide] |
| Member Portal | Web-based (SSO) | Single sign-on portal with parameterized applications per user permissions |

---

## 3. Performance Specifications

| Metric | Value | Conditions / Service |
|--------|-------|---------------------|
| EquityClear Daily Capacity | 20 million trades (40 million trade sides) | MCCP platform [Source: LSEG Technology] |
| EquityClear Throughput | 1,600 trades/second | Sustained throughput [Source: LSEG Technology] |
| EquityClear Peak (Actual) | ~16 million trade sides/day | First week of operation (March 2020, COVID volatility) |
| SwapClear Trade Registration | ~10 seconds (submission to novation) | Real-time trade registration [Source: RBA Assessment 2020] |
| SwapClear Daily Volume | 30,000+ trades/day peak | Via Murex MX.3 platform [Source: Murex] |
| SwapClear H1 2024 Volume | $779 trillion notional | Record half-year volume [Source: Clarus FT] |
| Margin Calculation Frequency | Real-time (intraday) + full EOD recalculation | All services |
| Collateral Management RTO | 2 hours | AWS multi-region architecture [Source: AWS re:Invent 2025] |
| Collateral Management RPO | Zero data loss | Multi-AZ replication [Source: AWS re:Invent 2025] |
| Uptime SLA | 99.9%+ [unverified] | PFMI-compliant; systemically important infrastructure |
| Operating Hours (EquityClear) | 24x6.5 | Covering global equity markets |
| Operating Hours (SwapClear) | 06:00 UK to 19:00 NY | ~13 hours daily |
| Operating Hours (ForexClear) | 24x5.5 | Trade registration |

### Performance History

| Year | Event | Impact |
|------|-------|--------|
| 2008 | Lehman Brothers default | $9 trillion IRS portfolio (66,390 trades) managed using only 35% of initial margin; no default fund losses [Source: LSEG SwapClear Risk Management] |
| 2020 (Mar) | COVID-19 market volatility | EquityClear MCCP processed ~80 million trade sides in first 5 days of live operation; system performed without incident [Source: FinanceFeeds] |
| 2024 (H1) | Record SwapClear volumes | $779 trillion notional cleared, up 15% YoY [Source: Clarus FT] |

---

## 4. Interfaces & Protocols

### 4.1 Clearing Connectivity

| Interface | Protocol / Technology | Services | Description |
|-----------|----------------------|----------|-------------|
| **ClearLink API** | FpML over IBM MQ | SwapClear, ForexClear, CDSClear | Primary interface for OTC trade submission, clearing acceptance, and real-time status updates; based on Financial products Markup Language (FpML) industry standard [Source: LCH ClearLink Overview] |
| **ForexClear API** | Proprietary | ForexClear | Direct connectivity for FX trade submission and clearing notifications |
| **CDSClear PMC API** | Proprietary | CDSClear | Portfolio Management and Certification; reporting API with LCH Portal security model |
| **LCAP Gateway** | MMTP (real-time) / SFTP (file) | LCH SA services (CDSClear, RepoClear SA, DigitalAssetClear) | Access server supporting real-time messaging and file-based data exchange; compresses and stores data in transit [Source: LCH SA Connectivity Guide] |
| **FIX Protocol** | FIX 4.x / 5.0 | Exchange-traded products (EquityClear, Listed Rates) | Standard protocol for trade submission from trading venues |
| **CMC Network** | Secure IP (dedicated) | All services | Customer Managed Connectivity -- secure network between CMC City PoPs and LCH Data Centres with dedicated "Last Mile" member connections [Source: LCH SA Connectivity Guide] |
| **MarkitWire / OSTTRA** | Middleware | SwapClear, ForexClear | Trade affirmation, matching, and routing for OTC derivatives |
| **Tradeweb STP** | Direct venue connection | SwapClear | Straight-through processing from Tradeweb execution to LCH clearing [Source: LSEG] |

### 4.2 Market Data Feeds

| Feed | Description |
|------|-------------|
| End-of-Day Prices | LCH publishes EOD settlement prices, yield curves, and zero-coupon curves used for margin and valuation |
| Intraday Risk Data | Real-time risk analytics available to members via portal and API |
| Curve Data | Yield curves, discount curves, and FX rates used in PAIRS model published to members |

### 4.3 Member Portal / Reporting

| Feature | Description |
|---------|-------------|
| **LCH Member Portal** | Web-based single sign-on (SSO) platform; parameterized access per user role/permissions [Source: LCH SA Connectivity Guide] |
| Position Reports | Real-time and EOD position, trade, and margin reports |
| Margin Calculators | LCH Rates Online Margin Calculator (SwapClear pre-trade IM estimation); CDSClear Margin Simulator [Source: LCH Margin Calculator PDF] |
| File Delivery | SFTP-based report delivery for batch/EOD files |
| Risk Analytics | Member-level risk dashboards, stress test results, what-if analysis |

### 4.4 SWIFT / FIX / Proprietary Protocols

| Protocol | Use Case |
|----------|----------|
| **SWIFT FIN / ISO 15022** | Collateral management instructions, settlement messages, payment messaging |
| **ISO 20022** | Collateral management -- LCH was an early adopter of ISO 20022 for collateral workflows [Source: SWIFT] |
| **FIX Protocol** | Trade submission for exchange-traded products; venue connectivity |
| **FpML** | OTC derivative trade messaging via ClearLink API |
| **MMTP** | Real-time messaging protocol for LCH SA services (via LCAP) |
| **SFTP** | Batch file delivery (reports, positions, margin data) |

---

## 5. Resilience & Business Continuity

### 5.1 Redundancy

| Item | Details |
|------|---------|
| On-premise Architecture | Active data centers with geographically separated disaster recovery sites for both LCH Ltd and LCH SA [Source: standard for PFMI-compliant systemically important CCPs] |
| Cloud Architecture (Collateral Mgmt) | Multi-region AWS deployment: primary region with 3 availability zones; secondary region for data replication (DR); tertiary environment on AWS Outposts capable of independent operation for up to 5 days [Source: AWS re:Invent 2025] |
| Network Redundancy | CMC network with multiple City PoPs providing redundant connectivity paths |
| EquityClear | Connects to 16 trading venues and 19 depositories; designed for continuous operation 24x6.5 |

### 5.2 Disaster Recovery

| Parameter | Specification |
|-----------|--------------|
| RTO (Recovery Time Objective) | **2 hours** for critical clearing and collateral systems (confirmed for Collateral Management System on AWS) [Source: AWS re:Invent 2025] |
| RPO (Recovery Point Objective) | **Zero data loss** -- multi-AZ and multi-region replication ensures no transaction data is lost [Source: AWS re:Invent 2025] |
| DR Site | Geographically separate from primary; for cloud-migrated services, secondary AWS region + AWS Outposts tertiary site [Source: AWS re:Invent 2025] |
| Independent Operation | Tertiary AWS Outposts environment can operate independently for up to 5 days in case of full cloud region failure [Source: AWS re:Invent 2025] |
| Testing | Regular DR testing with clearing members; BCP exercises covering pandemic, cyber-incident, and physical disruption scenarios |
| Regulatory Framework | Subject to Bank of England CBEST (UK cyber resilience testing) and ECB/Eurosystem cyber resilience frameworks |

### 5.3 Capacity Management

| Item | Details |
|------|---------|
| EquityClear Capacity | 20 million trades/day baseline; demonstrated ability to handle ~16 million trade sides/day under stress (March 2020) [Source: LSEG Technology, FinanceFeeds] |
| SwapClear Scalability | Murex MX.3 platform manages peak volumes exceeding 30,000 trades/day and has supported SwapClear's growth as volumes scaled globally [Source: Murex] |
| Cloud Scalability | Containerized cluster pods on Amazon EKS for elastic scaling; multi-AZ RDS for database resilience [Source: AWS re:Invent 2025] |
| Stress Capacity | LSEG's Autex Trade Route (trading network) successfully absorbed a 400% volume surge with zero incidents after Azure migration [Source: Microsoft; applies to LSEG broadly, not LCH-specific] |
| Load Testing | Regular capacity and performance testing as part of PFMI compliance; member connectivity testing |

---

## 6. Notable Technical Features

### 6.1 PAIRS Margin Methodology -- Technical Deep-Dive

**PAIRS (Portfolio Approach to Interest Rate Scenarios)** is LCH's proprietary margin model, used for SwapClear, ForexClear, and Listed Rates. It is one of the most sophisticated CCP margin models in the world, managing over $240 billion in initial margin.

#### Model Architecture

| Component | Specification |
|-----------|--------------|
| **Model Type** | Expected Shortfall (ES) based on filtered historical simulation with volatility scaling |
| **Confidence Level** | 99.7% (equivalent to ~2.75 standard deviations under normal distribution) |
| **Holding Period** | 5 days for clearing members; 7 days for clients (5 + 2 days for portfolio transfer) |
| **Lookback Period** | 10 years of daily historical market data |
| **Risk Factors** | Yield curves (by currency and tenor), FX rates, credit spreads (depending on service), inflation rates |
| **Volatility Model** | EWMA (Exponentially Weighted Moving Average) for volatility scaling of historical returns |

#### Calculation Process (Step-by-Step)

1. **Data Collection:** Collects 10 years of daily market data including yield curve movements, FX rate changes, and other relevant risk factors.

2. **Volatility Scaling:** Applies EWMA-based volatility scaling to historical returns. This is the "filtered" component -- historical scenarios are scaled to reflect current market volatility conditions. When current volatility is high, historical returns are amplified; when low, they are dampened. This makes the model responsive to changing market conditions.

3. **Scenario Generation:** Generates a distribution of simulated portfolio P&L changes by revaluing the portfolio under each volatility-scaled historical scenario over the holding period (5 or 7 days).

4. **Expected Shortfall Calculation:** Calculates ES at the 99.7% confidence level -- this is the expected loss conditional on losses exceeding the 99.7% VaR threshold. ES (unlike VaR) accounts for "fat tail" risk by averaging all losses beyond the threshold, making it more conservative.

5. **Initial Margin Determination:** The initial margin is set as the ES figure, subject to a floor.

[Source: RBA Assessment 2020 Appendix B; LCH Ltd Margin Methodology page; Clarus FT]

#### Anti-Procyclicality Floor

To prevent margin requirements from falling too low during periods of calm markets (and then spiking during stress, creating procyclical liquidity demands):

- LCH imposes a **floor** on initial margin based on an **unscaled** historical 10-year lookback **plus an additional 2.5-year window** specifically covering the Global Financial Crisis (2007-2009).
- This ensures that even when current volatility is very low, the floor captures GFC-level stress scenarios without volatility dampening.

[Source: RBA Assessment 2020 Appendix B]

#### Margin Add-ons

| Add-on | Purpose |
|--------|---------|
| **Credit Risk Add-on** | Captures credit exposure not fully reflected in base PAIRS model |
| **Liquidity Risk Add-on** | Accounts for potential costs of liquidating large or concentrated positions |
| **Concentration Risk Add-on** | Penalizes disproportionately large positions in specific tenors or currencies |
| **Stress Margin Add-on** | Discretionary add-on during periods of elevated market stress |
| **Wrong-way Risk Add-on** | Applied where a member's default risk is correlated with its portfolio risk [unverified] |

[Source: RBA Assessment 2020 Appendix B]

#### CDSClear Margin Model (LCH SA)

| Parameter | Specification |
|-----------|--------------|
| Model Type | Historical simulation with scaled returns; Expected Shortfall methodology |
| Confidence Level | 99.7% |
| Holding Period | 5 days |
| Lookback Period | From April 2007 (includes GFC period) |
| Risk Factors | CDS spread changes, recovery rate changes, jump-to-default risk |

[Source: LCH SA CDSClear Risk Management]

#### RepoClear SA Margin Model

- Historical simulation-based margin model with volatility scaling, calibrated for fixed income and repo-specific risk factors (interest rate risk, credit spread risk, settlement risk).
- Published margin model overview updated May 2024.

[Source: LCH SA Margin Model Overview, May 2024]

### 6.2 Portfolio Margining Across Asset Classes

LCH's **Portfolio Margining Service** is a key competitive differentiator, allowing cross-margining between:

- **Listed interest rate futures** (FMX SOFR futures) and **OTC IRS** (SwapClear)
- This recognizes offsetting risk across exchange-traded and OTC positions, producing significant capital efficiencies

Key milestones:
- **September 2025:** Marex became the first clearing firm to enable client access to portfolio margining benefits between FMX Futures Exchange and LCH Ltd positions [Source: Marex Press Release]
- The service is fully automated and reduces counterparty risk while providing margin savings

[Source: Coalition Greenwich; Marex]

### 6.3 Compression Services (Notional Reduction)

LCH operates one of the world's most impactful portfolio compression programs, critical for managing the enormous gross notional outstanding in OTC IRS markets.

| Metric | Value |
|--------|-------|
| Cumulative Compressed Notional (SwapClear) | > $7,000 trillion (over $1 quadrillion) [Source: LeapRate, Finance Magnates] |
| 2015 Single-Year Example | $323 trillion in trades compressed; $107 trillion net notional reduction [Source: LCH Compression page] |
| OSTTRA triReduce Monthly Record | ~$1 trillion additional gross notional reduction in September 2022 [Source: OSTTRA] |

**Compression Techniques:**
- **Proprietary bilateral compression:** Members can cancel or offset trades within their own portfolios within defined risk parameters
- **Multilateral compression (OSTTRA triReduce):** Cross-member compression cycles eliminate offsetting trades across multiple counterparties
- **Blended rate compression:** Combines multiple trades with different rates into fewer trades
- **Future cash flow netting:** Eliminates redundant cash flows across trades
- **Eligible products:** IRS, OIS, FRAs, basis swaps, zero-coupon inflation swaps

**ForexClear Compression:** Also available for FX NDF portfolios, reducing trade counts and notional values. [Source: LCH ForexClear Compression Factsheet]

### 6.4 Cloud Migration Initiatives

LSEG is undertaking a major multi-year cloud transformation affecting LCH systems:

| Initiative | Details |
|-----------|---------|
| **LSEG-Microsoft Partnership** | 10-year strategic partnership (announced Dec 2022); LSEG data platform migrating to Azure; Microsoft made equity investment in LSEG [Source: Microsoft News] |
| **LSEG-AWS Collaboration** | Multi-year collaboration extended in 2025; AWS named preferred cloud provider for Markets division (including LCH); 1,300+ AWS accounts across LSEG [Source: LSEG Press Release] |
| **LCH Collateral Management on AWS** | Core Collateral Management Service migrated to AWS in Q2 2025; first LCH clearing service on public cloud [Source: AWS re:Invent 2025] |
| **Architecture Pattern** | Multi-region: Primary (EKS + Oracle RDS + S3 + FSx), Secondary (DR replication), Tertiary (AWS Outposts, independent for 5 days) [Source: AWS re:Invent 2025] |
| **Dell Private Cloud** | Private cloud platform build-out via multi-year Dell Technologies collaboration for on-premise workloads [Source: The TRADE] |
| **Multicloud Strategy** | AWS (primary for clearing infrastructure), Azure (data/analytics, Workspace), GCP (selected workloads); hybrid model with significant on-premise footprint remaining [Source: AWS re:Invent 2025] |

### 6.5 Real-Time Risk Management Capabilities

- **Intraday margin monitoring:** Automated margin calls triggered when combined margin liability exceeds participant-specific credit thresholds
- **Trade-by-trade risk assessment:** EquityClear MCCP calculates exposure and margin changes on every individual trade (GPU-accelerated)
- **Real-time trade registration:** SwapClear novation within ~10 seconds of submission
- **Cover 2 stress testing:** Default fund sized to cover simultaneous default of two largest participants under extreme but plausible scenarios; stress tests run daily
- **Back-testing:** Daily and monthly back-testing of margin model performance against actual market moves

---

## 7. Comparison Notes

### vs. KRX/KSD Systems

| Aspect | LCH Systems | KRX/KSD Equivalent |
|--------|------------|-------------------|
| **CCP Operator** | LCH Ltd (UK) + LCH SA (France); owned by LSEG | KRX acts as CCP for its own markets; KSD (Korea Securities Depository) handles settlement |
| **Clearing System Provider** | LSEG Technology (Millennium), Murex, proprietary | KOSCOM provides IT infrastructure for all KRX clearing, settlement, and trading systems [Source: KOSCOM] |
| **Margin Methodology** | PAIRS (Expected Shortfall, filtered historical simulation, 99.7%, 10-year lookback) | EWMA-based VaR model; intraday margin calls introduced; SPAN-like methodology for derivatives [Source: IMF FSAP Korea 2014] |
| **Asset Class Coverage** | Multi-asset across separate services: OTC IRS, FX, repos, equities, CDS, digital assets | Integrated: equities (KOSPI, KOSDAQ), derivatives (KOSPI 200 options/futures, single stock futures, etc.), bonds, KONEX |
| **Architecture** | Heterogeneous -- different platforms per asset class; hybrid cloud + on-premise | Unified -- single KOSCOM-operated platform covering all KRX markets |
| **Cloud Adoption** | Active migration to AWS/Azure; Collateral Management on AWS since Q2 2025 | Primarily on-premise; KOSCOM data center [unverified -- limited public information on cloud strategy] |
| **OTC Clearing** | World's largest OTC IRS CCP ($240B IM); dedicated OTC services | KRX OTC CCP function launched more recently; smaller scale [Source: WFE article "A Milestone for Global Market Infrastructure in Seoul"] |
| **Compression** | Cumulative >$1 quadrillion compressed; critical for OTC IRS market structure | Not applicable at comparable scale (smaller OTC clearing volume) |
| **Portfolio Margining** | Cross-asset margining between listed futures and OTC IRS | Limited to within-market netting [unverified] |
| **Default Fund Size** | SwapClear: ~GBP 6 billion total; CDSClear: ~EUR 2.8 billion | Joint compensation fund + settlement reserves; significantly smaller in absolute terms [Source: IMF FSAP Korea] |
| **GPU Acceleration** | EquityClear MCCP uses GPU-accelerated parallel risk processing | Not publicly documented for KRX/KOSCOM systems |
| **Interoperability** | CCP interop with SIX x-clear, Cboe Clear Europe | Eurex-KRX link (cross-listing of KOSPI 200 options) [Source: Eurex] |

### Key Differentiators

1. **Scale in OTC clearing:** LCH SwapClear is the dominant global IRS CCP with ~95% market share and $240 billion in initial margin -- an order of magnitude larger than any other single CCP margin pool. KRX operates primarily in exchange-traded products.

2. **Multi-entity, multi-jurisdiction structure:** LCH operates across two legal entities (LCH Ltd, LCH SA) under different regulatory regimes (UK, EU), with QCCP recognition in 10+ jurisdictions. KRX operates as a single CCP within Korea's regulatory framework.

3. **PAIRS methodology sophistication:** The filtered historical simulation with EWMA volatility scaling, 99.7% ES confidence level, and anti-procyclicality floor represents a more complex margin approach than standard SPAN or VaR models typically used for exchange-traded products.

4. **Compression as systemic infrastructure:** LCH's compression services are a critical component of global OTC derivatives market infrastructure, having reduced over $1 quadrillion in gross notional. This function has no equivalent in exchange-traded markets.

5. **Cloud-first trajectory:** LSEG's multicloud strategy (AWS + Azure + private cloud) with core clearing services migrating to public cloud represents an industry-leading approach. Most Asian exchange groups, including KRX/KOSCOM, maintain primarily on-premise infrastructure.

6. **Cross-asset portfolio margining:** The ability to cross-margin between OTC IRS and listed futures is a significant competitive advantage for LCH, enabling capital efficiencies that single-asset CCPs cannot offer.

---

## Sources

1. [LSEG -- LCH Clearing Services](https://www.lseg.com/en/post-trade/clearing)
2. [LCH Ltd Margin Methodology (PAIRS)](https://www.lseg.com/en/post-trade/clearing/risk-management/ltd-risk-management/ltd-margin-methodology)
3. [LCH SA Margin Methodology](https://www.lseg.com/en/post-trade/clearing/risk-management/sa-risk-management/sa-margin-methodology)
4. [RBA Assessment of LCH Ltd SwapClear -- Appendix B (2020)](https://www.rba.gov.au/payments-and-infrastructure/financial-market-infrastructure/clearing-and-settlement-facilities/assessments/lch/2020/appendix-b.html)
5. [Clarus FT -- 2024 CCP Volumes and Share in IRD](https://www.clarusft.com/2024-ccp-volumes-and-share-in-ird/)
6. [Clarus FT -- What's New in CCP Disclosures Q4 2024](https://www.clarusft.com/whats-new-in-ccp-disclosures-4q24/)
7. [FinTech Futures -- LCH Implements Clearing and Settlement Solution from LSEG Technology](https://www.fintechfutures.com/fintech-innovation/lch-implements-clearing-and-settlement-solution-from-lseg-technology)
8. [FinanceFeeds -- LSEG Technology Implements New Clearing Platform for LCH EquityClear](https://financefeeds.com/lseg-technology-implements-new-clearing-platform-lchs-equityclear-service/)
9. [Murex -- LCH SwapAgent Implements Murex](https://www.murex.com/en/news/lch-swapagent-implements-murex)
10. [LCH ClearLink Overview (PDF)](https://www.lseg.com/content/dam/post-trade/en_us/documents/lch/resources/lch-swapclear-clearlink.pdf)
11. [LCH SA Connectivity Guide (PDF)](https://www.lseg.com/content/dam/post-trade/en_us/documents/lch/resources/lch-sa-connectivity-guide.pdf)
12. [Microsoft -- LSEG and Microsoft Launch 10-Year Strategic Partnership (Dec 2022)](https://news.microsoft.com/source/2022/12/12/lseg-and-microsoft-launch-10-year-strategic-partnership-for-next-generation-data-and-analytics-and-cloud-infrastructure-solutions-microsoft-to-make-equity-investment-in-lseg-through-acquisition-of-sh/)
13. [LSEG -- Extends Multi-Year Cloud Collaboration with AWS (2025)](https://www.lseg.com/en/media-centre/press-releases/2025/lseg-extends-multi-year-cloud-collaboration-with-aws)
14. [AWS re:Invent 2025 -- LSEG's Migration & Modernization Journey (MAM206)](https://dev.to/kazuya_dev/aws-reinvent-2025-lsegs-migration-modernization-journey-blueprint-for-cloud-success-mam206-ipm)
15. [AWS Industries Blog -- Cloud Adoption Update for FMI Providers 1H25](https://aws.amazon.com/blogs/industries/cloud-adoption-update-for-financial-market-infrastructure-providers-1h25/)
16. [Risk.net -- Clearing House of the Year: LCH (2024)](https://www.risk.net/awards/7960370/clearing-house-of-the-year-lch)
17. [LeapRate -- LCH SwapClear Compresses Over $1 Quadrillion](https://www.leaprate.com/news/lchs-swapclear-compresses-more-than-1-quadrillion-of-cleared-notional/)
18. [OSTTRA -- Trade Refactoring Unlocks Additional Compression Benefits](https://osttra.com/articles/trade-refactoring-unlocks-additional-compression-benefits/)
19. [Coalition Greenwich -- Portfolio Margining Imperative for Interest-Rate Derivatives](https://www.greenwich.com/market-structure-technology/portfolio-margining-imperative-interest-rate-derivatives)
20. [Marex -- First Clearing Firm to Enable Client Access to Margin Benefits with FMX and LCH (2025)](https://www.marex.com/news/2025/10/marex-first-clearing-firm-to-enable-client-access-to-competitive-margin-benefits-with-fmx-futures-exchange-and-lch-ltd/)
21. [WatersTechnology -- AFTAs 2020: Best New Technology -- LSEG Technology](https://www.waterstechnology.com/awards-rankings/7732176/aftas-2020-best-new-technology-introduced-over-the-last-12-months-trading-and-risk-lseg-technology)
22. [LCH ForexClear Factsheet (PDF)](https://www.lseg.com/content/dam/post-trade/en_us/documents/lch/fact-sheets/lch-forexclear-factsheet-a-global-leader.pdf)
23. [LCH SA Margin Model Overview (May 2024, PDF)](https://www.lseg.com/content/dam/post-trade/en_us/documents/lch/resources/margin-model-overview-may-2024.pdf)
24. [KOSCOM -- KRX Trading System](https://www.koscom.co.kr/eng/main/contents.do?menuNo=300005)
25. [IMF -- Republic of Korea FSAP 2014](https://www.imf.org/external/pubs/ft/scr/2014/cr14308.pdf)
26. [WFE -- A Milestone for Global Market Infrastructure in Seoul (KRX Clearing)](https://focus.world-exchanges.org/articles/krx-clearing)
27. [Eurex -- Eurex/KRX Link](https://www.eurex.com/ec-en/clear/eurex-krx-link)
28. [The TRADE -- LSEG Embarks on Private Cloud Platform Build with Dell Technologies](https://www.thetradenews.com/lseg-embarks-on-private-cloud-platform-build-out-through-multi-year-dell-technologies-collaboration/)
29. [Euromoney -- World's Best FX Clearing Venue 2025: LSEG FX and LCH ForexClear](https://www.euromoney.com/article/bbou8wzfesgg4g00c08gws0g8/awards/foreign-exchange-awards/the-worlds-best-fx-clearing-and-settlement-venue-2025-lseg-fx-and-lch-forexclear/)
30. [SWIFT -- ISO 20022 and LCH Collateral Management](https://www.swift.com/swift-resource/15021/download)
