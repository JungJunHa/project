# 미래에셋 빅데이터 페스티벌

## 📍 1. 소개
### 주제명 : 상대적 기업가치 및 지속가능성 평가를 통한 종목 추천 시스템
팀명 : 쿠스톡

팀원 : 정준하(팀장), 오윤진

![image](https://user-images.githubusercontent.com/71584305/140605177-adad078f-43b5-4caa-abf6-87a2984729fe.png)

### 프로젝트 요약 : 기존 미래에셋 데이터와 종목별 재무적 가치 데이터(기업의 상대 가치), 비재무적 가치 데이터(ESG 가치)를 종합하여 개인 맞춤형 종목 추천 서비스를 만들었다.

![image](https://user-images.githubusercontent.com/71584305/140605590-713b18a6-6433-4300-b767-b395deadb716.png)

## 📍 2. 데이터 분석 과정

### 외부 데이터 크롤링
- 한국 거래소: 종목별 정보 및 시가 정보 다운로드
- NAVER : 네이버 금융에서 종목별 업종 정보와 업종별 PER, 네이버 뉴스에서 ESG 관련 기사 크롤링
- FnGuide : ROE, EPS, EV/EBITDA와 같은 기업 상대 가치 지표 크롤링

### 기존 미래에셋 데이터
네이버 금융에서 종목명과 업종 정보를 크롤링하여 기존 미래에셋 데이터와 결합한 후, 관심 업종과 투자 선호 기간에 따른 분류를 진행하였다.

1. 고객별 매수 관심 업종 산출 : 고객별 매수량이 가장 높은 TOP 3 업종을 산출했으며, 매수량 TOP 3 업종과 그에 따른 매수량을 하나의 Dataframe으로 생성해 저장하였다.
2. 투자 선호 기간 분류 : 미래에셋 데이터의 'Daytrading', 'Swing', 'Buy&hold' 세 가지의 Feature의 고객별 1년간 총 평균을 구하여 K-Means Clustering을 진행하였다.

### 비재무적 가치 데이터
ESG 관련 뉴스에서 E,S,G 관련 키워드를 추출 후,  추출한 키워드 기반 E,S,G 각 섹터별 뉴스를 크롤링했다. 그 후 크롤링한 뉴스 본문 데이터에서 불용어와 특수문자를 제외한 명사를 추출하여 감성분석을 진행하였고 각 ESG 키워드 별 긍정/부정 비율 산출 및 상대적 점수화를 진행했다.

1. ESG 키워드 추출 : 'ESG'로 검색되는 최근 6개월 동안의 뉴스 제목 데이터를 크롤링한 후, 단어의 출현 빈도수와 중립성을 고려하여 E,S,G 각 섹터별 키워드를 3개씩 선정 및 추출하였다.
2. 키워드 기반 뉴스 크롤링 : 추출된 각 키워드를 이용하여 시가총액 상위 300개 종목에 대하여 키워드와 관련된 지난 6개월간의 네이버 뉴스를 크롤링하였다.
3. 단어 추출 및 감성 분석 : 긍정/부정 감정사전의 단어들과 기사에서 추출된 단어들을 불용어 처리 후 각각의 TF-IDF 벡터를 생성하였다. 이후 각 긍/부정 감정사전 벡터와 개별 벡터 기사 사이의 코사인 유사도를 계산하고 평균내어, 각 종목에 대한 특정 ESG 키워드(이슈) 기사의 긍/부정 비율을 구하였다.
4. 비재무적 가치 점수화 : 먼저 각 종목기사에 대해 ESG 키워드별로 긍/부정 비율에 기반한 점수를 계산하고 이러한 키워드별 점수의 평균 점수를 산출하였다. 마지막으로 이에 MSCI ESG 등급에 따른 가중치를 더한 후, Min-Max 정규화를 통해 종목별 최종 비재무적 가치 점수를 산출하였다.

### 재무적 가치 데이터
데이터 크롤링을 통해 네이버 금융 및 FnGuide에서 업종별 PER, ROE, EV/EBITDA, EPS 정보를 추출한 후 지표별 순위를 분석하여 이에 기반한 재무적 가치 점수를 산출하였다.

1. 기업 상대 지표 크롤링 : 네이버 금융에서 업종별 PER 정보를 크롤링, FnGuide에서 종목별 EPS, ROE, EV/EBITDA 정보를 크롤링한다.
2. 지표별 순위 산출 : ROE, EV/EBITDA, 시가/적정가격(적정가격 = 업종별 PER * EPS) 이렇게 세개의 지표에서 각각의 순위를 산출했다. ROE는 높을수록, EV/EBITDA와 시가/적정가격은 낮을수록 높은 순위를 주었다.
3. 재무적 가치 점수화 : 세개의 순위를 평균 낸 후 min-max 정규화를 거쳐 최종 재무적 가치 점수를 산출한다.

## 📍 3. 추천 시스템 개발

### 모델 구현 과정 소개

1. 점수 기반 종목 추천 : 앞서 계산한 재무적 점수와 비재무적 점수, 그리고 미래에셋 데이터에서 추출한 사용자 투자 성향과 관심 업종 정보를 조합하여 최종 순위를 산정, 개인 맞춤 종목을 추천한다.
2. 잠재요인 기반 종목 추천 : 위의 결과에서 추천된 종목에 대해 가격 변동성을 계산하여 True Label로 생성 후 잠재 요인 기반 협업 필터링을 통해 최종적으로 종목을 추천한다.

### 점수 기반 종목 추천 모델
점수 기반 모델은 앞에서 계산한 재무적 점수와 비재무적 점수,그리고 미래에셋 데이터의 사용자별 투자 선호 기간에 따른 가중치와 관심 업종에 따른 가중치 이 네가지 요소를 종합하여 최종 점수 및 순위를 도출한다.

- 투자 선호 기간별 가중치 : 비재무적 요소는 장기 투자로 갈수록 유의미해지는 경향이 있으므로 고객이 장기 투자를 선호할수록 비재무적 가치가 더 많이 반영될 수 있도록 장기, 중장기, 중기, 단기 순으로 1, 0.75, 0.5, 0.25만큼의 가중치를 비재무적 가치에 곱해줬다.
- 매수 관심 업종별 가중치 : 고객 관심 업종에 포함되는 종목의 경우 관심 업종별 가중치를 더해 주어서 고객이 이제껏 매수해온 종목이 우선적으로 추천될 수 있도록 한다.

### 잠재요인 기반 추천 모델
앞의 점수 기반 추천 시스템을 통해 추천된 종목들에 대한 가격 변동성을 계산하여 트루 라벨 데이터를 생성한 후 이를 기반으로 잠재요인 기반 협업 필터링을 수행한다. 이 과정을 통해 가격 안정성이 검증된 종목이 추천되도록 만들어 추천의 정확성을 높인다.

- 트루 라벨 데이터 생성 : 고객 투자 선호 기간별 가격 정보 수집할 기간 설정 -> 수집된 기간 내의 가격들을 모아 표준편차를 계산하여 변동성 산출 -> 추천된 종목 업종과 매수 관심 1,2,3위 업종에 포함되는 경우에 일정 값 차감

이렇게 생성한 투자 선호 기간별 트루 라벨 데이터를 이용하여, 잠재요인 기반 추천 모델인 sparse SVD를 통해 행렬 분해를 사용한 추천 시스템을 구현하였다. 
이때 변동성이 작은 종목이 안정적인 종목이라 판단하여 변동성이 작은 종목을 우선적으로 추천하였다.

## 📍 4. 모델 검증

### 검증 과정
네이버, Fnguide, investing.com에 평가된 종목들의 전문가 투자 의견 점수를 통해 투자 전망이 좋은 종목들이 추천되었는지 확인한다. 종합 전문가 투자 의견 점수는 세 금융 사이트에 평가된 전문가 점수를 평균 내었으며 추천 모델별, 선호 투자 기간별로 검증을 진행했다.

### 검증 결과
1. 점수 기반 추천 모델 검증 : 대부분 좋은 전문가 점수를 받은 종목들이 추천되었음을 확인할 수 있었으며 장기 투자로 갈수록 그래프의 형태가 개선되는 것으로 미루어 보아 정의한 비재무적 가치가 종목의 투자 전망에 유의미한 성과를 보였음을 알 수 있다.

<img width="682" alt="스크린샷 2021-11-06 오후 11 16 08" src="https://user-images.githubusercontent.com/71584305/140612839-c19c2e99-413a-49a7-a6a2-4d4b6c5857a6.png">

2. 잠재요인 기반 추천 모델 검증 : 그래프의 형태로 보아 잠재 요인 기반 추천 시스템을 추가적으로 적용하였을 때가, 점수 기반 추천 모델만을 사용했을 때보다, 높은 전문가 점수를 가지는 종목을 추천함을 알 수 있다. 
이로 미루어 보아, 잠재요인 기반 추천 시스템을 추가적으로 적용할 때 그 추천 성능이 개선된다는 사실을 알 수 있다.

<img width="680" alt="스크린샷 2021-11-06 오후 11 17 19" src="https://user-images.githubusercontent.com/71584305/140612880-ea575598-e5fd-4196-b1c4-474fb6e5b4e5.png">
