#Reference - http://wikidocs.net/231787

import asyncio 
from playwright.async_api import async_playwright

async def run_playwright():
    #비동기 방식으로 playwright 시작
    async with async_playwright() as p:
        #브라우저 실행 (headless=False로 설정하면 실제 브라우저 창이 뜸)
        browser = await p.chromium.launch(headless=False)
        page = browser.new_page()

        #Naver로 이동
        await page.goto('http://naver.com')

        #검색창에 키워드 입력 (네이버 검색창 id는 query)
        await page.fill('#query', '인공지능')

        #검색 버튼 클릭 (네이버 검색 버튼 class 나 id 지정)
        #await page.click('.btn_search')
        await page.click('#search-btn')

        #페이지 로드 대기
        await page.wait_for_load_state('networkilde')

        #제목 출력 및 스크린샷
        print(f'헌재 페이지 제목: {await page.title()}')
        await page.screenshot(path='./img/naver_search_result.png')

        #눈으로 확인할 수 있도록 10초동안 대기(실제 코드에서는 불필요)
        await page.wait_for_timeout(10000)

        await browser.close()

if __name__ == '__main__':
    asyncio.run(run_playwright())

