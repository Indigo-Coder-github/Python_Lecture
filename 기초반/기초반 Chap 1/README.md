# 기초반 1차시

## TOC

- [1. Python 개발환경 설치](#1-python-개발환경-설치)
  - [1-1. python 설치하기](#1-1-python-설치하기)
    - [1-1-1. Python 3.10 vs 3.11 vs 3.12](#1-1-1-python-310-vs-311-vs-312)
    - [1-1-2. Anaconda](#1-1-2-anaconda)
  - [1-2. ide는 어떤 것이 좋을까](#1-2-ide는-어떤-것이-좋을까)
    - [1-2-1. IDLE](#1-2-1-idle)
    - [1-2-2. PyCharm](#1-2-2-pycharm)
    - [1-2-3. VS Code](#1-2-3-vs-code)
    - [1-2-4. github.dev](#1-2-4-githubdev)
- [2. VS Code 다루기](#2-vs-code-다루기)
  - [2-1. 확장 설치하기](#2-1-확장-설치하기)
  - [2-2. 무언가 실행하기](#2-2-무언가-실행하기)
    - [2-2-1. .py, .ipynb](#2-2-1-py-ipynb)
  - [2-3. 디버깅](#2-3-디버깅)
    - [2-3-1. 중단점](#2-3-1-중단점)
    - [2-3-2. 변수](#2-3-2-변수)
    - [2-3-3. 조사식](#2-3-3-조사식)
    - [2-3-4. 호출스택](#2-3-4-호출스택)
- [3. Variable(변수)](#3-variable변수)
  - [3.1. Coding Convention](#3-1-coding-convention)
- [4. Constant(상수)](#4-constant상수)
- [5. 세미콜론, Indentation](#5-세미콜론-indentation)
- [6. Console I/O](#6-console-io)
  - [6-1. Console Input](#6-1-console-input)
  - [6-2. Console Output](#6-2-console-output)
    - [6-2-1. format](#6-2-1-format)
- [7. File I/O](#7-file-io)
  - [7-1. File Input](#7-1-file-input)
    - [7-1-1.](#7-1-1-with)
  - [7-2. File Output](#7-2-file-output)
- [8. Module(모듈)](#8-module모듈)
- [9. Comment(주석)](#9-comment주석)
- [10. Exception Handling(예외처리)](#10-exception-handling예외-처리)
  - [10-1. try, except](#10-1-try-except)
  - [10-2. finally, else](#10-2-finally-else)

## 1. Python 개발환경 설치

- 해당 강의 자료의 개발 환경은 Python 3.10, VS Code, Windows 10
- 자신이 차후 사용하고자 하는 목적에 따라 환경 설정이 달라질 수 있다.
  - 3.9 이상부터는 Windows 7 이상에서만 지원된다.
  - 일부 라이브러리의 버전은 3.8이나 3.9에 호환될 수 있으며 Linux를 필요로 할 수 있다.
  - 핵심 코드를 다른 언어로 작성한 라이브러리의 경우 해당 언어의 도구가 필요할 수 있다.

### 1-1. Python 설치하기

- <https://www.python.org/downloads> 에서 자신이 원하는 버전과 현재 자신의 OS에 맞춰 Python을 다운로드 할 수 있다.
<img src = "https://github.com/Indigo-Coder-github/Python_Lecture/blob/2024-1/%EA%B8%B0%EC%B4%88%EB%B0%98/%EA%B8%B0%EC%B4%88%EB%B0%98%20Chap%201/install%20python%201.png"></img>
- Add Python to PATH를 체크해놔야 나중에 환경변수를 편집하는 불상사가 발생하지 않는다.
<img src = "https://github.com/Indigo-Coder-github/Python_Lecture/blob/2024-1/%EA%B8%B0%EC%B4%88%EB%B0%98/%EA%B8%B0%EC%B4%88%EB%B0%98%20Chap%201/install%20python%202.png">
- for all users를 체크하는 것을 권장하는 편(관리자 권한이 부여됨)이다.
<img src = "https://github.com/Indigo-Coder-github/Python_Lecture/blob/2024-1/%EA%B8%B0%EC%B4%88%EB%B0%98/%EA%B8%B0%EC%B4%88%EB%B0%98%20Chap%201/install%20python%203.PNG">
- 최종적으로 install하여 명령 프롬프트에 python을 입력했을 때 python 인터프리터 창으로 진입하면 정상적으로 설치된 것이다.

#### 1-1-1. Python 3.10 vs 3.11 vs 3.12

- minor 버전의 매 업데이트는 약 한 달 주기로 10월에 이뤄진다.

||3.10|3.11|3.12|
|:-:|:-:|:-:|:-:|
|release date|2021-10-04|2022-10-24|2023-10-02|
|업데이트된 내용|복수타입힌트</br>에러메시지 개선</br>match-case문 추가|CPython 개선</br>복수 예외처리 동시처리</br>에러 메시지 추가 개선</br>type hint로 Self 추가|사용하는/사용하지 않는</br>모듈과 기능들 대규모 점검</br>f-string 개선|

#### 1-1-2. Anaconda

- Anaconda는 Python 라이브러리를 설치, 관리에 편의성을 지원하는 도구
  - 다만 자잘한 버그나 오류가 많아 사용에는 오히려 불편할수도 있다.
- pip와 기능이 동일하기 때문에 pip를 쓸 줄 안다면 굳이라는 생각이 들 수 있다.
- GUI 기반으로 라이브러리의 설치, 업그레이드 등을 지원해주고 R과의 호환성도 겸비하고 있다.

### 1-2. IDE는 어떤 것이 좋을까?

- IDE는 Integrated Development Environment(통합 개발 환경)의 줄임말로 프로그램 개발에 있어서 모든 기능을 통합한 프로그램이다.
- 대표적인 Python IDE는 IDLE, PyCharm, VS Code, github.dev가 있다.
  - 이외에도 XCode, Zed, goorm, 메모장 등이 있다.

#### 1-2-1. IDLE

- Python 기본 내장 IDE
- 텍스트 에디터에 색칠놀이 한 수준이라 실제 개발에선 잘 사용되지 않는다.

#### 1-2-2. PyCharm

- JetBrain사에서 제공하는 Python 전용 IDE
- 강력한 자동완성기능과 편의성을 제공한다.
- 유료라는 문제는 학교 이메일 라이선스로 해결할 수 있지만 IntelliJ와 마찬가지로 프로그램이 무겁다는 단점이 있다.

#### 1-2-3. VS Code

- Microsoft 사에서 제공하는 오픈소스 기반의 IDE
- 2016년 혜성처럼 등장해 자사의 Visual Studio를 밀어냈고 현재 점유율이 높은 IDE 중 하나이다.
- 가볍고 확장성이 좋으며 크로스 플랫폼이라는 장점이 있지만 완성도나 지원기능 측면에서 유료 IDE보다 상대적으로 부족해보인다는 단점이 있다.

#### 1-2-4. github.dev

- Github에서 제공하는 웹 기반 VS Code IDE
- VS Code의 장단점을 함께 공유한다고 보면 된다.
- 인터넷 접속이 가능하다면 군대 등의 특수 환경에서 웹기반 IDE로는 좋은 선택이라고 생각한다.

## 2. VS Code 다루기

### 2-1. 확장 설치하기

- VS Code는 오픈소스 기반이라 이에 대한 확장 기능들이 상당히 많다.
  - 언어에 대한 공식 지원, 혹은 사용자가 만든 지원들 뿐만 아니라 개발에 필요한 다양한 도구들도 있다.
  - [그만큼 정말 뻘짓같은 확장들도 꽤 있다.](https://www.youtube.com/watch?v=-5cSTqXGDUs)
- 왼쪽에 <img src = "https://github.com/Indigo-Coder-github/Python_Lecture/blob/2024-1/%EA%B8%B0%EC%B4%88%EB%B0%98/%EA%B8%B0%EC%B4%88%EB%B0%98%20Chap%201/%ED%99%95%EC%9E%A5.PNG">을 누르면(혹은 Ctrl+Shift+X) 상점처럼 확장이 열린다. 이 중에서 Microsoft에서 제공하는 Python을 설치한다.
  - 그 외 Don Jayamanne의 Python Extension Pack에서 Django와 Jinja(각각 Django와 Flask에서 필요하다.)를 제외하고 설치하는 것을 권장한다.
- 설치 시 기본 언어는 영어이다. 본인이 영어로 개발하는 습관을 들이고 싶다면 놔둬고 되고 한국어를 쓰고 싶다면 Microsoft에서 제공하는 Korean Language Pack for Visual Studio Code을 설치한다.

### 2-2. 무언가 실행하기

1. 파일-폴더 열기(혹은 Ctrl+K & Ctrl+O)를 통해 개발하려는 폴더 위치를 연다.
2. 파일-새 텍스트 파일(혹은 Ctrl+N)을 통해 언어 선택으로 Python을 선택하거나 저장(혹은 Ctrl+S)을 통해 .py의 형태로 파일을 저장하면 Python 코드로 인식한다.
3. 실행-디버깅없이 실행(혹은 Ctrl+F5)으로 디버깅하지 않고 실행할 수 있다.

#### 2-2-1. .py, .ipynb

- .py는 python 파일의 확장자이다.
- .ipynb는 Jupyter Notebook의 확장자이다.
  - Google colab에서도 지원되는 파일 확장자이다.
  - Python 파일과 다르게 Markdown과 python 코드의 혼용이 가능해 PPT 대용으로 괜찮으며 서버 개발 환경만 갖추고 있다면 어디서든 작업을 계속할 수 있다.
  - 출력 결과가 바로 나오는 것도 장점이다.
  - 다만 대부분의 코드는 배포 시 Python 파일로 배포되고 IDE보다 디버깅이 불편하다.
  - .ipynb는 json 형태로 작성된 파일이기 때문에 이를 .py로 변환하기 위해서 VS Code에서 [Jupyter 확장을 설치해야 한다.](https://stackoverflow.com/questions/64297272/best-way-to-convert-ipynb-to-py-in-vscode)

### 2-3. 디버깅

- VS Code에서 F5 단축키를 눌러 Python File을 선택하면 실행
- F11을 누르면 다음 줄로 이동하며 F5를 누르면 중단점에 다시 도달할 전까지 코드를 실행한다.
  - 중단점 없이 디버깅할 경우 오류가 난 지점에서 멈추며 오류가 없다면 프로그램을 정상적으로 종료한다.
- 오류의 원인을 찾지 못하거나 중요한 실행을 하기 전 단위 테스트를 할 때 매우 유용하다.
<img src = "https://github.com/Indigo-Coder-github/Python_Lecture/blob/2024-1/%EA%B8%B0%EC%B4%88%EB%B0%98/%EA%B8%B0%EC%B4%88%EB%B0%98%20Chap%201/%EB%94%94%EB%B2%84%EA%B9%85.png">

#### 2-3-1. 중단점

- line number 옆을 클릭해서 생성된 빨간 버튼
- 코드가 진행되다가 중단점이 있는 위치에서 멈추며 F11을 누르거나 F5를 누르면 해당 line이 실행된다.

#### 2-3-2. 변수

- 현재 실행되는 파일에서 사용하고 있는 변수
- Local은 지역변수, Global은 전역변수의 값을 보여준다.

#### 2-3-3. 조사식

- 현재 실행 파일에 대한 python 코드의 결과를 표시
- 예를 들어 조사식의 +버튼을 누르고 `print(i)`를 입력하면 콘솔 창에 현재 i값이 표시된다.
- 코드가 실행 중일 때 코드를 입력해 값을 조사할 수 있다.

#### 2-3-4. 호출스택

- 현재 스택 영역에 호출된 파일을 표시

## 3. Variable(변수)

- 값이 저장된 메모리 주소
  - 좀 더 쉽게 얘기하면 메모리(RAM)에서 값을 할당받는 (값이 저장되는) 공간
- 변수 이름은 반드시 문자로 시작해야 하며 특수 문자, 예약어를 제외한 문자로 작성해야 한다.
  - 한글도 가능하지만 권장하진 않는다.
  - 이미 선언한 함수나 변수의 이름을 재사용하면 이전의 선언 내용은 유지되지 않는다.
- python은 한 번에 복수의 변수를 선언할 수 있다.
- `del variable_name`을 통해 변수를 임의로 삭제할 수 있다.
- `variable_name = None`을 통해 값을 주지 않고 변수를 선언만 할 수 있다.
  - 변수는 존재하지만 아무 값도 없는 상태이며 NULL값을 가진다고 표현하기도 한다.

### 3-1. Coding Convention

- 특정 프로그래밍 언어 사용자들이 관습적으로 지키는 변수 명명 규칙
- Python도 커뮤니티 크기가 큰 만큼 PEP8의 Coding Convention 분량이 매우 크다.
  - 오히려 다른 언어에 의존하는 라이브러리는 이를 지키지 않는 경우도 허다해 API 문서를 읽기 어려운 경우도 있다.
- 아예 Coding Convention을 준수했는지 확인하는 [라이브러리](https://pypi.org/project/pep8-naming/)도 있다.
  - PyCharm의 경우 다른 IDE와 다르게 PEP8 준수 여부를 Warning으로 표시해주는 기능을 기본적으로 탑재한다.
- 아래는 많이 사용하는 Coding Convention의 일부이다.
  1. 클래스 이름은 CamelCase로 작성하되 내부 클래스 이름은 underscore를 앞에 붙인다.
  2. 함수명, 변수명은 소문자와 밑줄만을 이용해 작성한다.
  3. 상수명은 모듈 단위에서만 정의하고 대문자와 밑줄만을 이용해 작성한다.

## 4. Constant(상수)

- 첫 선언 이후 변하지 않는 값
  - `CONSTANT_NAME = "NAME"`형태로 선언한다.
  - Python 3.8 이상의 버전에서 `from typing import Final`을 통해 `CONSTANT_NAME: Final[int] = 1`로 선언할 순 있다.
- [하지만 Python에는 상수의 개념이 없다.](https://stackoverflow.com/questions/2682745/how-do-i-create-a-constant-in-python) 즉, 상수라고 선언한 변수의 값은 재할당할 수 있다.

## 5. 세미콜론, Indentation

- python은 indentation을 기준으로 줄을 구분
  - 즉, 줄 끝마다 세미콜론(;)을 붙일 필요가 없다.
  - 다만, 여러 줄로 쓸 코드를 한 줄로 작성하려면 세미콜론으로 구분해야 한다.
- 초창기에 Indentation을 공백 4칸을 기준으로 할지, tab 1칸으로 할지 많은 의견이 오고 갔으나 최종적으론 공백 4칸이 되었다.
  - IDE에서 탭으로 indentation을 하면 공백 4칸으로 보정해준다.
  - indentation을 정확히 지키지 못할 시 IndentationError가 발생한다.
- 같은 indentation에 있는 코드를 하나의 코드 블록에 속한다고 한다.
  - 다른 언어의 경우 일반적으로 중괄호로 나타낸다.

## 6. Console I/O

### 6-1. Console Input

- 콘솔 창에서 키보드의 입력 값을 전달받는 방식
- `input()`함수를 통해 입력을 받는다.
  - 코딩 테스트나 임베디드 등을 위해 표준 입력이 필요하다면 `sys.stdin.readline()`을 사용하며 [코딩 테스트 등의 여러 입력 케이스에 대해서는 해당 링크에 정리되어 있다.](https://velog.io/@yeseolee/Python-%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EC%9E%85%EB%A0%A5-%EC%A0%95%EB%A6%ACsys.stdin.readline)
- `input()`함수의 반환 타입은 문자열이기 때문에 다른 자료형으로 사용하고자 한다면 형 변환을 거쳐줘야 한다.

### 6-2. Console Output

- 출력 값을 콘솔 창에 띄워 표시하는 방식
- `print(params, sep=" ", end="\n")`함수를 통해 출력한다.
  - sep는 구분자로 여러 값 사이에 sep 값을 출력한다. default는 공백이다.
  - end는 맨 끝에 붙이는 값으로 출력이 다 끝나고 end 값을 출력한다. default는 줄바꿈이다.
  - 제어문자를 통해 [줄바꿈, 띄어쓰기, tab 등을 조절할 수 있다.](https://en.wikipedia.org/wiki/Control_character#In_ASCII)

#### 6-2-1. format

- 문자열 formatting을 지원하는 함수
  - format 함수에 전달되는 값은 출력할 수 있는 모든 자료형이라면 가능하다.
- python도 처음에는 다른 언어처럼 서식 지정자를(`%d`, `%s` 등) 지원했었으나 2.6부터 format 함수를, 3.6부터 f-string을 지원하기 시작했다.
  - 현재도 이 세 가지 방법은 모두 사용할 수 있지만 서식 지정자는 Pythonic한 방법이 아닌 것으로 여겨져 많이 사장됐다.
  - [전반적으로 f-string을 권장하지만 하위버전의 호환성 등을 고려하면](https://stackoverflow.com/questions/5082452/string-formatting-vs-format-vs-f-string-literal) [format 함수도 여전히 기용할 여지가 많다.](https://velog.io/@keywookim/%ED%8C%8C%EC%9D%B4%EC%8D%AC-f-string-formatting%EC%9D%80-%EB%AC%B4%EC%A0%81%EC%9D%BC%EA%B9%8C)
  - 좀 더 다양한 활용법은 위의 링크와 더불어 [여기서도](https://dojang.io/mod/page/view.php?id=2300) 확인할 수 있다. 해당 강의에서 format 함수의 복잡한 사용은 거의 없다.
- string 자료형의 메서드이기 때문에 출력뿐 아니라 문자열을 다루는 상황이라면 언제든 사용할 수 있다.

## 7. File I/O

### 7-1. File Input

- 파일에 있는 값을 읽어들여 입력하는 방식
- `open()`함수를 통해 파일을 변수에 저장하고 그 변수를 `read()`함수로 내용을 읽어들인다. 이후 `close()`함수로 안전하게 파일 읽기를 종료한다.
- `open()`함수의 대표적인 파라미터로는 file, mode, encoding이 있다.
  - file은 파일 경로이다. 필수적이며 첫 번째로 오는 인자이다.
    - 절대 경로로 지정해주지 않는다면 실행파일과 같은 위치부터 파일을 탐색한다.(상대경로)
  - mode는 파일을 어떤 방식으로 접근할 지를 나타낸다. "r"은 읽기 모드, "w"는 쓰기 모드를 나타낸다. file 파라미터 다음에 왔다면 mode라는 이름을 명시하지 않아도 된다.
    - [다른 더 많은 모드도 있다.](https://dojang.io/mod/page/view.php?id=2327)
  - encoding은 파일을 읽고 쓰는 규약이다. Python은 UTF-8을 사용하며 그 외 cp949, euc-kr 등이 있다.
- `read()`와 `readlines()`의 요소에는 개행문자(`\n`) 등의 제어 문자가 모두 저장된다.
- `readline()`함수는 한 줄만 읽어 반환한다. 때문에 반복문을 사용해야 한다.

#### 7-1-1. with

- `__enter__()`와 `__exit__()`함수를 사용하여 정의된 context manager에서 사용할 수 있는 구문
  - `with class_name() as another_name`형태로 사용한다.
- with 구문으로 파일을 불러올 때 `__enter__()`함수로 파일에 진입하고 with 구문 내부가 끝나면 `__exit__()`함수로 파일을 닫는 내부적 절차가 실행된다.
  - 덕분에 `close()` 함수를 사용하지 않아도 자동으로 파일 읽기를 종료하는 동시에 코드 줄 수를 줄일 수 있다.

### 7-2. File Output

- 출력 값을 파일에 저장하여 출력하는 방식
- 파일을 읽을 때와 마찬가지로 `open()` 함수를 사용하지만 쓰기 모드(w)로 설정하며 `write()` 함수를 통해 값을 쓴다.
  - `write(string)`함수는 string을 파일에 쓴다. 개행문자(`\n`)가 없으면 줄바꿈이 일어나지 않는다.
  - `writelines(list)`함수는 list의 요소를 모두 파일에 쓴다. write 함수와 마찬가지로 개행문자(`\n`)가 없으면 줄바꿈이 일어나지 않는다.

## 8. Module(모듈)

- 정의문과 구문을 갖고 있는 Python 파일
  - 이 모듈의 집합체를 package라고 한다.
  - package와 모듈의 집합체를 라이브러리라고 한다.
- Python은 파일 이름 자체가 모듈 이름이다.
- `from`과 `import`를 통해 모듈을 호출한다.
  - 내가 만든 파일을 모듈로 `import`하려면 실행 파일과 모듈 파일이 같은 경로 상에 위치해야 한다.
- `with`문에서 `as`를 사용하는 것처럼 모듈의 호출도 `as`를 사용해 별칭으로 호출할 수 있다.
- 모듈을 순환 참조할 경우 오류를 일으킨다.
  - `a.py`에서 `b.py`를 `import`하고 `b.py`에서 `a.py`를 `import`할 수 없다.
  - 여러 파일에 프로그래밍 하는 것이 익숙치 않다면 순환 참조를 일으키는 실수를 범할 수 있어 주의가 필요하다.

## 9. Comment(주석)

- 코드에 대한 보충설명
- `#`으로 시작하며 여러 줄을 한 번에 묶는 방식은 지원하지 않는다.
  - 간혹 '''으로 묶는 것이 가능하다는 설명이 보이지만 해당 기능은 엄밀히 말하면 Docstring으로 코드 전반을 설명하는 기능이다.
- 어느 위치에 쓰든 무관하며 주석 처리한 코드는 실행되지 않는다.
- 한글로도 쓸 수 있으나 [PEP8에 코드 주석에 대한 가이드라인이 준수하는 것이 좋다.](https://peps.python.org/pep-0008/#comments)
- **주석을 작성하는 것은 귀찮지만 나중에 자신이 작성한 코드조차 못알아보기 때문에 주석을 다는 습관을 들이는 것은 필수다.**

## 10. Exception Handling(예외 처리)

- 코드를 실행하다가 발생하는 오류가 예외(Exception)

### 10-1. try, except

- `try: code except Exception_Name: code`
  - code에 실행하고자 하는 코드를, Exception_Name에 검출하려는 오류를, Exception_Name에 해당하는 코드 블록에 오류가 발생했을 때 실행할 코드를 작성한다.
- Exception_Name은 선택사항이지만 명시하지 않을 경우 모든 예외에 대해 `except`문이 처리된다.
  - 다시 말해 어떤 예외가 발생했는지 정확히 파악할 수 없다.
  - PEP8에서도 `except`는 `except BaseException`과 동치라 키보드 입력이나 시스템 강제종료 등의 예외도 잡아낸다고 한다.
    - 특히 loop 안에서 `try except`가 작동하고 있다면 더욱 파악하기 어렵다고 한다.
    - 이를 위해 제안 사항은 아래와 같다.
      - 예외 처리를 출력하고자 한다면 사용자는 오류의 발생을 적어도 파악하고 있어야 함
      - 이를 깔끔하게 적고 싶다면 `raise`, `finally`문을 사용할 것
      - 처리할 예외 종류를 명확히 할 것
      - 추가적으로, 코드의 가독성을 위해 절대적으로 필요한 양의 코드만 작성할 것
    - 그래도 전체 예외 처리를 하고자 한다면 `except Exception`으로 명시할 것을 권장하고 있다.
- 예외 처리는 먼저 일어난 것부터, [더 상위에 있는 계층부터](https://docs.python.org/3/library/exceptions.html#exception-hierarchy) 하나만 처리한다.

### 10-2. finally, else

- `else`는 예외가 발생하지 않았을 때, `finally`는 예외 발생 여부와 무관하게 실행하는 코드이다.
