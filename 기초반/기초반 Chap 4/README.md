# 기초반 4차시

## TOC

- [1. Function(함수)](#1-function함수)
- [1. Console I/O](#1-console-io)
  - [1-1. Console Input](#1-1-console-input)
  - [1-2. Console Output](#1-2-console-output)
    - [1-2-1. format](#1-2-1-format)
- [2. File I/O](#2-file-io)
  - [2-1. File Input](#2-1-file-input)
    - [2-1-1. with](#2-1-1-with)
  - [2-2. File Output](#2-2-file-output)
- [3. Module(모듈)](#3-module모듈)

## 1. Function(함수)

- 반복적으로 사용하는 코드에 이름을 붙여 추상적으로 사용하도록 한 것
- `def function_name(parameters): code_block (with return)`로 선언하며 `function_name(parameters)`로 사용한다.
  - parameter는 매개변수라고 하며 argument와 인자라고 한다.
    - [parameter는 선언할 때 사용하는 변수이고 argument는 함수를 호출할 때 parameter에 전달하는 데이터이다.](https://stackoverflow.com/questions/156767/whats-the-difference-between-an-argument-and-a-parameter) 하지만 두 단어가 일반적으로 혼용된다.
    - 함수를 선언할 때 parameter의 초기값을 선언할 수 있으며 함수를 호출할 때 argument를 전달하지 않았다면 초기값을 값으로 가진다.
  - return은 선택 사항이다.
    - Python에서 함수는 복수의 값을 반환할 수 있으며 이 경우 tuple 형태로 반환한다.
    - 반환하는 값의 수와 이를 받는 변수의 수가 일치하면 unpacking이 이뤄진다. 일치하지 않으면 예외가 발생한다.
- `function_name(parameter_name=parameter_value)`로 호출한다.
- 최종적으로 함수는 `def function_name(args, args=default, *args, **kwargs)`의 형태로 parameter를 가진다.

## 2. Console I/O

### 2-1. Console Input

- 콘솔 창에서 키보드의 입력 값을 전달받는 방식
- `input()`함수를 통해 입력을 받는다.
  - 코딩 테스트나 임베디드 등을 위해 표준 입력이 필요하다면 `sys.stdin.readline()`을 사용하며 [코딩 테스트 등의 여러 입력 케이스에 대해서는 해당 링크에 정리되어 있다.](https://velog.io/@yeseolee/Python-%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EC%9E%85%EB%A0%A5-%EC%A0%95%EB%A6%ACsys.stdin.readline)
- `input()`함수의 반환 타입은 문자열이기 때문에 다른 자료형으로 사용하고자 한다면 형 변환을 거쳐줘야 한다.

### 2-2. Console Output

- 출력 값을 콘솔 창에 띄워 표시하는 방식
- `print(params, sep=" ", end="\n")`함수를 통해 출력한다.
  - sep는 구분자로 여러 값 사이에 sep 값을 출력한다. default는 공백이다.
  - end는 맨 끝에 붙이는 값으로 출력이 다 끝나고 end 값을 출력한다. default는 줄바꿈이다.
  - 제어문자를 통해 [줄바꿈, 띄어쓰기, tab 등을 조절할 수 있다.](https://en.wikipedia.org/wiki/Control_character#In_ASCII)

#### 2-2-1. format

- 문자열 formatting을 지원하는 함수
  - format 함수에 전달되는 값은 출력할 수 있는 모든 자료형이라면 가능하다.
- python도 처음에는 다른 언어처럼 서식 지정자를(`%d`, `%s` 등) 지원했었으나 2.6부터 format 함수를, 3.6부터 f-string을 지원하기 시작했다.
  - 현재도 이 세 가지 방법은 모두 사용할 수 있지만 서식 지정자는 Pythonic한 방법이 아닌 것으로 여겨져 많이 사장됐다.
  - [전반적으로 f-string을 권장하지만 하위버전의 호환성 등을 고려하면](https://stackoverflow.com/questions/5082452/string-formatting-vs-format-vs-f-string-literal) [format 함수도 여전히 기용할 여지가 많다.](https://velog.io/@keywookim/%ED%8C%8C%EC%9D%B4%EC%8D%AC-f-string-formatting%EC%9D%80-%EB%AC%B4%EC%A0%81%EC%9D%BC%EA%B9%8C)
  - 좀 더 다양한 활용법은 위의 링크와 더불어 [여기서도](https://dojang.io/mod/page/view.php?id=2300) 확인할 수 있다. 해당 강의에서 format 함수의 복잡한 사용은 거의 없다.
- string 자료형의 메서드이기 때문에 출력뿐 아니라 문자열을 다루는 상황이라면 언제든 사용할 수 있다.

## 3. File I/O

### 3-1. File Input

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

#### 3-1-1. with

- `__enter__()`와 `__exit__()`함수를 사용하여 정의된 context manager에서 사용할 수 있는 구문
  - `with class_name() as another_name`형태로 사용한다.
- with 구문으로 파일을 불러올 때 `__enter__()`함수로 파일에 진입하고 with 구문 내부가 끝나면 `__exit__()`함수로 파일을 닫는 내부적 절차가 실행된다.
  - 덕분에 `close()` 함수를 사용하지 않아도 자동으로 파일 읽기를 종료하는 동시에 코드 줄 수를 줄일 수 있다.

### 3-2. File Output

- 출력 값을 파일에 저장하여 출력하는 방식
- 파일을 읽을 때와 마찬가지로 `open()` 함수를 사용하지만 쓰기 모드(w)로 설정하며 `write()` 함수를 통해 값을 쓴다.
  - `write(string)`함수는 string을 파일에 쓴다. 개행문자(`\n`)가 없으면 줄바꿈이 일어나지 않는다.
  - `writelines(list)`함수는 list의 요소를 모두 파일에 쓴다. write 함수와 마찬가지로 개행문자(`\n`)가 없으면 줄바꿈이 일어나지 않는다.

## 4. Module(모듈)

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