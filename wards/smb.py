#내장 모듈
import os
import time
import json
from urllib.request import Request, urlopen
import asyncio
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
#외장 모듈
#pip install -r requirements.txt
from github import Github
import telegram

# 요청 설정 값
url = "https://www.smes.go.kr/sanhakin/usr/anns/hsspplCltgSttn.do"
data = {
    "dc_Req01": {
        "searchCondition": "0",
        "searchKeyword": "",
        "PAGE_NO": "1",
        "DATA_SIZE": "100",
        "BBSCLCODESE": ""
    }
}
headers = {
    "Content-Type": "application/json",
    "Accept": "application/json",
}

target = "주택특별공급 사업공고"

g = Github(os.environ["GITHUB_TOKEN"])
repo = g.get_repo("mson0129/telegram_bot")

chat_token = os.environ["CHAT_BOT_TOKEN"]
chat_id = os.environ["CHAT_USER_ID"]
bot = telegram.Bot(token = chat_token)

try:
    # URL Lib Request
    req = Request(url, data=json.dumps(data).encode("UTF-8"), headers=headers)
    for i in range(10):
        try:
            res = urlopen(req)
            break
        except:
            print(f"""{i+1}회 연결 에러""")
            if i == 9:
                raise ConnectionError
            else:
                time.sleep(5)
                continue
    
    # JSON 파싱 및 데이터 전처리
    res_json = json.loads(res.read().decode("UTF-8"))
    res_arr = [v for v in res_json["dc_getList01"] if v["LIMITDATEYN"] == "N" and v["CHRGDEPTNM"].find("서울") > -1] # 서울 지역만, 종료된 공고 제외
    # res_arr = [v for v in res_json["dc_getList01"] if v["CHRGDEPTNM"].find("서울") > -1] # 서울 지역만 - 테스트용

    # 결과가 1개 이상인 경우, 메시지 생성 & 보내기
    if len(res_arr) > 0:
        body = "\n"
        for v in res_arr:
            body += f"""<a href="https://www.smes.go.kr/sanhakin/websquare/wq_smesDtlBsns.do?NTTSN={v["NTTSN"]}&BBSCLCODESE={v["BBSCLCODESE"]}&BSNSCLCODESE={v["BSNSCLCODESE"]}">{v["BBSSJ"]}</a>\n접수기간: {v["RCEPTDT"]}\n\n"""
        text = "<b>{target}: {title}</b>\n{body}".format(target=target, title=f"""{len(res_arr)} 건""", body=body)
        asyncio.run(bot.send_message(chat_id = chat_id, text = text, parse_mode = "HTML"))
except ConnectionError as e:
    #비정상 종료
    #이슈 남기기
    title = "연결 에러"
    body = e
    repo.create_issue(title="{target}: {title}".format(target=target, title=title), body="{url}\n{body}".format(body=body, url=url))
    #텔레그램 메시지 보내기
    keyboard = [
        [telegram.InlineKeyboardButton(text="Github 저장소로 이동", url="https://github.com/mson0129/telegram_bot/issues")]
    ]
    text = "<b>{target}: {title}</b>\n{body}".format(target=target, title=title, body=body)
    asyncio.run(bot.send_message(chat_id = chat_id, text = text, parse_mode="HTML", reply_markup = telegram.InlineKeyboardMarkup(keyboard)))
except Exception as e:
    #연결 오류 외 비정상 종료
    #이슈 남기기
    title = "알 수 없는 오류"
    body = e
    repo.create_issue(title="{target}: {title}".format(target=target, title=title), body="{url}\n{body}\n".format(body=body, url=url))
    #텔레그램 메시지 보내기
    keyboard = [
        [telegram.InlineKeyboardButton(text="Github 저장소로 이동", url="https://github.com/mson0129/telegram_bot/issues")]
    ]
    text = "<b>{target}: {title}</b>\n{body}".format(target=target, title=title, body=body)
    asyncio.run(bot.send_message(chat_id = chat_id, text = text, parse_mode = "HTML", reply_markup = telegram.InlineKeyboardMarkup(keyboard)))
else:
    #정상 종료
    # #이슈 남기기
    # repo.create_issue(title="{target}: {title}".format(target=target, title=title), body="{url}\n{body}".format(body=body, url=url))
    # #이슈 클로징
    # open_issues = repo.get_issues(state='open')
    # for issue in open_issues:
    #     issue.edit(state='closed')
    pass