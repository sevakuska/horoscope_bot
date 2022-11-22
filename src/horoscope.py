import asyncio, aiohttp

import fake_useragent
from bs4 import BeautifulSoup


URL = 'https://horo.mail.ru/prediction/{}/today/'
USER_AGENT = fake_useragent.UserAgent()
PREDICT_ATR = 'article__item article__item_alignment_left article__item_html'
SIGN_ATR = 'hdr__inner'
DATE_ATR = 'link__text'


async def get_horoscope(sign: str) -> str:
    headers = {
        'User-Agent': USER_AGENT.random
    }
    async with aiohttp.ClientSession() as session:
        response = await session.get(url=URL.format(sign), headers=headers)
        status = response.status
        try:
            text = await response.text()
            soup = BeautifulSoup(text, 'html.parser')
            block = soup.find('div', class_=PREDICT_ATR)
            paragraphs = block.find_all('p')
            sign_block = soup.find('h1', class_=SIGN_ATR).text.split(':')[-1]
            date = soup.find('span', class_=DATE_ATR).text
            prediction = '\n\n'.join([p.text for p in paragraphs])
            return f'{sign_block}\n{date}\n\n{prediction}'
        except AttributeError:
            return 'Ошибка, попробуйте позже'
