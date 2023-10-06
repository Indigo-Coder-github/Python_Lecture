# 세미콜론, Indentation
- python은 indentation을 기준으로 줄을 구분
	- 즉, 줄 끝마다 세미콜론(;)을 붙일 필요가 없다.
	- 다만, 한 줄에 여러 코드를 붙이고자 하면 세미콜론으로 구분해야 한다.
- 초창기에 Indentation을 공백 4칸을 기준으로 할지, tab 1칸으로 할지 많은 의견이 오고 갔으나 최종적으론 공백 4칸이 되었다.
	- IDE에서 탭으로 indentation을 하면 공백 4칸으로 보정해준다.
	- indentation을 정확히 지키지 못할 시 IndentationError가 발생한다.
- if, for문 등의 내부 코드를 다른 언어에서는 중괄호로 묶었다면 Python에서는 쌍점(:)이후 다음 줄에 indentation을 주고 시작한다.
	- 이렇게 같은 indentation은 하나의 코드 블록에 속하며 다른 언어의 경우 일반적으로 중괄호로 묶이는 것과 대조적이다.
```python
print("first")
print("second")
#위와 동일한 출력
print("first"); print("second")
if True:
print(True)
##Output:IndentationError
##대부분의 IDE에서는 쌍점 이후 indentation을 보정
```
# Comment(주석)
- 코드에 대한 보충설명
- `#`으로 시작하며 여러 줄을 한 번에 묶는 방식은 지원하지 않는다.
	- 간혹 '''으로 묶는 것이 가능하다는 설명이 보이지만 해당 기능은 엄밀히 말하면 Docstring으로 코드 전반을 설명하는 기능이다.
- 어느 위치에 쓰든 무관하며 주석 처리한 코드는 실행하지 않는다.
- 한글로도 쓸 수 있으나 [PEP8에 코드 주석에 대한 가이드라인이 제공된다.](https://peps.python.org/pep-0008/#comments)
- **주석을 작성하는 것은 귀찮지만 나중에 자신이 작성한 코드조차 못알아보기 때문에 주석을 다는 습관을 들이는 것은 필수다.**
```python
#This is start of program
#print("a")
print("b")#This is print
#This is end of program
```
# Variable(변수)
- 값을 저장한 메모리 주소
	- 좀 더 쉽게 얘기하면 값을 할당받는 (값이 저장되는) 공간
- 변수 이름은 반드시 문자로 시작해야 하며 특수 문자, 예약어를 제외한 영어 대소문자, 숫자, underscore(`_`)를 사용해야 한다.
	- Python 내장 함수를 변수 명으로 사용하면 해당 함수가 무력화 된다.
- python은 변수의 수만큼 값의 수를 선언할 수 있다.
- `del variable_name`을 통해 변수를 삭제할 수 있다.
- `variable_name = None`을 통해 빈 변수를 만들 수 있다.
	- 변수는 존재하지만 아무 값도 없는 상태이며 NULL값을 가진다고 표현하기도 한다.
```python
#type(변수명)은 변수의 자료형을 알려주는 함수
print(type(zip()))
#Output:<class 'zip'>
zip = 1
zip()
#Output:TypeError
x, y, z = 1, 2, 3
print(x, y, z)
#Output:1 2 3
#이를 응용해 변수의 값을 쉽게 바꿀 수 있음
x, y = y, x
print(x, y)
#Output:2 1
del z
print(z)
#Output:NameError
```
## Constant(상수)
- 첫 선언 이후 변하지 않는 값
	- [Python에서는 상수를 선언할 수 없다.](https://stackoverflow.com/questions/2682745/how-do-i-create-a-constant-in-python) 상수라고 선언한 변수의 값은 재할당할 수 있다.
- `CONSTANT_NAME = "NAME"`형태로 상수라는 것을 표시할 순 있으나 그 값은 바꿀 수 있다.
	- Python 3.8 이상의 버전에서 `from typing import Final`을 통해 `CONSTANT_NAME: Final[int] = 1`로 선언할 순 있지만 마찬가지로 그 값은 바꿀 수 있다.
## Coding Convention
- 특정 프로그래밍 언어 사용자들이 관습적으로 지키는 변수 명명 규칙
- Python도 커뮤니티 크기가 큰 만큼 PEP8에도 어마한 양의 규칙을 명명했다.
	- 아예 Coding Convention을 준수했는지 확인하는 [라이브러리](https://pypi.org/project/pep8-naming/)도 있다.
	- PyCharm의 경우 PEP8 준수 여부를 Warning으로 표시해주기 때문에 변수 명명도 잘 됐는지 확인할 수 있다.
- 아래는 Coding Convention의 일부이다.
	1. 클래스 이름은 CamelCase로 작성한다.
		1. 내부 클래스 이름은 underscore를 앞에 붙인다.
	2. 함수명, 변수명은 소문자와 밑줄만을 이용해 작성한다.
	3. 상수명은 모듈 단위에서만 정의하고 대문자와 밑줄만을 이용해 작성한다.
# Console I/O
## Console Input
- 콘솔 창에서 키보드의 입력 값을 전달하는 입력 방식
- [[초급반 1주차#^3fac27|1주차에서 소개한 input함수를 사용한다.]]
```python
print(input())
#Output:입력한 값
#입력한 값을 변수에 저장
x = input()
```
- `input()`함수의 반환 타입은 문자열이기 때문에 다른 자료형으로 사용하고자 한다면 형 변환을 거쳐줘야 한다.
- `split()`함수는 parameter로 주는 값을 기준으로 문자열을 분할하는 함수이다.
	- default 값은 " "(공백)이다.
```python
#입력 값에 반점이 있다면 이를 기준으로 분할
x, y = input().split(",")
x, y = int(x), int(y)
print(x+y)
#Output:x+y 값
```
## Console Output
- 출력 값을 콘솔 창에 띄워 표시하는 출력 방식
- [[초급반 1주차#^5a5e69|1주차에서 소개한 print함수를 사용한다.]]
# File I/O
## File Input
- 파일에 있는 값을 전달하는 입력 방식
- open함수를 통해 파일 객체를 변수에 저장하여 사용한다.
	- 이때 파일 경로는 절대 경로로 지정해주지 않는다면 기본적으로 Python 실행 코드와 같은 위치에 있다고 간주한다.
- open함수의 대표적인 파라미터는 file, mode, encoding이 있다.
	- file 파라미터는 파일 경로로써 필수이며 첫 번째로 오는 인자이다.
	- mode 파라미터는 파일을 어떤 방식으로 접근할 지를 나타낸다.  "r"은 읽기 모드, "w"는 쓰기 모드를 나타낸다. file 파라미터 다음에 왔다면 mode라는 이름을 명시하지 않아도 된다.
		- [더 많은 모드도 있다.](https://dojang.io/mod/page/view.php?id=2327)
	- encoding 파라미터는 파일을 읽고 쓰는 규약으로 python은 UTF-8을 사용하며 그 외 cp949, euc-kr 등이 있다.
```python
#파일 확장자는 쓸 수만 있다면 어떤 것이든 가능
file = open("data.txt", "r", encoding="UTF-8")
my_text = file.read()
print(my_text)
#open함수를 사용했다면 반드시 close함수로 닫아야 함
#하지 않을 경우 메모리 누수가 발생
file.close()
```
- read함수는 텍스트를 통째로 읽어오기 때문에 줄바꿈은 개행문자( `\n`)로 처리된다.
	- 줄 단위로 처리하고 싶다면 readlines함수, readline함수를 사용해야 한다.
	- `readlines()` 함수는 각 줄을 요소로 하는 리스트를 반환한다.
	- `readline()`함수는 한 줄만 읽어 문자열을 반환한다. 때문에 반복문을 사용해야 한다.
```python
file = open("data.txt", "r", encoding="UTF-8")
my_text = file.readlines()
#Output:[line 1, line 2, line 3, ...]
#rstrip함수는 string의 함수로써 가장 오른쪽에 있는 문자를 제거함
for line in file: print(line.rstrip())
#Output:line 1
#		line 2
#		line 3
#		...
file.close()
```
### with
- `__enter__`와 `__exit__`함수를 사용하여 정의된 context manager에서 사용할 수 있는 구문
- `with class_name() as another_name`형태로 사용한다.
- with 구문으로 파일을 불러올 때 내부적으로 `__enter__`함수로 파일에 진입하고 with 구문 내부가 끝나면 `__exit__`함수로 파일을 닫는다.
	- 덕분에 close 함수를 사용하지 않아도 자동으로 메모리를 반납하는 동시에 코드 줄 수가 줄어든다.
```python
with open("data.txt", "r", encoding="UTF-8") as f:
    f.read()
```
## File Output
- 출력 값을 파일에 저장하는 출력 방식
- 파일을 읽을 때와 마찬가지로 open 함수를 사용하지만 쓰기 모드로 설정하며 write 함수를 통해 값을 쓴다.
	- `write(string)`함수는 string을 파일에 쓴다. 개행문자(`\n`)가 없으면 줄바꿈이 일어나지 않는다.
	- `writelines(list)`함수는 list의 string을 모두 읽어 파일에 쓴다. write 함수와 마찬가지로 개행문자(`\n`)가 없으면 줄바꿈이 일어나지 않는다.
```python
#"w"mode는 파일 전체를 덮어쓰기 때문에 기존 내용을 유지하려면 "a"로 설정
#"a"mode는 마지막 줄을 줄바꿈한 위치에서부터 쓰기 시작
string = "I have a pen. I have a pineapple."
list_string = ["pen", "pineapple\n", "apple", "pen"]
with open("data.txt", "w", encoding="UTF-8") as f:
    f.write(string)
    #Output:"I have a pen. I have a pineapple."
with open("data.txt", "w", encoding="UTF-8") as f:
    for line in string.split(" "): f.write(line+"\n")
    #Output:I
	#	    have
	#	    a
	#	    pen.
	#	    I
	#	    have
	#	    a
	#	    pineapple.
with open("data.txt", "w", encoding="UTF-8") as f:
	f.writelines(list_string)
	#Output:penpineapple
	#		applepen
```
# Exception Handling(예외 처리)
 - 코드 실행 시 발생한 오류가 예외(Exception)
## try, except
 - `try: code except (Exception_Name): code`
```python
try: #예외 발생을 검사할 코드를 try문에 작성
    x = input("젯수: ")
    print(10/x)
except: #예외 처리시 실행할 코드를 except문에 작성
    print("Exception raised")
#Input:0 Output:Exception raised

try:
    x = int(input("젯수: "))
    print(10/x)
except ZeroDivisionError as e: #0으로 나누기 예외만 처리함
    print("Exception raised because of ", e)
#Output:Exception raised because of division by zero
#원래는 ZeroDivisionError:division by zero가 출력되지만 as라는 구문을 통해 메시지만 출력토록 함
except ValueError: #숫자가 아닌 값에 대한 예외만 처리함
	print("Please input right value")
```
 - Exception_Name은 선택사항이지만 명시하지 않을 경우 모든 예외에 대해 `except`문을 처리한다.
	 - 다시 말해 어떤 예외가 발생했는지 정확히 알기 어렵다.
		 - PEP8에서도 `except`는 `except BaseException`과 같은 역할이라 키보드 입력이나 시스템 강제종료 등도 잡아내서 예외를 파악하기 어렵다고 설명한다.
			 - 특히 loop 안에서 `try except`가 작동하고 있다면 더욱 파악하기 어렵다고 한다.
		 - 이를 위해 제안 사항은 아래와 같다.
			 - 예외 처리를 출력하고자 한다면 사용자는 오류의 발생을 적어도 파악하고 있어야 함
			 - 이를 깔끔하게 적고 싶다면 `raise`, `finally`문을 사용할 것
			 - 명확한 예외 처리 종류를 명시할 것
			 - 추가적으로, 코드의 가독성을 위해 절대적으로 필요한 양의 코드만 작성할 것
		 - 그래도 전체 예외 처리를 하고자 한다면 `except Exception`을 사용할 것을 권장하고 있다.
 - 예외 처리는 먼저 일어난 것부터, [더 상위에 있는 계층부터](https://docs.python.org/3/library/exceptions.html#exception-hierarchy) 하나만 처리한다.
## finally, else
 - `else`는 예외가 발생하지 않았을 때, `finally`는 예외 발생 여부와 무관하게 실행하는 코드이다.
``` python
try:
    x = int(input("젯수: "))
    print(10/x)
except ZeroDivisionError as e: #0으로 나누기 예외만 처리함
    print("Exception raised because of ", e)
else:
	print("{} can divide any number.", x)
finally:
	print("{} is number.", x)
```
# 연산자
 - 좀 더 자세한 사항은 숫자 자료형에서 나오지만 Python에서 지원하는 계산 연산자는 사칙연산과 ** (제곱), //(몫), %(나머지)이며 그 외에 비교 연산, 할당 연산, 논리 연산, 비트 연산, 멤버쉽 연산, Identity 연산, 괄호 등을 지원한다.
```python
print(1.0+0.5)
print(1.0-0.5)
print(1.0/0.5)
print(1.0*0.5)
print(1.0//0.5)
print(1.0%0.5)
print(1.0**0.5)
```