# Python 개발환경 설치
 - 해당 강의에선 Python 3.10과 VS Code를 이용해 실습
## Python 설치하기
 - https://www.python.org/downloads 에서 자신이 원하는 버전과 현재 자신의 OS에 맞춰 Python을 다운로드 할 수 있다.
<img src = "https://github.com/Indigo-Coder-github/Python_Lecture/blob/2023-2/%EC%B4%88%EA%B8%89%EB%B0%98%201%EC%A3%BC%EC%B0%A8/install%20python%201.png" width="720">
 - Add Python to PATH를 체크해놔야 나중에 환경변수를 편집하는 불상사가 발생하지 않는다.
<img src = "https://github.com/Indigo-Coder-github/Python_Lecture/blob/2023-2/%EC%B4%88%EA%B8%89%EB%B0%98%201%EC%A3%BC%EC%B0%A8/install%20python%202.png" width="720">
 - for all users를 체크하는 것을 권장하는 편(관리자 권한이 부여됨)이다.
<img src = "https://github.com/Indigo-Coder-github/Python_Lecture/blob/2023-2/%EC%B4%88%EA%B8%89%EB%B0%98%201%EC%A3%BC%EC%B0%A8/install%20python%203.PNG" width="720">
 - 최종적으로 install하여 명령 프롬프트에 python을 입력했을 때 python 인터프리터 창으로 진입하면 정상적으로 설치된 것이다.

## Python 3.10 vs 3.11
|                 |                          3.10                          |                                           3.11                                            |
|:---------------:|:------------------------------------------------------:|:-----------------------------------------------------------------------------------------:|
|  release date   |                       2021-10-04                       |                                        2022-10-24                                         |
|    주요 특징    |                     stable version                     |                                         속도향상                                          |
| 업데이트된 내용 | 복수타입힌트</br>에러메시지 개선</br>match-case문 추가 | CPython 개선</br>복수 예외처리 동시처리</br>에러 메시지 추가 개선</br>type hint로 Self 추가 |
## Anaconda
 - Anaconda는 Python 라이브러리를 설치, 관리에 편의성을 지원하는 도구
 - pip와 기능이 동일하기 때문에 pip를 쓸 줄 안다면 굳이라는 생각이 들 수 있다.
 - GUI 기반으로 라이브러리의 설치, 업그레이드 등을 지원해주고 R과의 호환성도 겸비하고 있다.
## IDE는 어떤 것이 좋을까?
 - IDE는 Integrated Development Environment(통합 개발 환경)의 줄임말로 프로그램 개발에 있어서 모든 기능을 통합한 프로그램이다.
 - 대표적인 Python IDE는 IDLE, PyCharm, VS Code, github.dev가 있다.
### IDLE
 - Python 기본 내장 IDE
 - 텍스트 에디터에 색칠놀이 한 수준이라 실제 개발에선 잘 사용되지 않는다.
### PyCharm
 - JetBrain사에서 제공하는 Python 전용 IDE
 - 강력한 자동완성기능과 편의성을 제공한다.
 - 유료라는 문제는 학교 이메일 라이선스로 해결할 수 있지만 Intellisense와 마찬가지로 프로그램이 무겁다는 단점이 있다.
### VS Code
 - Microsoft 사에서 제공하는 오픈소스 기반 IDE
 - 2016년 혜성처럼 등장해 자사의 Visual Studio를 밀어내면서 현재 가장 인기있는 IDE이다.
 - 가볍고 확장성이 좋고 크로스 플랫폼이라는 장점이 있지만 완성도나 지원기능 측면에서 유료 IDE보다 상대적으로 부족해보인다는 단점이 있다.
### github.dev
 - Github에서 제공하는 웹 기반 VS Code IDE
 - VS Code의 장단점을 함께 공유한다고 보면 된다.
 - 인터넷 접속이 가능하다면 군대 등의 특수 환경에서 웹기반 IDE로는 좋은 선택이라고 생각한다.
