#!/usr/bin/env python3
"""
Comprehensive Glossary Overhaul Script:
1. Parses existing md/_common/glossary_en.md, md/_common/glossary_ko.md, and md/_common/glossary.db
2. Merges all entries into a unified canonical structure across 7 categories
3. Fixes KRX regulatory inaccuracies (Call Auction vs. Simultaneous Bids and Offers / 동시호가, Static vs. Dynamic VI, Sidecar & Derivatives Price Limits, Split Settlement, Lot Size, etc.)
4. Adds missing translations, definitions, and key market microstructure / order type / NXT terms
5. Removes cross-category duplicates and misplaced entries
6. Strictly sorts every category A-Z (case-insensitive)
7. Writes md/_common/glossary_en.md, md/_common/glossary_ko.md, and rebuilds md/_common/glossary.db (including FTS5 index)
"""

import pathlib
import re
import sqlite3

ROOT_DIR = pathlib.Path("/Users/jamin/Library/CloudStorage/GoogleDrive-jamingoo83@gmail.com/My Drive/Code/Antigravity/exchange_review")
EN_MD_PATH = ROOT_DIR / "md/_common/glossary_en.md"
KO_MD_PATH = ROOT_DIR / "md/_common/glossary_ko.md"
DB_PATH = ROOT_DIR / "md/_common/glossary.db"

CATEGORIES = [
    ("Trading", "매매 (Trading)"),
    ("Derivatives", "파생상품 (Derivatives)"),
    ("Clearing", "청산 (Clearing)"),
    ("Settlement", "결제 (Settlement)"),
    ("Technology", "기술 (Technology)"),
    ("Market Segments & Boards", "시장구분 (Market Segments & Boards)"),
    ("Regulation", "규제 (Regulation)"),
]

def parse_md(path: pathlib.Path):
    lines = path.read_text(encoding="utf-8").splitlines()
    cat = None
    cats = {}
    for line in lines:
        if line.startswith("## "):
            cat = line[3:].strip()
            cats[cat] = []
        elif line.startswith("|") and not line.startswith("|---") and not line.startswith("| English") and not line.startswith("| Term"):
            parts = [p.strip() for p in line.split("|")[1:-1]]
            if len(parts) >= 3:
                cats[cat].append(parts)
    return cats

def norm_key(s: str) -> str:
    s = s.strip()
    if s == "EFP (Exchange for Physical)": return "exchange for physical"
    if s == "EFS (Exchange for Swap)": return "exchange for swap"
    if s in ("FLEX (Full Line-speed Exchange)", "FLEX (JPX)"): return "flex (full line-speed exchange)"
    if s in ("NTP (New Trading Platform)", "NTP (ASX)"): return "ntp (new trading platform)"
    if s in ("Volatility Interruption (KRX)", "Volatility Interruption (VI) — KRX"): return "volatility interruption (vi) — krx"
    if s.startswith("SAIL"): return "sail (sola access information language)"
    if s.startswith("PRISMA") or s == "Prisma": return "prisma"
    if s in ("Central Counterparty", "Central Counterparty (CCP)"): return "central counterparty"
    if s.startswith("Market-Wide Circuit Breaker (US)") or s in ("Market-Wide Circuit Breaker", "Market-Wide Circuit Breaker (MWCB)"): return "market-wide circuit breaker"
    if s.startswith("Mid-Price Pegged Order"): return "mid-price pegged order"
    if s.startswith("Real-Time Price Limit (KRX)"): return "real-time price limit (krx)"
    if s.startswith("Financial Services Commission (Korea)"): return "financial services commission (korea)"
    if s.startswith("Financial Supervisory Service (Korea)"): return "financial supervisory service (korea)"
    if s.startswith("National Short-sale Detecting System"): return "national short-sale detecting system"
    if s.startswith("24X National Exchange"): return "24x national exchange"
    if s.startswith("Order Freeze"): return "order freeze (late auction cutoff)" 
    m = re.match(r"^(.*?)\s*\(([A-Za-z0-9/\-\s]+)\)$", s)
    if m:
        base, paren = m.group(1), m.group(2)
        if paren not in [
            "KRX", "Korea", "Taiwan", "Quebec", "China", "Saudi Arabia",
            "TWSE", "CCP", "Offer", "Expiry", "Asset", "Parallel Market",
            "Program Trading Suspension", "Derivatives Circuit Breaker",
            "Simultaneous Order Matching", "Price-Time Priority", "Single-Price Auction", "Dongsi Hoga"
        ]:
            return base.strip().lower()
    return s.lower()

def sort_key(item: dict) -> str:
    s = item["term_en"].lower()
    # Keep EXTURE (1st gen) -> EXTURE+ (2nd gen) -> Exture 3.0 (3rd gen) in logical order
    if s == "exture+":
        return "exture 2.0"
    return s

