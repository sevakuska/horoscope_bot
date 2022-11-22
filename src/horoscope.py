import asyncio, aiohttp

import fake_useragent
from bs4 import BeautifulSoup


URL = 'https://horo.mail.ru/prediction/{}/today/'
USER_AGENT = fake_useragent.UserAgent()
PREDICT_ATR = 'article__item article__item_alignment_left article__item_html'
DATE_ATR = 'link__text'


async def get_horoscope(sign: str) -> str:
    headers = {
        'User-Agent': USER_AGENT.random
    }
    async with aiohttp.ClientSession() as session:
        response = await session.get(url=URL.format(sign), headers=headers)
        text = await response.text()
        soup = BeautifulSoup(text, 'html.parser')
        block = soup.find('div', class_=PREDICT_ATR)
        paragraphs = block.find_all('p')
        date = soup.find('span', class_=DATE_ATR).text
        prediction = '\n\n'.join([p.text for p in paragraphs])
        return f'{date}\n\n{prediction}'
