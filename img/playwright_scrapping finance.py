#Reference - http://wikidocs.net/231787

import asyncio 
from playwright.async_api import async_playwright

async def run_extract():
    #비동기 방식으로 playwright 시작
    async with async_playwright() as p:
        #브라우저 실행 (headless=False로 설정하면 실제 브라우저 창이 뜸)
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()

        #Naver로 이동
        await page.goto('https://finance.naver.com/news/mainnews.naver')

        elements = page.locator('.block1')
        block1_list = await elements.all_inner_texts()

        print(block1_list)

        for block1 in block1_list:
            print(block1)
            
        #터미널에서 사용자가 엔터키를 입력할 때까지 브라우저가 꺼지지 않고 무한 대기하게 하려면 다음 코드를 사용
        input('터미널에서 [Enter]를 입력하면 브라우저가 종료됩니다.')

        await browser.close()

if __name__ == '__main__':
    asyncio.run(run_extract())

