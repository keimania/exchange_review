# CDS Clearing and Depository Services (CDS)

> **최종 업데이트:** 2026-04-07
> **조사 등급:** Tier 3
> **유형:** CCP (중앙청산소) / CSD (중앙예탁기관)

---

## 1. 개요 및 프로필 (Overview & Profile)

| 항목 | 내용 |
|------|------|
| 정식 명칭 | CDS Clearing and Depository Services Inc. |
| 약칭 | CDS |
| 웹사이트 | [https://www.cds.ca](https://www.cds.ca) |
| 설립연도 | 1970년 (1970년 6월 9일 법인 설립) |
| 국가 / 도시 | 캐나다 / 토론토 |
| 소유 구조 | The Canadian Depository for Securities Limited의 완전자회사 |
| 모회사 / 그룹 | TMX Group Inc. (2012년 Maple 거래 이후) |
| 감독기관 | Bank of Canada (캐나다 은행, 시스템적으로 중요한 결제시스템 감독 지정), Ontario Securities Commission (OSC), Autorite des marches financiers (AMF, 퀘벡), British Columbia Securities Commission |
| CPMI-IOSCO PFMI 준수 | 예 -- PFMI 자체평가 및 정성적 공시 발행 [Source: CDS PFMI Disclosure, cds.ca/resource/en/247] |
| QCCP 지위 | 해당 없음 -- CDS는 CNS 서비스(주식 차감)에 한해서만 CCP 기능 수행; 파생상품 CCP가 아님 |

### 주요 연혁 (Key Historical Milestones)

| 연도 | 사건 |
|------|------|
| 1970 | 증가하는 후선업무(back-office) 비용과 매매량에 대응하기 위해 Canadian Depository for Securities Limited 설립 [Source: [Wikipedia](https://en.wikipedia.org/wiki/Canadian_Depository_for_Securities)] |
| 1970-80년대 | 캐나다 주식 및 채권 시장에 대한 예탁 및 청산 서비스 점진적 확대 |
| 1996 | CDSX 프로젝트 착수 -- 통합 청산·결제 시스템 구축 |
| 2003 | **CDSX 가동** -- 레거시 시스템을 대체하는 통합 청산·결제·예탁 플랫폼 [Source: [CDS About](https://www.cds.ca/about/cds)] |
| 2012 | Maple Group 거래의 일환으로 TMX Group이 CDS를 인수, TMX 완전자회사로 편입 [Source: [Wikipedia](https://en.wikipedia.org/wiki/Canadian_Depository_for_Securities)] |
| 2014 | Bank of Canada에 의해 지급청산결제법(PCSA)에 따른 시스템적으로 중요한 FMI로 지정 |
| 2017 | CNS (Continuous Net Settlement) 서비스 개시 -- CCP 기능을 갖춘 주식 거래 차감 [Source: [OSC CDS Rule Review](https://www.osc.ca/en/industry/market-regulation/clearing-agencies-and-clearing-houses/recognized-clearing-agencies/cds-rule-review)] |
| 2024 (5월 27일) | **T+1 결제** 시행 -- 캐나다가 미국(5월 28일)보다 하루 앞서 T+1로 전환 [Source: [CDS T+1](https://www.cds.ca/solutions/cds-key-initiatives/t-1)] |
| 2025+ | **거래후처리 현대화(PTM, Post-Trade Modernization)** 추진 중 -- 기술 플랫폼 전면 교체 [Source: [Markets Media](https://www.marketsmedia.com/post-trade-modernization-a-game-changer-for-canada/)] |

> **KRX/KSD 비교:** CDS는 CSD와 CCP 기능을 단일 기관에 결합하고 있으며, 이는 KSD(한국예탁결제원)가 CSD, KRX가 거래소 상장 상품의 CCP 역할을 각각 수행하는 한국 모델과 유사하다. 캐나다에서 CDS의 CCP 기능은 주식 대상 CNS 서비스에 한정되는 반면, 한국은 KRX(CCP)와 KSD(CSD/결제) 간에 보다 명확한 기능 분리가 이루어져 있다.

---

## 2. 청산 모델 (Clearing Model)

### 2.1 CCP 서비스 (CCP Services)

CDS는 세 가지 별개의 금융시장인프라 기능을 운영한다 [Source: [CDS About](https://www.cds.ca/about/cds)]:

| 기능 | 설명 |
|------|------|
| **중앙예탁기관 (CSD)** | 약 4조 CAD 규모의 예탁증권 보관; 예탁적격 국내 및 국제 증권의 기록 관리 |
| **증권결제시스템 (SSS)** | CDSX를 통한 거래소 거래 및 장외(OTC) 주식, 채권, 단기금융시장 거래의 DVP 결제 |
| **중앙청산소 (CCP)** | 적격 거래소 거래 주식에 대한 CNS (Continuous Net Settlement) 서비스; 채무인수(novation)를 통해 CDS가 거래상대방으로 개입 |

| 상품군 | CCP 청산 (CNS) | 결제 (CDSX) |
|--------|---------------|-------------|
| 주식 | 예 (CNS 차감 및 채무인수) | 예 |
| 국채 | CCP 서비스 없음 | 예 |
| 회사채 | CCP 서비스 없음 | 예 |
| 단기금융시장 | CCP 서비스 없음 | 예 |
| OTC 상품 | CCP 서비스 없음 | 예 (건별결제) |

> **참고:** 캐나다의 상장파생상품 청산은 또 다른 TMX Group 자회사인 Canadian Derivatives Clearing Corporation (CDCC)이 CCP 서비스를 제공한다. CDS는 결제 인프라만 처리한다.

### 2.3 차감 (Netting)

- **CNS 서비스:** 적격 거래소 거래 주식에 대한 채무인수 방식의 다자간차감
- CDS는 지속적 차감 및 채무인수 절차를 통해 각 거래의 양측에 대한 거래상대방으로 자신을 대체 [Source: [CDS PFMI Disclosure](https://www.cds.ca/resource/en/247)]
- 차감은 다자간 기준으로 이루어져 결제 의무의 건수와 금액을 줄임
- 비CNS 거래는 CDSX 내에서 건별(Gross) 기준으로 결제

> **KRX/KSD 비교:** KRX의 주식 차감도 유사한 다자간차감 기반으로 운영된다. 다만 KRX는 CCP로서 모든 거래소 상장 상품에 대해 차감을 수행하는 반면, CDS의 CNS CCP 기능은 주식에 한정된다. 또한 한국은 주식에 T+2 결제주기(2026년 기준)를 적용하는 반면, 캐나다는 2024년 5월 T+1로 전환하였다.

### 2.4 청산 회원 자격 (Clearing Membership)

CDS는 CDSX에서 두 가지 주요 참가자 유형을 운영한다 [Source: [BIS Red Book - Canada](https://www.bis.org/cpmi/publ/d97_ca.pdf)]:

| 참가자 유형 | 역할 | 설명 |
|------------|------|------|
| **여신제공자 (Extender of Credit)** | 결제은행 / 주요 딜러 | 수신자에게 여신한도 제공; 자사 및 수신자의 일중 지급의무를 담보화; 통상 대형 은행 |
| **여신수혜자 (Receiver of Credit)** | 브로커-딜러 / 기관 | 일중 증권 매입을 위해 여신제공자로부터 일중 여신한도 수혜 |

추가 참가자 역할로 결제대리인(Settlement Agents), TA 참가자(Transfer Agent), ATON 참가자, ACT 참가자가 있다.

- 처리량: 일일 **210만 건 이상**의 거래소 거래 [Source: [CDS About](https://www.cds.ca/about/cds)]
- 크로스보더: 연간 **4,100만 건 이상**의 미국과의 크로스보더 거래

---

## 3. 리스크 관리 (Risk Management)

### 3.1 증거금 체계 (Margin Framework)

| 구성요소 | 설명 |
|----------|------|
| **개시증거금 (CNS)** | 불이행 시 잠재적 손실을 보전하기 위해 CNS 참가자에게 요구되는 담보; CNS Participant Fund 출연으로 징수 |
| **변동증거금** | 미결제 CNS 포지션에 대한 시가평가 조정 |
| **일중 증거금 추가 징수** | CDS는 PFMI 원칙 6에 따라 정기 및 비정기 일중 증거금 추가 징수 능력 보유 [Source: [OSC Notice](https://www.osc.ca/en/industry/market-regulation/clearing-agencies-and-clearing-houses/recognized-clearing-agencies/cds-rule-review/notice-material-rule-submission-2)] |
| **주식 헤어컷** | 담보로 제공된 증권에 적용 |

- Bank of Canada는 PTM 추진의 일환으로 CDS가 CNS 증거금 및 주식 헤어컷 모델 설계를 은행 기준에 부합시켜야 한다고 지적 [Source: [Bank of Canada 2024 Oversight Report](https://www.bankofcanada.ca/2025/05/release-2024-bank-canada-fmi-oversight-activities-annual-report/)]

### 3.3 손실부담순서 (Default Waterfall)

CNS 서비스는 정의된 손실부담순서를 보유한다 [Source: [CDS PFMI Disclosure](https://www.cds.ca/resource/en/247); [OSC CDS Procedures](https://www.osc.ca/sites/default/files/2022-01/cds_20141120_sn-rfc-procedures-cns-participant-default-fund.pdf)]:

| 순위 | 설명 |
|------|------|
| 1 | **불이행 참가자의 CNS Participant Fund 담보** (개시증거금) |
| 2 | **불이행 참가자의 CNS 공동기금(Default Fund) 출연분** |
| 3 | **CDS 자기자본** (CCP 자기자본 출연분) [unverified -- 정확한 규모 공개자료 미확인] |
| 4 | **생존 CNS 참가자의 공동기금 출연분** -- 잔여 손실을 생존 회원에게 비례 배분 |
| 5 | **추가분담금 부과 권한** -- CDS가 생존 참가자에게 추가 출연을 요청할 수 있음 [unverified] |

### 3.6 회복 및 정리 (Recovery & Resolution)

- **정리당국:** Bank of Canada가 지급청산결제법(PCSA)에 따라 시스템적으로 중요한 FMI로 지정된 CDS를 감독
- CDS는 Bank of Canada의 지정 FMI 리스크 관리 기준 준수 의무 [Source: [Bank of Canada](https://www.bankofcanada.ca/core-functions/financial-system/bank-canada-risk-management-standards-systemic-fmis/)]
- Bank of Canada는 2024년 CDS에 대해 지배구조, 비사이버 운영 리스크, 신용 리스크를 평가하는 핵심보증검토(core assurance reviews) 실시 [Source: [Bank of Canada 2024 Report](https://www.bankofcanada.ca/2025/05/release-2024-bank-canada-fmi-oversight-activities-annual-report/)]
- 회복 수단에는 생존 회원에 대한 손실 배분(비례 배분), 추가분담금 부과 권한, 잠재적 서비스 종료 포함 [unverified -- 구체적 회복 수단 완전히 확인되지 않음]

---

## 4. 결제 (Settlement)

### 4.1 결제주기 (Settlement Cycle)

| 상품 | 결제주기 | 비고 |
|------|---------|------|
| 주식 | **T+1** (2024년 5월 27일 이후) | 기존 T+2; 미국(2024년 5월 28일)보다 하루 앞서 T+1로 전환 |
| 국채 | T+1 | 주식 결제주기 변경에 맞추어 조정 |
| 회사채 | T+1 | 주식 결제주기 변경에 맞추어 조정 |
| 단기금융시장 | T+0~T+1 | 상품별 상이 |

**T+1 전환 결과:** T+1 시행 후 첫 주간 일일 결제실패율은 2% 미만을 유지하였으며, 주간 평균은 약 1%로 T+2 수준과 유사하였다. 기관 거래처리는 T+1 오전 3:59까지 90% 확인 목표를 향해 개선되는 추세를 보였다. [Source: [CDS T+1 Page](https://www.cds.ca/solutions/cds-key-initiatives/t-1); [CIBC Mellon](https://www.cibcmellon.com/en/newsroom/publications/straight-talk/2024/2024-05/st20240528-canada-implements-t+1-trading.jsp)]

> **KRX/KSD 비교:** 한국은 현재 주식에 T+2를 적용 중이다. 캐나다의 T+1 전환(미국과 공조)은 다수 시장보다 앞서 있다. 한국은 T+1 타당성을 검토 중이나 2026년 현재 전환 일정을 확정하지 않았다.

### 4.2 DVP 모델 (DVP Model)

- **BIS DVP Model 3** -- CDSX는 일중 증권이전에 대해 건별(item-by-item) 결제를 수행하고, 대응하는 지급의무는 지속적으로 차감 [Source: [BIS Red Book - Canada](https://www.bis.org/cpmi/publ/d97_ca.pdf)]
- 거래가 리스크 통제 검증을 통과하면, 거래상대방의 CDSX 계좌 기입을 통해 DVP 기준으로 결제
- 일말 CDS와 참가자 간의 순지급의무는 지정 은행을 통해 결제되며, 최종 지급은 **Lynx** (Payments Canada가 운영하는 캐나다 대액결제시스템)를 통해 **Bank of Canada** CDS 결제계좌로 이루어짐 [Source: [CDS Settlement Page](https://www.cds.ca/participants/settlement-and-clearing)]

> **KRX/KSD 비교:** KSD도 한국은행(BOK-Wire+)을 통해 결제하는 DVP 모델을 사용한다. 최종결제에 중앙은행화폐를 사용한다는 원칙은 동일하나, 구체적 DVP 모델 유형은 상이하다.

---

## 5. 기술 및 인프라 (Technology & Infrastructure)

| 항목 | 내용 |
|------|------|
| **시스템명** | **CDSX** (2003년 가동) |
| **아키텍처** | 통합 청산·결제·예탁 플랫폼 |
| **처리 용량** | 일일 210만 건 이상 거래소 거래; 연간 약 3억 7,400만 건 국내 증권 거래 |
| **주요 인터페이스** | Lynx (LVTS 후속), DTC (미국), Euroclear France, Japan Securities Depository Centre, SEB (Skandinaviska Enskilda Banken) |
| **현대화** | **거래후처리 현대화(PTM)** 추진 중 -- 2025년 이후 기술 플랫폼 전면 교체 계획 [Source: [Markets Media](https://www.marketsmedia.com/post-trade-modernization-a-game-changer-for-canada/)] |

- CDS는 DTC (미국)와 수탁 관계를 유지하여 연간 4,100만 건 이상의 크로스보더 결제를 지원
- CDSX는 영업일 중 지속적 결제를 통한 실시간 처리 제공

---

## 6. 규제 체계 (Regulatory Framework)

### 6.1 감독기관 (Supervising Authority)

| 규제기관 | 역할 |
|----------|------|
| **Bank of Canada** | 주요 감독 -- 지급청산결제법(PCSA)에 따라 시스템적으로 중요한 FMI로 지정 |
| **Ontario Securities Commission (OSC)** | 증권규제기관 인정 -- CDS를 청산기관으로 인정 |
| **Autorite des marches financiers (AMF)** | 퀘벡 증권규제기관 인정 |
| **British Columbia Securities Commission** | BC 증권규제기관 인정 |

### 6.2 주요 규정 (Key Regulations)

- **지급청산결제법 (PCSA, Payment Clearing and Settlement Act):** 연방 법률; Bank of Canada에 의해 CDS가 시스템적으로 중요한 FMI로 지정 [Source: [Bank of Canada](https://www.bankofcanada.ca/core-functions/financial-system/clearing-and-settlement-systems/)]
- **주(州) 증권법:** CDS는 온타리오, 퀘벡, 브리티시 컬럼비아 증권법에 따라 청산기관으로 인정
- **Bank of Canada 지정 FMI 리스크 관리 기준:** CDS는 CPMI-IOSCO PFMI 원칙을 반영한 이 기준을 준수해야 함 [Source: [Bank of Canada Standards](https://www.bankofcanada.ca/core-functions/financial-system/bank-canada-risk-management-standards-systemic-fmis/)]

### 6.3 PFMI 준수 (PFMI Compliance)

- CDS는 CPMI-IOSCO PFMI 정성적 자체평가 및 정량적 공시 발행
- 최신 공시: [cds.ca](https://www.cds.ca/resource/en/247)에서 확인 가능
- Bank of Canada가 PFMI 기준에 따른 정기 감독 평가 실시

---

## 7. 상호운용성 (Interoperability)

### 7.1 크로스보더 연계 (Cross-border Linkages)

| 파트너 CSD/예탁기관 | 유형 | 상품 |
|--------------------|------|------|
| **DTC (Depository Trust Company, 미국)** | 수탁 링크 | 크로스보더 주식 및 채권 결제; 연간 4,100만 건 이상 |
| **Japan Securities Depository Centre** | 수탁 링크 | 크로스보더 결제 |
| **Euroclear France** | 수탁 링크 | 크로스보더 결제 |
| **SEB (Skandinaviska Enskilda Banken)** | 수탁 링크 | 북유럽 시장 접근 |

- CDS는 CCP 상호운용 체계를 보유하지 않음 -- CCP 기능(CNS)은 국내 전용
- 크로스보더 결제는 직접적인 CCP 링크가 아닌 수탁 관계를 통해 지원

---

## 9. 최근 동향 (Recent Developments)

### T+1 결제 (2024)
- 캐나다는 2024년 5월 27일 성공적으로 T+1로 전환, 미국보다 하루 앞섬
- 전환 후 결제실패율 2% 미만 유지
- 미국/멕시코의 T+1 전환과 공조 [Source: [CDS T+1](https://www.cds.ca/solutions/cds-key-initiatives/t-1)]

### 거래후처리 현대화(PTM) 추진 (2025+)
- CDSX 플랫폼을 현대화하는 대규모 기술 교체 프로젝트
- Bank of Canada는 PTM의 일환으로 CDS가 CNS 증거금 및 주식 헤어컷 모델을 은행 기준에 부합시킬 것을 기대
- 캐나다 자본시장의 "게임 체인저"로 평가 [Source: [Markets Media](https://www.marketsmedia.com/post-trade-modernization-a-game-changer-for-canada/)]

### Bank of Canada 2024년 감독
- Bank of Canada는 2024년 CDS에 대해 지배구조, 비사이버 운영 리스크, 신용 리스크를 대상으로 핵심보증검토 실시 [Source: [Bank of Canada 2024 Report](https://www.bankofcanada.ca/2025/05/release-2024-bank-canada-fmi-oversight-activities-annual-report/)]

### CNS 서비스 개선
- 일중 증거금 추가 징수 역량의 지속적 강화
- 정기 일중 증거금 추가 징수를 CDS 일일 업무에 추가 [Source: [OSC Notice](https://www.osc.ca/en/industry/market-regulation/clearing-agencies-and-clearing-houses/recognized-clearing-agencies/cds-rule-review/notice-material-rule-submission-2)]

---

## 출처 (Sources)

1. [CDS About Page](https://www.cds.ca/about/cds) -- 공식 개요
2. [CDS Settlement & Clearing](https://www.cds.ca/participants/settlement-and-clearing) -- 결제 서비스
3. [CDS T+1 Initiative](https://www.cds.ca/solutions/cds-key-initiatives/t-1) -- T+1 전환 세부사항
4. [CDS PFMI Qualitative Disclosure](https://www.cds.ca/resource/en/247) -- CPMI-IOSCO 자체평가
5. [CDS PFMI Disclosure (2024)](https://www.cds.ca/resource/en/630) -- 최신 PFMI 공시
6. [Bank of Canada -- Clearing and Settlement Systems](https://www.bankofcanada.ca/core-functions/financial-system/clearing-and-settlement-systems/) -- 감독 체계
7. [Bank of Canada -- Risk-Management Standards for Designated FMIs](https://www.bankofcanada.ca/core-functions/financial-system/bank-canada-risk-management-standards-systemic-fmis/)
8. [Bank of Canada -- 2024 FMI Oversight Report](https://www.bankofcanada.ca/2025/05/release-2024-bank-canada-fmi-oversight-activities-annual-report/)
9. [OSC -- CDS Rule Review](https://www.osc.ca/en/industry/market-regulation/clearing-agencies-and-clearing-houses/recognized-clearing-agencies/cds-rule-review) -- 규제 공지
10. [OSC -- CNS Participant Default Fund Procedures](https://www.osc.ca/sites/default/files/2022-01/cds_20141120_sn-rfc-procedures-cns-participant-default-fund.pdf)
11. [BIS Red Book -- Canada (2011)](https://www.bis.org/cpmi/publ/d97_ca.pdf) -- CPSS 결제시스템 개요
12. [Wikipedia -- Canadian Depository for Securities](https://en.wikipedia.org/wiki/Canadian_Depository_for_Securities)
13. [CIBC Mellon -- T+1 Implementation](https://www.cibcmellon.com/en/newsroom/publications/straight-talk/2024/2024-05/st20240528-canada-implements-t+1-trading.jsp)
14. [Markets Media -- Post-Trade Modernization](https://www.marketsmedia.com/post-trade-modernization-a-game-changer-for-canada/)
15. [OSC -- Impact of T+1 on Failed Trades](https://www.osc.ca/en/news-events/reports-and-publications/impact-t1-settlement-failed-trades)
