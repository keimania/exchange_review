# SIX x-clear AG (SIX x-clear)

> **Last Updated:** 2026-04-07
> **Research Tier:** Tier 3 (Overview)
> **Type:** CCP (Central Counterparty)

---

## 1. Overview & Profile

| Item | Details |
|------|---------|
| Official Name | SIX x-clear AG |
| Abbreviation | SIX x-clear |
| Website | [https://www.six-group.com/en/products-services/securities-services/clearing.html](https://www.six-group.com/en/products-services/securities-services/clearing.html) |
| Year Established | 2003 |
| Country / City | Switzerland / Zurich |
| Ownership Structure | Subsidiary of SIX Securities Services AG, part of SIX Group AG |
| Parent Company / Group | SIX Group AG -- vertically integrated Swiss financial infrastructure group encompassing SIX Swiss Exchange (equities/bonds), SIX x-clear (CCP), SIX SIS (CSD), SIX Digital Exchange (SDX), BME (Spanish exchanges), and financial information services |
| Regulatory Authority | FINMA (Swiss Financial Market Supervisory Authority) as primary supervisor; SNB (Swiss National Bank) for systemically important services |
| CPMI-IOSCO PFMI Compliance | Yes -- publishes CPMI-IOSCO self-assessment and Public Quantitative Disclosures |
| QCCP Status | Licensed CCP under Swiss Financial Market Infrastructure Act (FMIA) since 28 March 2018; recognized Third Country CCP in EU and UK |
| Clearing Members | ~60 clearing members across European markets |
| Markets Served | 28 trading venues across 18 markets (combined with BME Clearing) |
| Position | Leading interoperable CCP for European cash equities; pioneer in CCP interoperability |

[Source: SIX Group -- Clearing Services, https://www.six-group.com/en/products-services/securities-services/clearing.html]
[Source: SIX Group -- 20 Years of Clearing, https://www.six-group.com/en/newsroom/news/securities-services/2023/20-years-clearing-anniversary.html]
[Source: SIX Group -- FINMA Recognition, https://www.six-group.com/en/newsroom/archive/2018/20180406-SIXxclear.html]

### Key Historical Milestones

| Year | Event |
|------|-------|
| 2003 | SIX x-clear established as CCP subsidiary of SIX Swiss Exchange (then SWX Swiss Exchange) |
| 2003 | Launch of clearing services for SIX Swiss Exchange equities |
| 2008 | Establishment of interoperability link with LCH Ltd for London Stock Exchange -- first CCP interoperability arrangement in Europe |
| 2008 | Interoperability link withstood Lehman Brothers collapse, proving robustness of the model |
| 2010s | Expansion of interoperability to additional European venues including Cboe Europe, Euronext, Nasdaq Nordic/Oslo |
| 2018 | FINMA authorization as CCP under the Financial Market Infrastructure Act (FMIA), 28 March 2018 |
| 2021 | FINMA approves SIX x-clear's first recovery plan |
| 2023 | 20th anniversary of clearing operations |
| 2025 (Dec) | SIX announces integration of SIX x-clear and BME Clearing into a single international multi-asset CCP named "SIX Clearing," headquartered in Madrid with presences in Zurich and Oslo |

[Source: SIX Group -- Interoperability 20 Years, https://www.six-group.com/en/newsroom/news/securities-services/2023/interoperability-20-years-clearing-anniversary.html]
[Source: SIX Group -- SIX x-clear/BME Clearing Integration, https://www.six-group.com/en/newsroom/media-releases/2025/20251204-six-clearing.html]
[Source: FINMA -- Resolution Report, https://www.finma.ch/en/enforcement/recovery-und-resolution-n/publikationen/resolution-report/archive/resolution-report/focus-on-financial-market-infrastructures/]

---

## 2. Clearing Model

### 2.1 CCP Services

SIX x-clear provides central counterparty clearing for cash equity and bond markets across Europe. Upon trade execution, SIX x-clear interposes itself as CCP through novation, becoming the buyer to every seller and the seller to every buyer.

| Service | Asset Classes | Venues |
|---------|--------------|--------|
| Swiss Market Clearing | Equities, ETFs, bonds | SIX Swiss Exchange |
| Pan-European Cash Equities | Equities, ETFs | London Stock Exchange, Cboe Europe, Euronext, Nasdaq Nordic/Oslo |
| Bond Clearing | Government and corporate bonds | SIX Swiss Exchange |

### 2.2 Clearing Process

- **Novation:** SIX x-clear assumes counterparty risk upon trade acceptance
- **Multilateral Netting:** Trades are netted on a multilateral basis per clearing member, segmented by house/client account, ISIN, currency, and settlement details
- **Netting Benefits:** Multilateral netting significantly reduces overall settlement volumes and associated costs for members
- **Core System:** SECOM is the core application for clearing and settlement services, including risk management, margin calculation, and clearing trade transactions

[Source: SIX Group -- Clearing Services]
[Source: SIX x-clear -- CPMI-IOSCO Disclosure, https://www.six-group.com/dam/download/securities-services/clearing/regulatory/consultation-responses/six-x-clear-iosco-en.pdf]

### 2.3 Membership

SIX x-clear serves approximately 60 clearing members. Members can clear for their own account (proprietary) or on behalf of clients. Membership requires meeting capital, operational, and technical requirements set by SIX x-clear.

---

## 3. Risk Management

### 3.1 Margin Framework

SIX x-clear employs a **Monte Carlo Value-at-Risk (VaR)** approach for its equities margin model:

- Portfolio margining approach that generates profit and loss scenarios
- Parametric assumptions (volatility, correlations) are checked daily against historical data
- **Anti-procyclicality measures:** Stressed periods are factored into margin calculations to avoid margins becoming excessively low during calm markets and to enable gradual increases during stress
- Margin requirements are designed to cover potential losses at a high confidence level (typically 99% or higher) over the liquidation period

[Source: SIX x-clear -- CPMI-IOSCO Disclosure]

### 3.3 Default Waterfall

SIX x-clear maintains a default waterfall to protect non-defaulting members in the event that losses from a member's default exceed the defaulter's own collateral:

1. **Defaulter's margin and collateral** -- initial margin and variation margin of the defaulting member
2. **Defaulter's default fund contribution** -- the defaulting member's contribution to the default fund
3. **SIX x-clear's own capital (skin-in-the-game)** -- a dedicated portion of SIX x-clear's own resources
4. **Non-defaulting members' default fund contributions** -- mutualized layer from surviving members
5. **Additional assessments** -- further calls on surviving members if needed [unverified]

*Note: Specific monetary amounts for each layer of the waterfall were not identified in publicly available sources at the time of writing.*

### 3.6 Recovery & Resolution

- **Recovery Plan:** First approved by FINMA in 2021 (subject to certain conditions)
- **Resolution Strategy:** FINMA's preferred resolution strategy for SIX x-clear aims to temporarily continue systemically critical functions for a maximum of six months to enable an orderly wind-down of operations
- **Systemically Important FMI:** SIX x-clear is designated as a systemically important financial market infrastructure by FINMA/SNB
- **Legal Basis:** Swiss Financial Market Infrastructure Act (FMIA) and Swiss Banking Act provide the framework for recovery and resolution

[Source: FINMA -- Focus on Financial Market Infrastructures, https://www.finma.ch/en/enforcement/recovery-und-resolution-n/publikationen/resolution-report/archive/resolution-report/focus-on-financial-market-infrastructures/]

---

## 4. Settlement

### 4.1 Settlement Cycle

- **Swiss Market:** T+2 standard settlement cycle for equities and bonds traded on SIX Swiss Exchange
- **European Markets:** T+2 in line with EU CSDR requirements for European venue trades
- **T+1 Transition:** The EU and UK are planning migration to T+1; Switzerland is expected to follow, though specific timelines remain under discussion [unverified]

### 4.2 DVP Model

- SIX x-clear does not itself operate a settlement system; settlement is performed through the relevant CSDs
- **Swiss Market Settlement:** Settled via SIX SIS (Swiss CSD) using DVP Model 1 (gross, simultaneous, and final transfer of securities and cash)
- **European Markets:** Settlement occurs through the relevant national CSDs or ICSDs depending on the trading venue (e.g., CREST for LSE, Euroclear for Euronext, etc.)
- Netted obligations from SIX x-clear are delivered to the relevant CSD for final settlement

[Source: SIX Group -- Clearing & Settlement Provisions, https://www.six-group.com/en/products-services/the-swiss-stock-exchange/trading/trading-provisions/clearing-and-settlement.html]

---

## 5. Technology & Infrastructure

- **SECOM Platform:** Core clearing and settlement application handling risk management, margin calculation, and trade clearing
- **Connectivity:** SIX x-clear connects to multiple European trading venues and CSDs through standardized interfaces
- **SIX Digital Exchange (SDX):** SIX Group operates a regulated digital asset exchange and CSD; potential future integration with x-clear clearing services [unverified]

---

## 6. Regulatory Framework

| Aspect | Details |
|--------|---------|
| Primary Legislation | Swiss Financial Market Infrastructure Act (FMIA, FinfraG) |
| Primary Supervisor | FINMA (Swiss Financial Market Supervisory Authority) |
| Oversight Authority | Swiss National Bank (SNB) -- for systemically important services |
| CCP License | Authorized as CCP under FMIA, 28 March 2018 |
| EU Status | Recognized Third Country CCP under EMIR |
| UK Status | Recognized Third Country CCP under UK EMIR |
| PFMI Compliance | Publishes CPMI-IOSCO self-assessments and PQD |
| Systemic Importance | Designated as systemically important FMI in Switzerland |

**Swiss-EU Equivalence Context:** Switzerland is not an EU/EEA member. SIX x-clear's EU recognition depends on the European Commission's equivalence decisions regarding Swiss regulation. This has been a politically sensitive topic given broader Swiss-EU relations. The planned integration with BME Clearing (which holds an EU CCP license) is partly motivated by securing direct EU market access.

[Source: SIX Group -- FINMA Recognition, https://www.six-group.com/en/newsroom/archive/2018/20180406-SIXxclear.html]

---

## 7. Interoperability

SIX x-clear is a pioneer and leader in CCP interoperability in Europe:

### Active Interoperability Links

| Partner CCP | Markets Covered | Since |
|-------------|----------------|-------|
| LCH Ltd | London Stock Exchange, others | 2008 |
| Cboe Clear Europe (formerly EuroCCP) | Cboe Europe | Various dates |

### Interoperability Model

- **Clearing Choice:** Trading participants on interoperable venues can choose which CCP clears their trades, enabling competition among CCPs
- **Cross-CCP Risk Management:** Interoperable CCPs maintain bilateral margin arrangements to cover inter-CCP exposures
- **Coverage:** By 2018, interoperability covered approximately 70% of European equity trades, with another 25% expected to gain clearing choice
- **Proven Resilience:** The LCH/x-clear interoperability link survived the Lehman Brothers collapse in 2008 without incident, serving as a template for subsequent interoperability arrangements

### Planned Integration (2025-2026)

- SIX announced in December 2025 the integration of SIX x-clear (Switzerland) and BME Clearing (Spain) into a single entity: **SIX Clearing**
- Headquartered in Madrid, with presences in Zurich and Oslo
- Will leverage BME Clearing's EU license for ECB EUR liquidity, T2, T2S access, and EU regulated market connectivity
- Combined entity will serve five asset classes across 28 trading venues and 18 markets
- Subject to regulatory approvals; 2026 focused on client readiness

[Source: SIX Group -- Integration Announcement, https://www.six-group.com/en/newsroom/media-releases/2025/20251204-six-clearing.html]
[Source: ESRB -- CCP Interoperability Arrangements, https://www.esrb.europa.eu/pub/pdf/reports/esrb.report190131_CCP_interoperability_arrangements~99908a78e7.en.pdf]

---

## 9. Recent Developments

| Date | Development |
|------|-------------|
| Dec 2025 | SIX announces integration of SIX x-clear and BME Clearing into "SIX Clearing" -- a single international, multi-asset CCP headquartered in Madrid |
| 2025 | SIX x-clear continues to expand interoperable clearing across European cash equity venues |
| 2025 | Post-trade results at SIX face headwinds from declining interest rates, motivating strategic consolidation |
| 2026 (planned) | Client preparation and migration planning for SIX Clearing integration |
| TBD | Regulatory approvals pending for the SIX x-clear / BME Clearing consolidation |

### Strategic Outlook

The formation of SIX Clearing represents a significant strategic move:
- Combines SIX x-clear's interoperable pan-European cash equity CCP model with BME Clearing's multi-asset capabilities (equities, fixed income, derivatives, energy, repos)
- Provides direct EU market access through BME Clearing's existing EU CCP license
- Positions the combined entity as an alternative to incumbent European CCPs (Eurex Clearing, LCH)
- Addresses the regulatory uncertainty around Swiss-EU equivalence

[Source: Finance Magnates -- SIX Pan-European Clearing, https://www.financemagnates.com/institutional-forex/exchanges/six-pushes-for-pan-european-clearing-crown-as-post-trade-results-face-rate-headwinds/]
[Source: Markets Media -- SIX Integrates CCPs, https://www.marketsmedia.com/six-integrates-ccps-to-position-for-growth/]

---

## Sources

- [SIX Group -- Clearing Services](https://www.six-group.com/en/products-services/securities-services/clearing.html)
- [SIX Group -- 20 Years of Clearing](https://www.six-group.com/en/newsroom/news/securities-services/2023/20-years-clearing-anniversary.html)
- [SIX Group -- Interoperability History](https://www.six-group.com/en/newsroom/news/securities-services/2023/interoperability-20-years-clearing-anniversary.html)
- [SIX Group -- SIX x-clear/BME Clearing Integration (Dec 2025)](https://www.six-group.com/en/newsroom/media-releases/2025/20251204-six-clearing.html)
- [SIX Group -- FINMA CCP Recognition (2018)](https://www.six-group.com/en/newsroom/archive/2018/20180406-SIXxclear.html)
- [SIX x-clear -- CPMI-IOSCO Disclosure](https://www.six-group.com/dam/download/securities-services/clearing/regulatory/consultation-responses/six-x-clear-iosco-en.pdf)
- [SIX Group -- Clearing & Settlement Provisions](https://www.six-group.com/en/products-services/the-swiss-stock-exchange/trading/trading-provisions/clearing-and-settlement.html)
- [FINMA -- Focus on Financial Market Infrastructures](https://www.finma.ch/en/enforcement/recovery-und-resolution-n/publikationen/resolution-report/archive/resolution-report/focus-on-financial-market-infrastructures/)
- [ESRB -- CCP Interoperability Arrangements (2019)](https://www.esrb.europa.eu/pub/pdf/reports/esrb.report190131_CCP_interoperability_arrangements~99908a78e7.en.pdf)
- [Finance Magnates -- SIX Pan-European Clearing](https://www.financemagnates.com/institutional-forex/exchanges/six-pushes-for-pan-european-clearing-crown-as-post-trade-results-face-rate-headwinds/)
- [IMF -- Switzerland FSAP 2019](https://www.imf.org/-/media/Files/Publications/CR/2019/1CHEEA2019010.ashx)
