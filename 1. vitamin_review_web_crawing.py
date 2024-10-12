from playwright.sync_api import sync_playwright
import pandas as pd
import re

# URL과 제품 리스트
url_ = [
        "https://brand.naver.com/koreaeundanhc/products/5736413637?nl-au=605091073afd44e6ac0e9ddc23c1a1fd&NaPm=ct%3Dlzlx1gmg%7Cci%3D3c3af1a972908e20e9f9577136a7339ed021c429%7Ctr%3Dslsf%7Csn%3D1444796%7Chk%3Dd1d1fe11a7a9cb712615134eea2ba042dc62e1a6",
        "https://brand.naver.com/dapharm/products/5684175077?expsTrCd=001139&tr=slsl&nl-au=357c8db8d72045eb96143af6df771bc1&NaPm=ct%3Dlzlyixs0%7Cci%3D2a71f6d18122391dfad7a56f82c2999cac491e19%7Ctr%3Dslsf%7Csn%3D2792751%7Chk%3D9ccc2db301f20acb1a2981e7415aa29fac63e16b",
        "https://brand.naver.com/naturalize/products/4911134422?nl-au=5301bbb4474945e8b386430c62801ca1&NaPm=ct%3Dlzlyk1wg%7Cci%3D3f259f5e5ca7a2fbcc80c691f399586f73e77dd0%7Ctr%3Dslsf%7Csn%3D308369%7Chk%3D76960dbf3a2eeb6bc2a5727980c089db5feb063f",
        "https://brand.naver.com/centrum/products/6304004923?nl-au=1413a37feccd4df7ba6186e47ce8a386&NaPm=ct%3Dlzlykxjc%7Cci%3D87b5accae043cb4c54812e45d0237b72193470e9%7Ctr%3Dslsf%7Csn%3D339120%7Chk%3D72993a6a45c95b35ab688a4722df3970ceec2462",
        "https://brand.naver.com/nutricore/products/384509110?nl-au=bd646cb2990d44d5b0f409229caa0b98&NaPm=ct%3Dlzlyldqo%7Cci%3Df51d93c72eed0d22193ab20ba9065e07df5bd13a%7Ctr%3Dslsf%7Csn%3D358231%7Chk%3D9e4d85d8632967c591d695751b4bc1e0d39d46e5",
        "https://brand.naver.com/denps/products/6639630476?nl-au=822ed5fff021417b8ad8dd1f67d938da&NaPm=ct%3Dlzlylq34%7Cci%3D00e6dae6d2808987c552e6965da53142efb933ed%7Ctr%3Dslsf%7Csn%3D397098%7Chk%3Debeb58b612947c3249ac703dddafa3a4c80d281f",
        "https://brand.naver.com/doctorprogram/products/6679537873?nl-au=b40fb77f80d74af8a64b70afcc26b5f8&NaPm=ct%3Dlzlym048%7Cci%3D691137630ac913604df047eec21ad1fcc0694c91%7Ctr%3Dslsf%7Csn%3D558168%7Chk%3Df2257def98fd8d2e8aa68095a00994e17a0047b4",
        "https://brand.naver.com/nlmall/products/6059241830?nl-au=579c3902e0e84e029eb504db949504cd&NaPm=ct%3Dlzlymcgo%7Cci%3D2b06d1a6c65f9247d1cd94ed9eab6a146f496422%7Ctr%3Dslsf%7Csn%3D966092%7Chk%3De61688cd8d252c7fcbc0220e3d76b905d0ecb2a7",
        "https://brand.naver.com/bayerofficial/products/4450801284?nl-au=50cc603a41224a17a2ac52b4998abb1c&NaPm=ct%3Dlzlynqm8%7Cci%3D15bc71522712dc318f72ceebc366142fce8b3b00%7Ctr%3Dslsf%7Csn%3D924306%7Chk%3D911c8fa39b51b48f2a58bc6ffbd9ad25a7b9183d",
        "https://brand.naver.com/intero/products/4719609296?nl-au=631506349b7248a39ab57a3005681a40&NaPm=ct%3Dlzlyo94w%7Cci%3D83d7f1f0e7696e3e00b78006f21b2d177d51f362%7Ctr%3Dslsl%7Csn%3D456757%7Chk%3D4fa1f53b9f5e03fe7e81b4ec2a0127662cf3dd46",
        "https://brand.naver.com/bayerofficial/products/4448056751?nl-au=ba7a4cb6c70e451386b6252236976c21&NaPm=ct%3Dlzlyornk%7Cci%3D19349e457c72d153132a25c09b187b3813e80f2b%7Ctr%3Dslsf%7Csn%3D924306%7Chk%3Def00c8108d02913b3d8343fd90f975cf134c33f9",
        "https://brand.naver.com/nutricore/products/384739504?nl-au=cbd107e7399345458bf3954e99d5c9c5&NaPm=ct%3Dlzlyp5jk%7Cci%3D4547af0a449cacb20d8d6b58f86b459f336650be%7Ctr%3Dslsf%7Csn%3D358231%7Chk%3D7a5359d007ea5408c68a8a10db05eb10e4bbbd8b",
        "https://brand.naver.com/ckdhc/products/7465955298?NaPm=ct%3Dlzlypv08%7Cci%3D08c5af82c4f8f638a2116f49874cac64c6ae1546%7Ctr%3Dslsl%7Csn%3D202775%7Chk%3D5c7181cfbfc17ef4d60db8488155f2dc6d3c235b",
        "https://brand.naver.com/hamsoa/products/4253740665?nl-au=b40b3dc0bd6243689bfb39bb257e1ee3&NaPm=ct%3Dlzlyrurk%7Cci%3Daf0db074243a0e368711b31a3d971f09ca5fab8e%7Ctr%3Dslsf%7Csn%3D159283%7Chk%3D006a86f52a53afc8090d895578ec5a5917b6ec35",
        "https://brand.naver.com/gnm/products/409795851?nl-au=ba807341ddeb487da06c3427de0b0b80&NaPm=ct%3Dlzlys6c8%7Cci%3Dcf3afd597d95e812eabbe043ec587dcf2e63d8df%7Ctr%3Dslsf%7Csn%3D202062%7Chk%3D367964c2e6359d345435e21a5709c9bc35da12ef",
        "https://brand.naver.com/nlmall/products/7937114185?nl-au=2dbc25e8c7e144469c1f22e2a58bdee2&NaPm=ct%3Dlzlysjgg%7Cci%3D59cc047765a087b240a40b534fd7bc9a821588cd%7Ctr%3Dslsf%7Csn%3D966092%7Chk%3Dab992e6948f94dc81fcd1b7d1a9fbdcd5c811a02",
        "https://brand.naver.com/gnm/products/7888865954?nl-au=aeac85107d374ec597715b6ab89cd225&NaPm=ct%3Dlzlyt8x4%7Cci%3Dc8e0b3db2b277b49c791126fa58902d11bb368a5%7Ctr%3Dslsf%7Csn%3D202062%7Chk%3Da493344ce269237e3ba5d099b94c1523942783b4",
        "https://brand.naver.com/centrum/products/6280762637?nl-au=2bad84c66c7d469fad8d3d3bc7b8ee49&NaPm=ct%3Dlzlytpw8%7Cci%3Dab6a6fd8a9f951d44d57891db612bf51378407b7%7Ctr%3Dslsf%7Csn%3D339120%7Chk%3D3345d73bba4e3073f5e5fdf00fe073fdd6caa418",
        "https://brand.naver.com/cenovis/products/4591680255?nl-au=2f582a48c5f446f49ffe990e22eaafd6&NaPm=ct%3Dlzlyuaq8%7Cci%3Dfd54eb77005c474cae59c44a0db30c68436f830d%7Ctr%3Dslsf%7Csn%3D456009%7Chk%3Df7df1c59e3110ce2670e185af4923d3464617958",
        "https://brand.naver.com/yuhan/products/5411758956?nl-au=5b023c340f484853b234f3d84e1d0c62&NaPm=ct%3Dlzly57y8%7Cci%3D59901370adb82b88e811b354cc5906003f69d685%7Ctr%3Dslsf%7Csn%3D2221700%7Chk%3Dbdca02457051bddfc45f457d191f68c0d3ce401c"
]

