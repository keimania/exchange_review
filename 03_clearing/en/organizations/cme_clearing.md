# CME Clearing

> **Last Updated:** 2026-04-07
> **Research Tier:** Tier 1 (Deep Dive)
> **Type:** CCP (Central Counterparty)

---

## 1. Overview & Profile

### 1.1 Organization Profile

| Item | Details |
|------|---------|
| Official Name | Chicago Mercantile Exchange Inc. (operating CME Clearing) |
| Abbreviation | CME Clearing |
| Website | [https://www.cmegroup.com/clearing](https://www.cmegroup.com/clearing) |
| Year Established | 1898 (as Chicago Butter and Egg Board); clearing house established 1919; CME Group formed via CME-CBOT merger in 2007 |
| Country / City | United States / Chicago, Illinois |
| Ownership Structure | Division of CME Group Inc. (NASDAQ: CME). CME Group also owns CBOT, NYMEX, and COMEX exchanges. CME Clearing is operated by Chicago Mercantile Exchange Inc., a wholly owned subsidiary of CME Group Inc. |
| Regulatory Authority | CFTC (primary, as registered Derivatives Clearing Organization under CEA Part 39); Board of Governors of the Federal Reserve System (under Dodd-Frank Title VIII SIFMU oversight); SEC (secondary, for security-based products via CME Securities Clearing Inc.) |
| CPMI-IOSCO PFMI Compliance | Yes -- publishes PFMI qualitative self-assessment disclosures and quarterly Public Quantitative Disclosures (PQD) ([CME PFMI Disclosure, November 2023](https://www.cmegroup.com/clearing/risk-management/files/cme-clearing-principles-for-financial-market-infrastructures-disclosure.pdf)) |
| QCCP Status | Yes -- recognised by ESMA as a third-country CCP under EU EMIR since June 2016, granting QCCP status for EU-regulated participants ([CME QCCP FAQ](https://www.cmegroup.com/clearing/files/faq-ccp-final.pdf); [European Commission Equivalence Decision, March 2016](http://europa.eu/rapid/press-release_IP-16-807_en.htm)) |
| SIFMU Designation | Designated as a Systemically Important Financial Market Utility (SIFMU) by the Financial Stability Oversight Council (FSOC) under Title VIII of the Dodd-Frank Act in July 2012 |

### 1.2 Key Historical Milestones

| Year | Event |
|------|-------|
| 1898 | Chicago Butter and Egg Board established as a commodity exchange |
| 1919 | Reorganised as the Chicago Mercantile Exchange; clearing house established |
| 1972 | CME launched the International Monetary Market (IMM), creating the first financial futures (currency futures) |
| 1981 | Eurodollar futures launched, becoming the world's most-traded futures contract |
| 1992 | CME Globex electronic trading platform launched -- the first global electronic trading system for futures and options |
| 2000 | CME demutualized |
| 2002 | CME Holdings Inc. became the first U.S. exchange to IPO on the NYSE |
| 2003 | CBOT transferred all clearing from independent Board of Trade Clearing Corp. to CME Clearing, creating capital efficiencies ([MarketsWiki](https://www.marketswiki.com/wiki/CME_Group_History_Timeline)) |
| 2007 | CME and CBOT officially merged to form CME Group Inc. (July) |
| 2008 | CME Group acquired NYMEX Holdings Inc. (including NYMEX and COMEX) |
| 2010 | CME Clearing began clearing OTC interest rate swaps |
| 2011 | CME Clearing Europe launched in London for European OTC clearing |
| 2012 | CME designated as SIFMU by FSOC under Dodd-Frank Title VIII |
| 2016 | ESMA recognised CME as third-country CCP (QCCP) under EU EMIR |
| 2017 | CME Clearing Europe wound down and closed (October 12, 2017); all clearing consolidated to CME Clearing in the U.S. ([CME Press Release, April 2017](https://www.cmegroup.com/media-room/press-releases/2017/4/12/cme_group_intendstoclosecmeeuropeandcmeclearingeuropebyyear-end.html)) |
| 2022 | CME Group announced 10-year strategic partnership with Google Cloud |
| 2023 | SPAN 2 margin framework went live for energy products (September 2023) |
| 2024 | CME-FICC cross-margining arrangement launched for proprietary accounts (January 2024); record ADV of 26.5 million contracts |
| 2025 | Record annual ADV of 28.1 million contracts; CME Securities Clearing Inc. received SEC approval (December 2025) for U.S. Treasury and repo clearing ([CME Press Release, December 2025](https://www.cmegroup.com/media-room/press-releases/2025/12/02/cme_group_announcesregulatoryapprovalofnewsecuritiesclearinghous.html)) |

---

## 2. Clearing Model

### 2.1 CCP Services

CME Clearing acts as the central counterparty (CCP) for all trades executed on or submitted through CME Group's four exchanges and OTC platforms. It clears the following product categories:

| Product Category | Exchange / Platform | Examples |
|-----------------|---------------------|----------|
| Interest Rate Derivatives | CME, CBOT | SOFR futures, U.S. Treasury futures & options, Eurodollar futures (legacy) |
| Equity Index Derivatives | CME | E-mini S&P 500, E-mini Nasdaq-100, Micro E-mini, Nikkei 225 futures |
| Foreign Exchange | CME | EUR/USD, JPY/USD, and 40+ FX pairs in futures & options |
| Agricultural Commodities | CBOT, CME | Corn, Soybeans, Wheat, Live Cattle, Lean Hogs, Dairy |
| Energy Products | NYMEX | WTI Crude Oil, Henry Hub Natural Gas, Refined Products |
| Metals | COMEX, NYMEX | Gold, Silver, Copper, Platinum, Palladium, Aluminum |
| OTC Interest Rate Swaps | CME ClearPort | SOFR swaps, USD IRS, cross-currency swaps, swaptions |
| OTC FX | CME ClearPort | OTC FX forwards and swaps (select currency pairs) |
| Cryptocurrency | CME | Bitcoin futures & options, Ether futures & options |

### 2.2 Novation Process

Upon acceptance of a trade for clearing, CME Clearing interposes itself as the legal counterparty to both sides of every transaction through the process of novation. The original bilateral contract between buyer and seller is extinguished and replaced by two new contracts: one between CME Clearing and the buyer, and one between CME Clearing and the seller. This ensures that each clearing member only faces CME Clearing as its counterparty, eliminating bilateral counterparty credit risk.

### 2.3 Netting

CME Clearing provides multilateral netting across all products within each clearing member's account. Variation margin (settlement variation) is netted across all positions within a given account, resulting in a single net pay or collect amount per settlement cycle. For performance bonds (initial margin), CME applies portfolio-based margining via SPAN / SPAN 2 that recognises offsets between correlated positions.

### 2.4 Clearing Membership Tiers & Requirements

CME, CBOT, NYMEX, and COMEX clearing memberships are entirely separate from one another. A firm must hold the appropriate division-specific clearing membership to clear products traded on that exchange.

**Membership Categories:**

Each exchange division recognises multiple categories of clearing members ([CME Rulebook Chapter 9](https://www.cmegroup.com/rulebook/CME/I/9/9.pdf); [NYMEX Rulebook Chapter 9](https://www.cmegroup.com/rulebook/NYMEX/1/9.pdf)):

| Category | Description |
|----------|-------------|
| CME Clearing Member | Authorised to clear all CME-listed products |
| CBOT Clearing Member | Authorised to clear all CBOT-listed products |
| NYMEX Clearing Member | Authorised to clear all NYMEX-listed products |
| COMEX Clearing Member | Authorised to clear all COMEX-listed products |
| IRS Clearing Member | Separate membership for OTC interest rate swap clearing (distinct guaranty fund) |

**Minimum Capital Requirements:**

| Member Type | Exchange-Traded Products | OTC-Traded Products |
|-------------|-------------------------|---------------------|
| Non-bank FCM | $5 million Adjusted Net Capital (per CFTC Reg. 1.17) | $50 million Adjusted Net Capital |
| Bank | $5 billion Tier I Capital | $50 million Tier I Capital |
| IRS Clearing Member | N/A | Capital >= 20% of aggregate IRS performance bond requirement |

Source: [CME Group Clearing Membership Requirements Summary](https://www.cmegroup.com/company/membership/files/summary-cme-group-clearing-membership-requirements.pdf)

**Number of Clearing Members:** Approximately 50-55 clearing firms across all divisions [unverified -- exact current count not publicly disclosed in aggregate; the CME Group clearing firms directory lists individual members ([Clearing Firms](https://www.cmegroup.com/clearing/financial-and-regulatory-surveillance/clearing-firms.html))].

---

## 3. Risk Management

### 3.1 Margin Framework: SPAN

CME Clearing developed the **SPAN (Standard Portfolio Analysis of Risk)** methodology, which has become the global standard for portfolio-based margin calculation, adopted by over 50 exchanges and clearing organisations worldwide ([SPAN Methodology Overview](https://www.cmegroup.com/solutions/risk-management/performance-bonds-margins/span-methodology-overview.html)).

**How SPAN Works:**

SPAN evaluates overall portfolio risk by calculating the worst reasonable loss that a portfolio of derivative and physical instruments might incur over a specified time period (typically one trading day for exchange-traded products, five days for OTC).

**16 Risk Scenarios:**

SPAN constructs 16 hypothetical risk scenarios based on two key parameters:
- **Price Scanning Range** -- calibrated to the distribution of price movements under normal market conditions (typically a 1-day, 99% confidence interval)
- **Volatility Scanning Range** -- calibrated to the distribution of implied volatility movements

The 16 scenarios represent combinations of:
- Price changes at fractions of the price scanning range (0, 1/3, 2/3, 1x, 2x, and 3x -- with 3x given reduced weight)
- Volatility changes (up and down by the volatility scanning range)

**Five Components of SPAN Risk:**

| Component | Description |
|-----------|-------------|
| **Scanning Risk** | The largest loss from the 16 risk scenarios for a given combined commodity group |
| **Intra-Commodity Spread Charge** | Captures basis risk between different expiration months within the same commodity (calendar spread risk) |
| **Inter-Commodity Spread Credit** | Recognises risk-reducing offsets between correlated commodity groups (e.g., WTI vs. Brent crude) |
| **Delivery Month Charge** | Additional charge for positions approaching physical delivery |
| **Short Option Minimum** | Floor margin requirement for deep out-of-the-money short options to capture tail risk |

**SPAN Margin Calculation:**

```
Performance Bond = MAX(Scanning Risk + Intra-Commodity Spread Charge + Delivery Month Charge
                       - Inter-Commodity Spread Credit,
                       Short Option Minimum)
```

Source: [CME SPAN Methodology](https://www.cmegroup.com/solutions/risk-management/performance-bonds-margins/span-methodology.html)

### 3.2 SPAN 2 Transition

CME is transitioning to **SPAN 2**, a next-generation VaR-based (Historical Value-at-Risk) margin framework. Key differences from legacy SPAN:

| Feature | SPAN (Legacy) | SPAN 2 |
|---------|---------------|--------|
| Methodology | 16 parametric scenarios | Thousands of HVaR scenarios from historical data |
| Risk Symmetry | Same margin for long and short positions | **Asymmetric** -- long and short margins differ based on historical risk profiles |
| Offset Calculation | Explicit inter-commodity spread credits | Offsets inherent in VaR calculation via portfolio covariance |
| Tail Risk | Short option minimum | Expected Shortfall (ES) component capturing tail losses beyond VaR threshold |
| Additional Factors | N/A | Seasonality, options term structure, liquidity/concentration costs |

**SPAN 2 Rollout Schedule (phased):**

| Asset Class | Go-Live Date |
|-------------|-------------|
| Energy Products | September 8, 2023 (completed) |
| Equity Products | October 18, 2024 (primary) / November 15, 2024 (backup) |
| Interest Rate & FX Products | Second half of 2024 |
| Agricultural & Remaining Products | Second half of 2025 |

During the multi-year transition, both SPAN and SPAN 2 run in parallel. Cross-model offsets between SPAN- and SPAN 2-margined products are supported via covariance. Legacy SPAN will continue to be supported for the foreseeable future.

Source: [SPAN 2 Framework Rollout](https://www.cmegroup.com/solutions/risk-management/performance-bonds-margins/span-methodology-overview/launching-span-2.html); [SPAN 2 Methodology](https://www.cmegroup.com/clearing/risk-management/span-overview/span-2-methodology.html)

### 3.3 Comparison: SPAN vs. PRISMA vs. STANS

| Feature | CME SPAN / SPAN 2 | Eurex PRISMA | OCC STANS |
|---------|-------------------|--------------|-----------|
| Operator | CME Clearing | Eurex Clearing | Options Clearing Corporation |
| Methodology | Parametric scenarios (SPAN) / HVaR + ES (SPAN 2) | Filtered Historical Simulation VaR + stress add-ons | Monte Carlo simulation |
| Confidence Level | 99%+ (SPAN); 99.7%+ (SPAN 2) [unverified] | 99.7% (2-day MPOR) | 99% (2-day MPOR) |
| Portfolio Scope | Futures, options, OTC swaps | Listed + OTC derivatives | Equity options, futures |
| Cross-Product Offsets | SPAN credits / VaR covariance (SPAN 2) | Full portfolio-based | Full portfolio-based |
| Liquidation Period | 1 day (ETD), 5 days (OTC IRS) | 2 days (listed), 5 days (OTC) | 2 days |

### 3.4 Margin Call Schedule

CME Clearing recalculates performance bond (margin) requirements at least once daily, but typically twice daily for exchange-traded derivatives:

| Cycle | Timing | Description |
|-------|--------|-------------|
| **End-of-Day (EOD)** | After market close (~4:00 PM CT) | Full recalculation of all positions against settlement prices; settlement variation pays/collects calculated |
| **Intraday** | Mid-morning (~10:00-11:00 AM CT) | Intraday mark-to-market; additional performance bond calls issued if needed |
| **Ad-hoc / Extraordinary** | As needed | CME Clearing has authority to issue additional margin calls at any time based on market conditions |

For OTC IRS and FX swaps, settlement variation is calculated at least once daily at end-of-day.

USD settlement cycles run twice daily (EOD and intraday) through CME's settlement banks. CME has authority to run additional cycles if market conditions warrant.

Source: [CME PFMI Disclosure, November 2023](https://www.cmegroup.com/clearing/risk-management/files/cme-clearing-principles-for-financial-market-infrastructures-disclosure.pdf)

### 3.5 Default Waterfall

CME Clearing maintains **two distinct financial safeguards waterfalls**, each with its own guaranty fund:

1. **Base Products Waterfall** -- covering futures, options, and OTC FX across CME, CBOT, NYMEX, and COMEX
2. **IRS Products Waterfall** -- covering OTC interest rate swaps and swaptions

**Base Products Default Waterfall (sequential application):**

| Layer | Resource | Approximate Size |
|-------|----------|-----------------|
| 1 | **Defaulting Clearing Member's Performance Bonds** (initial margin) | Varies by portfolio |
| 2 | **Defaulting Clearing Member's Guaranty Fund Contribution** | Pro-rata share |
| 3 | **CME Clearing's Own Contribution (Skin-in-the-Game / SITG)** | **$100 million** (pre-funded) |
| 4 | **Non-Defaulting Clearing Members' Guaranty Fund Contributions** | Mutualized pool (sized to Cover 2 standard) |
| 5 | **Assessment Powers** | Up to **2.75x** each non-defaulting member's guaranty fund contribution per single default event |
| 6 | **Recovery Tools** | Voluntary contributions, variation margin haircutting, mandatory tear-ups |

**IRS Products Default Waterfall (sequential application):**

| Layer | Resource | Approximate Size |
|-------|----------|-----------------|
| 1 | **Defaulting IRS Clearing Member's Performance Bonds** | Varies by portfolio |
| 2 | **Defaulting IRS Clearing Member's Guaranty Fund Contribution** | Pro-rata share |
| 3 | **CME Clearing's Own Contribution (SITG)** | **$150 million** (pre-funded) |
| 4 | **Non-Defaulting IRS Clearing Members' Guaranty Fund Contributions** | Mutualized pool (sized to Cover 2 standard) |
| 5 | **Assessment Powers** | Capped assessment on non-defaulting IRS clearing members |
| 6 | **Recovery Tools** | Gains haircutting, mandatory tear-ups, voluntary contributions, voluntary tear-ups |

**Guaranty Fund Sizing:**

- Each guaranty fund is sized to cover the default of the **two clearing members (and their affiliates) with the largest anticipated stress shortfalls** -- the "Cover 2" standard.
- As of December 31, 2024, guaranty fund contributions available to collateralise facilities totalled approximately **$10.1 billion** ([CME Inc. Financial Statements 2024](https://www.cmegroup.com/investor-relations/files/cme-inc-financial-statements.pdf)).
- CME Clearing maintained approximately **$87.4 billion** in cash within accounts at the Federal Reserve Bank of Chicago as of December 31, 2024 (representing performance bond and guaranty fund deposits).
- A **guaranty fund buffer** is maintained above the Cover 2 minimum to mitigate potential breaches.

Source: [CME Clearing Financial Safeguards Waterfalls](https://www.cmegroup.com/education/articles-and-reports/cme-clearing-financial-safeguards-waterfalls.html); [Financial Safeguards System](https://www.cmegroup.com/solutions/risk-management/financial-safeguards/cme-clearings-financial-safeguards-system.html); [CME Rulebook Chapter 8](https://www.cmegroup.com/rulebook/CME/I/8/8.pdf)

### 3.6 Stress Testing & Back-Testing

| Practice | Details |
|----------|---------|
| **Stress Testing Frequency** | Daily |
| **Scenario Types** | Historical scenarios and hypothetical (extreme but plausible) market conditions |
| **Confidence Level** | At least 99.9% |
| **Cover Standard** | Cover 2 -- sized to withstand simultaneous default of the two clearing members with the largest stress shortfalls |
| **Reverse Stress Testing** | Conducted routinely; results reviewed at least monthly to identify conditions that could exhaust guaranty fund resources |
| **Backtesting** | Performance bond adequacy backtested against actual market movements; reported quarterly via PQD |
| **Independent Validation** | Annual validation by independent experts |
| **Regulatory Examination** | CFTC and Federal Reserve Board conduct annual examinations of risk management practices |
| **CFTC Supervisory Stress Tests** | CFTC conducts periodic supervisory stress tests of major DCOs including CME ([CFTC Stress Test Report 2019](https://www.cftc.gov/system/files?file=2019/05/02/cftcstresstest042019.pdf)) |

Source: [CME Clearing Stress Testing Practices](https://www.cmegroup.com/articles/2025/cme-clearing-stress-testing-practices.html)

### 3.7 Recovery & Resolution Tools

CME Clearing has adopted specific recovery tools, particularly for the IRS waterfall, to address "end of waterfall" scenarios ([CME Advisory 19-365](https://www.cmegroup.com/notices/clearing/2019/11/Chadv19-365.html)):

| Tool | Description |
|------|-------------|
| **Variation Margin Gains Haircutting (VMGH)** | Pro-rata reduction in amounts owed to non-defaulting members with net gains for the relevant settlement cycle |
| **Mandatory Tear-Up** | Forced termination of contracts to re-establish a matched book; designed to localise impact to affected markets |
| **Voluntary Contributions** | IRS clearing members (and customers) may voluntarily contribute resources; only effective if aggregate contributions are sufficient to fully cover losses |
| **Voluntary Tear-Up** | Clearing members (and customers) may voluntarily terminate positions |
| **Assessment Powers** | Capped additional contributions from non-defaulting members (up to 2.75x guaranty fund contribution for Base products) |

**Resolution Authority:** The FDIC is the designated resolution authority for SIFMUs under Title II of the Dodd-Frank Act, though Title VIII provides a framework for the Federal Reserve to provide emergency lending to SIFMUs in extremis.

### 3.8 Cross-Margining Programs

See Section 7 (Interoperability) for details on CME-OCC and CME-FICC cross-margining arrangements.

---

## 4. Settlement

### 4.1 Settlement Cycle

| Product Type | Settlement Cycle | Details |
|-------------|-----------------|---------|
| **Futures (Variation Margin)** | Daily (T+0 or T+1 intraday) | Settlement variation (mark-to-market pays/collects) calculated and settled at least twice daily (EOD and intraday) |
| **Options on Futures** | Daily premium settlement; exercise/assignment T+1 | Premium paid/received next business day; exercise results in futures position |
| **OTC IRS** | Daily (variation margin) | At least once daily at end-of-day |
| **Physical Delivery (Futures)** | Delivery period varies by contract | Delivery occurs during designated delivery months per contract specifications |

### 4.2 DVP Model

For physically-delivered securities (e.g., U.S. Treasury futures expiry):

- Settlement occurs on a **DVP Model 1 (gross, real-time)** basis
- Delivery of U.S. Treasury securities occurs via **book-entry transfer in Fedwire Securities** between banks that are members of the Federal Reserve System
- Transfer of funds is conditional on delivery of the securities (true DVP)
- Clearing participants must make funds available to designated settlement banks the day prior to delivery

Source: [RBA Assessment -- Standard 11: Exchange-of-Value Settlements](https://www.rba.gov.au/payments-and-infrastructure/financial-market-infrastructure/clearing-and-settlement-facilities/assessments/chicago-mercantile-exchange/2014/standard-11.html)

### 4.3 Settlement Finality

Settlement finality is achieved when the settlement variation payment is debited/credited through the settlement bank accounts. Under CME rules, once a settlement cycle is completed and payments are effected, the transfers are final and irrevocable. CME Clearing's status as a SIFMU provides additional legal certainty under Title VIII of Dodd-Frank, which provides protections against potential legal challenges to netting and settlement finality.

### 4.4 Cash Settlement Process

For cash-settled contracts (e.g., E-mini S&P 500, Eurodollar/SOFR futures), final settlement prices are determined by reference to an external index or fixing rate on the last trading day. The cash settlement amount is calculated as the difference between the final settlement price and the prior day's settlement price, and is collected/paid through the standard variation margin settlement cycle.

### 4.5 Settlement Banks

CME Clearing uses the following **concentration banks** for settlement:

| Bank | Currencies |
|------|-----------|
| **BMO Harris Bank** | USD, MXN |
| **JPMorgan Chase (London)** | AUD, NOK, CHF, GBP, NZD, SEK, TRY, SGD, HKD, ZAR |
| **Citibank (London)** | EUR, CNH, DKK, PLN, CZK, HUF |
| **Citibank (Canada)** | CAD |

CME Clearing holds accounts at each settlement bank, and clearing members must maintain demand deposit cash accounts at one or more approved settlement banks. CME runs two USD settlement cycles daily (EOD and intraday).

Source: [Custodian and Settlement Banks](https://www.cmegroup.com/solutions/clearing/financial-and-collateral-management/custodian-and-settlement-banks.html)

---

## 5. Technology & Infrastructure

### 5.1 Core Systems

| System | Function |
|--------|----------|
| **CME Globex** | Electronic trading platform providing virtually 24-hour global market access for futures and options across all asset classes; housed at Aurora, IL data center |
| **CME Clearing Systems** | Post-trade clearing, risk management, and settlement processing infrastructure -- processes more than **1 billion trades per year** worth more than **$1 quadrillion** in notional value ([CME Group](https://www.cmegroup.com/solutions/clearing.html)) |
| **CME CORE** | Interactive margin calculator for clearing members and market participants to calculate margin requirements, access margin models, and run SPAN/SPAN 2 scenarios |
| **CME ClearPort** | OTC trade submission and clearing platform supporting block trades, EFPs/EFRs, and OTC derivatives clearing |
| **CME Direct** | Front-end platform providing trading and clearing member functionality |

### 5.2 Interface Protocols

| Protocol | Description |
|----------|-------------|
| **CME STP FIX** | Standard FIX 4.4 API with CME extensions for trade confirmation, query, and subscription streaming over TCP/IP |
| **CME STP FIXML** | FIXML 5.0 SP2 messaging over RESTful web services for cleared trade information retrieval |
| **CME ClearPort API** | API for OTC trade submission and management |
| **CME Globex iLink** | Order entry and management interface for electronic trading |
| **Market Data Platform (MDP)** | Real-time and historical market data feeds |

Source: [CME Straight Through Processing](https://www.cmegroup.com/solutions/processing-and-reporting/straight-through-processing.html); [CME STP FIX](https://cmegroupclientsite.atlassian.net/wiki/spaces/EPICSANDBOX/pages/599162891/CME+STP+FIX)

### 5.3 Data Center & Resilience

| Item | Details |
|------|---------|
| **Primary Data Center** | Aurora, Illinois -- 450,000 sq ft facility; operated by CyrusOne (owned by KKR/GIP since CME sold in 2016); serves as hub for CME Globex and all production applications |
| **Disaster Recovery** | New York Data Center (NYDC) -- DR site for all CME applications including iLink, Market Data, Clearing, and support applications |
| **DR Failover** | Manual activation process; CME can transfer operations to NYDC if Aurora is unavailable |
| **Notable Incident** | November 2025: 10+ hour outage due to cooling system failure at Aurora data center. DR site was available but failover threshold was set too high and activation was manually gated. CyrusOne subsequently installed additional cooling redundancy ([Crain's Chicago Business, 2025](https://www.chicagobusiness.com/finance-banking/cmes-data-center-adds-more-cooling-after-outage)) |

### 5.4 Google Cloud Partnership

CME Group entered a **10-year strategic partnership** with Google Cloud to transform its technology infrastructure:

| Initiative | Details |
|-----------|---------|
| **Private Cloud Region** | Announced June 2024 -- new private Google Cloud region and co-location facility in Aurora, IL, designed for ultra-low-latency networking and high-performance computing for futures and options trading ([CME Press Release, June 2024](https://www.cmegroup.com/media-room/press-releases/2024/6/26/cme_group_and_googlecloudannouncenewchicagoareaprivatecloudregio.html)) |
| **Google Cloud Universal Ledger (GCUL)** | Announced March 2025 -- CME Group piloting tokenisation technology using GCUL for seamless wholesale payments and asset tokenisation. Phase 1 completed; Phase 2 (settlement focus) underway with target market solutions in 2026 ([CME Press Release, March 2025](https://www.cmegroup.com/media-room/press-releases/2025/3/25/cme_group_will_introducetokenizationtechnologytoenhancecapitalma.html)) |
| **Cloud Migration** | Overall goal to migrate all technology to Google Cloud infrastructure |

---

## 6. Regulatory Framework

### 6.1 Primary Regulatory Status

| Designation | Authority | Basis |
|------------|-----------|-------|
| **Derivatives Clearing Organization (DCO)** | CFTC | Commodity Exchange Act (CEA); CFTC Part 39 regulations |
| **SIFMU** | FSOC / Federal Reserve Board | Dodd-Frank Act Title VIII (designated July 2012) |
| **Recognised Third-Country CCP** | ESMA | EU EMIR; recognised June 2016 (Tier 1 CCP) |
| **Registered Clearing Agency** | SEC | CME Securities Clearing Inc. (approved December 2025) -- for U.S. Treasury and repo clearing |

### 6.2 CFTC DCO Core Principles (Part 39)

CME Clearing must comply with all DCO Core Principles under the CEA, including but not limited to:

| Core Principle | Requirement |
|---------------|-------------|
| Financial Resources | Sufficient to cover default of two largest clearing members (Cover 2) |
| Participant & Product Eligibility | Appropriate admission and product eligibility standards |
| Risk Management | Comprehensive risk management framework with margin, stress testing, default management |
| Settlement Procedures | Timely completion of settlement obligations |
| Treatment of Funds | Segregation of customer funds from proprietary funds |
| Default Rules & Procedures | Clear rules for handling clearing member defaults |
| System Safeguards | Robust IT systems, business continuity, and cybersecurity |
| Reporting | Regulatory reporting to CFTC |
| Public Information | Transparent disclosure of rules, procedures, and risks |

### 6.3 SIFMU Oversight

As a designated SIFMU, CME is subject to enhanced supervisory standards:

- **Federal Reserve Board** oversight under Title VIII (delegated by FSOC)
- Annual joint examinations by CFTC and Federal Reserve Board
- Comprehensive evaluation of operations and risk management relative to DCO Core Principles
- Access to Federal Reserve discount window lending in extremis
- Enhanced recovery and resolution planning requirements

### 6.4 PFMI & Public Quantitative Disclosures

CME publishes:
- **CPMI-IOSCO Qualitative Self-Assessment** -- comprehensive PFMI disclosure document (last published November 2023)
- **Quarterly PQD Reports** -- public quantitative disclosures with key risk metrics (available at [CME CPMI-IOSCO Reporting](https://www.cmegroup.com/clearing/cpmi-iosco-reporting.html))
- **Annual Financial Statements** -- CME Inc. audited financials

---

## 7. Interoperability

### 7.1 CME-OCC Cross-Margining Program

| Item | Details |
|------|---------|
| **Established** | 1989 -- one of the earliest cross-margining arrangements globally |
| **Participants** | OCC (Options Clearing Corporation) and CME Clearing |
| **Purpose** | Combine hedged positions in equity index options (cleared by OCC) with equity index futures (cleared by CME) into a single portfolio for margin purposes |
| **Margin Model** | Combined positions margined using OCC's STANS (System for Theoretical Analysis and Numerical Simulations) portfolio methodology |
| **Eligibility** | Open to clearing members and their affiliates, market makers, and futures locals. Not generally available to retail customers due to differing securities vs. futures customer protection requirements |
| **Key Benefit** | SPX options (OCC) combined with E-mini S&P 500 futures (CME) for portfolio-level margin offsets |
| **Milestone** | 20th anniversary of partnership celebrated in 2019 ([CME-OCC 20 Years](https://investor.cmegroup.com/news-releases/news-release-details/options-clearing-corporation-and-cme-group-mark-20-years-cross)) |

Source: [OCC Cross-Margin Programs](https://www.theocc.com/risk-management/cross-margin-programs)

### 7.2 CME-FICC Cross-Margining Arrangement

| Item | Details |
|------|---------|
| **Launched** | January 2024 (proprietary/house accounts) |
| **Participants** | FICC (Fixed Income Clearing Corporation, a DTCC subsidiary) and CME Clearing |
| **Purpose** | Capital efficiencies for clearing members trading and clearing both U.S. Treasury securities (FICC) and Interest Rate futures (CME) |
| **Eligible Products** | FICC-cleared U.S. Treasury Notes and Bonds (>1 year maturity) from buy/sell or repo/reverse repo transactions, paired with CME Treasury futures |
| **Margin Methodology** | Both CCPs calculate margins on combined portfolios using their respective models; the more conservative result is applied with a joint margin savings percentage |
| **Customer Extension** | Proposed rule change filed May 2025 to extend program to end-user customers of dually-registered broker-dealers/FCMs; target go-live December 2025, subject to regulatory approval |
| **Significance** | A critical element for the upcoming SEC U.S. Treasury clearing mandate (effective December 31, 2026 for cash; June 30, 2027 for repo) |

Source: [CME-FICC Cross-Margining FAQ](https://www.cmegroup.com/trading/interest-rates/cleared-otc/faq-cme-ficc-cross-margining-arrangement-expansion.html); [DTCC-CME Cross-Margining Forum, April 2025](https://www.newyorkfed.org/medialibrary/microsites/tmpg/files/CME-Group-FICC-Cross-Margining-April2025.pdf)

### 7.3 Mutualization Across CME/CBOT/NYMEX/COMEX

All four exchange divisions share the **Base Products** financial safeguards waterfall. This means:
- A single Base guaranty fund covers futures, options, and OTC FX across all four divisions
- Clearing member default losses in any division can draw on the common Base guaranty fund
- IRS products have their own separate guaranty fund and waterfall
- This structure creates mutualization of default risk across all Base product clearing members regardless of which division they clear on

### 7.4 Global CCP Links

CME Clearing does not operate formal interoperability links (shared CCP clearing arrangements) with other global CCPs in the European sense (e.g., EuroCCP-LCH interoperability). Instead, CME maintains its position as a standalone CCP with:
- Cross-margining agreements (OCC, FICC)
- QCCP recognition in multiple jurisdictions
- Global client access via its clearing member network

---

## 8. Fees

### 8.1 Fee Structure Overview

CME Group charges clearing and transaction fees on a **per-side, per-contract** basis. Rates vary by:
- Product category and specific contract
- Member status (exchange member vs. non-member)
- Volume-based incentive program participation
- Transaction type (electronic, open outcry, block, EFP/EFR)

**Average Rate Per Contract:** $0.707 per side (Q4 2025) ([CME Q4 2025 Earnings](https://www.cmegroup.com/media-room/press-releases/2026/2/04/cme_group_inc_reportsfourthconsecutiveyearofrecordannualrevenuea.html))

### 8.2 Representative Clearing Fees by Product Category

| Product Category | Representative Contract | Exchange Fee (approx.) | Notes |
|-----------------|------------------------|----------------------|-------|
| **Equity Index** | E-mini S&P 500 (ES) | $0.60 per side (exchange fee, effective Feb 2025) + NFA $0.02 | Non-member all-in ~$1.18/side including surcharges |
| **Interest Rates** | Treasury Futures, SOFR | Varies; volume incentive programs available | Aggregate volume-based incentives across IR products |
| **Energy** | WTI Crude Oil, Natural Gas | Product-specific; member discounts apply | NYMEX division fees |
| **Metals** | Gold, Silver, Copper | Product-specific; member discounts apply | COMEX division fees |
| **Agricultural** | Corn, Soybeans, Wheat | Product-specific; member discounts apply | CBOT division fees |
| **OTC IRS** | SOFR Swaps | Varies by notional and tenor | Client fee schedules available ([CME OTC IRS Fees](https://www.cmegroup.com/markets/cleared-swaps/cleared-otc-irs-client-fee-schedules.html)) |
| **Cryptocurrency** | Bitcoin, Ether Futures | Product-specific | 24/7 trading supported (from May 2026) |

### 8.3 Membership / Seat Costs

CME Group memberships (seats) can be purchased or leased. Holding a seat provides reduced exchange fees:

| Membership Type | Trading Rights | Impact on Fees |
|----------------|---------------|---------------|
| CME (Full) | All CME-listed products | Lowest fee tier for CME products |
| CBOT (Full) | All CBOT-listed products | Lowest fee tier for CBOT products |
| NYMEX | All NYMEX-listed products | Lowest fee tier for NYMEX products |
| COMEX | All COMEX-listed products | Lowest fee tier for COMEX products |

Seat prices fluctuate based on market conditions. Leasing is an alternative to outright purchase.

### 8.4 Volume Incentive Programs

CME Group offers various volume-based incentive programs that reduce effective per-contract costs:
- **Interest Rate Product Incentives** -- aggregate volume-based incentives across multiple IR products (expanded August 2025)
- **FX Volume Incentives** -- modified volume thresholds (effective August 2025); reduced EFP/block surcharge (effective July 2025)
- **Market Maker Programs** -- reduced fees for registered market makers

Source: [Exchange Fees for Clearing & Trading](https://www.cmegroup.com/company/clearing-fees.html); [CME Fee Schedule, February 2025](https://www.cmegroup.com/company/files/cme-fee-schedule-2025-02-01.pdf)

---

## 9. Recent Developments

### 9.1 SPAN 2 Rollout (2023-2025)

The next-generation SPAN 2 margin framework has been rolling out in a phased, multi-year approach:
- **Energy products** went live September 2023
- **Equity products** went live October/November 2024
- **Interest rate and FX products** (including cleared swaps) targeted for second half of 2024
- **Agricultural and remaining products** targeted for second half of 2025
- Both SPAN and SPAN 2 run in parallel during the transition

Source: [SPAN 2 Framework Rollout](https://www.cmegroup.com/solutions/risk-management/performance-bonds-margins/span-methodology-overview/launching-span-2.html)

### 9.2 Google Cloud Partnership

- **June 2024:** Announced new private Google Cloud region and co-location facility in Aurora, IL for ultra-low-latency trading infrastructure
- **March 2025:** Piloting tokenisation technology using Google Cloud Universal Ledger (GCUL) for wholesale payments and asset tokenisation; Phase 1 completed, Phase 2 (settlement) underway with 2026 target for market solutions
- Long-term: 10-year strategic partnership to migrate all CME Group technology to Google Cloud

### 9.3 CME Securities Clearing & Treasury Clearing

- **December 2025:** SEC approved registration of **CME Securities Clearing Inc.** as a clearing agency for U.S. Treasury cash and repo securities
- **Q2 2026:** Target launch for CME Securities Clearing operations
- This positions CME as a **direct competitor to FICC (DTCC)** in the U.S. Treasury clearing space, in advance of the SEC's clearing mandate:
  - Cash Treasury transactions: clearing mandate effective **December 31, 2026**
  - Repo transactions: clearing mandate effective **June 30, 2027**
- CME Securities Clearing will integrate with existing CME Group clearing services and extend cross-margining with FICC

Source: [CME Securities Clearing](https://www.cmegroup.com/solutions/clearing/cme-securities-clearing.html); [CME Press Release, December 2025](https://www.cmegroup.com/media-room/press-releases/2025/12/02/cme_group_announcesregulatoryapprovalofnewsecuritiesclearinghous.html)

### 9.4 Record Volumes (2024-2025)

| Metric | 2024 | 2025 | Change |
|--------|------|------|--------|
| **Annual ADV** | 26.5 million contracts | 28.1 million contracts | +6% |
| **International ADV** | 7.8 million contracts | 8.4 million contracts | +8% |
| **Interest Rate ADV** | ~13.7 million | 14.2 million (record) | +4% |
| **Metals ADV** | -- | Record (up 34% YoY) | +34% |
| **Agricultural ADV** | -- | Record (up 8% YoY) | +8% |
| **Energy ADV** | -- | Record (up 8% YoY) | +8% |
| **Q4 2025 ADV** | -- | 27.4 million (record Q4) | +7% YoY |

Volume growth was broad-based across all six asset classes in both years.

Source: [CME 2024 ADV Press Release](https://www.cmegroup.com/media-room/press-releases/2025/1/03/cme_group_reportsrecordannualadvof265millioncontractsin2024drive.html); [CME 2025 ADV Press Release](https://www.cmegroup.com/media-room/press-releases/2026/1/05/cme_group_reportsrecordannualadvof281millioncontractsin2025up6ye.html)

### 9.5 24/7 Trading Expansion

- **May 2026:** CME Group launching **24/7 trading** for cryptocurrency futures and options (Bitcoin, Ether) on CME Globex, pending regulatory review
- Trading will be continuous with at least a 2-hour weekly maintenance window
- Weekend/holiday trades carry next business day trade date for clearing, settlement, and reporting
- This follows record crypto derivatives volumes: $3 trillion notional in 2025 and 2026 YTD ADV of 407,200 contracts (up 46% YoY)

Source: [CME Press Release, October 2025](https://www.cmegroup.com/media-room/press-releases/2025/10/02/cme_group_to_offeraround-the-clocktradingforcryptocurrencyfuture.html)

### 9.6 Financial Performance

| Metric | 2024 | 2025 |
|--------|------|------|
| **Total Revenue** | $6.1 billion | $6.5 billion |
| **Operating Income** | $3.9 billion | $4.2 billion |
| **Net Income** | $3.5 billion | $4.0 billion [unverified] |
| **Adjusted Operating Margin** | ~68% | 69.4% |
| **Clearing & Transaction Fee Revenue (Q4)** | -- | $1.3 billion |

Fourth consecutive year of record annual revenue, operating income, and EPS in 2025.

Source: [CME 2024 Earnings](https://www.cmegroup.com/media-room/press-releases/2025/2/12/cme_group_inc_reportsall-timerecordannualrevenueadjustedoperatin.html); [CME 2025 Earnings](https://www.cmegroup.com/media-room/press-releases/2026/2/04/cme_group_inc_reportsfourthconsecutiveyearofrecordannualrevenuea.html)

### 9.7 November 2025 Data Center Outage

On November 28, 2025, CME markets were down for more than 10 hours following a cooling system failure at the Aurora, IL data center (operated by CyrusOne). Although the New York DR site was available, the manual failover process and high activation thresholds prevented a swift switch. CyrusOne subsequently installed additional cooling redundancy. The incident prompted industry discussion about data center governance and failover procedures for critical financial infrastructure.

Source: [Crain's Chicago Business](https://www.chicagobusiness.com/finance-banking/cmes-data-center-adds-more-cooling-after-outage); [Network World](https://www.networkworld.com/article/4099088/cooling-crisis-at-cme-a-wakeup-call-for-modern-infrastructure-governance.html)

---

## Key Data Summary

| Metric | Value |
|--------|-------|
| Products Cleared | Futures, options, OTC IRS, OTC FX across CME, CBOT, NYMEX, COMEX |
| Annual ADV (2025) | 28.1 million contracts |
| Trades Processed Annually | >1 billion |
| Notional Value Processed Annually | >$1 quadrillion |
| Cash Held at Fed (Dec 2024) | ~$87.4 billion |
| Guaranty Fund Contributions (Dec 2024) | ~$10.1 billion |
| CME SITG (Base Waterfall) | $100 million |
| CME SITG (IRS Waterfall) | $150 million |
| SIFMU Designation | Yes (July 2012) |
| QCCP Status (EU) | Yes (June 2016) |
| Clearing Revenue (FY 2025) | Part of $6.5 billion total revenue |
| Margin Methodology | SPAN (legacy) transitioning to SPAN 2 (HVaR + ES) |
| Cover Standard | Cover 2 |

---

*This document is based on publicly available information from CME Group, CFTC filings, CPMI-IOSCO disclosures, and third-party sources. All figures are approximate and sourced as noted. Information marked [unverified] could not be confirmed from official sources at the time of research.*
