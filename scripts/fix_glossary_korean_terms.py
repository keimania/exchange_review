#!/usr/bin/env python3
"""
scripts/fix_glossary_korean_terms.py
Replaces romanized/phonetic Korean terms and crude brackets with official English & Korean financial terminology.
Updates:
- qmd/reference/glossary_ko.qmd
- qmd/reference/glossary_en.qmd
- md/_common/glossary_ko.md
- md/_common/glossary_en.md
- md/_common/glossary.db
"""

import os
import re
import sqlite3
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent

# Precise replacements for table rows:
# pattern: (search_term_in_first_col, new_english_term, new_korean_term_or_abbr)
REPLACEMENTS_KO = [
    (
        "Dongsi Hoga (동시호가)",
        "Call Auction (Simultaneous Order Matching)",
        "동시호가 (단일가매매, Call Auction)",
        "KRX의 단일가매매(Call Auction) 메커니즘으로, 시가·종가 및 변동성완화장치(VI) 발동 후 가격 결정에 사용된다. 일정 시간 동안 접수된 모든 호가를 동시 접수로 간주하여 단일 균형가격으로 일괄 체결한다 (전통적 명칭: 동시호가).",
        "KRX 시가·종가 결정 메커니즘 (Call Auction)"
    ),
    (
        "Jeopsokmaemae (접속매매)",
        "Continuous Trading (Price-Time Priority)",
        "접속매매 (연속매매, Continuous Trading)",
        "KRX의 정규 거래시간 중 개시 및 종가 단일가매매 사이에 가격-시간 우선원칙에 따라 주문을 연속적으로 체결하는 매매 방식이다 (전통적 명칭: 접속매매).",
        "KRX 정규시장 연속매매 방식"
    ),
    (
        "SAPI (시장전체 매매거래중단)",
        "Market-Wide Circuit Breaker (KRX)",
        "시장전체 매매거래중단 (서킷브레이커, MWCB)",
        "KRX의 시장전체 서킷브레이커 메커니즘으로, KOSPI 지수 하락률 -8%(1단계, 20분 거래중단), -15%(2단계, 20분 거래중단), -20%(3단계, 당일 매매 종료) 시 발동된다. 각 단계는 1분간 지속 확인 후 발동한다.",
        "KRX: KOSPI -8%/-15%/-20% 3단계 서킷브레이커"
    ),
    (
        "Conditional Limit Order (조건부지정가호가)",
        "Conditional Limit Order",
        "조건부지정가호가",
        None,
        None
    ),
    (
        "Sidecar (프로그램매매호가 효력정지)",
        "Sidecar (Program Trading Suspension)",
        "사이드카 (프로그램매매호가 효력정지)",
        None,
        None
    ),
    (
        "Volatility Interruption (변동성완화장치, VI) — KRX",
        "Volatility Interruption (VI) — KRX",
        "변동성완화장치 (VI, Volatility Interruption)",
        None,
        None
    ),
    (
        "KRX Night Session (야간거래)",
        "KRX Night Trading Session",
        "KRX 야간거래 (Night Trading Session)",
        None,
        None
    ),
    (
        "Sidecar (사이드카)",
        "Sidecar (Derivatives Circuit Breaker)",
        "사이드카 (파생상품 서킷브레이커)",
        None,
        None
    ),
    (
        "Joint Compensation Fund (손해배상공동기금)",
        "Joint Compensation Fund",
        "손해배상공동기금 (Joint Compensation Fund)",
        None,
        None
    ),
    (
        "Settlement Facilitation Deposit (결제촉진담보금)",
        "Settlement Facilitation Deposit",
        "결제촉진담보금 (Settlement Facilitation Deposit)",
        None,
        None
    ),
    (
        "Split Settlement (분할결제)",
        "Split Settlement",
        "분할결제 (Split Settlement)",
        None,
        None
    ),
    (
        "Electronic Securities Act (전자증권법)",
        "Electronic Securities Act",
        "전자증권법 (주식·사채 등의 전자등록에 관한 법률)",
        None,
        None
    ),
    (
        "Financial Investment Services and Capital Markets Act (자본시장법)",
        "Financial Investment Services and Capital Markets Act (FSCMA)",
        "자본시장과 금융투자업에 관한 법률 (자본시장법, FSCMA)",
        None,
        None
    ),
]