products = [
                "01고려은단",
                "02오쏘몰",
                "03네추럴라이즈",
                "04센트룸",
                "05뉴트리코어",
                "06덴프스",
                "07닥터프로그램",
                "08네츄럴라이프얼라이브",
                "09바이엘",
                "10인테로",
                "11바이엘",
                "12뉴트리코어",
                "13아임비타",
                "14함소아",
                "15GNM자연의품격",
                "16네츄럴라이트얼라이브",
                "17GNM자연의품격",
                "18센트룸",
                "19세노비스",
                "20유한양행"
]

def run(playwright):
    # 브라우저 및 페이지 설정
    browser = playwright.chromium.launch(headless=False)  # True로 설정하면 브라우저 창이 표시되지 않음
    page = browser.new_page()

    for i, (url, product) in enumerate(zip(url_, products), start=1):

        top = product[0:2]

        # 웹 페이지 열기
        page.goto(url)

        # 리뷰 탭 클릭
        page.click('a[data-name="REVIEW"]')

        # 클릭 후 로딩 대기
        page.wait_for_timeout(2000)

        vitamin_title = page.text_content(
            '#content > div > div._2-I30XS1lA > div._2QCa6wHHPy > fieldset > div._3k440DUKzy > div._1eddO7u4UC > h3'
        ).strip()

        # 데이터 저장을 위한 리스트 초기화
        data = []

        page_number = 1
        while True:
            try:
                # 현재 페이지의 모든 span 및 em 요소 선택
                review_num = page.query_selector_all(
                    '#REVIEW > div:nth-child(1) > div._2LvIMaBiIO > div._2g7PKvqCKe > ul > li')

                reviews = []

                for sm in range(1, len(review_num)+1):
                    sm_set = f'#REVIEW > div > div._2LvIMaBiIO > div._2g7PKvqCKe > ul > li:nth-child({sm}) > div > div > div > div._3-1uaKhzq4 > div > div._1McWUwk15j > '

                    score = page.query_selector(
                        f'{sm_set}div._3i1mVq_JBd > div._3HKlxxt8Ii > div._2V6vMO_iLm > em._15NU42F3kT'
                    ).text_content().strip()

                    review_t = page.query_selector(
                        f'{sm_set}div._3z6gI4oI6l > div > span._2L3vDiadT9'
                    ).text_content().strip()

                    rday = page.query_selector(
                        f'{sm_set}div._3i1mVq_JBd > div._3HKlxxt8Ii > div.iWGqB6S4Lq > span._2L3vDiadT9'
                    ).text_content().strip()

                    try:
                        sex = page.query_selector(
                            f'{sm_set}div._3i1mVq_JBd > div._3HKlxxt8Ii > div._2FXNMst_ak > dl > div._3F8sJXhFeW > dd > span._2L3vDiadT9'
                        ).text_content().strip()
                    except:
                        sex = ""

                    reviews.append({
                        'top': top,
                        'url': url,
                        'brand': product[2:],
                        'page': page_number,
                        'vitamin_title': vitamin_title,
                        'date': rday,
                        'sex': sex,
                        'score': score,  # 평점 추가
                        'review': review_t
                    })
                # 추출한 리뷰 데이터 저장
                data.extend(reviews)

                # 다음 페이지 버튼 찾기
                next_button = page.query_selector(
                    f'a[data-shp-inventory="revlist"][data-shp-contents-id="{page_number + 1}"]')
                print(f"\n페이지 {page_number}의 데이터 추출:")

                if not next_button:
                    # 더 이상 페이지가 없으면 종료
                    break

                next_button.click()

                # 클릭 후 로딩 대기
                page.wait_for_timeout(2000)

                # 페이지 번호 증가
                page_number += 1

            except Exception as e:
                print(f"페이지 {page_number}에서 오류 발생: {e}")
                break

        # 데이터프레임 생성
        df = pd.DataFrame(data)

        # 데이터프레임을 CSV 파일로 저장
        output_file = f"D:/멀티캠퍼스/비타민_프로젝트/final_data/{top}등_{product}_reviews.csv"
        df.to_csv(output_file, encoding="utf-8-sig", index=False)
        print(f"데이터 저장 완료: {output_file}")

    # 브라우저 종료
    browser.close()


with sync_playwright() as playwright:
    run(playwright)