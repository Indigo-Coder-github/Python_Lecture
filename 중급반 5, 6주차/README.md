# Crawling
## Crawling? Scraping?
- crawling은 조직화, 자동화된 방식으로 인터넷을 탐색하는 프로그램
	- 검색 엔진들이 검색 결과를 만들기 위해 여러 웹사이트를 탐색하기 위해 작동
- scraping은 목적하는 데이터를 웹사이트에서 긁어오는 프로그램
- 엄밀한 의미에서 crawling과 scraping은 다르지만 혼용되고 있음
	- 해당 자료는 관습적으로 사용하는 크롤링으로 용어를 통일
## 정적 크롤링
- 수집한 웹사이트 소스에서 데이터를 긁어오는 것
- 빠르지만 수집할 수 있는 데이터나 행동의 한계가 있음
## 동적 크롤링
- 웹 브라우저 상에서 행동하는 코드로 데이터를 긁어오는 것
- 느리지만 수집할 수 있는 데이터나 행동의 한계가 정적 크롤링에 비해 없음
# 크롤링 전략?
## 1. 수집하려는 데이터가 있는 사이트 탐색
- 필요한 데이터를 수집할 수 있는 적절한 사이트를 선정해야함
	- 구글이나 네이버를 무조건 크롤링하는 것은 실패할 가능성이 있음
- 웹에서 데이터를 수집하는 방법은 항상 크롤링만 있는 것은 아님
	- 구글, Meta, OpenAI 등 많은 곳에서 API를 제공하며 나무위키 등은 사전에 정적으로 저장된 덤프 파일을 제공
## 2. 사이트의 Bot 대응 여부
- 간단한 코드를 통해 응답 코드를 확인
	- 여러 번 반복해도 응답 코드가 200인지, 긁어오는 내용은 정상적인지 확인
	- 많은 사이트에서 웹 서버의 부하를 막기 위해 Bot을 막음
		- header에 user-agent를 전달하거나 stealth selenium 라이브러리를 사용
## 3. 추출하려는 데이터의 위치
<img src = "https://github.com/Indigo-Coder-github/Python_Lecture/blob/4def75a/%EC%B4%88%EA%B8%89%EB%B0%98%201%EC%A3%BC%EC%B0%A8/install%20python%202.png" width="720">

- 추출하려는 데이터 요소에 우클릭-검사를 통해 HTML 상에서 어디에 위치했는지 파악
	- JSON, XML이라면 해당 파일의 구조를 파악
	- 우측의 개발자모드는 F12를 통해 진입할 수 있음
- 추출하고자 하는 데이터가 여러 개이면서 공통적인 속성을 갖고 있다면 여러 개를 추출해 공통적인 패턴을 찾아야 함
	- 만약 정적 크롤링으로 불가능할 것 같다면 동적 크롤링 패턴을 어떻게 할 것인지 설계해야 함
# requests
- Python에서 단순하고 우아한, 사람지향적인 HTTP 라이브러리
- [전체적인 API는 여기서 참고](https://requests.readthedocs.io/en/latest/api/)
## Server-Client
<img src = "https://github.com/Indigo-Coder-github/Python_Lecture/blob/main/%EC%A4%91%EA%B8%89%EB%B0%98%205%2C%206%EC%A3%BC%EC%B0%A8/Server-Client.png" width="720">

```python
import requests
r = requests.get("https://ko.wikipedia.org/wiki/리만_가설")
print(r)
#Output:Response [200]
#requests.get으로 얻은 객체의 print 결과는 status code로 나타남
r.header["date"]
#Output:"Wed, 29 Nov 2023 06:29:26 GMT"
#HTML에서 header는 HTML의 메타데이터에 해당함
#이를 dict형태로 제공하며 dict를 다루듯이 다룰 수 있음
r.text
#Output: 응답으로 받아온 전체 HTML을 string 형태로 반환
```
## urllib, urllib2, urllib3?
- [해당 내용을 간략하게 요약하면 Python3의 표준 라이브러리는 urllib으로 통합되었음](https://stackoverflow.com/questions/2018026/what-are-the-differences-between-the-urllib-urllib2-urllib3-and-requests-modul)
- [urllib3와 requests는 내장 패키지가 아닌 third-library임, 특히 requests는 Python에서 공식적으로 권장함](https://docs.python.org/3/library/urllib.request.html)
## get, post, delete, put, patch
# BeautifulSoup
- 웹 스크래핑 등을 사용하는 프로젝트를 빠르게 개선할 수 있도록 디자인된 Python 라이브러리
- request로 가져온 객체의 내용을 분석하는 알고리즘이 필요한데 BeautifulSoup 라이브러리는 이를 위한 parser를 제공
	- parser는 byte 데이터
```python
import requests
from bs4 import BeautifulSoup as BS

r = requests.get("https://ko.wikipedia.org/wiki/리만_가설")
soup = BS(r.content, "html.parser")
#두 번째로 들어가는 파라미터는 내용의 parsing을 어떤 방식으로 할지 선택
#html.parser, lxml, xml, html5lib이 있으며 공식문서에서는 lxml을 권장
#lxml은 pip에서 별도로 설치 필요
print(soup.find_all("p"))
#Output:p태그에 해당하는 요소 전체를 탐색, 하나만 찾고 싶다면 find()를 사용
```
# JSON
- JavaScript객체의 구문에서 비롯한 가벼운 데이터 교환 표준이 JSON
	- `{key:value}`쌍을 기초로 함, Python dict와 유사
- Python에서는 이를 encoding/decoding 할 수 있는 내장 모듈로써 제공
```python
def get_artist_info(api_url: str, headers: dict, group_list: pd.DataFrame) -> None:
    for platform in range(4, len(group_list.columns)):
        artist_info = '/api/v3/artist/{}/{}?detail=true'.format(group_list.columns[platform][:-3], group[platform])
        for group in group_list.itertuples(index=False):
            response = requests.get(api_url+artist_info, headers=headers)
            with open('json/{}_info.json'.format(group.artist.replace(":","")),"w",encoding="UTF-8") as f:
                json.dump(response.json(), f, indent=4, ensure_ascii=False)
```
- `json.dump()`, `json.dumps()`는 Python 객체를 JSON으로, `json.load()`, `json.loads()`는 JSON을 Python 객체로 변환
	- JSON은 string형태로 다뤄짐
	- 파일로 저장하기 위해서는 `dump()`함수를, 단순히 string만 얻고자 한다면 `dumps()`함수를 사용
	- 마찬가지로 `load()`도 파일에서 읽어오는 것을, string에서 json으로 변환하고자 한다면 `loads()`를 사용
	- 다만 json과 dict가 완전히 호환되지 않기 때문에 parsing 과정에서 오류가 발생할 수 있음
## JSON 여부 확인
- 모든 사이트가 데이터를 JSON으로 주고 받는 것은 아님
- JSON으로 데이터를 주고 받지 않는 사이트에서 JSON으로 데이터를 주고받고자 시도하면 예외가 발생
	- [개발자 도구를 통해](https://stackoverflow.com/questions/27326573/how-to-find-the-link-for-json-data-of-a-certain-website) 주고받는 네트워크를 감시하여 JSON 사용 여부를 알 수 있지만 개인적으론 한 번 request를 넣어보는 것이 확실한 것 같음
# Selenium
- 웹 브라우저 자동화를 위한 다양한 툴과 라이브러리를 포괄적으로 제공하는 프로젝트
```

```
## Selenium과 BeautifulSoup 결합하기