def build_unified_glossary():
    en_cats = parse_md(EN_MD_PATH)
    ko_cats = parse_md(KO_MD_PATH)

    unified = {en_c: {} for en_c, _ in CATEGORIES}

    for en_c, ko_c in CATEGORIES:
        for parts in en_cats.get(en_c, []):
            term_en, abbr, def_en = parts[0], parts[1], parts[2]
            k = norm_key(term_en)
            if en_c == "Trading" and k == "continuous trading (price-time priority)":
                continue
            if en_c == "Derivatives" and k in ("exture+", "volatility interruption (vi) — krx", "systemically important financial market utility", "sidecar (derivatives circuit breaker)"):
                continue
            if en_c == "Clearing" and k == "security token":
                continue
            if en_c == "Regulation" and k == "pfmi":
                continue
            unified[en_c][k] = {
                "term_en": term_en,
                "abbr": abbr,
                "term_ko_en_col": f"{term_en} ({abbr})" if abbr and f"({abbr})" not in term_en else term_en,
                "term_ko": "",
                "def_en": def_en,
                "def_ko": "",
                "krx_note": "",
            }

        for parts in ko_cats.get(ko_c, []):
            en_col = parts[0]
            term_ko = parts[1]
            def_ko = parts[2]
            krx_note = parts[3] if len(parts) >= 4 else ""
            k = norm_key(en_col)

            if en_c == "Trading" and k == "continuous trading (price-time priority)":
                continue
            if en_c == "Derivatives" and k in ("filtered historical simulation", "prisma", "span", "span 2", "systemically important financial market utility", "sidecar (derivatives circuit breaker)"):
                continue
            if en_c == "Regulation" and k == "pfmi":
                continue

            if k in unified[en_c]:
                unified[en_c][k]["term_ko_en_col"] = en_col
                unified[en_c][k]["term_ko"] = term_ko
                unified[en_c][k]["def_ko"] = def_ko
                unified[en_c][k]["krx_note"] = krx_note
            else:
                abbr = ""
                term_en_clean = en_col
                m = re.match(r"^(.*?)\s*\(([A-Za-z0-9/\-]+)\)$", en_col)
                if m and m.group(2) not in ("Offer", "Expiry", "Asset"):
                    term_en_clean = m.group(1).strip()
                    abbr = m.group(2).strip()
                unified[en_c][k] = {
                    "term_en": term_en_clean,
                    "abbr": abbr,
                    "term_ko_en_col": en_col,
                    "term_ko": term_ko,
                    "def_en": "",
                    "def_ko": def_ko,
                    "krx_note": krx_note,
                }

    # --- 1. Fill missing EN definitions for the 18 Derivatives terms + Security Token in Regulation ---
    missing_en_defs = {
        ("Derivatives", "commodity futures"): (
            "Commodity Futures", "", "Commodity Futures",
            "Standardized exchange-traded contracts to buy or sell a specific quantity of a physical commodity (agricultural products, energy, metals) at a predetermined price on a specified future date"
        ),
        ("Derivatives", "contract specification"): (
            "Contract Specification", "", "Contract Specification",
            "The standardized document issued by an exchange defining the key terms of a futures or options contract, including contract size, tick size, contract months, last trading day, and settlement method"
        ),
        ("Derivatives", "daily settlement price"): (
            "Daily Settlement Price", "", "Daily Settlement Price",
            "The official daily reference price determined by an exchange at the end of each trading day for futures and options contracts, used for daily mark-to-market variation margin settlement and next-day price limits"
        ),
        ("Derivatives", "delivery"): (
            "Delivery", "", "Delivery",
            "The process at contract expiration by which the short position holder transfers the underlying physical asset to the long position holder or settles the obligation in cash"
        ),
        ("Derivatives", "derivatives"): (
            "Derivatives", "", "Derivatives",
            "Financial contracts whose value is derived from the price movement of an underlying asset, index, interest rate, currency, or commodity; major types include futures, options, and swaps"
        ),
        ("Derivatives", "equity index futures"): (
            "Equity Index Futures", "", "Equity Index Futures",
            "Standardized futures contracts based on an equity price index (e.g., S&P 500, KOSPI 200, Nikkei 225) that obligate the parties to settle the index value difference in cash at a specified future date"
        ),
        ("Derivatives", "equity index options"): (
            "Equity Index Options", "", "Equity Index Options",
            "Options contracts granting the holder the right, but not the obligation, to buy (call) or sell (put) the value of an underlying equity index at a specified strike price on or before expiration (e.g., SPX options, KOSPI 200 options)"
        ),
        ("Derivatives", "expiration (expiry)"): (
            "Expiration (Expiry)", "", "Expiration (Expiry)",
            "The point in time when a futures or options contract ceases to trade and all remaining open rights and obligations are either exercised, cash-settled, delivered, or expire worthless"
        ),
        ("Derivatives", "final settlement"): (
            "Final Settlement", "", "Final Settlement",
            "The ultimate fulfillment of obligations under an expiring futures or options contract at maturity through cash settlement (based on the final settlement price) or physical delivery"
        ),
        ("Derivatives", "futures"): (
            "Futures", "", "Futures",
            "Standardized, exchange-traded contracts obligating the buyer to purchase and the seller to sell a specific underlying asset or financial instrument at a predetermined price at a specified future time"
        ),
        ("Derivatives", "implied order"): (
            "Implied Order", "", "Implied Order",
            "A synthetic order automatically generated by an exchange matching engine from combinations of outright leg orders and calendar/strategy spread orders, pooling liquidity across related contracts (Implied IN / Implied OUT)"
        ),
        ("Derivatives", "interest rate futures"): (
            "Interest Rate Futures", "", "Interest Rate Futures",
            "Standardized futures contracts based on an interest-bearing instrument or benchmark rate (e.g., government bonds such as U.S. Treasury or KTB futures, or short-term rates such as SOFR, CORRA, or TONA)"
        ),
        ("Derivatives", "open interest"): (
            "Open Interest", "OI", "Open Interest (OI)",
            "The total number of outstanding futures or options contracts that remain open and have not yet been offset, exercised, or delivered at a given point in time; a key indicator of market depth and participation"
        ),
        ("Derivatives", "options"): (
            "Options", "", "Options",
            "Derivatives contracts that grant the buyer (holder) the right, but not the obligation, to buy (call) or sell (put) an underlying asset at a specified strike price on or before a specified expiration date in exchange for paying a premium"
        ),
        ("Derivatives", "position limit"): (
            "Position Limit", "", "Position Limit",
            "The maximum number of net long or short contracts in a specific derivative instrument that a single market participant or group of accounts is permitted to hold, set by an exchange or regulator to prevent market manipulation and excessive concentration"
        ),
        ("Derivatives", "spread trading"): (
            "Spread Trading", "", "Spread Trading",
            "A trading strategy involving the simultaneous purchase of one futures or options contract and sale of a related contract (e.g., calendar spread across expiries, inter-commodity spread, or option vertical/straddle spread) to profit from changes in the price differential"
        ),
        ("Derivatives", "swap"): (
            "Swap", "", "Swap",
            "A derivative contract in which two counterparties agree to exchange streams of cash flows over a specified period based on notional principal amounts; major categories include interest rate swaps (IRS), currency swaps, and credit default swaps (CDS)"
        ),
        ("Derivatives", "underlying (asset)"): (
            "Underlying (Asset)", "", "Underlying (Asset)",
            "The financial instrument, equity index, interest rate, currency, or physical commodity from which a derivative contract derives its value"
        ),
        ("Regulation", "security token"): (
            "Security Token", "", "Security Token",
            "A digital representation of a financial instrument (equity, bond, fund unit, or investment contract) issued and recorded on a distributed ledger (DLT/blockchain) under applicable securities law; in South Korea, mandatory registration of all security tokens with KSD is required under the revised Electronic Securities Act framework, effective January 2027"
        ),
    }

    for (cat, k), (t_en, abbr, t_ko_en, d_en) in missing_en_defs.items():
        if k in unified[cat]:
            unified[cat][k]["term_en"] = t_en
            unified[cat][k]["abbr"] = abbr
            unified[cat][k]["term_ko_en_col"] = t_ko_en
            unified[cat][k]["def_en"] = d_en

    # --- 2. Fill missing KO definitions for KSD, FSC (Korea), FSS (Korea) ---
    if "korea securities depository" in unified["Settlement"]:
        unified["Settlement"]["korea securities depository"].update({
            "term_en": "Korea Securities Depository (KSD)",
            "abbr": "KSD",
            "term_ko_en_col": "Korea Securities Depository (KSD)",
            "term_ko": "한국예탁결제원 (KSD)",
            "def_ko": "1974년 설립된 한국의 중앙예탁기관(CSD)으로 부산에 본사를 두고 있다. 증권 예탁·보관, 계좌대체 결제, 펀드 넷(FundNet) 결제, 명의개서 대행 서비스를 제공하며, ISO 20022 메시지 표준을 채택하였다. 전자증권법 개정에 따라 2027년 1월부터 토큰증권(보안토큰) 의무 전자등록 총괄기관 역할을 수행한다.",
            "krx_note": "한국 CSD; 1974년 설립(부산 본사); ISO 20022 채택",
        })

    if "financial services commission (korea)" in unified["Regulation"]:
        unified["Regulation"]["financial services commission (korea)"].update({
            "term_en": "Financial Services Commission (Korea)",
            "abbr": "FSC",
            "term_ko_en_col": "Financial Services Commission (Korea) (FSC)",
            "term_ko": "금융위원회 (FSC)",
            "def_ko": "대한민국의 최고 금융규제·정책 기관으로, 금융정책 수립, 금융기관 및 시장인프라(KRX, NXT, KSD 등) 인허가, 자본시장법 등 금융법령 제·개정을 관할하고 한국거래소(KRX)를 감독한다.",
            "krx_note": "한국 최고 금융정책·감독기관; KRX·NXT 인허가 및 감독",
        })

    if "financial supervisory service (korea)" in unified["Regulation"]:
        unified["Regulation"]["financial supervisory service (korea)"].update({
            "term_en": "Financial Supervisory Service (Korea)",
            "abbr": "FSS",
            "term_ko_en_col": "Financial Supervisory Service (Korea) (FSS)",
            "term_ko": "금융감독원 (FSS)",
            "def_ko": "금융위원회(FSC)의 지도·감독 하에 은행, 증권, 파생상품, 보험 등 전 금융권에 대한 검사, 감독, 불공정거래 조사 및 제재 집행을 수행하는 한국의 금융감독 집행기관이다.",
            "krx_note": "한국 금융검사·감독·불공정거래 조사 집행기관",
        })

    # --- 3. Standardize inconsistent naming between EN and KO ---
    if "market-wide circuit breaker" in unified["Trading"]:
        unified["Trading"]["market-wide circuit breaker"].update({
            "term_en": "Market-Wide Circuit Breaker (US)",
            "abbr": "MWCB",
            "term_ko_en_col": "Market-Wide Circuit Breaker (US) (MWCB)",
        })
    if "exchange for physical" in unified["Derivatives"]:
        unified["Derivatives"]["exchange for physical"].update({
            "term_en": "Exchange for Physical",
            "abbr": "EFP",
            "term_ko_en_col": "Exchange for Physical (EFP)",
        })
    if "exchange for swap" in unified["Derivatives"]:
        unified["Derivatives"]["exchange for swap"].update({
            "term_en": "Exchange for Swap",
            "abbr": "EFS",
            "term_ko_en_col": "Exchange for Swap (EFS)",
        })
    if "sail (sola access information language)" in unified["Derivatives"]:
        unified["Derivatives"]["sail (sola access information language)"].update({
            "term_en": "SAIL (SOLA Access Information Language)",
            "abbr": "SAIL",
            "term_ko_en_col": "SAIL (SOLA Access Information Language)",
        })
    if "flex (full line-speed exchange)" in unified["Technology"]:
        unified["Technology"]["flex (full line-speed exchange)"].update({
            "term_en": "FLEX (Full Line-speed Exchange)",
            "abbr": "FLEX",
            "term_ko_en_col": "FLEX (Full Line-speed Exchange)",
        })
    if "ntp (new trading platform)" in unified["Technology"]:
        unified["Technology"]["ntp (new trading platform)"].update({
            "term_en": "NTP (New Trading Platform)",
            "abbr": "NTP",
            "term_ko_en_col": "NTP (New Trading Platform)",
        })
    if "0dte options" in unified["Derivatives"]:
        unified["Derivatives"]["0dte options"].update({
            "term_en": "0DTE Options",
            "abbr": "0DTE",
            "term_ko_en_col": "0DTE Options",
            "term_ko": "당일만기옵션 (0DTE)",
            "def_en": "See: Zero Days to Expiration (0DTE)",
            "def_ko": "Zero Days to Expiration (0DTE) 참조. 거래 당일에 만기가 도래하는 초단기 옵션 계약이다.",
            "krx_note": "Zero Days to Expiration 참조",
        })

    # --- 4. Fix KRX Factual & Regulatory Errors and Enhance Key Entries ---
    # 4a. Call Auction (Single-Price Auction) — replace old 'call auction (simultaneous order matching)'
    if "call auction (simultaneous order matching)" in unified["Trading"]:
        del unified["Trading"]["call auction (simultaneous order matching)"]

    unified["Trading"]["call auction (single-price auction)"] = {
        "term_en": "Call Auction (Single-Price Auction)",
        "abbr": "",
        "term_ko_en_col": "Call Auction (Single-Price Auction)",
        "term_ko": "단일가매매 (단일가격에 의한 개별경쟁매매)",
        "def_en": "A price discovery mechanism (officially termed '단일가격에 의한 개별경쟁매매' at KRX) where orders accumulated over a specified period are matched at a single equilibrium price (합치가격) where aggregate buy and sell volumes intersect. Used at KRX for opening (08:30–09:00), closing (15:20–15:30), VI-triggered cooling-off (2-min), and after-hours single-price auctions. Contrary to the colloquial label 'simultaneous quotes' (동시호가), KRX single-price auctions apply strict price-time priority (가격·시간 우선원칙), NOT simultaneous arrival treatment, except when the auction price is determined at the daily upper or lower price limit (where simultaneous order quantity allocation rules apply) [KRX Equities Business Regulation Art. 22②③, Art. 23].",
        "def_ko": "일정 시간 동안 호가를 접수한 후 매도호가 합계수량과 매수호가 합계수량이 일정한 가격에서 합치하는 단일 가격(합치가격)으로 일괄 체결하는 매매 방식이다(KRX 정식 명칭: 단일가격에 의한 개별경쟁매매). KRX에서는 시가(08:30~09:00), 종가(15:20~15:30), 변동성완화장치(VI) 발동 시(2분), 시간외단일가 등에 사용된다. 관행적으로 호가접수 시간대를 '동시호가'라 부르기도 하나, 실제 규정상 상한가·하한가로 가격이 결정되는 예외적인 경우(동시호가 수량배분 특례)를 제외하고는 모든 단일가매매 호가에 동시 접수가 아닌 엄격한 '가격·시간 우선원칙'이 적용된다 [유가증권시장 업무규정 제22조②③, 제23조].",
        "krx_note": "KRX: 시가·종가·VI 가격 결정; 상·하한가 체결 외 가격·시간우선 적용 [업무규정 제22조·제23조]",
    }

    # 4b. Simultaneous Bids and Offers (Dongsi Hoga) — dedicated accurate entry at S
    unified["Trading"]["simultaneous bids and offers (dongsi hoga)"] = {
        "term_en": "Simultaneous Bids and Offers (Dongsi Hoga)",
        "abbr": "",
        "term_ko_en_col": "Simultaneous Bids and Offers (Dongsi Hoga)",
        "term_ko": "동시호가 (호가시간 선후 미구분 특례)",
        "def_en": "Under KRX rules (Equities Business Regulation Art. 2⑥, Art. 22③; Enforcement Rules Art. 34; Derivatives Business Regulation Art. 72③2), orders whose time of entry is not differentiated ('호가시간의 선후를 구분하지 아니하는 호가'). Strictly applied ONLY when a single-price call auction determines the price at the daily upper limit (limit-up buy orders, including market orders deemed limit-up) or lower limit (limit-down sell orders, including market orders deemed limit-down), as well as certain retail bond quotes. In such limit-up/limit-down executions, time priority is waived and fills are allocated by staged quantity priority (수량우선 단계별 배분: 100× trading unit → 1/2 of remaining quantity → remaining quantity; client orders prioritized over proprietary orders for ETFs/ETNs/ELWs). All non-limit-up/down call auction executions follow normal price-time priority.",
        "def_ko": "KRX 규정(유가증권시장 업무규정 제2조제6항·제22조제3항, 시행세칙 제34조)상 '호가시간의 선후를 구분하지 아니하는 호가'를 말한다. 시가 및 거래재개 후 최초가격 등을 결정하는 단일가매매에서 합치가격이 상한가로 결정될 때의 상한가 매수호가(상한가 간주 시장가호가 포함) 또는 하한가로 결정될 때의 하한가 매도호가(하한가 간주 시장가호가 포함)에 한하여 예외적으로 동시호가로 간주하며, 시간우선을 배제하고 수량우선(매매수량단위의 100배 → 잔량의 1/2 → 잔량 순 단계별 배분; ETF·ETN·ELW는 위탁매매호가 우선)을 적용한다. 상·하한가 체결 외의 일반 단일가매매에서는 동시호가가 아닌 시간우선원칙이 적용된다.",
        "krx_note": "KRX: 상·하한가 체결 시에만 시간우선 배제·수량배분 적용 [업무규정 제2조⑥·제22조③, 세칙 제34조]",
    }

    # 4c. Update Auction, Opening Auction, Closing Auction, Continuous Trading, Lot Size, Market Maker, Matching Engine, Corporate Governance Code, Best Execution
    unified["Trading"]["auction"].update({
        "term_ko": "경매 (단일가매매)",
        "def_en": "A trading mechanism where buy and sell orders are collected over a designated period and matched at a single clearing price that maximizes executable volume",
        "def_ko": "일정 기간 동안 매수·매도 주문을 수집한 후 체결 가능 수량을 극대화하는 단일 균형가격으로 일괄 체결하는 매매 방식이다.",
        "krx_note": "KRX: 단일가매매 (가격·시간우선 원칙 적용, 상·하한가 시에만 동시호가 배분)",
    })

    unified["Trading"]["opening auction"].update({
        "term_ko": "시가단일가매매 (개장 경매)",
        "def_en": "A call auction held at the start of the trading day to establish the official opening price from accumulated pre-open orders (e.g., NASDAQ Opening Cross at 09:30 ET; KRX Opening Call Auction 08:30–09:00 KST, during which Nextrade pauses trading from 08:50–09:00 KST to protect price discovery)",
        "def_ko": "거래일 개시 시점에 누적된 호가를 바탕으로 공식 시가를 결정하기 위해 실시하는 단일가매매이다. KRX는 08:30~09:00 호가를 접수하여 가격·시간 우선원칙(상·하한가 결정 시에는 동시호가 수량배분)으로 시가를 산출하며, 시가 대표성 보호를 위해 대체거래소(NXT)는 08:50~09:00 동안 거래를 일시 중단한다.",
        "krx_note": "KRX: 시가 단일가매매 (08:30~09:00, 가격·시간우선); NXT 08:50~09:00 휴장",
    })

    unified["Trading"]["closing auction"].update({
        "term_ko": "종가단일가매매 (장마감 경매)",
        "def_en": "A call auction held at the end of the regular trading session to determine the official closing price (e.g., NASDAQ Closing Cross at 16:00 ET; KRX Closing Call Auction 15:20–15:30 KST, during which Nextrade pauses trading to concentrate closing liquidity on KRX)",
        "def_ko": "정규 거래일 종료 시 공식 종가를 결정하기 위해 실시하는 단일가매매이다. KRX는 15:20~15:30 동안 호가를 접수하여 가격·시간 우선원칙에 따라 종가를 확정하며, 이 시간 동안 대체거래소(NXT)는 거래를 일시 중단하여 유동성을 KRX로 집중시킨다.",
        "krx_note": "KRX: 종가 단일가매매 (15:20~15:30, 가격·시간우선); NXT 15:20~15:30 휴장",
    })

    unified["Trading"]["continuous trading"].update({
        "term_en": "Continuous Trading",
        "abbr": "",
        "term_ko_en_col": "Continuous Trading",
        "term_ko": "접속매매 (복수가격에 의한 개별경쟁매매, 연속매매)",
        "def_en": "A trading method where incoming orders are matched immediately and continuously against resting orders in the central limit order book according to price-time priority, generating multiple execution prices throughout the session (officially termed '복수가격에 의한 개별경쟁매매' or '접속매매' at KRX) [KRX Equities Business Regulation Art. 24]",
        "def_ko": "정규 거래시간 중 시가 및 종가 단일가매매 사이에 주문이 호가장에 도착하는 즉시 가격·시간 우선원칙에 따라 선행호가의 가격으로 연속 체결되는 매매 방식이다(KRX 정식 명칭: 복수가격에 의한 개별경쟁매매, 전통적 명칭: 접속매매) [유가증권시장 업무규정 제24조].",
        "krx_note": "KRX: 복수가격에 의한 개별경쟁매매 (접속매매, 09:00~15:20) [업무규정 제24조]",
    })

    if "lot size" in unified["Trading"]:
        unified["Trading"]["lot size"]["krx_note"] = "KRX: 주권 1주 (유가증권시장 2014년 6월 1주 단일화, 코스닥 1주)"

    if "market maker" in unified["Trading"]:
        unified["Trading"]["market maker"]["krx_note"] = "KRX: 시장조성자(MM) 및 유동성공급자(LP) 제도 운영"

    if "matching engine" in unified["Technology"]:
        unified["Technology"]["matching engine"]["krx_note"] = "KRX: Exture 3.0 매매체결엔진 (2023년 가동)"

    if "corporate governance code" in unified["Regulation"]:
        unified["Regulation"]["corporate governance code"]["krx_note"] = "KRX: 기업지배구조보고서 의무공시 및 한국ESG기준원(구 한국기업지배구조원)"

    if "best execution" in unified["Regulation"]:
        unified["Regulation"]["best execution"].update({
            "def_en": "The regulatory obligation of broker-dealers to execute client orders on the most favorable terms reasonably available across competing trading venues (price, cost, speed, and likelihood of execution); enforced in South Korea under FSCMA Article 68-2 with the launch of Nextrade (NXT) in March 2025",
            "def_ko": "복수 거래소 환경에서 금융투자업자가 가격, 수수료, 체결 신속성 및 가능성 등을 종합 고려하여 고객 주문을 가장 유리한 조건으로 집행해야 하는 법적 의무이다. 한국에서는 2025년 3월 대체거래소(NXT) 출범과 함께 자본시장법 제68조의2에 따른 최선집행의무 및 증권사 SOR 시스템 운영이 전면 시행되었다.",
            "krx_note": "자본시장법 제68조의2; 2025년 3월 NXT 출범과 함께 전면 시행",
        })

    # 4d. Fix Volatility Interruption (VI) — KRX (Static VI = 10%, Dynamic VI = 3%/6%)
    unified["Trading"]["volatility interruption (vi) — krx"] = {
        "term_en": "Volatility Interruption (VI) — KRX",
        "abbr": "VI",
        "term_ko_en_col": "Volatility Interruption (VI) — KRX",
        "term_ko": "변동성완화장치 (VI, Volatility Interruption)",
        "def_en": "KRX's per-security price stabilization mechanism (Equities Business Regulation Art. 26-2; Enforcement Rules Art. 41-2) consisting of: (1) Dynamic VI (동적VI), triggered when a potential execution price deviates from the immediately preceding trade price by ±3% (KOSPI 200 constituents) or ±6% (other stocks) during continuous trading (±2% / ±4% during closing auction; ±1% on derivatives final trading day closing auction); and (2) Static VI (정적VI), triggered when a potential execution price deviates by ±10% from the preceding single-price auction price (or base price prior to opening). When triggered, continuous trading switches to a 2-minute single-price call auction (or extends call auction reception by 2 minutes) with a 30-second random end.",
        "def_ko": "개별 종목의 급격한 가격 변동을 완화하는 KRX의 안전장치(유가증권시장 업무규정 제26조의2, 시행세칙 제41조의2)로, ① 동적VI(잠정 체결가격이 직전 체결가격 대비 KOSPI 200 구성종목 ±3%, 기타 종목 ±6% 이상 이탈 시 발동; 종가 단일가 시 2%/4%, 파생 만기일 종가 단일가 시 1%)와 ② 정적VI(잠정 체결가격이 직전 단일가매매 가격 또는 시가 결정 전 당일 기준가격 대비 ±10% 이상 이탈 시 발동)로 구성된다. 발동 시 2분간 단일가매매로 전환(단일가매매 중 발동 시 호가접수시간 2분 연장)하고 30초 이내 랜덤엔드(무작위 종료)를 적용한다.",
        "krx_note": "KRX: 동적VI(직전가 대비 ±3%/±6%), 정적VI(직전 단일가 대비 ±10%); 2분 단일가+30초 랜덤엔드",
    }

    # 4e. Enhance Sidecar (Program Trading Suspension) in Trading
    unified["Trading"]["sidecar (program trading suspension)"] = {
        "term_en": "Sidecar (Program Trading Suspension)",
        "abbr": "Sidecar",
        "term_ko_en_col": "Sidecar (Program Trading Suspension)",
        "term_ko": "사이드카 (프로그램매매호가 효력정지)",
        "def_en": "KRX cash equity market mechanism that suspends the effectiveness of program trading orders for 5 minutes when benchmark futures experience sharp movements for 1 minute: in KOSPI, triggered when KOSPI 200 front-month futures move ±5% from base price [Equities Business Regulation Art. 16]; in KOSDAQ, triggered when KOSDAQ 150 futures move ±6% AND the KOSDAQ 150 index moves ±3% [KOSDAQ Business Regulation Art. 13]. Applied once per day and not triggered after 14:50 KST.",
        "def_ko": "선물가격 급변 시 현물 주식시장에 대한 차익·비차익 프로그램매매의 충격을 완화하기 위해 프로그램매매 호가 효력을 5분간 정지하는 KRX 제도이다. 유가증권시장(KOSPI)은 KOSPI 200 최근월물 선물이 기준가 대비 ±5% 이상 변동 상태가 1분간 지속될 때[업무규정 제16조], 코스닥시장은 코스닥150 선물이 ±6% 이상 변동하고 코스닥150 지수가 ±3% 이상 변동한 상태가 1분간 지속될 때 발동된다. 1일 1회 한정이며 14:50 이후에는 발동하지 않는다.",
        "krx_note": "KRX: KOSPI(선물 ±5%), KOSDAQ(선물 ±6% & 지수 ±3%) 1분 지속 시 5분간 효력정지",
    }

    # 4f. Add accurate KRX Derivatives Risk Control entries in Derivatives
    unified["Derivatives"]["multi-stage price limit expansion (krx)"] = {
        "term_en": "Multi-Stage Price Limit Expansion (KRX)",
        "abbr": "",
        "term_ko_en_col": "Multi-Stage Price Limit Expansion (KRX)",
        "term_ko": "단계별 가격제한폭 확대제도 (KRX 파생상품)",
        "def_en": "KRX derivatives market price limit mechanism (Derivatives Business Regulation Art. 70; Enforcement Rules Art. 56-2) introduced in June 2015 to replace the legacy standalone derivatives circuit breaker. For equity index futures (e.g., KOSPI 200 futures), daily price limits expand sequentially across three stages—Stage 1 (±8%), Stage 2 (±15%), and Stage 3 (±20%)—when the lead-month contract remains at the current stage's upper or lower limit for 5 minutes. Mandatory trading halts in equity derivatives are synchronized with the underlying cash equity market's Market-Wide Circuit Breaker (MWCB) [Art. 77].",
        "def_ko": "2015년 6월 기존 파생상품 독자 서킷브레이커(제78조)를 폐지하고 도입된 KRX 파생상품시장의 가격안정화 제도이다(파생상품시장 업무규정 제70조, 시행세칙 제56조의2). 주가지수선물(KOSPI 200 선물 등)의 가격제한폭을 기준가격 대비 1단계(±8%) → 2단계(±15%) → 3단계(±20%)로 설정하고, 기준종목 약정가격이 해당 단계 상·하한가에 도달한 후 5분 경과 시 다음 단계로 순차 확대한다. 시장전체 거래중단은 현물 주식시장 서킷브레이커(MWCB) 발동과 연동하여 실행된다(규정 제77조).",
        "krx_note": "KRX 파생: 주가지수선물 ±8%→±15%→±20% 3단계 확대 (5분 지속 시) [세칙 제56조의2]",
    }

    unified["Derivatives"]["real-time price limit (krx)"] = {
        "term_en": "Real-Time Price Limit (KRX)",
        "abbr": "RTPL",
        "term_ko_en_col": "Real-Time Price Limit (KRX) (RTPL)",
        "term_ko": "실시간 가격제한제도 (실시간상·하한가)",
        "def_en": "KRX derivatives market pre-trade dynamic price collar (Derivatives Business Regulation Art. 70-2; Enforcement Rules Art. 60-3 to 60-5) applied during continuous trading to prevent sudden price spikes from erroneous orders or momentary illiquidity. Buy orders above the Real-Time Upper Limit (실시간상한가, last trade price + price band) and sell orders below the Real-Time Lower Limit (실시간하한가, last trade price − price band) are rejected, while market orders breaching the band are automatically converted into limit orders at the real-time limit price.",
        "def_ko": "KRX 파생상품시장의 복수가격 개별경쟁거래(접속거래) 중 착오주문이나 일시적 수급 공백으로 인한 급격한 가격 급등락을 방지하기 위해 직전약정가격을 기준으로 실시간상한가 및 실시간하한가(직전약정가격 ± 가격변동폭)를 설정하는 동적 가격밴드 제도이다(파생상품시장 업무규정 제70조의2). 실시간상·하한가를 벗어나는 지정가호가는 접수가 거부되며, 시장가호가는 실시간상·하한가의 지정가호가로 자동 전환된다.",
        "krx_note": "KRX 파생: 직전약정가격 기준 실시간상·하한가 밴드 적용 [업무규정 제70조의2]",
    }

    # 4g. Fix Split Settlement arrow in KRX note
    if "split settlement" in unified["Settlement"]:
        unified["Settlement"]["split settlement"]["krx_note"] = "KSD: 2021년 도입; 단위 100억 → 50억 → 10억 단계적 축소"

    # 4h. Fix Stop Order Korean translation and enrich Mid-Price Pegged Order & Nextrade
    if "stop order" in unified["Trading"]:
        unified["Trading"]["stop order"].update({
            "term_ko": "스톱주문 (역지정가주문)",
            "def_en": "A conditional order that remains inactive until the market price reaches a specified trigger (stop) price, at which point it becomes a market order for immediate execution",
            "def_ko": "시장 가격이 사전에 지정한 트리거 가격(스톱가격)에 도달하면 시장가주문으로 활성화되어 즉시 체결을 추구하는 조건부 주문이다.",
            "krx_note": "KRX는 지정가로 전환되는 스톱지정가호가 운영 (2025년 3월~)",
        })

    if "mid-price pegged order" in unified["Trading"]:
        unified["Trading"]["mid-price pegged order"].update({
            "term_en": "Mid-Price Pegged Order (Midpoint Order)",
            "abbr": "MPL",
            "term_ko_en_col": "Mid-Price Pegged Order (MPL)",
            "term_ko": "중간가호가 (중간가격연동주문)",
            "def_en": "An order whose price is automatically pegged to the exact midpoint between the current best bid and best ask (NBBO or local BBO), providing price improvement and minimizing spread costs. Adopted across U.S. exchanges/ATSs, European dark pools, and introduced in South Korea by both KRX and Nextrade (NXT) in March 2025 [KRX Equities Business Regulation Art. 2④7].",
            "def_ko": "최우선 매수호가와 최우선 매도호가의 정중앙 가격(BBO/NBBO 중간값)으로 호가 가격이 자동 설정·조정되는 주문유형이다. 매수·매도 스프레드 비용을 절감하고 가격 개선을 제공하며, 한국에서는 2025년 3월 대체거래소(NXT) 출범과 함께 KRX 및 NXT 정규시장에 동시 도입되었다 [유가증권시장 업무규정 제2조④7호].",
            "krx_note": "KRX·NXT: 중간가호가 (2025년 3월 도입, 접속매매 중 허용) [업무규정 제2조④7호]",
        })

    if "nextrade" in unified["Market Segments & Boards"]:
        unified["Market Segments & Boards"]["nextrade"].update({
            "term_en": "Nextrade (NXT)",
            "abbr": "NXT",
            "term_ko_en_col": "Nextrade (NXT)",
            "term_ko": "넥스트레이드 (Nextrade, NXT)",
            "def_en": "South Korea's first Multilateral Trading Facility / Alternative Trading System (ATS), launched on March 4, 2025, ending KRX's 69-year monopoly. Operates 12-hour daily continuous trading (Pre-Market 08:00–08:50, Regular 09:00–15:20, After-Market 15:30–20:00 KST) across ~800 KOSPI/KOSDAQ equities, stabilizing at a 10–15% market share as of November 2026 within statutory volume caps (15% market-wide, 30% per stock). Halts matching during KRX's opening (08:50–09:00) and closing (15:20–15:30) call auctions to protect official price discovery, clears via KRX CCP, and connects via broker Smart Order Routing (SOR).",
            "def_ko": "2025년 3월 4일 공식 출범한 대한민국 최초의 다자간매매체결회사(대체거래소, ATS)로, KRX의 69년 단일 증권거래소 독점 체제를 복수 경쟁 체제로 전환시켰다. 일일 12시간 거래(프리마켓 08:00~08:50, 정규장 09:00~15:20, 애프터마켓 15:30~20:00)를 운영하며, 자본시장법상 거래량 한도(전체 시장 15%, 개별 종목 30%) 내에서 2026년 11월 현재 대상 우량주 기준 10~15% 점유율에 안착하였다. 시·종가 대표성 보호를 위해 KRX 시가 단일가(08:50~09:00) 및 종가 단일가(15:20~15:30) 시간에는 매매를 일시 정지하며, 증권사 SOR 최선집행 및 KRX CCP·KSD 통합 청산결제와 연동된다.",
            "krx_note": "한국 제1호 ATS (2025.3 출범); 점유율 10~15% 안착; KRX 시·종가 단일가 시간대 휴장",
        })

    if "maker-taker" in unified["Trading"]:
        unified["Trading"]["maker-taker"].update({
            "def_en": "A venue pricing model where passive liquidity providers (makers posting resting limit orders) receive a fee rebate or reduced fee while aggressive liquidity takers (orders removing resting liquidity) pay a higher execution fee; widely used in North America and Europe, and introduced by KRX in December 2025 in response to multi-venue competition with Nextrade",
            "def_ko": "호가장에 대기 주문을 제출하여 유동성을 공급하는 참가자(메이커)에게는 수수료 감면·리베이트를 부여하고, 대기 호가를 즉시 체결시켜 유동성을 소비하는 참가자(테이커)에게는 상대적으로 높은 수수료를 부과하는 가격 모델이다. KRX는 복수 거래소(NXT) 경쟁에 대응하여 2025년 12월 차등 수수료 체계를 도입하였다.",
            "krx_note": "KRX: 2025년 12월 메이커-테이커 차등 수수료 도입",
        })

    # --- 5. Add New Essential Trading & Market Microstructure Terms ---
    new_trading_terms = {
        "best limit order": {
            "term_en": "Best Limit Order",
            "abbr": "",
            "term_ko_en_col": "Best Limit Order",
            "term_ko": "최유리지정가호가",
            "def_en": "KRX order type (Equities Business Regulation Art. 2④4) where the party specifies security and quantity, and the price is automatically set to the best price on the opposite side of the order book at the time of receipt (i.e., best bid for a sell order, best ask for a buy order) to achieve immediate execution without crossing multiple price levels like a pure market order.",
            "def_ko": "종목과 수량만 지정하고 가격은 호가 접수 시점의 상대방 최우선호가 가격(매도호가의 경우 최우선 매수호가, 매수호가의 경우 최우선 매도호가)으로 자동 지정되는 KRX 호가 유형이다 [유가증권시장 업무규정 제2조④4호].",
            "krx_note": "KRX: 상대방 최우선호가 가격으로 자동 지정 [업무규정 제2조④4호]",
        },
        "best priority limit order": {
            "term_en": "Best Priority Limit Order",
            "abbr": "",
            "term_ko_en_col": "Best Priority Limit Order",
            "term_ko": "최우선지정가호가",
            "def_en": "KRX order type (Equities Business Regulation Art. 2④5) where the party specifies security and quantity, and the price is automatically set to the best price on the same side of the order book at the time of receipt (i.e., best ask for a sell order, best bid for a buy order) to passively join the top of the queue.",
            "def_ko": "종목과 수량만 지정하고 가격은 호가 접수 시점의 자기 방향 최우선호가 가격(매도호가의 경우 최우선 매도호가, 매수호가의 경우 최우선 매수호가)으로 자동 지정되어 대기 유동성을 공급하는 KRX 호가 유형이다 [유가증권시장 업무규정 제2조④5호].",
            "krx_note": "KRX: 자기 측 최우선호가 가격으로 자동 지정 [업무규정 제2조④5호]",
        },
        "imbalance only order": {
            "term_en": "Imbalance Only Order",
            "abbr": "OIO / CIO",
            "term_ko_en_col": "Imbalance Only Order (OIO / CIO)",
            "term_ko": "불균형상쇄주문 (OIO / CIO)",
            "def_en": "Specialized limit order type used in NASDAQ's Opening Cross (OIO) and Closing Cross (CIO) that executes only against order imbalances on the opposite side without moving the inside market price (buy OIOs are capped at the best bid; sell OIOs are floored at the best ask). Can be entered even after the late-auction Order Freeze, allowing market makers and HFTs to safely supply offsetting liquidity against passive rebalancing flows.",
            "def_ko": "NASDAQ의 시가(Opening Cross, OIO) 및 종가(Closing Cross, CIO) 경매 전용 호가로, 수량 불균형이 발생한 반대 방향에서만 불균형 해소 물량 한도 내로 체결된다. 호가 동결(Order Freeze) 이후에도 신규 제출이 가능하며, 최우선호가를 변경하지 못하도록 가격 상·하한(Cap)이 씌워져 시장조성자(MM)가 가격 왜곡 위험 없이 리밸런싱 불균형을 흡수할 수 있게 한다.",
            "krx_note": "NASDAQ 개·폐장 크로스 전용 유동성 공급 호가",
        },
        "limit-on-open / limit-on-close order": {
            "term_en": "Limit-on-Open / Limit-on-Close Order",
            "abbr": "LOO / LOC",
            "term_ko_en_col": "Limit-on-Open / Limit-on-Close Order (LOO / LOC)",
            "term_ko": "시가·종가 지정가주문 (LOO / LOC)",
            "def_en": "Orders that participate exclusively in the opening auction (LOO) or closing auction (LOC) and execute only if the determined auction cross price is equal to or better than the specified limit price; widely used by active institutional investors and quant funds seeking auction liquidity with price protection.",
            "def_ko": "개장 경매(Opening Cross/Auction, LOO) 또는 장마감 경매(Closing Cross/Auction, LOC)에만 참여하되, 산출된 합치가격이 지정한 한도 가격보다 유리하거나 같을 때만 체결되는 주문유형이다. 유동성이 집중되는 시·종가 경매에서 가격 보호를 원하는 액티브 기관투자자들이 주로 활용한다.",
            "krx_note": "미국(NASDAQ/NYSE) 등 시·종가 경매 전용 지정가주문",
        },
        "market-on-open / market-on-close order": {
            "term_en": "Market-on-Open / Market-on-Close Order",
            "abbr": "MOO / MOC",
            "term_ko_en_col": "Market-on-Open / Market-on-Close Order (MOO / MOC)",
            "term_ko": "시가·종가 시장가주문 (MOO / MOC)",
            "def_en": "Orders that participate exclusively in the opening auction (MOO) or closing auction (MOC) without a limit price, guaranteed top execution priority at the official auction cross price; extensively used by passive index funds and ETFs to execute benchmark rebalancing with zero tracking error.",
            "def_ko": "개장 경매(MOO) 또는 장마감 경매(MOC)에서 산출되는 단일 합치가격으로 최우선 체결을 보장받는 시장가 주문이다. 벤치마크 지수와의 추적오차(Tracking Error)를 0으로 맞춰야 하는 패시브 인덱스 펀드 및 ETF의 대규모 리밸런싱에 핵심적으로 사용된다.",
            "krx_note": "패시브 펀드·ETF 리밸런싱 핵심 수단; KRX는 종가 단일가에 조건부지정가·시장가 활용",
        },
        "order-driven market": {
            "term_en": "Order-Driven Market",
            "abbr": "",
            "term_ko_en_col": "Order-Driven Market",
            "term_ko": "주문주도형 시장 (경매시장)",
            "def_en": "A market microstructure model where buy and sell orders submitted by investors are aggregated in a central limit order book (CLOB) and matched directly against one another according to deterministic rules (such as price-time priority) without requiring dealer intermediation (e.g., KRX, JPX, Euronext, and modern NASDAQ continuous trading).",
            "def_ko": "투자자들이 제출한 매수·매도 주문(Order)이 중앙 호가장(Order Book)에 집적되어 딜러의 중개 없이 가격·시간 우선원칙 등 사전에 정해진 규칙에 따라 투자자 간 직접 매칭·체결되는 시장 구조이다(예: KRX, JPX, 현대 NASDAQ 장중 매매).",
            "krx_note": "KRX: 전형적인 주문주도형 시장 구조 채택",
        },
        "quote-driven market": {
            "term_en": "Quote-Driven Market",
            "abbr": "",
            "term_ko_en_col": "Quote-Driven Market",
            "term_ko": "호가주도형 시장 (딜러시장)",
            "def_en": "A market microstructure model (dealer market) where designated market makers or dealers continuously post two-sided bid and ask quotes using their own capital and inventory, and investors trade exclusively against the dealers' quotes rather than directly with other investors (e.g., OTC bond markets, FX markets, and pre-ECN legacy NASDAQ).",
            "def_ko": "전문 딜러(시장조성자, Market Maker)가 자기 자본과 재고(Inventory)를 바탕으로 지속적인 매수·매도 호가(Quote)를 제시하고, 투자자는 딜러가 제시한 가격에 딜러를 상대로 거래하는 시장 구조이다(예: 장외 채권시장, 외환시장, 과거 초기 NASDAQ).",
            "krx_note": "장외 채권·FX 등; 주식시장은 주문주도형 기반에 LP/MM 호가주도 요소를 결합한 하이브리드화 추세",
        },
        "random end": {
            "term_en": "Random End",
            "abbr": "",
            "term_ko_en_col": "Random End",
            "term_ko": "랜덤엔드 (무작위 종료)",
            "def_en": "An anti-manipulation mechanism in call auctions where the exact auction matching time is randomized within a short window (e.g., within 30 seconds at KRX during VI auctions, or at ASX, Deutsche Börse, and Euronext) to deter last-second spoofing and phantom order placement.",
            "def_ko": "단일가매매 마감 직전에 허수 호가를 대량 입력했다가 취소하여 예상체결가를 왜곡하는 시세조종(스푸핑)을 방지하기 위해, 정확한 체결 시점을 일정 시간 범위 내에서 무작위로 결정하는 장치이다. KRX는 변동성완화장치(VI) 발동 시 및 단기과열·저유동성 단일가매매 등에서 30초 이내 무작위 종료를 적용한다 [시행세칙 제35조①].",
            "krx_note": "KRX: VI 발동 및 단기과열·저유동성 단일가매매 시 30초 이내 무작위 종료 [세칙 제35조①]",
        },
        "smart order routing": {
            "term_en": "Smart Order Routing",
            "abbr": "SOR",
            "term_ko_en_col": "Smart Order Routing (SOR)",
            "term_ko": "스마트주문라우팅 (SOR)",
            "def_en": "An automated order execution system used by brokers in fragmented, multi-venue markets to fulfill Best Execution obligations by scanning real-time quotes, depths, and fees across competing trading venues (e.g., KRX and Nextrade in South Korea; 16 exchanges and ATSs in the U.S.) and routing orders to the optimal venue(s).",
            "def_ko": "복수 거래소(시장 파편화) 체제에서 증권사가 최선집행의무(Best Execution)를 이행하기 위해 각 거래소(예: 한국의 KRX와 NXT, 미국의 16개 거래소 및 ATS)의 호가 잔량, 가격, 수수료, 체결 가능성을 실시간으로 비교·분석하여 가장 유리한 거래소로 주문을 자동 배분·전송하는 시스템이다.",
            "krx_note": "한국: 2025년 3월 NXT 출범과 함께 전 증권사 SOR 구축 의무화 (KRX·NXT 자동 배분)",
        },
        "stop-limit order": {
            "term_en": "Stop-Limit Order",
            "abbr": "",
            "term_ko_en_col": "Stop-Limit Order",
            "term_ko": "스톱지정가호가",
            "def_en": "A conditional order specifying both a trigger (stop) price and a limit price; once the market trade price reaches or breaches the stop price, the order is automatically activated as a limit order in the order book. Introduced at KRX and Nextrade (NXT) in March 2025 [KRX Equities Business Regulation Art. 2④8; Enforcement Rules Art. 15-2].",
            "def_ko": "스톱가격(조건 가격)과 지정가격을 동시에 설정하는 조건부 호가로, 시장의 현재가(체결가)가 스톱가격에 도달하면 지정가호가로 효력이 발생하여 호가장에 진입하는 주문유형이다. 한국에서는 2025년 3월 대체거래소(NXT) 출범에 맞춰 KRX 및 NXT 정규시장에 도입되었으며, 지정가호가로 전환된 시점을 접수시간으로 하여 시간우선순위를 부여한다 [유가증권시장 업무규정 제2조④8호, 시행세칙 제15조의2].",
            "krx_note": "KRX·NXT: 2025년 3월 도입; 효력 발생 시점 기준 시간우선 적용 [업무규정 제2조④8호, 세칙 제15조의2]",
        },
    }

    for k, val in new_trading_terms.items():
        unified["Trading"][k] = val

    unified["Trading"]["auction collar / auction extension"] = {
        "term_en": "Auction Collar / Auction Extension",
        "abbr": "",
        "term_ko_en_col": "Auction Collar / Auction Extension",
        "term_ko": "경매 가격제한밴드 및 경매연장",
        "def_en": "Safeguard mechanisms in opening, closing, and volatility call auctions that restrict the indicative clearing price within predefined percentage or tick bands around a reference price (Auction Collar) or automatically extend the order collection window (Auction Extension / Imbalance Freeze) when severe order imbalances threaten disorderly price dislocations (used by NASDAQ, Euronext, Deutsche Börse, and KRX static/dynamic VI extensions).",
        "def_ko": "개·폐장 또는 변동성 단일가 경매에서 막대한 수급 불균형(예: 대규모 MOO/MOC 쏠림)으로 인해 합치가격이 기준가격 대비 비정상적인 범위를 벗어날 우려가 있을 때, 체결 가격의 상·하한 밴드를 제한(Auction Collar)하거나 경매 시간을 자동으로 연장(Auction Extension)하여 추가 반대 유동성 유입을 유도하는 시장안정화 장치이다.",
        "krx_note": "NASDAQ 크로스 및 유럽 거래소 운용; KRX는 시·종가 단일가 중 VI 발동 시 2분 연장",
    }

    unified["Trading"]["order freeze (late auction cutoff)"] = {
        "term_en": "Order Freeze (Late Auction Cutoff)",
        "abbr": "",
        "term_ko_en_col": "Order Freeze (Late Auction Cutoff)",
        "term_ko": "호가 동결 (경매 마감 직전 취소·정정 제한)",
        "def_en": "An anti-spoofing rule in call auctions (such as NASDAQ Opening Cross at 09:28 ET and Closing Cross at 15:50/15:55 ET) that prohibits cancellation or unfavorable modification of on-open/on-close orders (MOO/LOO/MOC/LOC) during the final minutes before the cross, while still permitting liquidity-supplying Imbalance Only Orders (OIO/CIO) to enter and offset imbalances.",
        "def_ko": "단일가 경매 마감 직전 일정 시간(예: NASDAQ 개장 2분 전인 09:28, 장마감 10분/5분 전)부터 기존 경매 전용 주문(MOO·LOO·MOC·LOC)의 취소 및 불리한 가격 정정을 금지하는 시세조종(스푸핑) 방지 규칙이다. 단, 불균형을 해소하는 방향의 유동성 공급 주문(OIO/CIO) 신규 진입은 허용하여 안정적 가격발견을 유도한다.",
        "krx_note": "NASDAQ 개·폐장 크로스 핵심 장치; KRX는 마감 시점 30초 랜덤엔드로 스푸핑 방지",
    }

    unified["Market Segments & Boards"]["24x national exchange"] = {
        "term_en": "24X National Exchange",
        "abbr": "24X",
        "term_ko_en_col": "24X National Exchange (24X)",
        "term_ko": "24X 내셔널 거래소 (미국 24시간 주식거래소)",
        "def_en": "U.S. SEC-approved national securities exchange pioneering 23/5 (overnight weekday) U.S. cash equity trading infrastructure; catalyzed industry-wide overnight session expansion by NYSE Arca (22-hour Pillar trading) and NASDAQ (23-hour weekday trading) targeting APAC and European investors during 2025–2026.",
        "def_ko": "미국 SEC로부터 주 5일 23시간(심야·새벽 세션 포함) 미국 주식 현물 매매 승인을 획득한 신설 정규 증권거래소이다. 2025~2026년에 걸쳐 NYSE Arca(22시간) 및 NASDAQ(23시간) 등 주류 거래소의 심야 거래 인프라 확충과 SIP·DTCC 야간 청산 연동을 촉발하였다.",
        "krx_note": "미국 24/5 주식거래 확산 촉매; 아태 지역 주간 시간대 미국 주식 직접 매매 지원",
    }

    unified["Market Segments & Boards"]["korea value-up index"] = {
        "term_en": "Korea Value-Up Index",
        "abbr": "",
        "term_ko_en_col": "Korea Value-Up Index",
        "term_ko": "코리아 밸류업 지수",
        "def_en": "Benchmark equity index launched by KRX in September 2024 as a centerpiece of the government's Corporate Value-Up Program to address the 'Korea Discount'; selects 100 KOSPI and KOSDAQ companies excelling in capital efficiency (ROE, PBR), shareholder returns, and governance disclosure, supported by listed Value-Up ETFs and KRX Value-Up index futures.",
        "def_ko": "코리아 디스카운트 해소와 상장기업의 자본효율성·주주환원 제고를 위해 KRX가 산출·발표하는 대표 기업가치 우수 지수(100종목)이다. 수익성, 주주환원, 시장평가(PBR), 자본효율성(ROE) 기준을 충족한 유가증권·코스닥 상장사로 구성되며, 연계 ETF 및 밸류업 지수선물이 상장되어 기관 벤치마크로 운용된다.",
        "krx_note": "KRX 기업 밸류업 프로그램 핵심 벤치마크 지수; 연계 ETF 및 지수선물 운용",
    }

    unified["Regulation"]["national short-sale detecting system"] = {
        "term_en": "National Short-sale Detecting System (KRX)",
        "abbr": "NSDS",
        "term_ko_en_col": "National Short-sale Detecting System (KRX) (NSDS)",
        "term_ko": "무차입공매도 중앙차단 시스템 (NSDS)",
        "def_en": "KRX's centralized automated surveillance system launched on March 31, 2025 alongside the resumption of short selling in South Korea; cross-verifies institutional investors' internal short-selling balance management systems against all KRX and Nextrade trade executions and borrow records to detect and block naked (uncovered) short selling.",
        "def_ko": "2025년 3월 31일 공매도 전면 재개와 함께 한국거래소(KRX)가 구축·가동한 중앙 집중식 무차입 공매도 자동 적출 시스템이다. 법인·기관투자자의 내부 잔고관리시스템 보고 내역과 KRX·NXT 전체 매매체결 및 대차거래 내역을 상시 교차 검증하여 불법 무차입 공매도를 전수 적발·차단한다.",
        "krx_note": "KRX: 2025년 3월 31일 가동; 기관 잔고관리시스템과 3중 검증망 구축",
    }

    unified["Settlement"]["same-day affirmation"] = {
        "term_en": "Same-Day Affirmation",
        "abbr": "SDA",
        "term_ko_en_col": "Same-Day Affirmation (SDA)",
        "term_ko": "당일 매매확인 (SDA)",
        "def_en": "The operational requirement under T+1 settlement regimes (such as U.S. SEC Rule 15c6-2 implemented May 2024) that institutional trade allocations, confirmations, and affirmations between broker-dealers, custodians, and investment managers be completed on trade date (T+0) prior to CSD/CCP cutoff; exceeds 95% completion via DTCC CTM as of 2026.",
        "def_ko": "T+1 결제주기 체제(미국 SEC Rule 15c6-2 등)에서 기관투자자·수탁은행·브로커 간 매매 배분(Allocation), 확인(Confirmation), 확약(Affirmation) 절차를 매매 당일(T+0) 마감 시한 내에 완료하는 프로세스이다. 2026년 현재 미국 DTCC CTM 기준 95% 이상의 당일 확약률을 기록하며 한국·유럽 T+1 전환의 핵심 선결 인프라로 꼽힌다.",
        "krx_note": "미국 SEC Rule 15c6-2 의무화; 한국 T+1 전환 로드맵의 핵심 외국인·기관 과제",
    }

    unified["Regulation"]["active account requirement"] = {
        "term_en": "Active Account Requirement",
        "abbr": "AAR",
        "term_ko_en_col": "Active Account Requirement (AAR)",
        "term_ko": "활성계좌 의무 (AAR)",
        "def_en": "A key provision of EU EMIR 3.0 (entered into force December 2024) requiring EU financial and non-financial counterparties subject to the clearing obligation to hold an active, operational clearing account at an EU-authorized CCP and clear a representative number of trades in systemically important euro- and Polish zloty-denominated interest rate derivatives through it, reducing reliance on third-country Tier 2 CCPs (such as LCH Ltd).",
        "def_ko": "2024년 12월 발효된 EU EMIR 3.0의 핵심 조항으로, 청산의무 대상인 EU 금융·비금융 거래상대방에게 EU 역내 인가 CCP(예: Eurex Clearing)에 실제 작동하는 활성 청산계좌를 보유하고 시스템적으로 중요한 유로화·폴란드 즈워티화 금리파생상품의 일정 대표 물량을 의무 청산하도록 요구하는 규제이다. 영국 CCP(LCH Ltd 등)에 대한 역외 청산 의존도를 축소하기 위해 도입되었다.",
        "krx_note": "EU EMIR 3.0 핵심 조항 (2024년 12월 발효); EU 역내 CCP 활성계좌 의무화",
    }

    return unified