REPLACEMENTS_EN = [
    (
        "Dongsi Hoga (동시호가)",
        "Call Auction (Simultaneous Order Matching)",
        "",
        "KRX's single-price call auction mechanism (traditionally referred to as Simultaneous Bids and Offers or 'Dongsi Hoga') used for opening price, closing price, and VI-triggered auction price determination; all orders accumulated during the period are treated as arriving simultaneously and matched at a single equilibrium price."
    ),
    (
        "Jeopsokmaemae (접속매매)",
        "Continuous Trading (Price-Time Priority)",
        "",
        "KRX's continuous trading method (traditionally termed 'Jeopsokmaemae') using price-time priority matching between opening and closing call auctions; standard continuous order book matching."
    ),
    (
        "SAPI (시장전체 매매거래중단)",
        "Market-Wide Circuit Breaker (KRX)",
        "MWCB",
        "KRX's market-wide circuit breaker mechanism; triggers at KOSPI decline of -8% (Level 1, 20-min halt), -15% (Level 2, 20-min halt), and -20% (Level 3, trading terminated for the day); each level requires a 1-minute sustained duration confirmation before activation."
    ),
    (
        "Conditional Limit Order (조건부지정가호가)",
        "Conditional Limit Order",
        "",
        None
    ),
    (
        "Sidecar (프로그램매매호가 효력정지)",
        "Sidecar (Program Trading Suspension)",
        "",
        None
    ),
    (
        "Volatility Interruption (변동성완화장치, VI)",
        "Volatility Interruption (VI) — KRX",
        "VI",
        None
    ),
    (
        "KRX Night Session (야간거래)",
        "KRX Night Trading Session",
        "",
        None
    ),
    (
        "Sidecar (사이드카)",
        "Sidecar (Derivatives Circuit Breaker)",
        "",
        None
    ),
    (
        "Joint Compensation Fund (손해배상공동기금)",
        "Joint Compensation Fund",
        "",
        None
    ),
    (
        "Settlement Facilitation Deposit (결제촉진담보금)",
        "Settlement Facilitation Deposit",
        "",
        None
    ),
    (
        "Split Settlement (분할결제)",
        "Split Settlement",
        "",
        None
    ),
    (
        "Electronic Securities Act (전자증권법)",
        "Electronic Securities Act",
        "",
        None
    ),
    (
        "Financial Investment Services and Capital Markets Act (자본시장법)",
        "Financial Investment Services and Capital Markets Act (FSCMA)",
        "FSCMA",
        None
    ),
    (
        "KSD (Korea Securities Depository, 한국예탁결제원)",
        "Korea Securities Depository (KSD)",
        "KSD",
        None
    ),
]

def update_markdown_file(file_path: Path, is_korean_file: bool):
    lines = file_path.read_text(encoding="utf-8").splitlines()
    new_lines = []
    replacements = REPLACEMENTS_KO if is_korean_file else REPLACEMENTS_EN

    for line in lines:
        if not line.startswith("|") or line.startswith("|---") or line.startswith("| English") or line.startswith("| Term"):
            new_lines.append(line)
            continue

        parts = [p.strip() for p in line.split("|")]
        # parts format: ['', term, col2, col3, col4, ''] (length >= 4)
        if len(parts) < 4:
            new_lines.append(line)
            continue

        term = parts[1]
        matched = False
        for rep in replacements:
            old_term = rep[0]
            if term == old_term:
                matched = True
                new_term = rep[1]
                parts[1] = f" {new_term} "
                
                new_col2 = rep[2]
                if new_col2:
                    parts[2] = f" {new_col2} "

                if len(rep) > 3 and rep[3] is not None and len(parts) >= 4:
                    parts[3] = f" {rep[3]} "
                if len(rep) > 4 and rep[4] is not None and len(parts) >= 5:
                    parts[4] = f" {rep[4]} "

                new_line = "|".join(parts)
                new_lines.append(new_line)
                break

        if not matched:
            new_lines.append(line)

    file_path.write_text("\n".join(new_lines) + "\n", encoding="utf-8")
    print(f"Updated {file_path}")

