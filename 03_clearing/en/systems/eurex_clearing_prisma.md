# Eurex Clearing -- C7 Architecture & PRISMA Margin Engine

> **Last Updated:** 2026-04-07
> **System Category:** Clearing System

---

## 1. System Overview

| Item | Details |
|------|---------|
| System Name | C7 / Eurex Clearing Prisma |
| Operated By | Eurex Clearing AG (Deutsche Borse Group) |
| Purpose | CCP clearing, post-trade processing, and portfolio-based risk management / margining |
| Launch Year | C7: phased rollout from ~2017 (derivatives) through 2021 (securities); Prisma: 2012 |
| Current Version | C7 Release 11.1+ (derivatives clearing); C7 CAS Release 2.293; Prisma Release 15.0 |
| Vendor / In-house | In-house (Deutsche Borse Group), with TCS (Tata Consultancy Services) as technology partner for C7 SCS modernization |

### System Evolution

| Period | System Name | Key Changes |
|--------|-------------|-------------|
| Pre-2012 | Eurex Clearing Classic | Monolithic legacy clearing system; product-by-product margining (Risk-Based Margining) |
| 2012 | Prisma Launch | Introduction of portfolio-based margining using Filtered Historical Simulation (FHS) VaR; initially for listed derivatives |
| 2012-2017 | Prisma expansion | Extension to OTC IRS (EurexOTC Clear), cross-margining between listed FI and OTC IRS within PFI01 liquidation group |
| ~2017 onwards | C7 Core | Next-generation clearing architecture replacing Eurex Clearing Classic; phased migration of derivatives clearing |
| 2021 | C7 SCS Launch | C7 Securities Clearing Service goes live (September 2021) for cash market clearing (Xetra, XFRA) |
| 2022-2025 | C7 CAS | C7 Client Administration Service rollout; multiple releases for member administration and reporting |
| 2025 | C7 Release 11.1 | Total Return Futures strategy, negative trade/settlement prices, cross-product margining for US FCM clients (May 2025) |
| 2025 | Prisma Bonds | Prisma methodology extended to bonds and repos; mandatory migration from Risk-Based Margining from 8 December 2025 |
| 2025 | Prisma Release 15.0 | Annual recalibration of margin floors effective 16 June 2025; margin concentration add-on for OTC IRS portfolios |
| 2026 | Ongoing | Further clearing architecture advances, regulatory compliance (EMIR 3.0), secured funding enhancements |