def write_markdown_and_db(unified):
    en_lines = [
        "# English Glossary — Global Exchange Research",
        "",
        "> Terms are added as they are encountered during research. Keep alphabetically sorted within each category.",
        "",
        "---",
    ]
    ko_lines = [
        "# 한영 대역 용어집 — 글로벌 거래소 조사",
        "",
        "> 조사 중 새 용어가 발견될 때마다 추가. 카테고리별 영문 기준 알파벳순 정렬.",
        "",
        "---",
    ]

    db_rows = []

    for en_c, ko_c in CATEGORIES:
        en_lines.append("")
        en_lines.append(f"## {en_c}")
        en_lines.append("")
        en_lines.append("| Term | Abbreviation | Definition |")
        en_lines.append("|------|-------------|-----------|")

        ko_lines.append("")
        ko_lines.append(f"## {ko_c}")
        ko_lines.append("")
        ko_lines.append("| English | Korean | 정의 (Definition) | KRX 참고사항 |")
        ko_lines.append("|---------|--------|-------------------|-------------|")

        sorted_items = sorted(unified[en_c].values(), key=sort_key)
        for item in sorted_items:
            t_en = item["term_en"]
            abbr = item["abbr"]
            t_ko_en = item["term_ko_en_col"]
            t_ko = item["term_ko"]
            d_en = item["def_en"]
            d_ko = item["def_ko"]
            note = item["krx_note"]

            en_lines.append(f"| {t_en} | {abbr} | {d_en} |")
            ko_lines.append(f"| {t_ko_en} | {t_ko} | {d_ko} | {note} |")

            db_rows.append((t_en, abbr, t_ko, en_c, ko_c, d_en, d_ko, note))

    EN_MD_PATH.write_text("\n".join(en_lines) + "\n", encoding="utf-8")
    KO_MD_PATH.write_text("\n".join(ko_lines) + "\n", encoding="utf-8")
    print(f"Wrote {EN_MD_PATH} ({len(db_rows)} terms)")
    print(f"Wrote {KO_MD_PATH} ({len(db_rows)} terms)")

    # Rebuild SQLite DB cleanly
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("DROP TABLE IF EXISTS terms_fts")
    cur.execute("DROP TABLE IF EXISTS terms")

    cur.execute("""
    CREATE TABLE terms (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        english_term TEXT NOT NULL,
        abbreviation TEXT,
        korean_term TEXT,
        category_en TEXT NOT NULL,
        category_ko TEXT NOT NULL,
        definition_en TEXT,
        definition_ko TEXT,
        krx_note TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)

    cur.executemany("""
    INSERT INTO terms (
        english_term, abbreviation, korean_term,
        category_en, category_ko, definition_en, definition_ko, krx_note
    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """, db_rows)

    cur.execute("""
    CREATE VIRTUAL TABLE terms_fts USING fts5(
        english_term, korean_term, abbreviation, definition_en, definition_ko, krx_note,
        content='terms',
        content_rowid='id'
    )
    """)
    cur.execute("INSERT INTO terms_fts(terms_fts) VALUES('rebuild')")

    conn.commit()
    conn.close()
    print(f"Rebuilt {DB_PATH} with {len(db_rows)} rows and FTS5 index.")

if __name__ == "__main__":
    unified = build_unified_glossary()
    write_markdown_and_db(unified)
