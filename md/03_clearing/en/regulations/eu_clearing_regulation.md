# EU Clearing & Settlement Regulation

> **Last Updated:** 2026-04-07
> **Status:** Comprehensive draft

---

## 1. Regulatory Authorities

### 1.1 ESMA (European Securities and Markets Authority)

**CCP Supervision Role:**
- ESMA serves as the central supervisory authority for CCPs in the EU, with its role significantly enhanced under EMIR 2.2 (2019) and further strengthened by EMIR 3.0 (2024).
- Under EMIR 3.0, ESMA has been granted expanded direct supervision powers over EU CCPs, particularly regarding the monitoring of systemic risk and the enforcement of the Active Account Requirement (AAR).
- As of March 2026, ESMA supervises a diverse set of over 50 entities across 21 countries, ranging from small specialized firms to large global players.
[Source: ESMA, "Supervision," https://www.esma.europa.eu/esmas-activities/supervision; ESMA 2026 Annual Work Programme]

**CCP Supervisory Committee:**
- Established under EMIR 2.2, the CCP Supervisory Committee is an internal committee of ESMA responsible for:
  - Preparing decisions relating to the supervision of third-country CCPs (TC-CCPs)
  - Coordinating with national competent authorities (NCAs) on CCP oversight
  - Conducting tiering assessments of TC-CCPs (Tier 1 vs. Tier 2)
  - Overseeing CCP stress tests and risk model validation
- The Committee is chaired by an independent Chair and includes representatives from NCAs and the ECB.
[Source: ESMA, "CCP Policy," https://www.esma.europa.eu/central-counterparties/ccp-policy]

**Third-Country CCP Recognition:**
- Under EMIR Article 25, ESMA is responsible for recognizing third-country CCPs that wish to provide clearing services to EU clearing members or trading venues.
- Recognition requires:
  1. An equivalence decision by the European Commission for the third country's legal and supervisory framework
  2. Cooperation arrangements (MoUs) between ESMA and the relevant third-country authority
  3. A tiering determination (Tier 1 or Tier 2)
- **Tier 1 TC-CCPs:** Not systemically important to the EU; subject to lighter supervision with reliance on home-country regulation.
- **Tier 2 TC-CCPs:** Systemically important to the EU or likely to become so; must comply with relevant EMIR requirements (directly or via "comparable compliance") and are subject to direct ESMA supervision.
- Since recognizing two UK CCPs (LCH Ltd, ICE Clear Europe) as Tier 2 in 2022, ESMA has conducted four annual review assessments, validated numerous changes to their risk models, and conducted two CCP stress test exercises (as of March 2026).
[Source: ESMA, "Third-Country CCPs," https://www.esma.europa.eu/central-counterparties/third-country-ccps; ESMA 2026 AWP]

### 1.2 National Competent Authorities (NCAs)

**Role in CCP Authorization:**
- NCAs remain the primary authority for authorizing EU-based CCPs under EMIR.
- The authorization process requires the NCA to:
  - Conduct a risk assessment of the applicant CCP
  - Establish and chair a supervisory college
  - Ensure all EMIR organizational, conduct, and prudential requirements are met
  - Consult with ESMA and the relevant college members
- NCAs supervise authorized EU CCPs on an ongoing basis, subject to ESMA coordination.
[Source: FMA Austria, "Authorisation & Ongoing Supervision," https://www.fma.gv.at/en/capital-markets/emir/authorisation-ongoing-supervision/]

**CSD Authorization under CSDR:**
- Under CSDR (Regulation (EU) No 909/2014), NCAs are responsible for authorizing CSDs established in their jurisdiction.
- Authorization requirements include organizational structure, governance, capital adequacy, and operational resilience.
- NCAs also supervise ongoing compliance with CSDR requirements, including settlement discipline obligations.
[Source: ESMA, "Central Securities Depositories," https://www.esma.europa.eu/esmas-activities/markets-and-infrastructure/central-securities-depositories]

**Colleges of Supervisors:**
- For each authorized EU CCP, a college of supervisors is established comprising:
  - The CCP's NCA (as chair)
  - ESMA representatives
  - NCAs of the most relevant clearing members
  - NCAs of trading venues served by the CCP
  - NCAs of interoperable CCPs
  - Relevant central banks of issue
- The college facilitates information exchange, coordinates supervisory activities, and provides opinions on CCP authorization and significant rule changes.
[Source: ESMA, "Opinion on the composition of CCP colleges under EMIR," ESMA/2015/838]

### 1.3 ECB / National Central Banks

**Role in Settlement Oversight:**
- The ECB and Eurosystem central banks have an oversight role for payment and settlement systems under the Treaty on the Functioning of the EU.
- The ECB participates in CCP supervisory colleges as the central bank of issue for the euro.
- National central banks oversee CSDs in their jurisdictions in coordination with NCAs, particularly regarding settlement in central bank money.
[Source: ECB, "TARGET2-Securities," https://www.ecb.europa.eu/paym/target/t2s/html/index.en.html]

**T2S Governance:**
- The TARGET2-Securities (T2S) platform is owned and operated by the Eurosystem.
- Decision-making authority rests with the ECB Governing Council.
- Key governance bodies include:
  - **Market Infrastructure Board (MIB):** Responsible for day-to-day management of TARGET2 and T2S, and for all Eurosystem market infrastructure projects.
  - **CSD Steering Group (CSG):** Coordinates the positions and requirements of participating CSDs.
  - **Advisory Group on Market Infrastructures for Securities and Collateral (AMI-SeCo):** Advises on clearing, settlement, and collateral management issues; composed of representatives from securities market participants, CSDs, CCPs, and central banks.
[Source: ECB, "What is T2S?", https://www.ecb.europa.eu/paym/t2s/about/html/index.en.html]

**Central Bank Money Settlement:**
- T2S enables DVP (Delivery versus Payment) settlement in central bank money (euro and Danish krone).
- Settlement in central bank money eliminates commercial bank credit risk, in line with PFMI Principle 9.
- 24 CSDs from 23 European countries are connected to T2S, using central bank money for cash settlement.
[Source: ECB, "TARGET2-Securities," https://www.ecb.europa.eu/paym/target/t2s/html/index.en.html]

---

## 2. Key Legislation & Regulations

### 2.1 EMIR (European Market Infrastructure Regulation)

#### Original EMIR (2012)
- **Regulation (EU) No 648/2012**, adopted 4 July 2012, entered into force 16 August 2012.
- Implemented G20 commitments (Pittsburgh 2009) for OTC derivatives reform.
- Key requirements:
  - Mandatory central clearing for standardized OTC derivatives
  - Reporting of all derivative contracts to trade repositories
  - Risk mitigation techniques for non-centrally cleared OTC derivatives (bilateral margining, timely confirmation, portfolio reconciliation, dispute resolution)
  - Authorization and prudential requirements for EU CCPs
  - Recognition framework for third-country CCPs
[Source: EUR-Lex, Regulation (EU) No 648/2012]

#### EMIR Refit (2019)
- **Regulation (EU) 2019/834**, adopted 20 May 2019.
- Simplified and streamlined certain requirements:
  - Reduced reporting burden for non-financial counterparties (NFCs) below clearing thresholds
  - Simplified clearing threshold calculation for NFCs
  - Suspended clearing obligation for pension scheme arrangements (subsequently extended multiple times)
  - Improved transparency of CCP margin models
[Source: EUR-Lex, Regulation (EU) 2019/834]

#### EMIR 2.2 (2019) -- Third-Country CCP Supervision
- **Regulation (EU) 2019/2099**, adopted 23 October 2019.
- Established the enhanced supervisory framework for third-country CCPs:
  - Creation of the CCP Supervisory Committee within ESMA
  - Two-tier classification system (Tier 1 and Tier 2) for TC-CCPs
  - Direct ESMA supervision of Tier 2 TC-CCPs
  - "Comparable compliance" mechanism for Tier 2 TC-CCPs
  - Nuclear option: power for ESMA to recommend that a TC-CCP is of such systemic importance that it should not be recognized (requiring relocation to the EU)
- Motivated by Brexit concerns regarding the systemic importance of UK CCPs (particularly LCH Ltd) to EU financial stability.
[Source: EUR-Lex, Regulation (EU) 2019/2099]

#### EMIR 3.0 (2024) -- Active Account Requirement, Enhanced EU CCP Supervision
- **Regulation (EU) 2024/2987**, published in the Official Journal on 4 December 2024, entered into force on 24 December 2024.
- The most significant reform of EMIR since its inception.
[Source: EUR-Lex, Regulation (EU) 2024/2987; Jones Day, "EMIR 3 Published in the Official Journal," December 2024]

**Active Account Requirement (AAR):**
- Financial counterparties (FCs) and non-financial counterparties (NFCs) exceeding the clearing threshold must maintain an "active account" at an authorized EU CCP for clearing in-scope derivative contracts.
- **In-scope products:**
  - Interest rate derivatives denominated in euro (EUR) or Polish zloty (PLN)
  - Euro-denominated short-term interest rate derivatives (STIRs)
- **Operational conditions** -- the active account must be:
  1. Permanently functional
  2. Operationally capable of handling all of the entity's new in-scope transactions at short notice
  3. Able to accept the rapid transfer of in-scope transactions from other CCPs
- **Exemption:** Counterparties clearing at least 85% of their in-scope derivative contracts (by gross notional value) through authorized EU CCPs are exempt from the operational conditions.
- **Implementation timeline:**
  - AAR obligation applies from 24 June 2025
  - ESMA consultation on draft RTS closed 27 January 2025
  - ESMA submitted final RTS to the European Commission by 25 June 2025
[Source: Ashurst, "EU EMIR: EMIR 3 and the Active Account Requirement," 2025; ESMA Consultation Paper ESMA91-1505572268-3856, November 2024; PwC, "EMIR 3.0: Navigating the Active Account Requirement," 2025]

**Strengthened ESMA Direct Supervision Powers:**
- Enhanced powers for ESMA in supervising both EU and third-country CCPs
- Expanded mandate for CCP stress testing and risk model validation
- Greater coordination authority over NCA supervisory activities
[Source: ESMA CCP Policy, https://www.esma.europa.eu/central-counterparties/ccp-policy]

**Anti-Procyclicality Provisions for Margin:**
- EMIR has always required CCPs to adopt at least one of three anti-procyclicality (APC) margin measures. EMIR 3.0 strengthens these provisions:
  - Option 1: Apply a margin buffer of at least 25% that can be temporarily exhausted in stress periods
  - Option 2: Assign at least a 25% weight to stressed observations in the lookback period
  - Option 3: Ensure that margins are not lower than those calculated using a 10-year historical lookback period including stressed observations
- ESMA published final guidelines on APC margin measures in 2023 (ESMA91-1505572268-3217), recommending standardized application and enhanced transparency of APC tool usage.
- EMIR 3.0 mandates more robust disclosure of margin model procyclicality metrics.
[Source: ESMA Guidelines on CCP APC Margin Measures, ESMA70-151-1496; ESMA Final Report, July 2023]

**Cross-Margining Facilitation:**
- EMIR 3.0 facilitates cross-margining between exchange-traded derivatives (ETD) and OTC derivatives within the same liquidation group at an EU CCP.
- The distinction between "OTC" and "ETD" derivatives has been removed from the counterparty risk limit calculation, so both are treated equally unless cleared at an authorized/recognized CCP.
- This benefits EU CCPs such as Eurex Clearing, which offers cross-margining between OTC interest rate derivatives and listed STIR futures.
- Permanent exemption of single-stock options and equity index options from bilateral initial and variation margin requirements for uncleared trades (aligning with the U.S. framework).
[Source: A&O Shearman, "EMIR 3 and Clearing in the EU," 2024; Eurex, "EMIR 3.0 at Eurex," https://www.eurex.com/ec-en/rules-regs/emir3-0]

**Other Key EMIR 3.0 Provisions:**
- Revised clearing threshold calculations: FCs must now calculate both cleared and uncleared positions; NFCs continue to calculate only uncleared positions (with hedging exclusion maintained).
- EBA validation requirement for pro-forma initial margin models used by counterparties for uncleared OTC derivatives.
- Expanded scope of ESMA's annual CCP stress test.
[Source: National Law Review, "EMIR 3: Active Account, Clearing Threshold and Exemptions," December 2024]

### 2.2 CSDR (Central Securities Depositories Regulation)

- **Regulation (EU) No 909/2014**, adopted 23 July 2014, entered into force 17 September 2014.
- Provides a harmonized framework for the authorization, supervision, and operation of CSDs in the EU.
[Source: EUR-Lex, Regulation (EU) No 909/2014]

**CSD Authorization Requirements:**
- CSDs must be authorized by their home NCA to operate in the EU.
- Key requirements include:
  - Adequate governance and organizational structure
  - Minimum capital requirements
  - Operational risk management (including IT resilience, business continuity planning)
  - Participant access rules (fair, open, non-discriminatory)
  - Record-keeping and reporting obligations
  - Segregation of participants' securities
[Source: ESMA, "Central Securities Depositories"]

**Settlement Discipline Regime:**

*Cash Penalties (Implemented 1 February 2022):*
- CSDR Article 7 mandates a daily cash penalty for all transactions that fail to settle by the intended settlement date (ISD).
- Penalties are calculated and applied by CSDs at the end of each business day from ISD through to actual settlement date.
- CSDs collect penalties from failing participants at least monthly for redistribution to the receiving participant.
- Penalty rates vary by asset class (e.g., equities, government bonds, corporate bonds, SME growth market instruments).
- **Effectiveness assessment:** ESMA's review found that while the penalty mechanism has improved settlement efficiency, approximately 81% of cash penalties are less than EUR 50, raising questions about the administrative burden relative to the deterrent effect.
- **ESMA's 2024 advice:** Proposed maintaining the current mechanism design with a moderate increase of penalty rates across most asset classes and introducing progressive penalties (increasing each subsequent day of the fail) to strengthen the deterrent effect. The European Commission was expected to adopt these proposals in Q1 2026.
[Source: ESMA, "Final Report on Technical Advice on CSDR Penalty Mechanism," ESMA74-2119945925-2059, November 2024; ICMA, "CSDR Settlement Discipline," https://www.icmagroup.org/market-practice-and-regulatory-policy/secondary-markets/secondary-markets-regulation/csdr-settlement-discipline/]

*Mandatory Buy-In (Deferred/Modified Status):*
- The original CSDR mandated a mandatory buy-in process where a failing participant does not deliver within an extension period after the ISD:
  - **Standard extension period:** 4 business days after ISD
  - **SME growth market instruments:** 15 business days
  - **Other illiquid instruments:** Up to 7 business days
- The mandatory buy-in regime has been **repeatedly deferred** and was never implemented in its original form.
- The **CSDR Refit (2023)** significantly modified the mandatory buy-in regime:
  - Buy-ins are no longer automatically mandatory; they will only be activated if settlement efficiency does not meet defined thresholds after a monitoring period.
  - Securities financing transactions (SFTs) are excluded from the buy-in regime.
  - Cash penalties that arise from settlement fails not attributable to the participants are excluded.
  - The European Commission can activate mandatory buy-ins through a delegated act if settlement efficiency deteriorates below specified thresholds.
- As of April 2026, mandatory buy-ins have not been activated. [unverified -- precise activation status subject to recent EC decisions]
[Source: Norton Rose Fulbright, "CSDR Refit: The Key Changes," 2024; ICMA, "CSDR Settlement Discipline"]

**Settlement Internalization Reporting:**
- CSDR requires investment firms and credit institutions that settle transactions outside a CSD (settlement internalizers) to report quarterly to their NCA on the volume and value of internalized settlements.
- This enables regulators to monitor settlement activity occurring outside the regulated CSD infrastructure.
[Source: BNP Paribas Securities Services, "CSDR Regulation Memo"]

**CSD Passporting:**
- CSDs authorized in one EU Member State may provide services in other Member States through a passporting mechanism.
- The **CSDR Refit (2023)** simplified the passporting process, reducing administrative complexity for cross-border CSD operations.
[Source: Norton Rose Fulbright, "CSDR Refit: The Key Changes"]

### 2.3 MiFID II / MiFIR (Clearing-Related Provisions)

**Access and Interoperability Provisions:**
- MiFID II/MiFIR establish open access provisions requiring trading venues and CCPs to offer non-discriminatory access to each other.
- CCPs must accept requests for access from trading venues, and trading venues must provide trade feeds to CCPs upon request, subject to risk management conditions.
[Source: EUR-Lex, Directive 2014/65/EU (MiFID II), Regulation (EU) No 600/2014 (MiFIR)]

**Clearing Obligation for Derivatives:**
- While the clearing obligation itself is established under EMIR, MiFID II/MiFIR provide complementary provisions:
  - Trading obligation for sufficiently liquid derivatives that are subject to the clearing obligation
  - Reporting requirements for cleared and uncleared derivatives
[Source: ESMA, "CCP Policy"]

**Open Access for CCPs and Trading Venues:**
- MiFIR Articles 35-36 establish the open access framework:
  - CCPs must accept clearing requests from any trading venue, regardless of whether the CCP has an existing relationship with that venue
  - Trading venues must provide trade data to any CCP wishing to clear transactions executed on the venue
  - Transitional provisions and exemptions were available for certain CCPs and exchanges (e.g., derivatives exchanges operating vertically integrated models)
[Source: EUR-Lex, Regulation (EU) No 600/2014 (MiFIR)]

### 2.4 Bank Recovery and Resolution Directive (BRRD) -- CCP Aspects

- **Directive 2014/59/EU** (BRRD) establishes the framework for recovery and resolution of credit institutions and investment firms.
- While primarily directed at banks, the BRRD is relevant to CCPs through:
  - Capital treatment of banks' exposures to CCPs (interconnection between bank resolution and CCP resilience)
  - Resolution of clearing member banks and the implications for CCP default management
  - Coordination between bank resolution authorities and CCP resolution authorities
[Source: EUR-Lex, Directive 2014/59/EU]

### 2.5 CCP Recovery and Resolution Regulation (2021)

- **Regulation (EU) 2021/23**, adopted 16 December 2020, entered into force 12 February 2021.
- Key provisions on recovery planning applied from **12 February 2022**; most remaining provisions applied from **12 August 2022**.
- Establishes a harmonized EU framework for the recovery and resolution of CCPs, ensuring that CCPs and regulators can act decisively in a crisis to preserve critical clearing functions while limiting the impact on financial stability and public funds.
[Source: EUR-Lex, Regulation (EU) 2021/23, https://eur-lex.europa.eu/eli/reg/2021/23/oj/eng; European Commission, "Recovery and Resolution of CCPs"]

**Recovery Plan Requirements:**
- Every EU CCP must maintain a recovery plan, approved by its NCA and reviewed by the supervisory college.
- The recovery plan must contain:
  - A range of recovery tools and scenarios (including default and non-default loss events)
  - Indicators and triggers for activating recovery measures
  - Assessment of the impact of recovery tools on clearing members, their clients, and the broader financial system
  - Arrangements for continuity of critical clearing functions during recovery
[Source: EUR-Lex, Regulation (EU) 2021/23, Articles 9-13]

**Resolution Tools:**
The regulation provides resolution authorities with the following tools:

1. **Position Allocation Tool (Article 29):**
   - Resolution authorities may transfer, reduce, or terminate the CCP's outstanding contracts to rematch its book.
   - Includes partial or full tear-up of contracts.

2. **Loss Allocation Tools (Articles 30-31):**
   - **Variation Margin Gains Haircutting (VMGH):** Haircuts on outgoing variation margin payments to absorb losses.
   - **Resolution Cash Calls:** May amount to up to twice the applicable default fund contribution requirement of each relevant clearing member.
   - **Write-down and conversion:** Write-down of claims against the CCP or conversion of debt instruments to equity.

3. **Sale of Business Tool:**
   - Resolution authorities may sell all or part of the CCP's business to a third-party acquirer without shareholder consent.

4. **Bridge CCP:**
   - Critical clearing functions may be transferred to a temporary bridge CCP operated by the resolution authority.

5. **Tear-Up of Contracts:**
   - Partial or full termination of the CCP's outstanding contracts as a last-resort measure.
[Source: EUR-Lex, Regulation (EU) 2021/23; BNP Paribas, "The EU CCP Recovery and Resolution Regulation," December 2024; JP Morgan, "EU CCP Recovery and Resolution Regulation Disclosure"]

**Resolution Authorities:**
- Each Member State must designate a resolution authority for CCPs authorized in its jurisdiction.
- The resolution authority may be the NCA, the central bank, or a separate dedicated authority.
- Resolution authorities must prepare resolution plans for each CCP, in consultation with the supervisory college and ESMA.
[Source: EUR-Lex, Regulation (EU) 2021/23, Articles 3-4]

**No Creditor Worse Off (NCWO) Principle:**
- The regulation incorporates the NCWO safeguard: no clearing member, client, or shareholder should be left worse off under resolution than they would have been under normal insolvency proceedings.
- An independent valuation must be carried out to assess whether NCWO has been respected.
- Compensation may be payable from a dedicated fund if the NCWO principle is breached.
[Source: EUR-Lex, Summary, "Recovery and resolution of central counterparties," https://eur-lex.europa.eu/EN/legal-content/summary/recovery-and-resolution-of-central-counterparties.html]

---

## 3. CCP Authorization & Capital Requirements

### 3.1 EMIR Authorization Process

**College of Supervisors Role:**
- Before granting authorization, the NCA must establish a supervisory college composed of:
  - ESMA
  - The NCA of the CCP (as chair)
  - NCAs responsible for the most relevant clearing members
  - NCAs of trading venues served by the CCP
  - NCAs of interoperable CCPs
  - Relevant central banks of issue
- The college conducts a joint risk assessment and provides a non-binding opinion on the authorization. The NCA takes the final authorization decision.
[Source: ESMA, "Opinion on the composition of CCP colleges under EMIR," ESMA/2015/838; FMA Austria, "Authorisation & Ongoing Supervision"]

**Capital Requirements:**
- **Minimum initial capital:** EUR 7.5 million (permanent and available).
- Beyond the minimum, a CCP's capital (including retained earnings and reserves) must be:
  - Proportionate to the risk stemming from the CCP's activities
  - Sufficient to ensure an orderly winding-down or restructuring over an appropriate time span
  - Adequate to protect the CCP against credit, counterparty, market, operational, legal, and business risks not already covered by specific financial resources (margins, default fund)
- EMIR Article 16 further specifies that capital must at all times be sufficient to cover operational expenses for a winding-down period (minimum 6 months for general business risk [unverified]).
[Source: ESMA, "Article 16 Capital Requirements," https://www.esma.europa.eu/publications-and-data/interactive-single-rulebook/emir/article-16-capital-requirements]

**Organizational Requirements:**
- Robust governance arrangements with a clear organizational structure, well-defined lines of responsibility
- Board composition requirements (including independent members)
- Risk committee with clearing member representation
- Chief Risk Officer and Chief Compliance Officer functions
- IT systems and operational resilience requirements
- Business continuity and disaster recovery arrangements
- Outsourcing governance framework
[Source: EMIR Articles 26-35]

**Ongoing Compliance:**
- NCAs conduct regular supervisory reviews and evaluations (SREP) of authorized CCPs.
- ESMA has published Guidelines to harmonize CCP supervisory reviews and evaluation under EMIR (2024).
- Annual reporting, stress testing, and back-testing requirements.
- CCPs must notify NCAs of any material changes to their rules, procedures, or risk models.
[Source: ESMA, "Guidelines to harmonise CCP supervisory reviews and evaluation under EMIR," 2024]

### 3.2 Third-Country CCP Recognition

**Tier 1 vs. Tier 2 Classification:**
- **Tier 1 TC-CCPs:** Not systemically important to the EU financial system. Subject to lighter requirements; ESMA primarily relies on the home-country supervisor.
- **Tier 2 TC-CCPs:** Systemically important or likely to become so. Must comply with EMIR requirements directly or via comparable compliance. Subject to ongoing ESMA supervision including:
  - Annual review assessments
  - Risk model validation for any changes
  - Participation in ESMA CCP stress test exercises
  - Regular information sharing with home-country authorities
[Source: ESMA, "Third-Country CCPs"]

**Comparable Compliance Assessment:**
- Tier 2 TC-CCPs may apply for a "comparable compliance" determination from ESMA.
- This allows the TC-CCP to comply with home-country rules (rather than EMIR directly) where ESMA determines those rules achieve equivalent regulatory outcomes.
- The assessment is conducted on a requirement-by-requirement basis.
[Source: ESMA, "ESMA consults on tiering, comparable compliance and fees under EMIR 2.2"]

**Systemic Importance Determination:**
- ESMA's tiering assessment considers:
  - The nature, size, and complexity of the TC-CCP's business with EU clearing members and trading venues
  - The effect that the failure or disruption of the TC-CCP would have on EU financial markets, financial institutions, or the broader financial system
  - The TC-CCP's clearing membership structure and the degree to which EU entities rely on its services
- ESMA reviews tiering at least every five years, or when the TC-CCP extends or reduces its EU-facing activities.
[Source: ESMA, "Third-Country CCPs"]

**Active Account Requirement under EMIR 3.0:**
- In addition to the recognition framework, EMIR 3.0 introduces the AAR which requires that EU counterparties subject to the clearing obligation maintain an active account at an authorized EU CCP for in-scope products.
- This is a demand-side measure (targeting EU clearing members and clients) that complements the supply-side TC-CCP recognition regime.
- The AAR is designed to reduce excessive concentration of euro-denominated derivative clearing at non-EU CCPs (particularly LCH Ltd in London).
[Source: Ashurst, "EU EMIR: EMIR 3 and the Active Account Requirement"]

---

## 4. PFMI Compliance

### 4.1 EU Adoption of PFMI

**How EMIR/CSDR Map to PFMI Principles:**
- The CPMI-IOSCO Principles for Financial Market Infrastructures (PFMI), published in April 2012, provide 24 principles for FMIs and 5 responsibilities for authorities.
- The EU adopted the PFMI principles primarily through:
  - **EMIR** (for CCPs and Trade Repositories): EMIR's prudential, organizational, and conduct requirements are designed to be at least as stringent as the PFMI principles. Key mappings include:
    - PFMI Principle 4 (Credit Risk) -> EMIR Articles 41-44 (Margin, Default Fund, Skin-in-the-Game)
    - PFMI Principle 5 (Collateral) -> EMIR Article 46 (Collateral Requirements)
    - PFMI Principle 6 (Margin) -> EMIR Articles 41-42 (Margin Requirements)
    - PFMI Principle 7 (Liquidity Risk) -> EMIR Article 44 (Liquidity Risk Controls)
    - PFMI Principle 13 (Participant-Default Rules) -> EMIR Article 48 (Default Procedures)
    - PFMI Principle 15 (General Business Risk) -> EMIR Article 16 (Capital Requirements)
  - **CSDR** (for CSDs): CSDR requirements map to relevant PFMI principles for CSDs and SSSs, including:
    - PFMI Principle 8 (Settlement Finality) -> CSDR Article 39 (Settlement Finality)
    - PFMI Principle 9 (Money Settlements) -> CSDR provisions for settlement in central bank money via T2S
    - PFMI Principle 11 (CSDs) -> CSDR authorization and operational requirements

**CPMI-IOSCO Assessment Results for EU CCPs:**
- The European Commission and ESMA have participated in CPMI-IOSCO implementation monitoring assessments.
- The EU jurisdiction has generally been assessed as "broadly observed" or "observed" for most PFMI principles applicable to CCPs and CSDs.
- EU CCPs are required to publish CPMI-IOSCO Public Quantitative Disclosures (PQD) on a quarterly basis and qualitative self-assessments against the PFMI Disclosure Framework.
- Individual EU CCP PFMI assessments are available from the relevant NCAs and from the CCPs themselves (e.g., Eurex Clearing, LCH SA, EuroCCP).
[Source: CPMI-IOSCO, "Principles for Financial Market Infrastructures," April 2012; CPMI-IOSCO Implementation Monitoring Reports]

---

## 5. Settlement Framework

### 5.1 T2S (TARGET2-Securities)

**Governance and Operation (ECB):**
- T2S is a pan-European settlement platform owned and operated by the Eurosystem (the ECB and the national central banks of the euro area).
- Launched in June 2015, with phased migration of CSDs completed in September 2017.
- T2S provides a single, borderless pool for securities settlement in central bank money (EUR and DKK).
- Decision-making authority: ECB Governing Council, supported by the Market Infrastructure Board (MIB), CSD Steering Group (CSG), and AMI-SeCo advisory group.
[Source: ECB, "What is TARGET2-Securities (T2S)?", https://www.ecb.europa.eu/paym/target/t2s/html/index.en.html]

**Participating CSDs:**
- **24 CSDs from 23 European countries** are connected to T2S, including:
  - Major CSDs: Euroclear France, Euroclear Belgium, Euroclear Nederland, Clearstream Banking Frankfurt, Monte Titoli (Italy), Iberclear (Spain), VP Securities (Denmark), Interbolsa (Portugal), among others.
  - Euroclear Bank (ICSD) has been in the process of joining T2S. [unverified -- precise go-live date]
- Participation is voluntary, governed by the T2S Framework Agreement (contract setting out mutual rights and obligations between the Eurosystem and participating CSDs).
- Non-euro CSDs can participate for settlement in EUR and/or other eligible currencies.
[Source: ECB, "What is T2S?"; Wikipedia, "TARGET2-Securities"]

**DVP in Central Bank Money:**
- T2S operates a real-time DVP settlement model, ensuring simultaneous and irrevocable transfer of securities and cash.
- Cash settlement occurs in dedicated central bank money accounts (T2S Dedicated Cash Accounts, or DCAs) held at the respective national central bank.
- This eliminates commercial bank credit risk in the cash leg of settlement.
- T2S supports both real-time gross settlement and multiple batch optimization cycles throughout the settlement day.
[Source: ECB, "TARGET2-Securities"]

**Migration History and Current Status:**
- **Wave 1 (June 2015):** Monte Titoli (Italy), Maltese CSD, Romanian CSD, Swiss CSD (SIX SIS, for settlement in EUR)
- **Wave 2 (March 2016):** Euroclear Belgium, Euroclear France, Euroclear Nederland, Interbolsa (Portugal), NBB-SSS (Belgium)
- **Wave 3 (September 2016):** Clearstream Banking Frankfurt, OeKB CSD (Austria), VP Lux (Luxembourg), and others
- **Wave 4 (February 2017):** Iberclear (Spain), and Bratislava and Ljubljana CSDs
- **Wave 5 (September 2017):** VP Securities (Denmark -- settling in both EUR and DKK), Euroclear Finland, Baltic CSDs
- As of 2026, T2S settles hundreds of millions of transactions annually, processing a significant proportion of EU securities settlement.
[Source: ECB, "TARGET2-Securities"; Banco de Espana, "TARGET2-Securities"]

### 5.2 Settlement Cycle -- T+1 Transition

**Current T+2 under CSDR:**
- CSDR mandated a harmonized T+2 settlement cycle for transferable securities admitted to trading or traded on EU trading venues, effective from 1 January 2015 (previously most EU markets operated on T+3, with migration to T+2 completed by October 2014).
[Source: CSDR Article 5]

**EU T+1 Planned Transition (11 October 2027):**
- On 18 November 2024, ESMA published its report recommending that the EU move to T+1 no later than **11 October 2027**.
- The recommendation was adopted by EU co-legislators and **published in the EU Official Journal on 14 October 2025**, with the T+1 requirement to apply from **11 October 2027**.
[Source: ESMA, "ESMA proposes to move to T+1 by October 2027," November 2024; Societe Generale Securities Services, "T+1 in Europe," 2025; European Commission, "T+1 Settlement," February 2025]

**ESMA Consultation and Timeline:**
- ESMA recommended a **three-phase implementation:**
  1. **Phase 1 (by Q3 2025):** Finalize definition of technical solutions
  2. **Phase 2 (by end 2026):** Implement technical solutions across market participants and infrastructure
  3. **Phase 3 (2027):** Industry-wide testing culminating in go-live on 11 October 2027
- A phased-in implementation schedule beginning in December 2026 and concluding by 11 October 2027 was designed to ensure a smooth transition.
[Source: ESMA, "Shortening the settlement cycle to T+1 in the EU," https://www.esma.europa.eu/esmas-activities/markets-and-infrastructure/shortening-settlement-cycle-t1-eu]

**Industry Readiness / Governance:**
- The **EU T+1 Governance Structure** was established on 22 January 2025, composed of ESMA, the ECB, and the European Commission, alongside the financial industry.
- ESMA published a **High-Level Roadmap to T+1 Securities Settlement in the EU** on 30 June 2025.
- Key industry readiness challenges include:
  - Harmonization of corporate actions processing and FX settlement timing
  - Adjustment of post-trade matching and confirmation processes
  - Impact on securities lending and borrowing
  - Coordination with UK and Swiss T+1 transitions
- The UK and Switzerland are coordinating their T+1 transitions to align closely with the EU's October 2027 date.
[Source: ESMA, "New governance structure for transition to T+1 settlement cycle kicks off," January 2025; ESMA High-Level Roadmap, June 2025; BNP Paribas, "T+1 in Europe"]

### 5.3 Settlement Discipline (CSDR)

**Cash Penalty Regime (Implementation Since February 2022):**
- The CSDR settlement discipline cash penalty regime has been in effect since **1 February 2022**.
- Penalties are applied daily for each business day that a transaction remains unsettled past the ISD.
- Penalty rates (per asset class, as basis points of the value of the failed transaction per day):
  - Liquid shares: 1.0 bps/day
  - Government bonds and assimilated: 0.5 bps/day [unverified -- rates subject to ESMA's proposed revisions]
  - Corporate bonds: 0.5 bps/day [unverified]
  - SME growth market instruments: 0.25 bps/day [unverified]
  - Other financial instruments: 0.5 bps/day [unverified]
- Cash penalties for failure to deliver cash: based on the official interest rate for overnight credit charged by the central bank issuing the settlement currency, with a floor of zero.
- **Administration:** CSDs calculate and apply penalties at end of day; collect from failing participants and redistribute to receiving participants at least monthly.
[Source: ICMA, "CSDR Settlement Discipline"; Euroclear, "CSDR Settlement Discipline: Settlement Penalties"]

**Fail Rates and Statistics:**
- Since implementation, the penalty mechanism has contributed to improved settlement efficiency across EU markets.
- However, ESMA's analysis found that a large proportion of penalties are very small in absolute terms (81% below EUR 50), questioning the deterrent effect relative to administrative costs.
- ESMA proposed in November 2024:
  - A moderate increase to penalty rates across most asset classes
  - Introduction of **progressive penalties** (increasing each subsequent fail day) to incentivize faster resolution
  - Adjustments to the treatment of late matching penalties and penalties related to cash fails
- The European Commission was expected to adopt revised penalty rates in Q1 2026. [unverified -- precise adoption date]
- A major TARGET Services incident on 27-28 February 2025 led NCAs to suspend cash penalty application for those dates.
[Source: ESMA Final Report on CSDR Penalty Mechanism, November 2024; ESMA, "ESMA finalises its advice on the CSDR Penalty Mechanism"]

**Mandatory Buy-In (Deferred/Modified Status):**
- The mandatory buy-in regime under CSDR Article 7 has been deferred since the regulation's initial implementation.
- The **CSDR Refit (Regulation (EU) 2023/2845)**, published December 2023, fundamentally restructured the buy-in regime:
  - Buy-ins are no longer automatically mandatory; they serve as a backstop activated only by the European Commission (via delegated act) if settlement efficiency deteriorates below defined thresholds.
  - SFTs are excluded from the buy-in scope.
  - Cash compensation as an alternative to buy-in is preserved.
- As of April 2026, mandatory buy-ins have **not been activated**. The cash penalty regime remains the primary settlement discipline tool.
[Source: Norton Rose Fulbright, "CSDR Refit: The Key Changes"; ICMA, "CSDR Settlement Discipline"]

---

## 6. Interoperability

### 6.1 CCP Interoperability under EMIR

**Framework for Interoperable Links:**
- EMIR Title V (Articles 51-54) establishes the framework for interoperability arrangements between CCPs.
- An interoperability arrangement allows a CCP to clear trades executed on a trading venue that is served by another CCP, enabling market participants to choose their CCP regardless of where they trade.
- Key requirements for interoperability:
  - Both CCPs must apply for NCA approval of the link
  - Robust risk management for the inter-CCP exposure
  - Adequate margin and collateral arrangements between the linked CCPs
  - Coordinated default management procedures
  - Legal opinions on enforceability of the arrangement
[Source: EMIR Articles 51-54; ESRB, "CCP Interoperability Arrangements," January 2019]

**Risk Management for Interoperable CCPs:**
- Interoperable CCPs must manage their exposure to each other through:
  - Appropriate margin requirements for the inter-CCP leg
  - Dedicated default fund contributions or other financial safeguards
  - Intraday exposure monitoring and management
  - Coordinated stress testing
- The ESRB's 2019 report identified risks arising from interoperability, including contagion risk, liquidity risk, and operational risk, and recommended enhanced monitoring by ESMA and NCAs.
[Source: ESRB, "CCP Interoperability Arrangements," January 2019, https://www.esrb.europa.eu/pub/pdf/reports/esrb.report190131_CCP_interoperability_arrangements~99908a78e7.en.pdf]

**Current Interoperability Arrangements in the EU:**
- As of 2026, there are **five CCP interoperability arrangements** in Europe, involving:
  - **EU-authorized CCPs:** EuroCCP (Netherlands), CC&G/Euronext Clearing (Italy), LCH SA (France)
  - **Recognized third-country CCPs:** LCH Ltd (UK), SIX x-clear (Switzerland, including its Norwegian branch SIX x-clear NO)
- These arrangements primarily cover cash equities and ETFs traded on European trading venues (e.g., Euronext, CBOE Europe, Aquis Exchange).
- **EMIR 3.0 expansion:** Under EMIR 3.0, interoperability arrangements are no longer restricted to transferable securities and money market instruments; they may now also relate to any financial or non-financial instruments.
[Source: ESRB Report, January 2019; A&O Shearman, "EMIR 3 and Clearing in the EU"]

---

## 7. Cross-Border Arrangements

### 7.1 UK Post-Brexit

**Temporary Recognition of UK CCPs (LCH Ltd, ICE Clear Europe, LME Clear):**
- Following the UK's withdrawal from the EU on 31 January 2020 (transition period ended 31 December 2020), UK CCPs lost their EU authorization.
- ESMA granted temporary recognition to three UK CCPs from 1 January 2021: **LCH Ltd, ICE Clear Europe, and LME Clear**.
- **LCH Ltd** and **ICE Clear Europe** were classified as **Tier 2 TC-CCPs** (systemically important), subject to direct ESMA supervision.
- **LME Clear** was classified as **Tier 1 TC-CCP**.
[Source: ESMA, "ESMA to recognise three UK CCPs from 1 January 2021"; ESMA, "ESMA extends the tiering and recognition of the three UK-based CCPs"]

**Equivalence Extension:**
- The European Commission originally adopted a time-limited equivalence decision for the UK's CCP regulatory framework.
- On **31 January 2025**, the Commission adopted an extension of UK CCP equivalence for **three years until 30 June 2028** (applying from 1 July 2025, when the previous decision expired on 30 June 2025).
- This extension provides continuity for EU market participants clearing at UK CCPs while the EMIR 3.0 AAR is implemented.
[Source: European Commission, "Commission extends time-limited equivalence for UK central counterparties," January 2025; AIMA, "European Commission Proposes to Extend UK CCP Equivalence Beyond 2025"]

**EMIR 3.0 Active Account Implications:**
- The AAR is the primary policy tool to reduce EU reliance on UK CCPs for euro-denominated derivative clearing.
- EU counterparties must maintain an active account at an EU CCP (e.g., Eurex Clearing) for in-scope interest rate derivatives and STIRs, even if they continue to also clear at UK CCPs.
- The 85% threshold exemption means that counterparties already clearing predominantly at EU CCPs face minimal additional burden.
- The long-term strategic intent is to build EU CCP capacity and market liquidity, particularly at Eurex Clearing, to serve as a viable alternative to LCH Ltd for euro-denominated interest rate derivative clearing.
[Source: Eurex, "EMIR 3.0 active accounts are set to change the European clearing landscape"; Ashurst, "EU extends UK CCP equivalence"]

**Long-Term Equivalence Decisions:**
- The current equivalence decision remains time-limited (until 30 June 2028).
- The European Commission has not adopted a permanent or open-ended equivalence decision for the UK.
- The future of UK CCP access to EU markets depends on the success of the AAR in building EU clearing capacity and on ongoing EU-UK regulatory cooperation.
- The UK's own **Temporary Recognition Regime (TRR)** for EU CCPs operating in the UK was extended to 31 December 2026 (further extendable by HM Treasury). [unverified -- may have been further extended since]
[Source: Bank of England, "Information on the effect of the UK's withdrawal from the EU on FMI supervision"]

### 7.2 Third-Country Equivalence

**Equivalence Decisions for Non-EU Jurisdictions:**
- The European Commission has adopted equivalence decisions for the CCP regulatory frameworks of numerous third countries, enabling their CCPs to apply for ESMA recognition.
- Key jurisdictions with CCP equivalence decisions include:
  - **United States** (CFTC-regulated CCPs)
  - **United Kingdom** (time-limited, until 30 June 2028)
  - **Japan** (JFSA-regulated CCPs)
  - **Singapore** (MAS-regulated CCPs)
  - **Hong Kong** (SFC/HKMA-regulated CCPs)
  - **Australia** (ASIC/RBA-regulated CCPs)
  - **South Korea** (FSC/FSS-regulated CCPs)
  - **India, Canada, Switzerland, Brazil, Mexico, South Africa**, and others
- Equivalence is assessed on a jurisdiction-by-jurisdiction and activity-by-activity basis.
[Source: European Commission, "Equivalence decisions"; ESMA, "Third-Country CCPs"]

**Impact on Non-EU CCPs:**
- Equivalence + recognition allows non-EU CCPs to offer clearing services to EU clearing members and trading venues.
- The EMIR 2.2 tiering regime and EMIR 3.0 AAR have increased regulatory scrutiny and operational requirements for non-EU CCPs serving EU markets.
- Tier 2 TC-CCPs face substantial compliance costs (comparable compliance or direct EMIR compliance, ESMA supervisory fees).
- The AAR creates incentives for EU clearing volume to shift to EU-authorized CCPs, potentially reducing the market share of non-EU CCPs in euro-denominated products.

**ESMA-Korea MoU:**
- ESMA and the FSC/FSS of Korea have signed a Memorandum of Understanding regarding cooperation on ESMA's monitoring of Korean CCPs' compliance with recognition conditions under EMIR Article 25.
- The European Commission adopted an equivalence decision determining that Korea's CCP regulatory framework (under the FSCMA) is equivalent to EMIR requirements.
- This enables KRX (as a CCP) to seek ESMA recognition, although KRX has not applied for recognition as it does not provide significant cross-border clearing services to EU members. [unverified]
[Source: ESMA, "Memorandum of Understanding -- ESMA and FSC/FSS Korea"]

---

## 8. Recent Regulatory Changes (2023-2026)

### 8.1 EMIR 3.0 Implementation

| Milestone | Date | Status |
|-----------|------|--------|
| EMIR 3.0 published in EU Official Journal | 4 December 2024 | Completed |
| Entry into force | 24 December 2024 | Completed |
| ESMA consultation on AAR RTS | November 2024 - January 2025 | Completed |
| AAR obligation applies | 24 June 2025 | Completed |
| ESMA final RTS submitted to European Commission | 25 June 2025 | Completed |
| Ongoing implementation and monitoring | 2025-2026 | In progress |

[Source: ESMA, "EMIR 3 Active Account Requirement" publications; Jones Day, December 2024]

### 8.2 CSDR Refit

| Milestone | Date | Status |
|-----------|------|--------|
| CSDR Refit provisional agreement | 27 June 2023 | Completed |
| Published in EU Official Journal | 27 December 2023 | Completed |
| Entry into force | 16 January 2024 | Completed |
| First provisions apply | 1 May 2024 | Completed |
| Remaining provisions apply | 17 January 2026 | Completed |
| ESMA amendments to settlement discipline RTS (supporting T+1) | 13 October 2025 | Completed |

Key CSDR Refit changes:
1. **Settlement discipline:** Modified mandatory buy-in regime (now a backstop, not automatic); SFTs excluded; enhanced cash penalty framework.
2. **Passporting:** Simplified cross-border CSD service provision.
3. **Banking-type ancillary services:** Easier access for CSDs to provide or access banking-type services.
4. **Third-country CSD oversight:** Streamlined framework for non-EU CSDs operating in the EU.
5. **Supervisory cooperation:** Enhanced coordination between NCAs and ESMA.
[Source: Norton Rose Fulbright, "CSDR Refit: The Key Changes"; Regulation (EU) 2023/2845]

### 8.3 Digital Finance Package (DLT Pilot Regime for Market Infrastructure)

- **Regulation (EU) 2022/858** (DLT Pilot Regime) entered into force on **23 March 2023**.
- Creates a regulatory sandbox for DLT-based market infrastructures, allowing:
  - **DLT Multilateral Trading Facilities (DLT MTFs)**
  - **DLT Settlement Systems (DLT SSs)**
  - **DLT Trading and Settlement Systems (DLT TSSs)** -- combined trading and settlement on a single DLT platform
- Covers the issuance, recording, transfer, and storage of tokenized financial instruments (security tokens / DLT financial instruments).
- Settlement may occur in central bank money, commercial bank money, or e-money tokens.
- Originally limited to specific financial instruments below defined thresholds. [unverified]
[Source: EUR-Lex, Regulation (EU) 2022/858; ESMA, "DLT Pilot Regime"]

**Recent Developments:**
- **2024:** German regulator BaFin licensed **21X** under the DLT Pilot Regime to operate a fully regulated blockchain-based trading and settlement venue.
- **December 2025:** The European Commission proposed a **major upgrade** to the DLT Pilot Regime:
  - Raising the issuance threshold from EUR 6 billion to EUR 100 billion
  - Expanding eligibility to all MiFID II securities (not just stocks, bonds, and funds)
  - Broadening the scope to facilitate wider adoption of DLT in post-trade infrastructure
- **June 2025:** ESMA published its report on the functioning and review of the DLT Pilot Regime under Article 14 of the Regulation.
[Source: ESMA, "DLT Pilot Regime," https://www.esma.europa.eu/esmas-activities/digital-finance-and-innovation/dlt-pilot-regime; Ledger Insights, "EU Commission floats major DLT Pilot Regime upgrade," December 2025]

### 8.4 T+1 Preparations

| Milestone | Date | Status |
|-----------|------|--------|
| ESMA T+1 report and recommendation | 18 November 2024 | Completed |
| EU T+1 Governance Structure established | 22 January 2025 | Completed |
| Phase 1: Technical solutions defined | Q3 2025 | Completed |
| ESMA High-Level Roadmap published | 30 June 2025 | Completed |
| Legislative text published in EU Official Journal | 14 October 2025 | Completed |
| ESMA settlement discipline RTS amendments | 13 October 2025 | Completed |
| Phase 2: Implementation of technical solutions | By end 2026 | In progress |
| Phase 3: Industry-wide testing | Early 2027 | Upcoming |
| **T+1 go-live** | **11 October 2027** | Upcoming |

Coordination with other jurisdictions:
- The UK is expected to align its T+1 transition closely with the EU's October 2027 date. [unverified -- precise UK date]
- Switzerland is also coordinating its transition with the EU timeline.
- The U.S. successfully moved to T+1 in May 2024; India moved to T+1 in January 2023.
[Source: ESMA, "Shortening the settlement cycle to T+1 in the EU"; BNP Paribas, "T+1 in Europe"]

---

## 9. Comparison with Korea

### 9.1 Key Differences

| Aspect | EU | Korea |
|--------|-----|-------|
| **Primary Legislation** | EMIR (648/2012, as amended by EMIR Refit, 2.2, 3.0), CSDR (909/2014, as amended by CSDR Refit) | Financial Investment Services and Capital Markets Act (FSCMA) |
| **CCP Regulator** | ESMA (supranational) + NCAs (national) via colleges of supervisors | FSC (policy/licensing) + FSS (supervision/examination) + BOK (oversight of payment/settlement systems) |
| **CCP Structure** | Multiple CCPs -- Eurex Clearing, LCH SA, EuroCCP, CC&G, ICE Clear Europe, etc. | Single CCP -- KRX acts as the sole CCP for exchange-traded products |
| **CSD Structure** | Multiple CSDs -- 24+ CSDs connected to T2S; plus ICSDs (Euroclear Bank, Clearstream Banking) | Single CSD -- Korea Securities Depository (KSD), established as a special corporation under FSCMA |
| **CCP Authorization** | NCA authorization with supervisory college, ESMA coordination; minimum EUR 7.5M capital | KRX is established by law as a self-regulatory organization and CCP; regulated under FSCMA |
| **Settlement Infrastructure** | T2S (pan-European, ECB-operated, DVP in central bank money) | KSD operates the settlement system; BOK-Wire+ for cash settlement in central bank money |
| **Settlement Cycle** | T+2 (transitioning to T+1 on 11 October 2027) | T+2 for equities; T+1 for government bonds; T+0 for general bonds |
| **Settlement Discipline** | Cash penalties (since Feb 2022); mandatory buy-in (deferred, backstop only under CSDR Refit) | Settlement failure handling governed by KRX/KSD rules; penalties and default procedures defined in KRX rulebook [unverified] |
| **CCP Interoperability** | 5 interoperability arrangements among EU and third-country CCPs | No CCP interoperability -- single CCP model |
| **DVP Model** | T2S uses real-time DVP with multiple batch optimization cycles; BIS Model 1 (gross-gross) for real-time | KSD uses gross securities / net cash (BIS Model 2) for equities [unverified]; DVP for all instruments |
| **Recovery & Resolution** | Dedicated CCP R&R Regulation (EU) 2021/23 with specific tools (VMGH, tear-up, cash calls, sale of business) | No dedicated CCP recovery and resolution law; handled under general financial stability framework and FSCMA provisions [unverified] |
| **Third-Country CCP Access** | Recognition framework (Tier 1 / Tier 2) under EMIR Article 25; equivalence decisions | Korean CCPs do not generally serve foreign clearing members directly; ESMA-Korea MoU exists for recognition purposes |
| **Cross-Margining** | Facilitated under EMIR 3.0 (ETD/OTC cross-margining within same liquidation group) | KRX provides cross-margining for exchange-traded derivatives (KOSPI 200 futures/options) [unverified] |
| **PFMI Compliance** | EMIR/CSDR designed to be compliant; CPMI-IOSCO assessments conducted | IMF/World Bank FSAP assessment (2014) assessed KRX CCP and BOK-Wire+ against PFMI; generally assessed as broadly observed [Source: IMF FSAP 2014, cr14308/cr14309] |
| **Clearing Obligation** | Mandatory central clearing for standardized OTC derivatives (IRS, CDS indices) at authorized/recognized CCPs | No mandatory OTC clearing obligation comparable to EMIR; exchange-traded derivatives are centrally cleared by KRX by default [unverified] |
| **Active Account Requirement** | EMIR 3.0 AAR for euro-denominated IRDs and STIRs | No equivalent requirement |
| **DLT/Innovation** | DLT Pilot Regime (Regulation 2022/858) for tokenized securities settlement | KSD exploring blockchain for cross-border settlement (e.g., KSD blockchain platform for OTC derivatives reporting) [unverified] |
| **T+1 Transition** | Legislated for 11 October 2027 | KSD/KRX initiated discussions on T+1 transition (working group established October 2025); no legislated timeline yet |

### 9.2 Structural Observations

**Centralized vs. Decentralized Model:**
- Korea operates a highly centralized post-trade model: a single exchange group (KRX) acts as both the exchange and the CCP, and a single CSD (KSD) handles all settlement. This simplifies interoperability concerns but concentrates risk.
- The EU operates a decentralized model with multiple CCPs, CSDs, and trading venues across 27 Member States, requiring extensive regulatory coordination (colleges, ESMA oversight, T2S harmonization). This provides competition and choice but introduces complexity.

**Regulatory Overlap:**
- In Korea, both the FSC/FSS and the BOK have overlapping responsibilities for KRX and KSD oversight, which the 2014 IMF FSAP noted as a potential coordination challenge.
- In the EU, the division between ESMA (supranational) and NCAs (national) is more clearly delineated under EMIR, though the EMIR 3.0 reforms further centralize supervisory powers at ESMA.

**Settlement Efficiency:**
- Korea's single-CSD model and shorter settlement cycles for bonds (T+1 and T+0) suggest a more streamlined settlement process.
- The EU's multi-CSD environment, even with T2S, involves greater cross-border complexity. The T+1 transition is a major industry-wide project requiring coordination across 24 CSDs and their market communities.

[Source: IMF, "Republic of Korea: FSAP -- Detailed Assessment of Observance of the CPSS-IOSCO PFMI," 2014; BIS, "Payment, clearing and settlement systems in Korea," Red Book 2011; Clearstream, "Market infrastructure -- South Korea"]

---

## Sources

### Primary Legislation
- [EMIR -- Regulation (EU) No 648/2012](https://eur-lex.europa.eu/eli/reg/2012/648/oj/eng)
- [EMIR 3.0 -- Regulation (EU) 2024/2987](https://eur-lex.europa.eu/eli/reg/2024/2987/oj/eng)
- [CSDR -- Regulation (EU) No 909/2014](https://eur-lex.europa.eu/eli/reg/2014/909/oj/eng)
- [CSDR Refit -- Regulation (EU) 2023/2845](https://eur-lex.europa.eu/eli/reg/2023/2845/oj/eng)
- [CCP Recovery and Resolution -- Regulation (EU) 2021/23](https://eur-lex.europa.eu/eli/reg/2021/23/oj/eng)
- [DLT Pilot Regime -- Regulation (EU) 2022/858](https://eur-lex.europa.eu/eli/reg/2022/858/oj/eng)

### ESMA Publications
- [ESMA -- Third-Country CCPs](https://www.esma.europa.eu/central-counterparties/third-country-ccps)
- [ESMA -- CCP Policy](https://www.esma.europa.eu/central-counterparties/ccp-policy)
- [ESMA -- Central Securities Depositories](https://www.esma.europa.eu/esmas-activities/markets-and-infrastructure/central-securities-depositories)
- [ESMA -- DLT Pilot Regime](https://www.esma.europa.eu/esmas-activities/digital-finance-and-innovation/dlt-pilot-regime)
- [ESMA -- Shortening the Settlement Cycle to T+1](https://www.esma.europa.eu/esmas-activities/markets-and-infrastructure/shortening-settlement-cycle-t1-eu)
- [ESMA -- EMIR 3 Active Account Requirement Consultation Paper (November 2024)](https://www.esma.europa.eu/sites/default/files/2024-11/ESMA91-1505572268-3856_Consultation_Paper_EMIR_3_Active_Account_Requirement.pdf)
- [ESMA -- Final Report on CSDR Penalty Mechanism (November 2024)](https://www.esma.europa.eu/sites/default/files/2024-11/ESMA74-2119945925-2059_Final_Report_on_Technical_Advice_on_CSDR_Penalty_Mechanism.pdf)

### ECB / T2S
- [ECB -- What is TARGET2-Securities (T2S)?](https://www.ecb.europa.eu/paym/target/t2s/html/index.en.html)
- [ECB -- T2S About](https://www.ecb.europa.eu/paym/t2s/about/html/index.en.html)

### European Commission
- [EC -- Recovery and Resolution of CCPs](https://finance.ec.europa.eu/capital-markets-union-and-financial-markets/financial-markets/post-trade-services/recovery-and-resolution-central-counterparties-ccps_en)
- [EC -- T+1 Settlement (February 2025)](https://finance.ec.europa.eu/news/t1-settlement-2025-02-14_en)
- [EC -- Commission extends UK CCP equivalence (January 2025)](https://finance.ec.europa.eu/news/commission-extends-time-limited-equivalence-uk-central-counterparties-2025-01-31_en)

### Industry & Advisory Sources
- [Ashurst -- EU EMIR: EMIR 3 and the Active Account Requirement](https://www.ashurst.com/en/insights/eu-emir-emir-3-and-the-active-account-requirement/)
- [A&O Shearman -- EMIR 3 and Clearing in the EU](https://www.aoshearman.com/en/insights/emir-3-and-clearing-in-the-eu)
- [Norton Rose Fulbright -- CSDR Refit: The Key Changes](https://www.nortonrosefulbright.com/en/knowledge/publications/3fec092d/csdr-refit-the-key-changes)
- [Jones Day -- EMIR 3 Published in the Official Journal (December 2024)](https://www.jonesday.com/en/insights/2024/12/emir-3-published-in-the-official-journal-of-the-european-union)
- [BNP Paribas -- EU CCP Recovery and Resolution Regulation (December 2024)](https://globalmarkets.cib.bnpparibas/app/uploads/sites/4/2024/12/eu-ccp-rrr-dec24.pdf)
- [ICMA -- CSDR Settlement Discipline](https://www.icmagroup.org/market-practice-and-regulatory-policy/secondary-markets/secondary-markets-regulation/csdr-settlement-discipline/)
- [ESRB -- CCP Interoperability Arrangements (January 2019)](https://www.esrb.europa.eu/pub/pdf/reports/esrb.report190131_CCP_interoperability_arrangements~99908a78e7.en.pdf)

### Korea-Specific
- [IMF -- Republic of Korea: FSAP Detailed Assessment of CPSS-IOSCO PFMI (2014)](https://www.imf.org/external/pubs/ft/scr/2014/cr14308.pdf)
- [BIS -- Payment, Clearing and Settlement Systems in Korea (Red Book 2011)](https://www.bis.org/cpmi/publ/d97_kr.pdf)
- [Clearstream -- Market Infrastructure: South Korea](https://www.clearstream.com/clearstream-en/res-library/market-coverage/market-infrastructure-south-korea-1283522)
- [ESMA -- MoU with FSC/FSS Korea](https://www.esma.europa.eu/sites/default/files/library/revised_mou_esma-fsc_fss_korea_tc-ccps_-_final.pdf)
- [Chambers and Partners -- Financial Services Regulation 2025: South Korea](https://practiceguides.chambers.com/practice-guides/financial-services-regulation-2025/south-korea)
