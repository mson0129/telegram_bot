#내장 모듈
import os
from urllib.request import urlopen
#외장 모듈
from bs4 import BeautifulSoup
from github import Github
import telegram

'''
#ID 받아오기
chat_token = os.environ["CHAT_BOT_TOKEN"]
bot = telegram.Bot(token = chat_token)
updates = bot.getUpdates()
for u in updates:
    print(u.message['chat']['id'])
''' 

#크롤링
url = "https://store.sony.co.kr/handler/ViewProduct-Start?productId=32851960"

#BeautifulSoup4
html = urlopen(url)
bsObject = BeautifulSoup(html, "html.parser")
parent_path = bsObject.find("p", class_="btnArea")
links = parent_path.find_all("a")
if links[1].text != "일시품절":
    #입고 완료: 메시지 보내기
    result = "A7s3: 지금 바로 구매하세요.\n" + url
    chat_token = os.environ["CHAT_BOT_TOKEN"]
    chat_id = os.environ["CHAT_USER_ID"]
    chat_text = result
    bot = telegram.Bot(token = chat_token)
    bot.sendMessage(chat_id = chat_id, text = chat_text)
else:
    try:
        g = Github(os.environ["MY_GITHUB_TOKEN"])
        repo = g.get_user().get_repo("telegram_bot")
        repo.create_issue(title="A7S III 와드", body="재고없음")
        print("A7S III 와드: 재고없음")
    except:
        print("에러 발생했습니다.")