def update_sqlite_db(db_path: Path):
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()

    db_updates = [
        # (id or old_name, new_eng, new_abbr, new_ko, new_def_en, new_def_ko, new_note)
        (
            381,
            "Call Auction (Simultaneous Order Matching)",
            "",
            "동시호가 (단일가매매, Call Auction)",
            "KRX's single-price call auction mechanism (traditionally referred to as Simultaneous Bids and Offers or 'Dongsi Hoga') used for opening price, closing price, and VI-triggered auction price determination; all orders accumulated during the period are treated as arriving simultaneously and matched at a single equilibrium price.",
            "KRX의 단일가매매(Call Auction) 메커니즘으로, 시가·종가 및 변동성완화장치(VI) 발동 후 가격 결정에 사용된다. 일정 시간 동안 접수된 모든 호가를 동시 접수로 간주하여 단일 균형가격으로 일괄 체결한다 (전통적 명칭: 동시호가).",
            "KRX 시가·종가 결정 메커니즘 (Call Auction)"
        ),
        (
            382,
            "Continuous Trading (Price-Time Priority)",
            "",
            "접속매매 (연속매매, Continuous Trading)",
            "KRX's continuous trading method (traditionally termed 'Jeopsokmaemae') using price-time priority matching between opening and closing call auctions; standard continuous order book matching.",
            "KRX의 정규 거래시간 중 개시 및 종가 단일가매매 사이에 가격-시간 우선원칙에 따라 주문을 연속적으로 체결하는 매매 방식이다 (전통적 명칭: 접속매매).",
            "KRX 정규시장 연속매매 방식"
        ),
        (
            383,
            "Market-Wide Circuit Breaker (KRX)",
            "MWCB",
            "시장전체 매매거래중단 (서킷브레이커, MWCB)",
            "KRX's market-wide circuit breaker mechanism; triggers at KOSPI decline of -8% (Level 1, 20-min halt), -15% (Level 2, 20-min halt), and -20% (Level 3, trading terminated for the day); each level requires a 1-minute sustained duration confirmation before activation.",
            "KRX의 시장전체 서킷브레이커 메커니즘으로, KOSPI 지수 하락률 -8%(1단계, 20분 거래중단), -15%(2단계, 20분 거래중단), -20%(3단계, 당일 매매 종료) 시 발동된다. 각 단계는 1분간 지속 확인 후 발동한다.",
            "KRX: KOSPI -8%/-15%/-20% 3단계 서킷브레이커"
        ),
        (
            384,
            "Sidecar (Program Trading Suspension)",
            "Sidecar",
            "사이드카 (프로그램매매호가 효력정지)",
            "KRX mechanism that suspends program trading orders for 5 minutes when KOSPI 200 front-month futures price moves +/-5% from base price for 1 minute; applied once per day, not after 14:50 KST.",
            "KOSPI 200 근월물 선물 가격이 기준가 대비 ±5% 변동 상태가 1분간 지속될 경우 프로그램매매 호가를 5분간 정지하는 KRX의 메커니즘이다. 하루 1회에 한해 적용되며 14:50 이후에는 발동하지 않는다.",
            "KRX: KOSPI 200 선물 ±5% 1분 지속 시 발동; 1일 1회 한정"
        ),
        (
            385,
            "Volatility Interruption (VI) — KRX",
            "VI",
            "변동성완화장치 (VI, Volatility Interruption)",
            "KRX's per-stock dynamic circuit breaker mechanism consisting of Static VI (triggers at 3% for KOSPI 200 constituents, 6% for others from last call auction price) and Dynamic VI (triggers at 10% from last trade price); activates a 2-minute cooling-off call auction with random 30-second close.",
            "KRX의 개별종목 서킷브레이커로, 정적VI(직전 단일가매매 가격 대비 일정 비율 이탈 시 발동)와 동적VI(직전 체결가 대비 일정 비율 이탈 시 발동)로 구성된다. 발동 시 2분간의 냉각 단일가매매 후 매매를 재개한다.",
            "KRX: 정적VI(3%/6%), 동적VI(±3%)"
        ),
        (
            387,
            "KRX Night Trading Session",
            "",
            "KRX 야간거래 (Night Trading Session)",
            "KRX's independently operated after-hours derivatives trading session (18:00-06:00 KST), launched June 9, 2025, replacing the previous Eurex-linked arrangement; covers 10 products including KOSPI 200 futures/options, Mini products, KOSDAQ 150, USD futures, and KTB futures.",
            "KRX가 독자적으로 운영하는 시간외 파생상품 거래 세션(18:00~06:00 KST)으로, 2025년 6월 9일 Eurex 연계 방식을 대체하여 출시되었다. KOSPI 200 선물/옵션, 미니 상품, KOSDAQ 150, USD 선물, KTB 선물 등 10개 상품을 커버한다.",
            "2025년 6월 9일 출시; 10개 상품"
        )
    ]

    for item in db_updates:
        tid, eng, abbr, ko, def_en, def_ko, note = item
        cur.execute("""
            UPDATE terms 
            SET english_term = ?, abbreviation = ?, korean_term = ?, definition_en = ?, definition_ko = ?, krx_note = ?
            WHERE id = ?
        """, (eng, abbr, ko, def_en, def_ko, note, tid))

    conn.commit()
    conn.close()
    print(f"Updated SQLite DB at {db_path}")

def main():
    update_markdown_file(ROOT_DIR / "qmd/reference/glossary_ko.qmd", is_korean_file=True)
    update_markdown_file(ROOT_DIR / "qmd/reference/glossary_en.qmd", is_korean_file=False)
    update_markdown_file(ROOT_DIR / "md/_common/glossary_ko.md", is_korean_file=True)
    update_markdown_file(ROOT_DIR / "md/_common/glossary_en.md", is_korean_file=False)
    update_sqlite_db(ROOT_DIR / "md/_common/glossary.db")
    print("All glossary files successfully updated!")

if __name__ == '__main__':
    main()
