# Japan Securities Clearing Corporation (JSCC)

> **Last Updated:** 2026-04-07
> **Research Tier:** Tier 2 (Standard)
> **Type:** CCP (Central Counterparty)

---

## 1. Overview & Profile

| Item | Details |
|------|---------|
| Official Name | Japan Securities Clearing Corporation (日本証券クリアリング機構) |
| Abbreviation | JSCC |
| Website | [https://www.jpx.co.jp/jscc/en/](https://www.jpx.co.jp/jscc/en/) |
| Year Established | 2002 (founded); January 2003 (commenced clearing operations) |
| Country / City | Japan / Tokyo |
| Ownership Structure | Wholly-owned subsidiary of Japan Exchange Group, Inc. (JPX) |
| Parent Company / Group | Japan Exchange Group, Inc. (JPX) -- listed on TSE (TYO: 8697) |
| Regulatory Authority | Japan Financial Services Agency (JFSA) -- primary supervisor; Bank of Japan (BOJ) -- oversight of IRS clearing activities |
| CPMI-IOSCO PFMI Compliance | Yes -- publishes PFMI Self-Assessment Disclosure (latest: March 31, 2025) and Quantitative Disclosures quarterly ([JSCC PFMI Disclosure](https://www.jpx.co.jp/jscc/en/company/cimhll0000000osu-att/JSCC_PFMI_Disclosure_20250331_EN.pdf)) |
| QCCP Status | Yes -- recognized as QCCP under EU CRR; exempt DCO under US CFTC (original order October 2015, amended September 2025); recognized in Canada (Ontario Securities Commission), Australia, Hong Kong, Singapore ([Source: JSCC Regulatory Status page](https://www.jpx.co.jp/jscc/en/company/regulatory-status.html)) |

> **JPX Group Structure:** JPX is a holding company that owns Tokyo Stock Exchange (TSE), Osaka Exchange (OSE), and JSCC as its three core operating subsidiaries. JSCC serves as the sole CCP for all exchange-traded products on TSE and OSE, as well as for OTC derivatives (IRS, CDS) and OTC JGB transactions. JSCC accounts for more than 10% of JPX's consolidated operating revenue. This vertically integrated model is comparable to KRX, where KRX itself performs clearing functions through its internal CCP division, though JSCC is a separate legal entity within the JPX group.

### Key Historical Milestones

| Year | Event |
|------|-------|
| 2002 | JSCC founded by five Japanese exchanges (TSE, Osaka Securities Exchange, Nagoya SE, Sapporo SE, Fukuoka SE) and the Japan Securities Dealers Association (JSDA) |
| 2003 (Jan) | Licensed as the first clearing organization in Japan to conduct "Securities Obligation Assumption Service" under the Securities and Exchange Law; commenced clearing for cash equity transactions on Japanese stock exchanges |
| 2004 | Expanded clearing to listed derivatives (futures and options) on Osaka Securities Exchange |
| 2007 | Began clearing for PTS (Proprietary Trading System) transactions |
| 2011 (Jul) | Launched CDS clearing service (initially started by TSE, transferred to JSCC) |
| 2012 (Oct) | Launched IRS (Interest Rate Swap) clearing service |
| 2013 (Jan) | Became a wholly-owned subsidiary of the newly formed Japan Exchange Group (JPX), following the merger of TSE Group and Osaka Securities Exchange |
| 2013 (Oct) | Launched OTC JGB clearing service (absorbed the clearing functions of Japan Government Bond Clearing Corporation, JGBCC) |
| 2014 | Japan implemented mandatory clearing obligation for certain OTC derivatives (CDS on iTraxx Japan index; JPY-denominated IRS) |
| 2018 (May) | JGB settlement cycle shortened to T+1 (from T+2) |
| 2019 (Jul) | Equities settlement cycle shortened from T+3 to T+2 |
| 2020 (Jul) | Merged with Japan Commodity Clearing House Co., Ltd. (JCCH); expanded clearing to listed commodity derivatives (TOCOM products: gold, rubber, energy, etc.) |
| 2023 (Nov) | Migrated margin methodology from SPAN to VaR for listed futures and options |
| 2024 (Mar) | Enhanced cross-margining between IRS and listed derivatives (3-month TONA futures included in IRS cross-margin) |
| 2024 | Won Asia Risk Awards "Clearing House of the Year"; IRS clearing volume doubled to record ¥8.3 quadrillion (US$56.3 trillion) |
| 2025 (Sep) | CFTC issued amended exempt DCO order and no-action letter allowing US customers to clear JPY IRS at JSCC |
| 2026 (Apr) | Listed Derivatives April 2026 Project go-live (April 13): VaR margin software upgrade to v4.0, new commodity products, enhanced margin offsets |

[Source: [JSCC History](https://www.jpx.co.jp/jscc/en/company/history.html); [Wikipedia](https://en.wikipedia.org/wiki/Japan_Securities_Clearing_Corporation); [Risk.net - Clearing house of the year: JSCC](https://www.risk.net/awards/7959892/clearing-house-of-the-year-jscc)]

---

## 2. Clearing Model

### 2.1 CCP Services

JSCC operates five distinct clearing businesses, each with its own separate default waterfall and clearing fund:

| Product Class | Service Description | Key Statistics |
|--------------|---------------------|----------------|
| **Cash Products** (Equities) | Clearing for all cash equity, ETF, REIT, and bond transactions on TSE, Nagoya SE, Sapporo SE, Fukuoka SE, and PTS venues (Japannext, Chi-X Japan, etc.) | 124 clearing participants (as of Jan 2024, combined with Listed Derivatives) |
| **Listed Derivatives** (Futures & Options) | Clearing for all listed financial and commodity derivatives on Osaka Exchange (index futures/options, JGB futures/options, TONA futures, commodity futures including gold, crude oil, rubber, electricity, LNG) | Separate default funds maintained for: Index Futures, JGB Futures, Petroleum Futures, Listed Commodity Derivatives |
| **IRS (Interest Rate Swaps)** | OTC clearing of JPY-denominated IRS (plain vanilla, OIS/TONA-based); also clears USD, EUR, AUD-denominated IRS | 26 clearing participants; ¥8.3 quadrillion cleared in 2024; ~60-70% global share of cleared JPY IRS; IM ~¥1.5-1.6 trillion ([Source: Clarus FT Q1 2025](https://www.clarusft.com/whats-new-in-ccp-disclosures-q1-2025/)) |
| **CDS (Credit Default Swaps)** | OTC clearing of iTraxx Japan index CDS | 11 clearing participants; IM ~¥62 billion (Q1 2025) ([Source: Clarus FT Q1 2025](https://www.clarusft.com/whats-new-in-ccp-disclosures-q1-2025/)) |
| **OTC JGB** | Clearing of OTC JGB cash and repo transactions | 41 clearing participants; ~80% of domestic JGB trades cleared at JSCC (no regulatory mandate) |

> **Comparison with KRX:** KRX acts as CCP internally for both exchange-traded equities and derivatives on its own markets, whereas JSCC is a separate legal entity serving multiple exchanges. Both operate as the sole domestic CCP for their respective exchange-traded products. JSCC's OTC clearing scope (IRS, CDS, JGB) is broader than KRX's current CCP services.

### 2.2 Novation Process

- **Exchange-traded products (equities, listed derivatives):** JSCC assumes obligations through novation at the point of trade execution on the exchange. JSCC becomes the buyer to every seller and seller to every buyer, extinguishing the original bilateral obligation between trading counterparties.
- **OTC derivatives (IRS, CDS):** Upon trade registration/acceptance by JSCC, the original bilateral contract is extinguished and replaced by two new contracts -- one between JSCC and each original counterparty.
- **OTC JGB:** Similar novation upon registration; JSCC assumes the obligation for both delivery and payment.

[Source: [JSCC DVP Settlement System](https://www.jpx.co.jp/jscc/en/cash/cash/assumption-obligation/dvp.html)]

### 2.3 Netting

- **Cash Products:** Multilateral netting of delivery and payment obligations among all clearing participants. Securities delivery obligations and payment obligations are netted separately per issue and per settlement date, resulting in a single net obligation per participant per issue.
- **Listed Derivatives:** Daily mark-to-market with netting of variation margin payments. At expiry/exercise, physical delivery obligations (e.g., JGB futures) are netted.
- **IRS:** Multilateral netting of payment obligations on each payment date.
- **OTC JGB:** Multilateral netting of both securities delivery and cash payment obligations (bilateral netting for repo transactions, multilateral netting for outright transactions).

### 2.4 Clearing Membership

JSCC maintains separate clearing qualifications for each clearing business. A firm may hold clearing qualifications for one or more businesses.

| Clearing Business | Participant Types | Requirements | Number of Members (approx.) |
|-------------------|-------------------|--------------|----------------------------|
| Cash Products | Clearing Participant; Non-Clearing Participant (routes through a Clearing Participant) | Net assets, capital adequacy ratio, operational capability, BOJ current account or designated settlement bank | ~100+ (combined with Listed Derivatives: 124 as of Jan 2024) |
| Listed Derivatives | Clearing Participant (separate qualifications for Index Futures, JGB Futures, Commodity Derivatives) | Minimum net assets, sufficient financial resources, operational systems, contribution to clearing fund | Included in the 124 above |
| IRS | IRS Clearing Participant; Client Clearing (introduced for buy-side access) | Minimum net assets ¥10 billion [unverified]; operational capability for OTC derivatives; ISDA membership typical | 26 |
| CDS | CDS Clearing Participant | Minimum net assets; CDS trading/risk management capability | 11 |
| OTC JGB | JGB Clearing Participant | Financial requirements; BOJ-NET access for settlement | 41 |

> **Note:** JSCC's September 2025 CFTC amended exemption allows US-based eligible contract participants (ECPs) to clear JPY IRS through non-US JSCC clearing members that are affiliates of CFTC-registered FCMs. This is a client clearing arrangement, not direct membership. [Source: [CFTC Letter No. 25-32](https://www.cftc.gov/csl/25-32/download)]

---

## 3. Risk Management

### 3.1 Margin Framework

JSCC transitioned its listed derivatives margin methodology from SPAN to VaR in November 2023, a major reform after years of industry consultation.

| Product Class | Methodology | Confidence Level | Holding Period | Key Details |
|--------------|-------------|-----------------|----------------|-------------|
| **Cash Products** (Equities) | VaR-based (DVP margin for settlement risk) | 99% [unverified] | T+2 settlement exposure | Margin calculated based on the potential price fluctuation during the settlement period; collateral accepted includes cash and eligible securities |
| **Listed Derivatives** (Futures & Options) | **VaR** (since Nov 2023; previously SPAN) -- two methods: Historical Simulation VaR (HS-VaR) and Alternative Simulation VaR (AS-VaR) | 99% or higher | 1-2 days (product-dependent) | VaR uses 1,250+ historical data points (vs. SPAN's 16 scenarios); provides more market-sensitive margin requirements; VaR Margin Software (VMA) v3.0, upgrading to v4.0 in April 2026 |
| **IRS** | Historical Simulation -- Expected Shortfall (HS-ES) | Average of worst 1% (ES) | 5 days (house); 7 days (client) | Reference period: 1,250 business days; covers interest rate fluctuation risk on NPV; also includes concentration add-on and liquidity risk charges |
| **CDS** | VaR / Expected Shortfall | 99.5%+ [unverified] | 5 days | Covers spread risk, jump-to-default risk; initially adopted VaR in July 2011 |
| **OTC JGB** | VaR-based | 99%+ [unverified] | 1-2 days [unverified] | Covers price fluctuation risk during the settlement period |

**Cross-Margining:** Since March 2024, JSCC provides cross-margin functionality between IRS positions and listed derivatives (particularly 3-month TONA futures and 10-year JGB futures). Estimated margin reduction: 50-60% for a sample portfolio combining TONA OIS, TONA futures, and JGB futures positions. [Source: [Risk.net - Clearing house of the year: JSCC](https://www.risk.net/awards/7959892/clearing-house-of-the-year-jscc)]

> **Comparison with KRX:** KRX uses a modified SPAN-based methodology (KRX-SPAN) for listed derivatives and a VaR-based method for OTC clearing. JSCC's migration from SPAN to VaR in November 2023 aligns it more closely with global trends (LCH, Eurex have long used VaR/PRISMA), while KRX still relies on its SPAN-derived system for listed derivatives.

### 3.2 Margin Call Schedule

| Product Class | Regular Margin Call | Intraday Margin Call |
|--------------|--------------------|--------------------|
| Cash Products | End-of-day calculation; payment by next morning before settlement | Intraday calls possible in volatile markets |
| Listed Derivatives | End-of-day calculation; payment by start of next business day | Intraday margin calls triggered when unrealized losses exceed thresholds |
| IRS | Daily margin call based on end-of-day valuation | Intraday margin calls in stressed conditions |
| CDS | Daily margin call | Intraday calls possible |
| OTC JGB | Daily margin call | Intraday calls possible |

[Source: [JSCC Margin page](https://www.jpx.co.jp/jscc/en/risk/margin.html)]

### 3.3 Default Waterfall

JSCC maintains **separate default waterfalls** for each clearing business. The fundamental principle is "Defaulter Pays First" -- the defaulting member's own resources are exhausted before any mutualized resources are used. JSCC interposes its own capital ("skin in the game") between the defaulter's resources and the mutualized clearing fund, maintaining incentive alignment.

#### General Default Waterfall Structure (applicable across clearing businesses):

| Layer | Resource | Description | Approximate Size |
|-------|----------|-------------|-----------------|
| **1** | Defaulter's Margin | Initial margin, variation margin, and any other collateral deposited by the defaulting clearing participant | Varies by participant |
| **2** | Defaulter's Clearing Fund Contribution | The defaulting participant's contribution to the relevant clearing fund | Varies by participant |
| **3** | JSCC's Own Resources (First Tier -- Settlement Guarantee Reserve) | JSCC's dedicated capital contribution ("skin in the game") -- funded from JSCC's stockholders' equity | Varies by business; e.g., IRS: up to ¥2 billion; Listed Derivatives: funded partly from ¥9.1 billion total settlement guarantee reserve (of which ¥7 billion from OSE for non-energy commodity futures) |
| **4** | Non-Defaulting Participants' Clearing Fund + JSCC Additional Contribution (Second Tier) | Mutualized clearing fund contributions from surviving members, consumed pro rata alongside additional JSCC capital contribution | See Clearing Fund sizes below |
| **5** | Assessment Powers (Special Clearing Charge) | JSCC may levy additional assessments on non-defaulting clearing participants (capped, typically up to the amount of their clearing fund contribution) | Up to 1x clearing fund contribution [unverified] |
| **6** | JSCC Remaining Capital / Recovery Tools | Remaining JSCC equity; potential application of variation margin gains haircutting (VMGH); partial tear-up of positions | JSCC residual equity |

> **Note on IRS waterfall specifics:** JSCC contributes up to ¥2 billion as First Tier IRS Settlement Guarantee Reserve, plus an additional ¥2 billion consumed pro rata with non-defaulting participants' IRS Clearing Fund (total JSCC "Compensation Capital" for IRS: up to ¥4 billion). [Source: [JSCC Loss Compensation page](https://www.jpx.co.jp/jscc/en/risk/default-waterfall.html); [OSC JSCC Exemption Application](https://www.osc.ca/sites/default/files/2024-07/jscc_20240718_application-exemption_0.pdf)]

### 3.4 Default Fund / Guarantee Fund

JSCC operates **separate clearing funds** for each clearing business. The required size is calibrated to cover the simultaneous default of the two largest clearing participants (Cover 2 standard) for most products.

| Clearing Business | Default Coverage Standard | Approximate Clearing Fund Size | Notes |
|-------------------|--------------------------|-------------------------------|-------|
| Cash Products | Cover 2 | [unverified -- included in overall listed figures] | Funded by clearing participant contributions |
| Listed Derivatives -- JGB Futures & Options | Cover 2 | ¥64.7 billion ($435 million, Q4 2024) -- up 52.4% YoY | Significant increase driven by BOJ policy normalization and JGB volatility ([Source: Risk.net](https://www.risk.net/risk-quantum/7961205/jscc-dtcc-government-bond-units-see-default-fund-surge)) |
| Listed Derivatives -- Index Futures | Cover 2 | [unverified -- separate fund] | |
| Listed Derivatives -- Commodity | Cover 1 (largest single participant) for non-petroleum; Cover 2 for petroleum | [unverified] | Includes ¥7 billion OSE-funded settlement guarantee reserve for non-energy commodities |
| IRS | Cover 2 | Minimum contribution: ¥100 million per participant; total IRS IM ~¥1.5 trillion | Clearing fund sized to cover excess loss beyond margin for top 2 defaults |
| CDS | Cover 2 | [unverified -- smaller fund given 11 participants] | |
| OTC JGB | Cover 2 | ¥237.0 billion (as of June 2025) | Largest single clearing fund, reflecting the massive size of Japan's JGB market |

> **JSCC is considering consolidating its 10 separate default funds within the listed derivatives segment** as part of broader membership and default management reforms (as of early 2026). This could simplify the structure and potentially provide better mutualization of risk. [Source: [Risk.net](https://www.risk.net/risk-management/7963158/jscc-considers-default-fund-consolidation)]

### 3.5 Stress Testing & Back-testing

- **Stress Testing:** JSCC conducts regular stress testing of its margin and clearing fund adequacy using both historical and hypothetical scenarios. Stress scenarios cover extreme market movements (e.g., 2008 financial crisis, 2011 earthquake, 2020 COVID shock, BOJ policy shifts).
- **Back-testing:** Daily back-testing of margin model adequacy; results are published in PQD disclosures. The VaR model targets at least 99% coverage, meaning margin should cover actual portfolio losses on at least 99% of days.
- **Reverse Stress Testing:** JSCC conducts reverse stress tests to identify scenarios that could exhaust default resources.
- **Frequency:** Stress tests and back-tests are conducted at least monthly for clearing fund adequacy and daily for margin adequacy.

[Source: [JSCC PFMI Disclosure](https://www.jpx.co.jp/jscc/en/company/cimhll0000000osu-att/JSCC_PFMI_Disclosure_20250331_EN.pdf)]

### 3.6 Recovery & Resolution

- **Recovery Tools:**
  - **Assessment powers:** JSCC can levy Special Clearing Charges on non-defaulting participants (capped amounts).
  - **Variation Margin Gains Haircutting (VMGH):** Available for IRS and CDS clearing; haircuts applied to VM payments to in-the-money participants.
  - **Partial tear-up:** JSCC has the power to terminate some or all of the defaulter's positions through auction or forced allocation to surviving members.
  - **Position auction:** For IRS, CDS, and OTC JGB, non-defaulting participants participate in an auction process to absorb the defaulter's portfolio.
- **Resolution Authority:** JFSA has resolution authority over JSCC under the Financial Instruments and Exchange Act (FIEA). The JFSA can issue business improvement orders, conduct inspections, and ultimately rescind JSCC's license.
- **No separate CCP resolution regime:** Japan does not have a dedicated CCP recovery and resolution framework comparable to the EU's CCP Recovery and Resolution Regulation (CCPRRR). Resolution relies on existing FIEA powers. [unverified]

> **Comparison with KRX:** KRX's default management relies on the defaulter's margin, KRX's own Joint Compensation Fund contribution, and then the non-defaulting members' Joint Compensation Fund. KRX also maintains a Settlement Risk Fund. Both KRX and JSCC follow the "defaulter pays first" principle, but JSCC's framework is more granular with separate waterfalls per product class.

---

## 4. Settlement

### 4.1 Settlement Cycle

| Product | Settlement Cycle | Notes |
|---------|-----------------|-------|
| Cash Equities (TSE and other exchanges) | **T+2** | Shortened from T+3 on July 16, 2019 |
| Listed Derivatives | T+1 (for daily settlement / VM); Physical delivery varies | JGB futures physical delivery on T+2 of delivery date |
| IRS | Varies by payment frequency | Cash settlement of net payment obligations |
| CDS | Per ISDA standard settlement terms | |
| OTC JGB (Outright) | **T+1** | Shortened from T+2 on May 1, 2018 |
| OTC JGB (Repo) | Varies (T+0 to T+1 typical) | |

> **Note on T+1 for equities:** As of April 2026, Japan has not yet formally announced a transition to T+1 for cash equities, unlike the US (moved to T+1 in May 2024). The industry is monitoring global trends, but no specific timeline has been set. [unverified]

### 4.2 DVP Model

- **Cash Products:** JSCC operates a DVP (Delivery Versus Payment) settlement system that ensures simultaneous, gross settlement of both securities and funds. Securities can only be delivered on condition that payment is completed, and vice versa. Settlement is final at the point of transfer.
- **DVP Model:** JSCC uses a **DVP Model 3** approach for exchange-traded cash products -- securities are settled on a net basis through JASDEC's book-entry transfer system, while funds are settled on a net basis through BOJ-NET (for BOJ current account holders) or designated settlement banks.
- **OTC JGB:** DVP settlement through BOJ-NET, with securities and cash legs settled simultaneously.

[Source: [JSCC DVP Settlement System](https://www.jpx.co.jp/jscc/en/cash/cash/assumption-obligation/dvp.html)]

### 4.3 Settlement Finality

- Under JSCC's DVP settlement scheme, settlement of cash and securities between a clearing participant and JSCC is **final and irrevocable at the time of transfer**.
- The legal basis for settlement finality is provided by the Financial Instruments and Exchange Act (FIEA) and the Act on Book-Entry Transfer of Company Bonds, Shares, etc.
- BOJ-NET transfers are final under the Bank of Japan Act.
- JASDEC book-entry transfers are final under the Book-Entry Transfer Act.

[Source: [JSCC Settlement page](https://www.jpx.co.jp/jscc/en/risk/collateral/settlement.html)]

### 4.4 CSD / Settlement Infrastructure

| Infrastructure | Role | Operator |
|---------------|------|----------|
| **JASDEC** (Japan Securities Depository Center, Inc.) | CSD for equities, corporate bonds, investment trusts, and other securities; operates the book-entry transfer system | Private sector entity; designated CSD under the Book-Entry Transfer Act |
| **BOJ-NET** (Bank of Japan Financial Network System) | RTGS system for interbank fund settlement; also handles JGB book-entry transfers | Bank of Japan |
| **JDCC** (JASDEC DVP Clearing Corporation) | CCP for off-exchange (non-exchange transaction deliveries, NETDs) securities settlement through JASDEC's DVP system | Subsidiary of JASDEC |

> **Settlement flow for exchange-traded equities:** Trade on TSE/other exchanges --> Clearing by JSCC (novation + multilateral netting) --> Securities delivery via JASDEC book-entry transfer --> Funds settlement via BOJ-NET or designated settlement banks --> DVP finality

> **Comparison with KRX:** In Korea, KSD (Korea Securities Depository) serves as both the CSD and the settlement agent, while KRX acts as CCP. The structure is similar to Japan's JASDEC + JSCC arrangement. Both countries use a DVP Model 3 approach for equities settlement.

### 4.5 CSD Linkages

- **JASDEC:** Primary domestic CSD linkage for all equity and corporate bond settlement.
- **BOJ (as JGB CSD):** JGB settlement occurs through BOJ-NET's book-entry system, not JASDEC.
- **International linkages:** JASDEC maintains linkages with international CSDs (Euroclear, Clearstream) for cross-border settlement of Japanese securities, though these are JASDEC's linkages rather than JSCC's directly.

### 4.6 Securities Lending & Borrowing

- JSCC operates a securities lending facility to support settlement of cash products, allowing clearing participants to borrow securities to fulfill delivery obligations and avoid settlement fails.
- For JGB transactions, the BOJ also operates a Securities Lending Facility (SLF) that supports market liquidity.

---

## 5. Technology & Infrastructure

### 5.1 Interface Protocols

| System / Protocol | Description |
|------------------|-------------|
| **Clearing System** | JSCC operates proprietary clearing systems for each clearing business; connected to exchanges (TSE arrowhead, OSE J-GATE) for trade feed |
| **JASDEC Connection** | Interface with JASDEC's book-entry transfer system for securities settlement (proprietary protocol) |
| **BOJ-NET Connection** | Interface with BOJ-NET for funds settlement and JGB transfers |
| **IRS Clearing Platform** | Accepts trade registrations from trade matching platforms (e.g., MarkitWire/DTCC, Tradeweb) and trade execution platforms (SEFs) |
| **VaR Margin Software (VMA)** | Proprietary margin calculation engine; currently v3.0, upgrading to v4.0 in April 2026; clearing participants can run the same software for pre-trade margin estimation |
| **PTS Connectivity** | Connected to multiple PTS venues (Japannext, Chi-X Japan) for clearing of off-exchange equity trades |
| **FIX Protocol** | Used for certain connectivity with PTS and international participants [unverified] |

### 5.2 Resilience

- **Business Continuity Planning (BCP):** JSCC maintains comprehensive BCP arrangements including a secondary operations site (backup center) geographically separated from the primary site.
- **RPO/RTO:** Recovery Time Objective of 2 hours for critical systems [unverified]; Recovery Point Objective targets zero data loss.
- **System Availability:** JSCC's systems are designed for high availability consistent with PFMI Principle 17 requirements.
- **Cyber Security:** JSCC participates in JPX group-wide cyber security initiatives and information sharing arrangements.
- **Collateral Tokenization Pilot:** JSCC participated in a DTCC industry sandbox initiative exploring how CCPs could use tokenization technology to optimize collateral management processes for clearing members and buy-side firms, including margin call automation. [Source: [Risk.net](https://www.risk.net/awards/7959892/clearing-house-of-the-year-jscc)]

---

## 6. Regulatory Framework

### 6.1 Supervising Authority

| Authority | Role |
|-----------|------|
| **JFSA (Japan Financial Services Agency)** | Primary regulator and supervisor; licenses JSCC as a Financial Instruments Clearing Organization under the FIEA; conducts inspections; issues business improvement orders |
| **Bank of Japan (BOJ)** | Oversight of JSCC, particularly for IRS clearing and systemically important payment/settlement systems; conducts joint inspections with JFSA |
| **Ministry of Economy, Trade and Industry (METI)** | Supervisory role for commodity derivatives clearing (joint supervision with JFSA following TOCOM integration) [unverified] |

### 6.2 Key Regulations

| Regulation | Description |
|-----------|-------------|
| **Financial Instruments and Exchange Act (FIEA)** | Primary law governing JSCC's CCP activities; Article 2, Paragraph 29 defines "Financial Instruments Obligation Assumption Services" |
| **Cabinet Office Ordinance on Financial Instruments Clearing Organizations** | Detailed rules for CCP operations, risk management, capital requirements |
| **JSCC Business Rules** | JSCC's own rulebook governing clearing qualification, margin, default management, settlement, and fees for each clearing business |
| **Commodity Derivatives Act** | Governs commodity derivatives clearing (applicable post-TOCOM integration) |
| **Act on Book-Entry Transfer of Company Bonds, Shares, etc.** | Governs book-entry transfer and settlement finality for securities |

### 6.3 PFMI Compliance

- JSCC publishes comprehensive PFMI (Principles for Financial Market Infrastructures) self-assessment disclosures, most recently updated March 31, 2025.
- The disclosure covers all 24 PFMI principles applicable to CCPs.
- JSCC also publishes quarterly CPMI-IOSCO Public Quantitative Disclosures (PQD), providing over 200 quantitative data fields covering margin, default resources, credit risk, collateral, liquidity risk, and back-testing.
- The PQD data is available on the [JSCC Quantitative Disclosure page](https://www.jpx.co.jp/jscc/en/company/fmi-pdf2.html) and is also aggregated by CCP Global.

[Source: [JSCC PFMI Disclosure (March 2025)](https://www.jpx.co.jp/jscc/en/company/cimhll0000000osu-att/JSCC_PFMI_Disclosure_20250331_EN.pdf)]

### 6.4 Reporting Requirements

- **Trade Reporting:** OTC derivative transactions (IRS, CDS) must be reported to a licensed trade repository under JFSA rules, consistent with G20 commitments.
- **Clearing Obligation:** Japan mandates clearing for certain OTC derivatives -- specifically, JPY-denominated plain vanilla IRS and iTraxx Japan CDS indices -- at a licensed CCP (JSCC is the only eligible CCP).
- **PQD Disclosure:** Quarterly public quantitative disclosure following CPMI-IOSCO standards.
- **Annual Reporting:** JSCC submits annual reports and financial statements to JFSA.

---

## 7. Interoperability

### 7.1 CCP Interoperability Arrangements

- JSCC does **not** currently operate any CCP interoperability arrangements (CCP links) with other CCPs.
- As the sole CCP for Japanese exchange-traded products and the dominant CCP for JPY OTC derivatives, there has been limited demand for interoperability.

> **Comparison with KRX:** Like KRX, JSCC operates as a domestic monopoly CCP without interoperability links. This contrasts with European CCPs (e.g., LCH EquityClear, Eurex Clearing, Cboe Clear Europe) which operate interoperable clearing arrangements for cash equities.

### 7.2 Cross-border Arrangements

| Jurisdiction | Status | Details |
|-------------|--------|---------|
| **United States (CFTC)** | Exempt DCO | Original exemption order October 2015; amended September 2025 to allow US customer clearing of JPY IRS under specified conditions ([Source: CFTC](https://www.cftc.gov/media/12671/JSCC%20AmendedExemptionOrder_09-12-2025/download)) |
| **European Union (ESMA)** | Third-country CCP recognition; QCCP status | EU clearing participants can clear at JSCC with favorable capital treatment |
| **Canada (Ontario)** | Exempt clearing agency | OSC granted exemption for JSCC (2024 application) ([Source: OSC](https://www.osc.ca/en/securities-law/orders-rulings-decisions/japan-securities-clearing-corporation-s-147)) |
| **Australia (ASIC)** | Recognized [unverified] | Allows Australian participants to access JSCC |
| **Hong Kong (SFC)** | Recognized [unverified] | |
| **Singapore (MAS)** | Recognized [unverified] | |

---

## 8. Fees

### 8.1 Clearing Fees

JSCC's clearing fees are generally considered competitive -- reportedly around half to one-third of fees charged by other major global CCPs for comparable OTC products.

| Product Class | Fee Structure | Key Rates |
|--------------|--------------|-----------|
| **Cash Products** (Equities) | Per-transaction fee based on trade value | Varies by exchange and trade type; details on [JSCC fee schedule](https://www.jpx.co.jp/jscc/en/cash/futures/fee.html) |
| **Listed Derivatives** | Per-contract fee varying by product type | Product-specific; e.g., JGB Futures, Index Futures, Commodity Futures each have separate rates |
| **IRS** | Notional-based fee | Competitive with global CCPs; specific rates not publicly summarized in a single source |
| **CDS** | Notional-based fee | |
| **OTC JGB** | Transaction-based fee | |

[Source: [JSCC Clearing Fee -- Listed Derivatives](https://www.jpx.co.jp/jscc/en/cash/futures/fee/derivativesfee.html)]

### 8.2 Membership Fees

| Fee Type | Amount | Notes |
|----------|--------|-------|
| JGB Futures Clearing Qualification -- Monthly Fee | ¥100,000 | Waived if monthly clearing fees exceed ¥100,000 |
| Index Futures Clearing Qualification -- Monthly Fee | ¥120,000 | Waived if monthly clearing fees exceed ¥100,000 |
| Other qualification fees | Varies | Each clearing business has its own qualification and monthly fee structure |

[Source: [JSCC Clearing Fee page](https://www.jpx.co.jp/jscc/en/cash/futures/fee.html)]

---

## 9. Recent Developments

### 2024
- **Record IRS clearing volume:** JSCC cleared ¥8.3 quadrillion (US$56.3 trillion) in JPY IRS in 2024, doubling the 2023 record. Monthly clearing volume surpassed ¥1,000 trillion for the first time in December 2024. This growth was driven by Japan's changing interest-rate environment as the BOJ exited its ultra-loose monetary policy. [Source: [Risk.net](https://www.risk.net/insight/markets/7962837/japan%E2%80%99s-yen-swaps-go-global)]
- **Cross-margin enhancement:** March 2024 -- 3-month TONA futures included in IRS cross-margin functionality, enabling estimated 50-60% margin reduction for combined portfolios.
- **Asia Risk Award:** Won "Clearing House of the Year" at Asia Risk Awards 2024 for VaR migration and cross-margin innovation.
- **CFTC engagement:** Intensified discussions with CFTC regarding US customer access to JSCC's IRS clearing service.

### 2025
- **CFTC breakthrough (September 2025):** CFTC issued amended exempt DCO order and no-action letter (Letter No. 25-32) permitting US customers (eligible contract participants) to clear JPY IRS at JSCC through non-US clearing member affiliates of CFTC-registered FCMs. This was a landmark achievement removing a long-standing impediment. [Source: [CFTC](https://www.cftc.gov/csl/25-32/download)]
- **Initial margin reform proposals:** JSCC consulted with clearing members on further refinements to initial margin and clearing fund calculation methods for listed derivatives. [Source: [FIA](https://www.fia.org/fia/articles/fia-responds-jscc-consultation-initial-margin-and-clearing-fund-calculation-methods)]

### 2026
- **Listed Derivatives April 2026 Project (go-live April 13, 2026):** Major system upgrade including VaR Margin Software upgrade from v3.0 to v4.0, improved VaR margin calculation methodology, new commodity products (Pocket Gold 100 Futures, Pocket Platinum 100 Futures), and enhanced margin offsets across asset classes. [Source: [JSCC News](https://www.jpx.co.jp/jscc/en/information/news/tsnlk000000121hh1.html)]
- **Default fund consolidation review:** JSCC is considering reorganizing its 10 separate default funds within the listed derivatives segment into a consolidated structure, as part of a broader review of membership and default management. [Source: [Risk.net](https://www.risk.net/risk-management/7963158/jscc-considers-default-fund-consolidation)]
- **Collateral tokenization:** JSCC continues to participate in DTCC-led industry sandbox exploring tokenization of collateral for margin optimization.

---

## Sources

### Official JSCC / JPX Sources
- [JSCC Official Website](https://www.jpx.co.jp/jscc/en/)
- [JSCC Company Profile](https://www.jpx.co.jp/jscc/en/company/profile.html)
- [JSCC History](https://www.jpx.co.jp/jscc/en/company/history.html)
- [JSCC Regulatory Status](https://www.jpx.co.jp/jscc/en/company/regulatory-status.html)
- [JSCC Loss Compensation (Default Waterfall)](https://www.jpx.co.jp/jscc/en/risk/default-waterfall.html)
- [JSCC Clearing Fund](https://www.jpx.co.jp/jscc/en/risk/clearing-fund.html)
- [JSCC Margin](https://www.jpx.co.jp/jscc/en/risk/margin.html)
- [JSCC DVP Settlement System](https://www.jpx.co.jp/jscc/en/cash/cash/assumption-obligation/dvp.html)
- [JSCC Clearing Fees -- Listed Derivatives](https://www.jpx.co.jp/jscc/en/cash/futures/fee/derivativesfee.html)
- [JSCC PFMI Disclosure (March 31, 2025)](https://www.jpx.co.jp/jscc/en/company/cimhll0000000osu-att/JSCC_PFMI_Disclosure_20250331_EN.pdf)
- [JSCC Quantitative Disclosure Page](https://www.jpx.co.jp/jscc/en/company/fmi-pdf2.html)
- [JSCC Corporate Information (July 2025)](https://www.jpx.co.jp/jscc/en/company/rkra7f00000001jl-att/corporateinfo_202507_en.pdf)
- [JSCC Listed Derivatives April 2026 Project](https://www.jpx.co.jp/jscc/en/information/news/tsnlk000000121hh1.html)
- [JPX Working Paper: Migration to New Margin Calculation Method](https://www.jpx.co.jp/english/corporate/research-study/working-paper/JPXWP_Vol45e.pdf)

### Regulatory Sources
- [CFTC -- JSCC Amended Exemption Order (September 2025)](https://www.cftc.gov/media/12671/JSCC%20AmendedExemptionOrder_09-12-2025/download)
- [CFTC Letter No. 25-32 -- No-Action (September 2025)](https://www.cftc.gov/csl/25-32/download)
- [Ontario Securities Commission -- JSCC Exemption Application (July 2024)](https://www.osc.ca/sites/default/files/2024-07/jscc_20240718_application-exemption_0.pdf)
- [JSDA -- Move to T+2 Settlement in Japan](https://www.jsda.or.jp/en/activities/research-studies/files/t2_en_cyukan_201603.pdf)

### Industry / Analytics Sources
- [Clarus FT -- What's New in CCP Disclosures Q1 2025](https://www.clarusft.com/whats-new-in-ccp-disclosures-q1-2025/)
- [Clarus FT -- What's New in CCP Disclosures 4Q24](https://www.clarusft.com/whats-new-in-ccp-disclosures-4q24/)
- [Risk.net -- Clearing House of the Year: JSCC (2024)](https://www.risk.net/awards/7959892/clearing-house-of-the-year-jscc)
- [Risk.net -- Clearing Members Welcome JSCC Initial Margin Reforms](https://www.risk.net/risk-management/7959997/clearing-members-welcome-jscc-initial-margin-reforms)
- [Risk.net -- JSCC Considers Default Fund Consolidation](https://www.risk.net/risk-management/7963158/jscc-considers-default-fund-consolidation)
- [Risk.net -- JSCC, DTCC Government Bond Units See Default Funds Surge](https://www.risk.net/risk-quantum/7961205/jscc-dtcc-government-bond-units-see-default-fund-surge)
- [Risk.net -- Japan's Yen Swaps Go Global](https://www.risk.net/insight/markets/7962837/japan%E2%80%99s-yen-swaps-go-global)
- [CCP Global -- The Year in Clearing: 2024](https://ccp-global.org/sites/default/files/2025-07/CCPG_2024_Clearing%20Report_17.07.2025.pdf)
- [FIA -- Response to JSCC Consultation on IM and Clearing Fund](https://www.fia.org/fia/articles/fia-responds-jscc-consultation-initial-margin-and-clearing-fund-calculation-methods)
- [WFE Focus -- Addressing Global OTC Derivative Clearing Mandates](https://focus.world-exchanges.org/articles/jscc-derivatives-clearing)
- [OpenGamma -- Clearing with JSCC for JPY IRS Trading](https://opengamma.com/clearing-with-jscc/)
- [Wikipedia -- Japan Securities Clearing Corporation](https://en.wikipedia.org/wiki/Japan_Securities_Clearing_Corporation)

### Settlement Infrastructure Sources
- [JASDEC -- DVP Settlement System](https://www.jasdec.com/en/system/dvp/)
- [Clearstream -- Settlement Process Japan](https://www.clearstream.com/clearstream-en/res-library/market-coverage/settlement-process-japan-1283556)
- [BIS -- Payment, Clearing and Settlement Systems in Japan (Red Book)](https://www.bis.org/publ/cpss105_jp.pdf)
- [Bank of Japan -- Payment and Settlement Systems Report](https://www.boj.or.jp/en/research/brp/psr/data/psr190426.pdf)
