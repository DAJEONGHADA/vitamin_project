# 비타민 제품 리뷰 분석을 통한 비타민 제품 추천


## [프로젝트 소개]
건강기능 식품은 2019년부터 2023년까지 연평균 5.9% 정보 시장규모가 커지는 중이며, 건강 관리와 에너지 회복을 돕는 새로운 고함량 비타민 제품의 인기가 급상승하고 있습니다. 

그 중 성장과 발달에 필요한 영양소가 더 많이 필요하기 때문에 다른 사람들보다 더 많은 비타민을 섭취해야 하는 특정 타겟층인 ‘임산부’와 ‘아이’를 대상으로 하는 상위 20위에 속하는 비타민 제품의 리뷰의 키워드 분석을 통해 특성과 성분 정보에 집중되는 경향이 있는지 파악한 후, 제품을 추천을 하는 목적으로 프로젝트를 진행하였습니다.

과다 섭취 또는 특정 성분에 대한 민감성으로 인해 이러한 현상이 발생할 수 있음을 발견하고, 상위 20위 제품 중 소비자에게 적합한 구성을 가진 제품을 선정하여 추천을 할 수 있으며 따라서 자신의 필요에 맞는 제품을 선택할 수 있도록 지원 가능합니다. 

### ⏳ 진행기간
- 2024.08.13. ~ 2024. 08.20. (8일)
### 🧑‍🤝‍🧑 역할
- 비타민 제품 네이버 리뷰 데이터 수집 및 전처리, 키워드 분석, tf-idf 분석
### 🧾 데이터 수집
- 상위 20위 판매 사이트 비타민 제품 리뷰 데이터 
### 📊 분석결과
- 임산부와 아이가 자주 섭취하는 비타민 제품 중 일부에서 냄새가 강하고, 설사, 비린 맛, 알레르기 반응 등의 부작용이 나타나는 사례가 확인되었음. 이러한 부작용과 관련된 주요 성분을 분석한 결과, 실제 제품에 동일한 성분이 포함되어 있으며, 과다 섭취 또는 특정 성분에 대한 민감성으로 인해 이러한 현상이 발생할 수 있음을 발견함. 이에 따라 상위 20위 제품 중 소비자에게 적합한 성분 구성을 가진 제품을 선정하여 추천할 수 있음.

### 🖥️ 코드
0. user.dic : 사용자 사전
1. vitamin_review_web_crawing.py : 비타민 제품 리뷰 웹크롤링
2. vitamin_review_tokenize.ipynb : 비타민 제품 리뷰 토근화
3. vitamin_review_wordcloud.ipynb : 비타민 제품 리뷰 워드클라우드
4. vitamin_review_tfidf.ipynb : 비타민 제품 리뷰 tf-idf