# IDE 다루기
## 확장 설치하기
 - VS Code는 오픈소스 기반이라 이에 대한 확장 기능들이 상당히 많다.
	 - 언어에 대한 공식 지원, 혹은 사용자가 만든 지원들 뿐만 아니라 개발에 필요한 다양한 도구들도 있다.
	 - [그만큼 정말 뻘짓같은 확장들도 꽤 있다.](https://www.youtube.com/watch?v=-5cSTqXGDUs)
 - 왼쪽에 <img src = "https://github.com/Indigo-Coder-github/Python_Lecture/blob/2023-2/%EC%B4%88%EA%B8%89%EB%B0%98%201%EC%A3%BC%EC%B0%A8/%ED%99%95%EC%9E%A5.PNG">을 누르면(혹은 Ctrl+Shift+X) 상점처럼 확장이 열린다. 이 중에서 Microsoft에서 제공하는 Python을 설치한다.
	 - 그 외 Don Jayamanne의 Python Extension Pack에서 Django와 Jinja(각각 Django와 Flask에서 필요하다.)를 제외하고 설치하는 것을 권장한다.
 - 설치 시 기본 언어는 영어이다. 본인이 영어로 개발하는 습관을 들이고 싶다면 놔둬고 되고 한국어를 쓰고 싶다면 Microsoft에서 제공하는 Korean Language Pack for Visual Studio Code을 설치한다.
## 무언가 실행하기
 - 파일-폴더 열기(혹은 Ctrl+K, Ctrl+O)를 통해 개발하려는 폴더 위치를 연다.
 - 이후 파일-새 텍스트 파일(혹은 Ctrl+N)을 통해 언어 선택으로 Python을 선택하거나 저장(혹은 Ctrl+S)을 통해 .py의 형태로 파일을 저장하면 python 파일로 인식한 코드 intellisense가 제공된다.
### .py, .ipynb
 - .py는 python 파일의 확장자이다.
 - .ipynb는 Jupyter Notebook의 확장자이다.
	 - Google colab에서 지원되는 파일 확장자이다.
	 - py와 다르게 md와 python 코드의 혼용이 가능해 PPT 대용으로 괜찮으며 서버 개발 환경만 갖추고 있다면 어디서든 작업을 계속할 수 있다.
	 - 출력 결과가 바로 나오는 것도 장점이다.
	 - 다만 대부분의 코드는 배포 시 .py로 배포되고 디버깅이 IDE보다 불편하다.
	 - .ipynb를 .py로 변환하기 위해서 VS Code에서 [Jupyter 확장을 설치해야 한다.](https://stackoverflow.com/questions/64297272/best-way-to-convert-ipynb-to-py-in-vscode)
```python
import os
my_input = input("이곳에 입력하세요: ")
for i in range(1,5):
	print("{}회: {}\n{}".format(i, input, os.listdir()))
```
 - VS Code에서 Ctrl+F5 단축키로 디버깅하지 않고 실행할 수 있다.
## Module(모듈)
 - 정의문과 구문을 갖고 있는 Python 파일
	 - 이 모듈의 집합체는 package로써 모듈과 마찬가지로 import로 불러온다.
 - python 파일 이름 자체가 모듈 이름이다.
	 - 즉 `import os`는 `os.py`를 `import`한 것이다.
 - 내가 만든 파일을 모듈로 `import`하고자 하면 불러오는 파일과 모듈 파일이 같은 경로 상에 위치해야 한다.
 - 모듈을 import한 것만으로는 그 모듈 내의 기능을 사용할 수 없기 때문에 `os.listdir()`처럼 `.`을 통해 접근해야 한다.
 - 모듈은 순환 참조를 할 경우 오류를 일으킨다.
	 - `a.py`에서 `b.py`를 `import`하고 `b.py`에서 `a.py`를 `import`할 수 없다.
	 - 여러 파일에 프로그래밍 하는 것이 익숙치 않다면 순환 참조를 일으키는 실수를 범할 수 있어 주의가 필요하다.
```python
#os.py에서 listdir을 불러옴
from os import listdir
#os.py에 있는 모든 기능을 불러옴
from os import *
#os.py를 os_functions라는 이름으로 불러옴
import os as os_functions
#아래 코드는 NameError가 발생함
print(os.listdir())
#os.py에서 listdir을 directory라는 이름으로 불러옴
from os import listdir as directory
#sklearn package의 cluster 모듈에서 KMeans 클래스 불러오기
from sklearn.cluster import KMeans
```
## input
 - input 함수로 input 전에 출력할 것을 전달한다. 전달하지 않으면 바로 입력 커서가 나타난다.
 - 코딩 테스트나 임베디드 등에 표준 입력이 필요하다면 아래와 같은 코드를 통해 input을 받는다.
	 - 코딩 테스트에서 자주 쓰이는 입력은 [해당 링크에 정리되어 있다.](https://velog.io/@yeseolee/Python-%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EC%9E%85%EB%A0%A5-%EC%A0%95%EB%A6%ACsys.stdin.readline)
```python
import sys
my_input = sys.stdin.readline()
```
## print
 - 출력하고자 하는 값을 print에 넣어준다.
	 - sep는 구분자로 default 값은 공백이며 다른 값을 주면 여러 값 사이에 전달했던 값을 출력한다.
	 - end는 맨 끝에 붙이는 값으로 default 값은 줄바꿈이며 다른 값을 주면 해당 값의 출력이 다 끝나고 전달했던 값을 출력한다.
	 - 그 외에 제어문자를 통해 [줄바꿈, 띄어쓰기, tab 등을 조절할 수 있다.](https://en.wikipedia.org/wiki/Control_character#In_ASCII)
```python
print("This","is","Σπάρτη", sep="!")
#Output:This!is!Σπάρτη
#sep를 활용한 출력
print("I have a pen", end=". ")
print("I have a pineapple")
#Ouput:I have a pen. I have a pineapple
#end를 활용한 출력
print("start\tend\thigh\tlow")
#Output:start    end    high    low
#제어문자를 활용한 출력
```
## format
 - 문자열 formatting을 지원하는 함수
 - python도 처음에는 서식 지정자를(`%d`, `%s` 등) 지원했었으나 2.6부터 format 함수를, 3.6부터 f-string을 지원하기 시작했다.
	 - 현재도 이 세 가지 방법은 모두 사용할 수 있지만 서식 지정자는 Pythonic한 방법이 아닌 것으로 여겨져 많이 사장됐다.
	 - [전반적으로 f-string을 권장하지만 하위버전의 호환성 등을 고려하면](https://stackoverflow.com/questions/5082452/string-formatting-vs-format-vs-f-string-literal)[format 함수도 여전히 기용할 여지가 많다.](https://velog.io/@keywookim/%ED%8C%8C%EC%9D%B4%EC%8D%AC-f-string-formatting%EC%9D%80-%EB%AC%B4%EC%A0%81%EC%9D%BC%EA%B9%8C)
	 - 좀 더 다양한 활용법은 위의 링크와 더불어 [여기서도](https://dojang.io/mod/page/view.php?id=2300)확인할 수 있다. 해당 강의에서 format 함수의 복잡한 사용은 거의 없다.
 - string 자료형의 함수이기 때문에 출력 뿐만이 아니라 문자열을 다루는 상황이라면 언제든 사용할 수 있다.
	 - format 함수에 전달되는 값은 출력할 수 있다면 모두 무관하다.
```python
var1 = "format specifiers"
var2 = "formatting"
var3 = "f-string"
print("This is %s".%var1) #서식 지정자를 활용
print("This is {}".format(var2)) #format 함수를 활용
print(f"This is {var3}") #f-string을 활용
```
## 디버깅
 - VS Code에서 F5 단축키를 눌러 Python File을 선택하면 실행
 - F11을 누르면 다음 줄로 이동하며 F5를 누르면 중단점에 다시 도달할 전까지 코드를 실행한다.
	 - 중단점 없이 디버깅할 경우 오류가 난 지점에서 멈추며 오류가 없다면 프로그램을 정상적으로 종료한다.
 - 오류의 원인을 찾지 못하거나 중요한 실행을 하기 전 단위 테스트를 할 때 매우 유용하다.
<img src = "https://github.com/Indigo-Coder-github/Python_Lecture/blob/2023-2/%EC%B4%88%EA%B8%89%EB%B0%98%201%EC%A3%BC%EC%B0%A8/%EB%94%94%EB%B2%84%EA%B9%85.png" width="720">

### 중단점
 - line number 옆을 클릭해서 생성된 빨간 버튼
 - 코드가 진행되다가 중단점이 있는 위치에서 멈추며 F11을 누르거나 F5를 누르면 해당 line이 실행된다.
### 변수
 - 현재 실행되는 파일에서 사용하고 있는 변수
 - Local은 지역변수, Global은 전역변수의 값을 보여준다.
### 조사식
 - 현재 실행 파일에 대한 python 코드의 결과를 표시
 - 예를 들어 조사식의 +버튼을 누르고 `print(i)`를 입력하면 콘솔 창에 현재 i값이 표시된다.
 - 코드가 실행 중일 때 코드를 입력해 값을 조사할 수 있다.
### 호출스택
 - 현재 스택 영역에 호출된 파일을 표시
# Python 개발을 위해 도움이 될만한 것들
## Chat GPT
 - 그는 신이다.
 - GPT-4의 플러그인 지원, 입력 다양화 등 계속해서 발전하고 있지만 출시 초창기보다 성능이 떨어졌다는 논문들이 발표되었다.
## 구글링
 - 그는 신이다. 2
 - 한 문서만 보면 해당 정보의 정확성을 장담할 수 없어 편향될 수 있기 때문에 여러 개를 교차검증 해봐야 한다.
## StackOverFlow
 - https://www.stackoverflow.com
 - chat gpt가 나타나기 이전에 코딩의 신으로 없는 질문이 없고 모든 코드는 stackoverflow의 코드의 짜깁기라 할 정도
 - 영어 기반의 전세계적 코딩 관련 Q&A 사이트로 24시간 이내에 하나의 답변은 받을 수 있다.
 - 다만 질문 형식에 대한 규정이 좀 유연하지 않아 질문글이 이상하면 비추를 줄 수 있으며 다른 사용자에 의해 질문글이 수정될 수도 있다.
 - 코딩 이외의 주제에 대해서는 StackExchange에서 얘기할 수 있으며 최근에는 이를 필두로 정보보안, 머신러닝 등의 자매 사이트도 개설됐다.
## GeekNews
 - https://www.news.hada.io
 - 개발과 관련하여 최신 뉴스, Github Repo등의 주요 내용을 요약해 올리는 포럼 형식으로 올리는 사이트
 - 한국어이며 아무나 올릴 수 있음에도 불구하고 최신성과 정확도가 생각보다 좋다.
 - 개발 트렌드를 읽거나 개발 관련 뉴스를 얻기 좋은 사이트이다.
## PEP
 - https://peps.python.org/pep-0000/
 - 세부적인 Python 코딩 스타일 지침서
 - 요즘엔 IDE에서 어느 정도 잡아준다.
 - 배포할 목적이 없다면 엄격히 지킬 필요가 없지만 배포하려고 한다면 주요 가이드라인은 지켜주는 것이 좋다.
 - 내용이 상당히 길은 영어 문서이니 정독하기 보단 필요할 때마다 찾아보는 것을 추천한다.
## Python 공식문서
 - https://docs.python.org/3/
 - Python 전체 내장 기능에 대한 공식문서
 - 한국어 역본도 있으나 좀 불완전하다.
 - 영어가 되어도 장문이고 어느 정도 배경지식이 있어야 좀 읽히지만 정확성은 제일 높다.
# 코딩 잘하는 방법
 - 인내는 연단을, 연단은 소망을 이루는 줄 앎이로다(롬 5:4)
 - 그러나 내가 가는 길을 그가 아시나니 그가 나를 단련하신 후에는 내가 순금 같이 되어 나오리라(욥 23:10)
