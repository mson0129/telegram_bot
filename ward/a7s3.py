#내장 모듈
import os
#외장 모듈
from urllib.request import urlopen
from bs4 import BeautifulSoup
import telegram

'''
#ID 받아오기
chat_token = os.getenv("CHAT_BOT_TOKEN")
bot = telegram.Bot(token = chat_token)
updates = bot.getUpdates()
for u in updates:
    print(u.message['chat']['id'])
''' 

#크롤링
url = "https://store.sony.co.kr/handler/ViewProduct-Start?productId=32851960"
name = "A7s3"

#BeautifulSoup4
html = urlopen(url)
bsObject = BeautifulSoup(html, "html.parser")
parent_path = bsObject.find("p", class_="btnArea")
links = parent_path.find_all("a")
if links[1].text != "일시품절":
    result = name + ": " + "지금 바로 구매하세요.\n" + url

#메시지 보내기
chat_token = os.getenv("CHAT_BOT_TOKEN")
chat_id = os.getenv("CHAT_USER_ID")
chat_text = result
bot = telegram.Bot(token = chat_token)
bot.sendMessage(chat_id = chat_id, text = chat_text)
