# 텔레그램 봇

[![MIT License](https://img.shields.io/github/license/mson0129/telegram_bot)](https://www.mit.edu/~amini/LICENSE.md)
![Repo Size](https://img.shields.io/github/repo-size/mson0129/telegram_bot)
![Last Commit](https://img.shields.io/github/last-commit/mson0129/telegram_bot)
![Release Version](https://img.shields.io/github/v/release/mson0129/telegram_bot)
[![Hits](https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2Fmson0129%2Ftelegram_bot&count_bg=%2379C83D&title_bg=%23555555&icon=&icon_color=%23E7E7E7&title=hits&edge_flat=false)](https://hits.seeyoufarm.com)

![PyGithub](https://img.shields.io/badge/PyGithub-v1.51-blue)
![python-telegram-bot](https://img.shields.io/badge/python--telegram--bot-v13.1-blue)
![beautifulsoup4](https://img.shields.io/badge/beautifulsoup4-v4.9.3-blue)

[![Git Push](https://github.com/mson0129/telegram_bot/workflows/Git%20Push/badge.svg?event=schedule "Github Actions")](https://github.com/mson0129/telegram_bot/actions)
[![Wards](https://github.com/mson0129/telegram_bot/workflows/A7S%20III%20Wards/badge.svg?event=schedule "Github Actions")](https://github.com/mson0129/telegram_bot/actions)

Github Actions에 등록된 Workflow를 트리거 이벤트에 따라 실행하고, 그 실행결과를 텔레그램 메시지로 보내거나 이슈에 등록합니다.

## Github Actions의 특징과 관련 코드 및 설정
Github Actions가 가지고 있는 특징이 있으며, 해당 특징에서 발생하는 제약 사항을 극복하기 위한 파일 및 설정을 포함하고 있습니다.

### Github Action의 특징
Github Actions의 경우 아래와 같은 특징이 있습니다.
* cron(crontab)으로 지정한 스케쥴 대로 모든 것이 실행되지 않음
* cron으로 지정할 수 있는 최소 스케줄 간격은 5분임
* cron으로 지정한 시간보다 실제 실행시 15분 이상 지연 실행됨
* 저장소(Repository)에 60일 이상 변경사항이 없을 경우 Actions는 비활성화됨
* Private 저장소인 경우 월 사용량(2,000분)에 제한이 있음
* 트리거 이벤트가 발생할 때마다 새로운 가상 OS 환경이 준비되어 매번 Python 외장 모듈의 설치가 필요함

### 관련 파일
#### [date.txt](https://github.com/mson0129/telegram_bot/blob/main/date.txt)
60일 이상 저장소 변경사항 없을 경우, Actions가 비활성화되는 것을 막기 위한 파일입니다.
["Git Push" Action](https://github.com/mson0129/telegram_bot/blob/main/.github/workflows/gitpush.yml)이 한 달에 한 번씩 date.txt 파일을 생성하고 저장소에 변경사항을 반영합니다.

#### [requirements.txt](https://github.com/mson0129/telegram_bot/blob/main/requirements.txt)
매 실행시 Python 외장 모듈 설치를 위한 파일입니다.
작성한 코드 실행 전에 pip install 명령을 통해 파일 내 지정한 모듈을 설치합니다.
Node.js에서 package.json 파일 내 dependencies 값과 같은 역할입니다.
["A7S III Ward" Action](https://github.com/mson0129/telegram_bot/blob/main/.github/workflows/ward_a7s3.yml)의 "Install dependencies"에서 모듈을 설치합니다.

### 관련 설정
#### 저장소 비밀 변수 설정(Settings > Secret)
비공개(Private) 저장소인 경우 월 사용량 제한이 있으므로, 저장소를 공개 저장소로 사용하는 것이 좋습니다.
다만 Github이나 텔레그램과 연동하기 위해 사용되는 인증 토큰/키, ID들은 민감 정보이므로 소스코드로부터 분리가 필요합니다.
이들은 저장소 비밀 변수로 설정이 가능하며, 해당 정보는 Python 코드 내에서 환경변수로 그 값을 가져올 수 있습니다.
(os 모듈 import 후, os.environ 딕셔너리 활용)

1. 메시지를 보낼 텔레그램 봇의 토큰

    텔레그램 내 [BotFather](t.me/BotFather)를 통해 생성한 값입니다.

2. 메시지를 받을 텔레그램 사용자 아이디
3. 저장소에 이슈를 생성(Creating)하고 마감(Closing)하기 위한 깃험 사용자 액세스 토큰

    Github > Settings > Developer Settings > Personal access tokens에서 생성한 값입니다.

깃헙 저장소(Github Repository) 내에 설정(Settings)에 있는 Secret에 메시지를 보낼 봇 토큰, 메시지를 받을 사용자 아이디가 저장되어 있습니다.
해당 정보는 노출되지 않습니다.

## 액션(Actions)
### 와드(Wards)
#### [A7S III 와드](https://github.com/mson0129/telegram_bot/blob/main/wards/a7s3.py)

소니스토어 A7S III 와드입니다. 재고 입고시에 텔레그램으로 봇이 메시지를 보내줍니다. 재고 입고 여부와 상관 없이 확인 결과를 저장소 이슈로 생성(Creating)하고 마감(Closing)합니다.

# 참조(References)
## 예제 코드(Articles)
### Github Actions
* [피터팬의 좋은 방 구하기 예제](https://github.com/heejongahn/tinkerbell-template)

    * Node.js 및 TypeScript 기반

    * [마이크로 소프트웨어 잡지](https://www.imaso.co.kr/archives/5649)에서 접하여 가장 먼처 잠조하였던 코드이며, 피터팬의 좋은 방 구하기에서 값을 가져와 저장소 이슈를 생성하는 방식으로 결과를 저장합니다. Node.js 특성 상 처리하는 업무 대비 파일 및 코드량이 많아 Python을 검토하는 계기가 되었습니다.

* [Github Action Practice](https://github.com/jonnung/github-action-practice)

    * Node.js 및 JavaScript 기반

    * Github Actions 초심자가 검토하기 좋은 미니멀한 예제입니다.

* [Github Action 사용법 정리](https://zzsza.github.io/development/2020/06/06/github-action/)

    * Python 기반

    * Yes24를 크롤링(Crawling)하여 저장소 이슈를 생성하는 방식으로 결과를 저장(피터팬의 좋은 방 구하기 예제와 동일 작동)합니다.

### 텔레그램(Telegram)

* [파이썬을 이용하여 텔레그램(Telegram) 메세지 보내기](https://pydole.tistory.com/entry/Python-%ED%8C%8C%EC%9D%B4%EC%8D%AC%EC%9D%84-%EC%9D%B4%EC%9A%A9%ED%95%98%EC%97%AC-%ED%85%94%EB%A0%88%EA%B7%B8%EB%9E%A8Telegram-%EB%A9%94%EC%84%B8%EC%A7%80-%EB%B3%B4%EB%82%B4%EA%B8%B0)

    * Python 기반
    
    * 매우 간단한 텔레그렘 메시지 보내기 예제입니다.

* [python으로 telegram bot 활용하기](https://blog.psangwoo.com/coding/2016/12/08/python-telegram-bot-1.html)

    * Python 기반
    
    * 텔레그램 메시지 보내기 예제입니다. 1편 외에 이후 후속편에서 InlineKeyboard 등 추가 기능들도 확인할 수 있습니다.

## 개발자 문서(Developer Documents)
* [Github Actions](https://docs.github.com/en/free-pro-team@latest/actions)
* [PyGithub](https://pygithub.readthedocs.io)
* [python-telegram-bot](https://python-telegram-bot.readthedocs.io)