[Source: [Eurex C7 Releases](https://www.eurex.com/ec-en/support/initiatives/c7-releases); [Eurex Clearing Prisma](https://www.eurex.com/ec-en/services/margining/eurex-clearing-prisma); [C7 Introduction Circular](https://www.eurex.com/ec-en/find/circulars/Introduction-of-C7-Eurex-Clearing-s-new-clearing-architecture-Information-on-scope-and-timeline-213474); [Prisma Bonds Circular](https://www.eurex.com/ec-en/find/circulars/clearing-circular-4609908)]

---

## 2. Architecture

### 2.1 High-Level Design

The Eurex Clearing technology ecosystem is composed of several distinct but integrated platforms:

```
+--------------------------------------------------------------+
|                  Eurex Clearing Infrastructure                |
|                                                               |
|  +------------------+   +-------------------+                 |
|  |   C7 Core        |   |  EurexOTC Clear   |                |
|  |  (Derivatives     |   |  (OTC IRS/NDF     |                |
|  |   Clearing)       |   |   Clearing)       |                |
|  +--------+---------+   +--------+----------+                |
|           |                       |                           |
|  +--------+---------+   +--------+----------+                 |
|  |  C7 SCS          |   |  F7 Repo          |                |
|  |  (Securities      |   |  (Repo Trading    |                |
|  |   Clearing)       |   |   & Clearing)     |                |
|  +--------+---------+   +--------+----------+                |
|           |                       |                           |
|  +--------+----------+-----------+----------+                 |
|  |           Eurex Clearing Prisma          |                 |
|  |        (Margin & Risk Engine)            |                 |
|  +--------+----------+-----------+----------+                |
|           |                       |                           |
|  +--------+---------+   +--------+----------+                 |
|  |  C7 ARP          |   |  C7 CAS           |                |
|  |  (Advanced Risk   |   |  (Client Admin    |                |
|  |   Protection)     |   |   Service)        |                |
|  +------------------+   +-------------------+                 |
|                                                               |
|  +---------+  +--------+  +--------+  +----------+           |
|  |  CRE    |  |  ERS   |  | Prisma |  | Clearing |           |
|  | Reports |  |  Risk  |  | Calc.  |  |   GUI    |           |
|  +---------+  +--------+  +--------+  +----------+           |
+--------------------------------------------------------------+
         |                      |                    |
    Clearstream            T2S / T2           Clearing Members
   (Settlement)         (Cash/Securities)    (Connectivity)
```

**Architecture type:** Hybrid -- transitioning from monolithic legacy to **microservices-based architecture** (C7 SCS on Red Hat OpenShift); on-premise core with selective cloud adoption (Google Cloud for D7, cPME, analytics).

[Source: [TCS Eurex Case Study](https://www.tcs.com/what-we-do/industries/capital-markets/case-study/eurex-central-counterparty-clearing-legacy-modernization)]

### 2.2 Core Components

#### C7 Clearing Platform

C7 is Eurex Clearing's next-generation clearing architecture, replacing the legacy "Eurex Clearing Classic" system through a stepwise migration approach.

| Component | Function | Status |
|-----------|----------|--------|
| **C7 Core** | Central clearing engine for listed derivatives (futures, options); novation, position management, settlement instruction generation | Production (multiple releases) |
| **C7 Securities Clearing Service (C7 SCS)** | Securities clearing for Frankfurt Stock Exchange (XETR, XFRA) and Eurex securities (XEUR); handles trade capture, netting, settlement instruction generation, corporate actions | Production since September 2021 |
| **C7 Client Administration Service (C7 CAS)** | Member and account administration, reporting configuration, user entitlements, OTC report receiver management | Production; CAS Release 2.293 live October 2025 |
| **C7 Advanced Risk Protection (C7 ARP)** | Pre-trade and real-time risk controls; maintains member risk limits; interfaces with Prisma for limit breach detection; member Stop/Release functionality | Integrated into C7 |

**C7 SCS Modernization Details (TCS Partnership):**

The migration from Eurex Clearing Classic to C7 SCS was executed in partnership with TCS:

- **Phase 1:** Clearing of securities market and derivatives settlement transactions. TCS designed robust, high-performing system components to handle high throughput and low-latency requirements.
- **Phase 2:** Clearing of repo market transactions. Addressed complex functionality and migration to a new collateral management system.
- **Architecture:** Microservice-based, deployed on **Red Hat OpenShift** container platform. Independently scalable components replace the monolithic legacy application.
- **Benefits:** Flexible scaling for increased trade traffic; faster time-to-market for new products and services (e.g., additional currency support, extended trading hours); reduced operational overhead.
- **Development methodology:** Distributed agile methods with test automation.

[Source: [TCS Eurex Case Study](https://www.tcs.com/what-we-do/industries/capital-markets/case-study/eurex-central-counterparty-clearing-legacy-modernization)]

**Recent C7 Releases:**

| Release | Production Date | Key Features |
|---------|----------------|--------------|
| C7 Release 11.1 | 19 May 2025 | Total Return Futures strategy support; negative trade/settlement prices; cross-product margining for US FCM clients |
| C7 CAS Release 2.289.7 | 15 May 2025 | Reporting ID improvements; system enhancements |
| C7 CAS Release 2.293 | 20 October 2025 | New OTC Report Receiver admission type; reporting improvements |
| C7 SCS Enhancements | November 2025 | Corporate actions handling improvements |
| C7 Release Notes | 18 March 2026 | Functional and technical enhancements overview published |

[Source: [C7 Releases](https://www.eurex.com/ec-en/support/initiatives/c7-releases); [C7 CAS Releases](https://www.eurex.com/ec-en/support/initiatives/c7-client-administration-service/C7-CAS-Releases-2900566)]

---

#### PRISMA Margin Engine -- Portfolio Risk Integrated System and Margin Approach

**Eurex Clearing Prisma** (Portfolio-based Risk management by Simulating scenario Matrices and Assessing market risks) is Eurex Clearing's proprietary portfolio-based margin methodology, introduced in 2012. It represents a fundamental shift from product-by-product margining to portfolio-level risk assessment.

##### Core Methodology: Filtered Historical Simulation (FHS)

The FHS approach combines the benefits of historical simulation (no distributional assumptions, captures fat tails and non-linear payoffs) with GARCH-type volatility filtering to ensure the model reacts quickly to changing market conditions.

**Scenario Generation Process:**

1. **Raw historical returns:** Collect daily returns for all risk factors over a 3-year lookback window (approximately 750 trading days).
2. **Volatility filtering:** Apply a GARCH-type filter to scale historical returns by the ratio of current conditional volatility to historical volatility at each observation date. This ensures that in high-volatility regimes, scenarios reflect current elevated risk, while in low-volatility regimes, the filtered scenarios remain responsive.
3. **Filtered scenarios:** The 750 filtered historical scenarios represent potential portfolio P&L outcomes calibrated to current market conditions.
4. **Stress period scenarios:** An additional 250 scenarios are drawn from identified historical stress episodes (e.g., 2008 financial crisis, 2011 European debt crisis, 2020 COVID-19 crash). These are also filtered to ensure consistency.
5. **Full revaluation:** Each portfolio is revalued under all 1,000 scenarios using full pricing models (not delta-gamma approximations), capturing non-linear risks for options and complex instruments.
6. **VaR calculation:** The initial margin is set as the **maximum** of:
   - Filtered Historical Simulation VaR at the target confidence level (99% for listed, 99.5% for OTC)
   - Stress Period VaR at the same confidence level
7. **Subsampling technique:** Filtered historical and stress period scenario prices are divided into non-overlapping scenario subsamples for robust VaR estimation.

[Source: [Eurex Clearing Prisma](https://www.eurex.com/ec-en/services/margining/eurex-clearing-prisma); [Eurex Clearing Prisma Brochure (2014)](https://www.eurex.com/resource/blob/2287018/05702c2d06312fc083c9419d81414db5/data/2014-Brosch-re-Eurex-Clearing-Prisma-E.pdf); [Part 8: Forward Looking Margin Simulations](https://www.eurex.com/ec-en/find/news/Part-8-Forward-looking-margin-simulations-into-periods-of-stress-3193710)]

##### Key Parameters

| Parameter | Specification |
|-----------|--------------|
| Model Type | Filtered Historical Simulation (FHS) with Value-at-Risk (VaR) |
| Confidence Level | 99% for listed products; 99.5% for OTC instruments |
| Historical Scenarios | 750 filtered-historical scenarios (3-year lookback) |
| Stress Scenarios | 250 stress period scenarios from identified historical stress episodes |
| Total Scenarios | 1,000 (750 + 250) |
| Risk Measure | Maximum of FHS VaR and Stress Period VaR |
| Revaluation | Full revaluation under each scenario (not delta-gamma approximation) |
| Holding Period -- Listed Equity Derivatives | 2-3 days (PEQ01 liquidation group) |
| Holding Period -- Listed Fixed Income | 2 days (PFI01_HP2 split) |
| Holding Period -- OTC IRS | 5 days (PFI01_HP5 split) |
| Procyclicality Mitigation | Stress period VaR serves as prudent margin floor during low-volatility regimes |
| Floor Recalibration | Annual recalibration (e.g., effective 16 June 2025) |
| Stress Period Selection | Calibrated to long-term (at least 10 years), 99% VaR to ensure stable flooring |

##### Margin Components

Prisma initial margin consists of multiple additive components:

| Component | Description |
|-----------|-------------|
| **Market Risk Initial Margin (MRIM)** | Core risk component based on FHS; captures potential portfolio value changes under historical and stress scenarios via full revaluation |
| **Liquidity Adjustment (LA)** | Accounts for the cost of liquidating concentrated positions; adjusts for bid-ask spread widening and market impact during portfolio close-out |
| **KnockIn / Event Risk Component** | Additional margin for specific risk events (e.g., barrier events for structured products, dividend event risk for single stock derivatives) |
| **Margin Concentration Add-on** | Supplementary margin for concentrated OTC IRS portfolios; introduced December 2025 |
| **Correlation Break Adjustment** | Adjustment to account for potential breakdown of historical correlations during stress periods [unverified -- referenced in methodology but details limited] |

The backward-looking component (filtered historical VaR) ensures model reactivity to changing market conditions, while the forward-looking component (stress period VaR) ensures margin stability and counters procyclicality.

##### Liquidation Groups

Products are organized into Liquidation Groups based on shared risk characteristics. Margin offsets (cross-margining) are permitted within a liquidation group but not across liquidation groups.

| Liquidation Group | Products | Holding Period | Notes |
|-------------------|----------|---------------|-------|
| **PFI01** (Fixed Income) | Listed FI futures/options + OTC IRS, OIS, FRA, basis swaps, zero-coupon inflation swaps | Split: HP2 (2-day) for listed; HP5 (5-day) for OTC | Cross-margining between listed and OTC within this group |
| **PEQ01** (Equity) | Listed equity/index derivatives | 2-3 days | Reduced from 4 to 3 days; subsequently to 2 days for some products |
| **FX Liquidation Group** | OTC FX NDFs | 2 days [unverified] | |
| **Repo/Bonds** | Repo, GC Pooling, bonds | Varies | Migrating from Risk-Based Margining to Prisma Bonds (mandatory from 8 December 2025) |

##### Cross-Margining Algorithm

Cross-margining is a distinctive and economically significant feature of Prisma, enabling margin offsets between products with different holding periods within the same liquidation group:

1. **Portfolio assessment:** The system evaluates whether listed FI/money market positions within PFI01 are economically sensible hedges to the OTC portfolio.
2. **Holding period optimization:** If the listed positions qualify as hedges, they are moved from the 2-day holding period split to the 5-day split. Although this increases the holding period for those positions, the portfolio-level diversification benefit from combining them with OTC positions more than offsets the increased time horizon.
3. **Net margin calculation:** The combined portfolio is then evaluated at the 5-day horizon, producing a lower total margin than the sum of separate listed (2-day) and OTC (5-day) margins.
4. **Margin savings:** Potential savings of **up to 70%** depending on portfolio composition (e.g., a portfolio with listed Euro-Bund futures hedging OTC EUR IRS).

**Advantage over SPAN:** Unlike CME's SPAN methodology (which calculates margin product-by-product with limited inter-commodity spread credits using 16 scanning scenarios), Prisma assesses risk at the portfolio level using full revaluation under 1,000 historical scenarios, enabling more accurate capture of hedging benefits and tail risk.

[Source: [Eurex Clearing Cross-Margining](https://www.eurex.com/ec-en/services/margining/cross-margining)]

---

#### EurexOTC Clear

EurexOTC Clear provides central clearing for OTC derivative transactions, with a focus on interest rate derivatives.

| Parameter | Details |
|-----------|---------|
| Products | Plain vanilla IRS, OIS, FRA, basis swaps, zero-coupon inflation swaps (ZCIS), FX NDFs |
| Currencies | EUR, USD, GBP, CHF, JPY, DKK, NOK, SEK, PLN, CZK, HUF (11 currencies) |
| Trade Sources | Approved Trade Sources (ATS) including MarkitWire, Bloomberg, Tradeweb |
| Compression | Portfolio compression services to reduce line items and gross notional |
| Margin Methodology | Prisma (PFI01 liquidation group, 5-day holding period, 99.5% confidence) |
| Notional Outstanding | EUR 43,668 billion (end-2025, +31% YoY) |
| Avg Daily Cleared Volume | EUR 280 billion (2025, +35% YoY) |

EurexOTC Clear has its own release track separate from C7, with regular enhancements for new product support, regulatory compliance, and connectivity improvements.

[Source: [EurexOTC Clear](https://www.eurex.com/ec-en/clear/eurex-otc-clear/about-eurex-otc-clear); [EurexOTC Clear Technology](https://www.eurex.com/ec-en/technology/eurexotc-clear)]

---

#### Cloud Prisma Margin Estimator (cPME)

cPME is a cloud-based margin simulation tool available to both members and non-members of Eurex Clearing, providing transparency into Prisma margin calculations.

| Parameter | Details |
|-----------|---------|
| Access Methods | Browser-based GUI and RESTful API |
| Hosting | Deutsche Borse VPC on **Google Cloud Platform** (EU datacenters); migrated from previous infrastructure in 2023 |
| Availability | 24 hours a day (with brief interruptions during snapshot loading) |
| API Performance | 95% of requests responded in **less than 1 second** |
| ETD Margin Accuracy | Code identical to production Prisma environment; results match CC050 report for same date/time |
| OTC Margin Accuracy | Independent implementation of margin methodology; may differ a few percent from official EurexOTC margin |
| Input Formats | CB202 member report; CSV file with additional trades; concurrent format support |
| Cost | Free of charge |
| Use Cases | Pre-trade margin estimation; what-if analysis; portfolio optimization; clearing member onboarding assessment |

The cPME API documentation is publicly available, including OpenAPI specifications on GitHub.

[Source: [Cloud Prisma Margin Estimator](https://deutsche-boerse-risk.github.io/CloudPrismaMarginEstimator/); [GitHub Repository](https://github.com/Deutsche-Boerse-Risk/CloudPrismaMarginEstimator); [cPME GCP Migration Circular](https://www.eurex.com/ec-en/find/circulars/Eurex-Clearing-Readiness-Newsflash-Cloud-Prisma-Margin-Estimator-CPME-migration-to-Google-Cloud-Platform-3931142)]

---

#### Risk Engine -- Real-Time Risk Monitoring

Eurex Clearing's risk monitoring infrastructure consists of two main components:

**Enhanced Risk Solution (ERS):**

| Parameter | Details |
|-----------|---------|
| Purpose | Real-time risk data distribution to clearing and non-clearing members |
| Coverage | All asset classes: derivatives, cash equities, bonds, repo |
| Data Distributed | Risk-relevant margin parameters, position information, overall margin requirements, detailed margin components, cash flows, collateral valuations, margin shortfall/surplus |
| Standards | Based on open standards for integration into member in-house risk systems |
| Cost | Free of charge |
| Interface | Web-based GUI (ERS GUI) with risk manager dashboards; data feed for programmatic consumption |

**C7 Advanced Risk Protection (ARP):**

| Parameter | Details |
|-----------|---------|
| Purpose | Pre-trade and real-time risk limit management |
| Functions | Maintain member risk limits; detect limit breaches (interfacing with Prisma); member Stop/Release functionality |
| Access | C7 Clearing GUI; programmatic API |
| Scope | Covers all C7 cleared products |

[Source: [Eurex ERS Press Release](https://mondovisione.com/media-and-resources/news/eurex-clearing-introduces-realtime-risk-management-for-all-customers-clearing-an-2011124/); [C7 ARP Functional Reference Guide](https://www.eurex.com/resource/blob/3202446/5c50f388c13754438fe0c7b26c5f9cc4/data/Eurex-Clearing-ARP-Functional-Reference-Guide-Rel.-9.0.pdf)]

### 2.3 Technology Stack

| Layer | Technology | Notes |
|-------|-----------|-------|
| Container Platform | Red Hat OpenShift | Used for C7 SCS microservices deployment |
| Architecture Pattern | Microservices (C7 SCS); transitional for other components | Legacy monolithic components being progressively retired |
| Cloud Platform | Google Cloud Platform (GCP) | 10-year strategic partnership (announced February 2023); used for cPME, D7, analytics |
| Cloud Services | Google Cloud VMware Engine, BigQuery, Analytics Hub | Deutsche Borse among first users of GCP VMware Engine |
| Messaging / Connectivity | Proprietary protocols (ETI), FIX/FIXML, SFTP (CRE) | Multiple connectivity options |
| Risk Calculation Engine | Eurex Clearing Prisma (proprietary) | Filtered Historical Simulation with full revaluation |
| Reporting Infrastructure | Common Report Engine (CRE) -- SFTP-based | OpenSSH authentication |
| Development Methodology | Distributed Agile with test automation (TCS partnership) | |
| Programming Language | Not publicly disclosed | [unverified -- Java/C++ likely based on industry norms for clearing systems] |
| Operating System | Linux-based (OpenShift runs on RHEL/CoreOS) | |
| DLT / Blockchain | Integrated with HQLAx DLT for collateral mobilisation; D7 DLT for tokenized securities | |

[Source: [TCS Eurex Case Study](https://www.tcs.com/what-we-do/industries/capital-markets/case-study/eurex-central-counterparty-clearing-legacy-modernization); [Deutsche Borse Google Cloud Partnership](https://www.deutsche-boerse.com/dbg-en/media/news-stories/press-releases/Deutsche-B-rse-Group-and-Google-Cloud-Announce-Strategic-Partnership-to-Accelerate-Innovation-3405724); [Google Cloud Deutsche Borse Case Study](https://cloud.google.com/customers/deutsche-boerse)]

---

## 3. Performance Specifications

| Metric | Value | Conditions / Notes |
|--------|-------|--------------------|
| Daily Quote Capacity | 800+ million quotes per day | Eurex Exchange T7 platform (trading side) |
| Average Daily Contracts | ~7 million contracts per day | Listed derivatives on Eurex Exchange |
| Annual Cleared Contracts | 2,065.9 million contracts (2025) | Full year listed derivatives |
| OTC Daily Cleared Volume | EUR 280 billion average (2025) | OTC IRS notional |
| Repo Daily Volume | EUR 406.1 billion average term-adjusted (2025) | Record year |
| cPME API Response Time | <1 second for 95% of requests | Margin estimation API |
| T7 Order Response Time | ~6 milliseconds | Via Enhanced Transaction Interface (trading side) |
| Monthly Cleared Value | EUR 11+ trillion | Across all asset classes |
| Margin Recalculation | End-of-day full; intraday near-time | Prisma margin engine |

Note: Specific clearing-side throughput metrics (transactions per second, clearing latency) are not publicly disclosed by Eurex Clearing. The metrics above combine trading-side and clearing-side publicly available data.

[Source: [Eurex Exchange Marketplace](https://www.eurex.com/ex-en/find/about-us/the-market-place); [Eurex Full Year 2025 Figures](https://www.eurex.com/ex-en/find/news-center/news/Full-year-and-December-2025-figures-at-Eurex-4891494)]

---

## 4. Interfaces & Protocols

### 4.1 Clearing Connectivity

| Interface | Protocol | Description |
|-----------|----------|-------------|
| **Enhanced Transaction Solution (ETS)** | Proprietary binary | Optional high-performance trading/clearing interface; introduced with Eurex Release 10.0 |
| **Enhanced Trading Interface (ETI)** | Proprietary binary | Low-latency API for trading and clearing; ~6ms order response time |
| **FIX / FIXML** | FIX 4.2/4.4, FIXML | Post-trade clearing and settlement messaging; widely used by ISVs |
| **C7 APIs** | Proprietary | APIs for C7 SCS and C7 CAS integration |
| **Common Report Engine (CRE)** | SFTP (OpenSSH) | Central solution for all trading and clearing report retrieval; end-of-day reports in TXT and XML formats; single source for all non-transactional files |
| **Connectivity Options** | Leased line, Internet, Multi-Member-Service Operator | Members choose preferred hardware platform and OS |

[Source: [Eurex CRE](https://www.eurex.com/ex-en/support/technology/common-report-engine); [ETS Circular](https://www.eurex.com/ex-en/find/circulars/Enhanced-Transaction-Solution-ETS-Introduction-of-new-optional-Trading-Interface-Eurex-Release-10.0-Changes-to-Legal-Documents-due-to-new-Features-Introduction-of-new-Reports-and-Discontinuation-of-Eurex-Reports--196272)]

### 4.2 Eurex Clearing GUI / Prisma Calculator

| Tool | Description | Access |
|------|-------------|--------|
| **Clearing GUI** | Web-based GUI for clearing activities across listed derivatives, securities, OTC business; includes C7 ARP services | Members only; via Eurex connectivity |
| **ERS GUI** | Web-based dashboard for real-time risk monitoring; margin coverage, exposure views | Members only |
| **Prisma Online Margin Calculator** | Browser-based margin simulation for listed and OTC products | Members; via Eurex website |
| **Cloud Prisma Margin Estimator (cPME)** | Cloud-based GUI and RESTful API for margin estimation; hosted on GCP | Members and non-members; free of charge |

[Source: [Eurex Prisma Calculators](https://www.eurex.com/ex-en/trade/margin-calculators/eurexotc-clear-prisma-margin-calculator); [cPME Documentation](https://deutsche-boerse-risk.github.io/CloudPrismaMarginEstimator/)]

### 4.3 SWIFT / FIX / XML Interfaces

| Interface | Usage |
|-----------|-------|
| **SWIFT** | Settlement messaging with Clearstream and other CSDs; standard MT5xx messages for securities settlement |
| **FIX/FIXML** | Post-trade clearing messages; trade confirmation; position reporting |
| **XML Reports** | Eurex Clearing XML Reports (reference manual V7.1.0); detailed clearing, margin, and settlement reports delivered via CRE |
| **ISO 20022** | Alignment with T2S and T2 messaging standards for settlement in central bank money |

[Source: [Eurex Clearing XML Reports Reference Manual](https://www.eurex.com/resource/blob/2559052/1d7c5d0b9ca7a34198cab317c7af8914/data/Eurex-Clearing-XML-Reports-Reference-Manual.pdf)]

### 4.4 Reference Data

| Data Type | Description |
|-----------|-------------|
| Product Reference Data | Instrument definitions, contract specifications, expiry calendars |
| Risk Parameters | Prisma scenario files, margin parameters, volatility surfaces |
| Member/Account Data | Via C7 CAS; member configurations, account structures |
| Price Data | End-of-day settlement prices; intraday reference prices for margin monitoring |

---

## 5. Resilience & Business Continuity

### 5.1 Redundancy & Disaster Recovery

| Aspect | Details |
|--------|---------|
| Data Center Architecture | Dual-site architecture; primary production and simulation/DR infrastructure |
| DR Infrastructure | T7 simulation infrastructure serves as DR production environment in disaster scenarios |
| Co-location Continuity | Co-location customers can use existing connections to access DR environment |
| Recovery Time Objective | Designed to meet EMIR requirement of **2-hour RTO** for critical services |
| DR Testing | Regular disaster recovery tests (typically semi-annually); participation serves to ensure transition requirements are met and emergency procedures are validated |
| BCP Framework | Group-wide incident and crisis management process (Deutsche Borse Group level); covers loss of IT, workspace, and staff scenarios |
| BCP Testing | Regular and comprehensive testing of business continuity arrangements |

[Source: [Eurex BCP](https://www.eurex.com/ec-en/find/about-us/business-continuity-planning); [T7 DR Concept 2025](https://www.eurex.com/resource/blob/4651858/b6f4ff08ad7dd3ce49a66f7ccaa369ab/data/T7_Disaster_Recovery_Concept_2025_v_1.2.pdf)]

### 5.2 Regulatory Resilience Requirements

| Regulation | Requirement |
|-----------|-------------|
| **EMIR** | 2-hour recovery time; robust governance and operational risk management |
| **DORA** (Digital Operational Resilience Act) | ICT risk management, incident reporting, digital operational resilience testing, third-party risk management; applicable from January 2025 |
| **CPMI-IOSCO PFMI** | Principle 17 (Operational Risk): FMIs should identify, monitor, and manage operational risk; achieve recovery within 2 hours |

### 5.3 Capacity Management

- C7 SCS microservices architecture on OpenShift enables **independent horizontal scaling** of individual components
- System designed to handle significant increases in trade traffic without burdening operations or development teams
- Regular capacity planning aligned with market growth projections
- Load testing as part of release management process [unverified -- industry standard practice]

---

## 6. Notable Technical Features

### 6.1 PRISMA Methodology Deep-Dive

**Filtered Historical Simulation (FHS) Approach:**

The FHS methodology, originally developed by Barone-Adesi, Engle, and Mancini (2008), is used by Eurex Clearing Prisma to combine the non-parametric benefits of historical simulation with the responsiveness of GARCH-type volatility models. Key characteristics:

- **No distributional assumptions:** Unlike parametric VaR or Monte Carlo approaches, FHS preserves the empirical distribution of returns including fat tails, skewness, and complex dependence structures.
- **Volatility conditioning:** GARCH-type filtering scales historical returns by the ratio of current to historical conditional volatility. In periods of rising volatility, filtered scenarios produce larger potential losses; in calm periods, the stress period VaR provides a floor.
- **Full revaluation:** Each portfolio is repriced under all 1,000 scenarios using full pricing models, accurately capturing non-linear risks (gamma, vega, convexity for fixed income).
- **Subsampling:** Non-overlapping subsamples improve the robustness of VaR estimates and reduce sensitivity to individual extreme observations.

**Anti-Procyclicality Measures:**

Eurex Clearing employs multiple mechanisms to prevent margins from being excessively low during calm markets and spiking sharply during stress:

1. **Stress Period VaR floor:** The margin is always at least as large as the stress period VaR, preventing margins from falling too low during benign market conditions.
2. **Annual floor recalibration:** Stress period parameters and margin floors are recalibrated annually (e.g., effective 16 June 2025) based on long-term historical data spanning at least 10 years.
3. **Gradual adjustment:** The FHS volatility filter ensures margins adjust gradually rather than through sudden jumps.
4. **EMIR compliance:** Eurex monitors two procyclicality metrics: maximum relative margin increase (short-term) and peak-to-trough ratio (long-term funding uncertainty).

**Stress Margin Components:**

The 250 stress scenarios are selected from identified historical stress episodes across different asset classes. The stress period dates are calibrated to the long-term (at least 10-year) 99% VaR to ensure stable flooring. Annual updates of stress period parameters are published via clearing circulars (e.g., the annual update effective 29 June 2020 and subsequent years).

[Source: [Eurex Clearing Prisma](https://www.eurex.com/ec-en/services/margining/eurex-clearing-prisma); [Part 8: Forward Looking Margin Simulations](https://www.eurex.com/ec-en/find/news/Part-8-Forward-looking-margin-simulations-into-periods-of-stress-3193710); [CFTC Eurex Clearing Margin Performance During 2020](https://www.cftc.gov/media/5501/GMAC_121720Eurex/download)]

### 6.2 D7 -- Digital Post-Trade Platform

D7 is Deutsche Borse Group's next-generation platform for fully digital issuance and processing of securities, operated by Clearstream and integrated with Eurex Clearing infrastructure.

| Component | Description |
|-----------|-------------|
| **D7 Digital** | Cloud-backed service (built with Google Cloud) for end-to-end digital securities issuance; creates and registers securities within seconds instead of up to two days |
| **D7 DLT** | Tokenized securities platform based on distributed ledger technology; fully CSDR-compliant |
| **Scale** | Processes 45,000+ digital issuances per week; 2+ million issued securities; EUR 44+ billion total volume |
| **Products** | Retail structured products, debt capital market instruments, digital commercial paper |
| **Integration** | D7 digital commercial paper traded on Eurex Repo F7 and cleared through Eurex Clearing |
| **DLT Collateral** | Eurex Clearing became the first CCP globally to launch DLT-enabled collateral mobilisation (July 2025, with HQLAx and Clearstream) |

[Source: [Deutsche Borse D7](https://www.deutsche-boerse.com/dbg-en/markets-services/ps-technology/ps-7-market-technology/ps-d7); [D7 DLT Launch](https://www.deutsche-boerse.com/dbg-en/media/news-stories/press-releases/D7-DLT-Clearstream-Launches-Tokenized-Securities-Platform-4757912); [WFE Clearstream D7 Article](https://focus.world-exchanges.org/articles/clearstream-db-d7)]

### 6.3 Cloud Adoption Strategy

Deutsche Borse Group's cloud strategy centers on a 10-year strategic partnership with Google Cloud (announced February 2023):

| Initiative | Details |
|-----------|---------|
| **Cloud Migration** | Multi-cloud infrastructure; significant workloads migrated since 2019 |
| **cPME on GCP** | Cloud Prisma Margin Estimator deployed in Deutsche Borse VPC on GCP within EU |
| **D7 on GCP** | D7 Digital built on Google Cloud's secure infrastructure with BigQuery and Analytics Hub |
| **Cloud-Native Trading Engine** | New cloud-native trading engine for digital trading platform with 24/7 availability and internet API access |
| **Digital Assets Platform** | Cloud-native market infrastructure combining centralized and decentralized finance for crypto spot and derivatives |
| **Data Analytics** | Google Cloud's data and analytics capabilities for market data distribution and analytics use cases |
| **VMware Engine** | Deutsche Borse among first users of Google Cloud VMware Engine for migrating existing VMware workloads |

[Source: [Deutsche Borse Google Cloud Partnership](https://www.deutsche-boerse.com/dbg-en/media/news-stories/press-releases/Deutsche-B-rse-Group-and-Google-Cloud-Announce-Strategic-Partnership-to-Accelerate-Innovation-3405724); [Google Cloud Blog](https://cloud.google.com/blog/topics/financial-services/lessons-from-deutsche-borse-groups-cloud-native-trading-engine)]

### 6.4 Partnership Initiatives (ISV Ecosystem)

| Partner | Domain | Integration |
|---------|--------|-------------|
| **TCS** | Technology | C7 SCS modernization; microservices architecture; ongoing development partnership |
| **Google Cloud** | Infrastructure | 10-year strategic partnership; cloud hosting for D7, cPME, analytics |
| **HQLAx** | DLT Collateral | DLT-enabled collateral mobilisation for Eurex Clearing margin |
| **Pirum** | Post-trade | Post-trade automation for Lending CCP |
| **EquiLend** | Securities Lending | Trade sourcing for Lending CCP |
| **CLS** | FX Settlement | Settlement of OTC FX-related cash flows |
| **ISV Community** | Connectivity | Multiple ISVs provide FIX-based connectivity solutions for clearing members |

---

## 7. Comparison Notes

### vs. KRX/KSD Systems

| Aspect | Eurex C7 / PRISMA | KRX / KSD Equivalent |
|--------|-------------------|---------------------|
| **Clearing System** | C7 (microservices on OpenShift); phased migration from legacy monolith | KRX integrated clearing system (part of EXTURE+ platform ecosystem) |
| **Margin Methodology** | PRISMA: Filtered Historical Simulation VaR; portfolio-based; 1,000 scenarios (750 historical + 250 stress) | SPAN-based margin for derivatives (Standard Portfolio Analysis of Net Risk); 16 scanning scenarios per product; product-by-product with limited inter-commodity credits |
| **Confidence Level** | 99% (listed) / 99.5% (OTC) | 99% for KOSPI 200 derivatives [unverified] |
| **Cross-Margining** | Yes -- within liquidation groups; listed-OTC cross-margining with up to 70% savings | Limited cross-margining; KRX provides some inter-product spread credits within SPAN framework |
| **Risk Approach** | Portfolio-level full revaluation under historical scenarios | Scenario-based scanning with parameterized risk arrays |
| **Anti-Procyclicality** | Stress period VaR floor; annual recalibration | Margin floor mechanisms [unverified -- details not publicly available] |
| **OTC Clearing** | EurexOTC Clear for IRS, OIS, FRA, inflation swaps, NDF in 11 currencies | KRX CCP for KRW-denominated OTC IRS and CRS (authorized under Capital Markets Act) |
| **Margin Simulation Tool** | cPME (free, cloud-based, API + GUI, on Google Cloud) | KRX margin calculator (member-facing) [unverified] |
| **Architecture** | Microservices (C7 SCS on OpenShift); hybrid cloud | Integrated platform (EXTURE+ ecosystem); primarily on-premise |
| **DLT/Digital** | D7 DLT for tokenized securities; HQLAx DLT collateral | KSD exploring DLT-based bond issuance and security token platforms [unverified] |
| **Cloud Strategy** | 10-year Google Cloud partnership; selective migration | On-premise focused with selective cloud exploration [unverified] |
| **CSD Integration** | Vertically integrated with Clearstream (same group); settlement via T2S | KSD (Korea Securities Depository) is separate entity but deeply integrated with KRX |
| **Default Waterfall** | EUR 1.7 billion total Eurex/Deutsche Borse commitment (SITG + SSITG + equity + backstop) | KRX default fund structure per Capital Markets Act [details vary] |
| **Regulatory Framework** | EMIR (EU); DORA; CFTC DCO registration | Capital Markets Act (Korea); FSC/FSS supervision |

### Key Differentiators of Eurex C7/PRISMA

1. **Portfolio-based margining vs. product-based:** PRISMA's FHS approach evaluates risk at the portfolio level using full revaluation under 1,000 scenarios, providing more accurate margin requirements that recognize hedging and diversification. KRX's SPAN-based approach uses 16 scanning scenarios per product with limited portfolio-level offsets. This is a fundamental methodological difference -- PRISMA can offer up to 70% margin savings for hedged portfolios.

2. **Microservices architecture:** C7 SCS's deployment on Red Hat OpenShift represents a modern containerized approach that enables independent scaling of components, faster feature delivery, and operational flexibility. This contrasts with the more traditional integrated platform approach used by KRX.

3. **Cloud-native margin tools:** cPME provides free, cloud-based margin simulation with production-equivalent code via RESTful API, enabling pre-trade margin optimization. This level of transparency and accessibility in margin simulation tools is a distinctive offering.

4. **Listed-OTC cross-margining:** The ability to cross-margin between listed fixed income products and OTC IRS within the PFI01 liquidation group is a key competitive advantage, particularly relevant for the EMIR 3.0 active account requirement driving EU-based clearing.

5. **DLT integration:** Eurex Clearing's early adoption of DLT-enabled collateral mobilisation (first CCP globally, July 2025) and integration with the D7 tokenized securities platform positions it at the forefront of post-trade digital transformation.

6. **Vertical integration:** Deutsche Borse Group's vertical integration (Eurex Exchange for trading, Eurex Clearing for CCP, Clearstream for CSD/ICSD) creates a seamless value chain, particularly for repo (Eurex Repo F7 trading -> Eurex Clearing CCP -> Clearstream settlement). KRX has a similar vertical integration model with KSD.

---

## Sources

1. [Eurex Clearing C7 Releases](https://www.eurex.com/ec-en/support/initiatives/c7-releases) -- Official C7 release information and documentation
2. [Eurex Clearing Prisma](https://www.eurex.com/ec-en/services/margining/eurex-clearing-prisma) -- PRISMA methodology overview
3. [Eurex Clearing Cross-Margining](https://www.eurex.com/ec-en/services/margining/cross-margining) -- Cross-margining methodology
4. [TCS Eurex Case Study](https://www.tcs.com/what-we-do/industries/capital-markets/case-study/eurex-central-counterparty-clearing-legacy-modernization) -- C7 SCS modernization technology details
5. [Cloud Prisma Margin Estimator Documentation](https://deutsche-boerse-risk.github.io/CloudPrismaMarginEstimator/) -- cPME technical documentation
6. [cPME GitHub Repository](https://github.com/Deutsche-Boerse-Risk/CloudPrismaMarginEstimator) -- API specifications and documentation
7. [Deutsche Borse Google Cloud Partnership](https://www.deutsche-boerse.com/dbg-en/media/news-stories/press-releases/Deutsche-B-rse-Group-and-Google-Cloud-Announce-Strategic-Partnership-to-Accelerate-Innovation-3405724) -- Strategic cloud partnership announcement
8. [Google Cloud Deutsche Borse Case Study](https://cloud.google.com/customers/deutsche-boerse) -- Cloud adoption details
9. [Google Cloud Blog: Cloud-Native Trading Engine](https://cloud.google.com/blog/topics/financial-services/lessons-from-deutsche-borse-groups-cloud-native-trading-engine) -- Cloud-native architecture details
10. [Deutsche Borse D7 Platform](https://www.deutsche-boerse.com/dbg-en/markets-services/ps-technology/ps-7-market-technology/ps-d7) -- D7 digital post-trade platform
11. [D7 DLT Launch](https://www.deutsche-boerse.com/dbg-en/media/news-stories/press-releases/D7-DLT-Clearstream-Launches-Tokenized-Securities-Platform-4757912) -- Tokenized securities platform
12. [WFE Clearstream D7 Article](https://focus.world-exchanges.org/articles/clearstream-db-d7) -- D7 platform overview
13. [Eurex Clearing Prisma Brochure (2014)](https://www.eurex.com/resource/blob/2287018/05702c2d06312fc083c9419d81414db5/data/2014-Brosch-re-Eurex-Clearing-Prisma-E.pdf) -- Original PRISMA methodology documentation
14. [CFTC: Eurex Clearing Margin Performance During 2020](https://www.cftc.gov/media/5501/GMAC_121720Eurex/download) -- Margin model performance during COVID-19
15. [Part 8: Forward Looking Margin Simulations](https://www.eurex.com/ec-en/find/news/Part-8-Forward-looking-margin-simulations-into-periods-of-stress-3193710) -- Stress period VaR methodology
16. [Eurex Clearing BCP](https://www.eurex.com/ec-en/find/about-us/business-continuity-planning) -- Business continuity planning
17. [T7 Disaster Recovery Concept 2025](https://www.eurex.com/resource/blob/4651858/b6f4ff08ad7dd3ce49a66f7ccaa369ab/data/T7_Disaster_Recovery_Concept_2025_v_1.2.pdf) -- DR infrastructure
18. [Eurex Full Year 2025 Figures](https://www.eurex.com/ex-en/find/news-center/news/Full-year-and-December-2025-figures-at-Eurex-4891494) -- Volume and performance statistics
19. [EurexOTC Clear](https://www.eurex.com/ec-en/clear/eurex-otc-clear/about-eurex-otc-clear) -- OTC clearing service overview
20. [Eurex Common Report Engine](https://www.eurex.com/ex-en/support/technology/common-report-engine) -- CRE technical documentation
21. [C7 ARP Functional Reference Guide](https://www.eurex.com/resource/blob/3202446/5c50f388c13754438fe0c7b26c5f9cc4/data/Eurex-Clearing-ARP-Functional-Reference-Guide-Rel.-9.0.pdf) -- Advanced Risk Protection documentation
22. [Eurex 2026 Roadmap](https://www.eurex.com/ex-en/find/circulars/Eurex-Readiness-Newsflash-Our-path-for-2026--4867350) -- 2026 development plans
23. [Prisma Margin Floor Recalibration Circular (2025)](https://www.eurex.com/ec-en/find/circulars/clearing-circular-4441804) -- Annual margin floor update
24. [Prisma Bonds Circular](https://www.eurex.com/ec-en/find/circulars/clearing-circular-4609908) -- Extension of Prisma to bonds and repos
25. [cPME GCP Migration Circular](https://www.eurex.com/ec-en/find/circulars/Eurex-Clearing-Readiness-Newsflash-Cloud-Prisma-Margin-Estimator-CPME-migration-to-Google-Cloud-Platform-3931142) -- Cloud migration details
