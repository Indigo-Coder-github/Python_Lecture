# 기초반 2차시

## TOC

- [1. Variable(변수)](#1-variable변수)
  - [1-1. Coding Convention](#1-1-coding-convention)
- [2. Constant(상수)](#2-constant상수)
- [3. 세미콜론, Indentation](#3-세미콜론-indentation)
- [4. Comment(주석)](#4-comment주석)
- [5. Numeric Type](#5-numeric-type)
  - [5-1. int](#5-1-int)
  - [5-2. float](#5-2-float)
  - [5-3. complex](#5-3-complex)
  - [5-4. 연산자](#5-4-연산자)
    - [5-4-1. int, float 연산자](#5-4-1-int-float-연산자)
    - [5-4-2. 비트 연산자](#5-4-2-비트-연산자)
- [6. Boolean Type](#6-boolean-type)
  - [6-1. Boolean 연산자(논리 연산자)](#6-1-boolean-연산자논리-연산자)
  - [6-2. 비교 연산자](#6-2-비교-연산자)
- [7. Condition Statement (조건문)](#7-condition-statement-조건문)

## 1. Variable(변수)

- 값이 저장된 메모리 주소
  - 좀 더 쉽게 얘기하면 메모리(RAM)에서 값을 할당받는 (값이 저장되는) 공간
- 변수 이름은 반드시 문자로 시작해야 하며 특수 문자, 예약어를 제외한 문자로 작성해야 한다.
  - 한글도 가능하지만 권장하진 않는다.
  - 이미 선언한 함수나 변수의 이름을 재사용하면 이전의 선언 내용은 유지되지 않는다.
- python은 한 번에 복수의 변수를 선언할 수 있다.
- `del variable_name`을 통해 변수를 임의로 삭제할 수 있다.
- `variable_name = None`을 통해 값을 주지 않고 변수를 선언만 할 수 있다.
  - 변수는 존재하지만 아무 값도 없는 상태이며 NULL값을 가진다고 표현하기도 한다.

```python
var = 1
변수 = None
print(var)
del var
print(var)
```

### 1-1. Coding Convention

- 특정 프로그래밍 언어 사용자들이 관습적으로 지키는 변수 명명 규칙
- Python도 커뮤니티 크기가 큰 만큼 PEP8의 Coding Convention 분량이 매우 크다.
  - 오히려 다른 언어에 의존하는 라이브러리는 이를 지키지 않는 경우도 허다해 API 문서를 읽기 어려운 경우도 있다.
- 아예 Coding Convention을 준수했는지 확인하는 [라이브러리](https://pypi.org/project/pep8-naming/)도 있다.
  - PyCharm의 경우 다른 IDE와 다르게 PEP8 준수 여부를 Warning으로 표시해주는 기능을 기본적으로 탑재한다.
- 아래는 많이 사용하는 Coding Convention의 일부이다.
  1. 클래스 이름은 CamelCase로 작성하되 내부 클래스 이름은 underscore를 앞에 붙인다.
  2. 함수명, 변수명은 소문자와 밑줄만을 이용해 작성한다.
  3. 상수명은 모듈 단위에서만 정의하고 대문자와 밑줄만을 이용해 작성한다.

```python
class ExampleClass(): pass
def example_function(): pass
example_variable = None
EXAMPLE_CONSTANT = None
```

## 2. Constant(상수)

- 첫 선언 이후 변하지 않는 값
  - `CONSTANT_NAME = "NAME"`형태로 선언한다.
  - Python 3.8 이상의 버전에서 `from typing import Final`을 통해 `CONSTANT_NAME: Final[int] = 1`로 선언할 순 있다.
- [하지만 Python에는 상수의 개념이 없다.](https://stackoverflow.com/questions/2682745/how-do-i-create-a-constant-in-python) 즉, 상수라고 선언한 변수의 값은 재할당할 수 있다.

```python
PI = 3.14
print("π is {}".format(PI))
PI = 1.141
print("Is π {}?".format(PI))
```

## 3. 세미콜론, Indentation

- python은 indentation을 기준으로 줄을 구분
  - 즉, 줄 끝마다 세미콜론(;)을 붙일 필요가 없다.
  - 다만, 여러 줄로 쓸 코드를 한 줄로 작성하려면 세미콜론으로 구분해야 한다.
- 초창기에 Indentation을 공백 4칸을 기준으로 할지, tab 1칸으로 할지 많은 의견이 오고 갔으나 최종적으론 공백 4칸이 되었다.
  - IDE에서 탭으로 indentation을 하면 공백 4칸으로 보정해준다.
  - indentation을 정확히 지키지 못할 시 IndentationError가 발생한다.
- 같은 indentation에 있는 코드를 하나의 코드 블록에 속한다고 한다.
  - 다른 언어의 경우 일반적으로 중괄호로 나타낸다.

## 4. Comment(주석)

- 코드에 대한 보충설명
- `#`으로 시작하며 여러 줄을 한 번에 묶는 방식은 지원하지 않는다.
  - 간혹 '''으로 묶는 것이 가능하다는 설명이 보이지만 해당 기능은 엄밀히 말하면 Docstring으로 코드 전반을 설명하는 기능이다.
- 어느 위치에 쓰든 무관하며 주석 처리한 코드는 실행되지 않는다.
- 한글로도 쓸 수 있으나 [PEP8에 코드 주석에 대한 가이드라인이 준수하는 것이 좋다.](https://peps.python.org/pep-0008/#comments)
- **주석을 작성하는 것은 귀찮지만 나중에 자신이 작성한 코드조차 못알아보기 때문에 주석을 다는 습관을 들이는 것은 필수다.**

```python
#print("a")
print("b")
```

## 5. Numeric Type

### 5-1. int

- `int(x, base=10)`생성자를 통해 int형으로 바꿀 수 있음
- 크기 제한이 없다.

### 5-2. float

- `float(x=0.0)`생성자를 통해 float형으로 바꿀 수 있음
- C언어의 double형에 해당하는 정확도를 가진다.

### 5-3. complex

- `complex(real=0, imag=0)`이나 `complex(string)`생성자를 통해 complex형으로 바꿀 수 있음
- 실수부와 허수부 모두 부동 소수점 방식을 사용한다.
  - 실수부는 `z.real`로, 허수부는 `z.imag`로 추출하며 실수로 표기된다.

```python
print(int(10.0))
print(int("1010", base=2))
print(float(10))
print(complex(10, 10))
print(complex("10+10j"))
print(complex("10+10j").real, complex("10+10j").imag)

```

### 5-4. 연산자

- 연산자 우선순위는 [해당 링크를 따른다.](https://docs.python.org/3/reference/expressions.html#operator-summary)

|연산자|결과|비고|
|:-:|:-:|:-:|
|`x+y`|더하기||
|`x-y`|빼기||
|`x*y`|곱하기||
|`x/y`|나누기||
|`x//y`|몫|x, y 모두 정수가 아니라면 반환값은 항상 실수</br>complex는 지원하지 않음|
|`x%y`|나머지|complex는 지원하지 않음|
|`-x`|부정||
|`+x`|변하지 않음||
|`abs(x)`|절댓값||
|`divmod(x, y)`|몫, 나머지쌍|complex는 지원하지 않음|
|`pow(x, y, mod=None)`|x의 y제곱|mod에 파라미터를 입력하면 나머지 반환</br>0의 0제곱은 1로 정의함|
|`x**y`|x의 y제곱|0의 0제곱은 1로 정의함|

```python
print(10+10)
print(10-10)
print(10*10)
print(10/10)
print(10//10)
print(10%10)
print(10**10)
print(-10)
print(+10)
print(abs(-10))
print(divmod(10, 10))
print(pow(10, 10))
print(pow(10, 10, 10))
```

#### 5-4-1. int, float 연산자

- 더 많은 함수는 [math](https://docs.python.org/3/library/math.html#module-math) 모듈과 [cmath](https://docs.python.org/3/library/cmath.html#module-cmath)모듈에서 정의하고 있음

|연산자|결과|
|:-:|:-:|
|`math.trunc(x)`|정수부 반환|
|`round(x, n)`|소수 n번째 자릿수까지 표기되도록 반올림|
|`math.floor(x)`|x이하의 가장 큰 정수 반환|
|`math.ceil(x)`|x이상의 가장 작은 정수 반환|

```python
import math

print(math.trunc(10.1010101))
print(round(10.1010101, 5))
print(math.floor(10.1010101))
print(math.ceil(10.1010101))
```

#### 5-4-2. 비트 연산자

- 정수가 주어지면 해당 정수의 모든 비트 값에 대한 연산을 수행

|연산자|결과|비고|
|:-:|:-:|:-:|
|`x\|y`|x or y 비트연산||
|`x^y`|x xor y 비트연산||
|`x&y`|x and y 비트연산||
|`x<<n`|왼쪽으로 n비트만큼 shift|n은 음수값을 허용하지 않음|
|`x>>n`|오른쪽으로 n비트만큼 shift|n은 음수값을 허용하지 않음|
|`~x`|비트를 반전||

```python
# 10진수인 1010은 2진수로 1111110010, 1000은 2진수로 1111101000
print(1010|1000)
# 1111110010 | 1111101000 = 1111111010 = 1018
print(1010&1000)
# 1111110010 & 1111101000 = 1111100000 = 992
print(1010^1000)
# 1111110010 ^ 1111101000 = 0000011010 = 26
print(~1010)
# ~1111110010  = -1011
print(1010<<2)
# 1111110010 << 2 = 111111001000 = 4040
print(1010>>2)
# 1111110010 >> 2 = 11111100 = 252
```

## 6. Boolean Type

- True, False라는 두 개의 상수로 구성된 타입
- 내장 함수 `bool(value)`를 사용하면 value의 Boolean 타입을 반환해준다.
  - `None`, `False`, `0`, `0.0`, `0j`, `''`, `()`, `[]`, `{}`, `set()`, `range(0)`은 False로, 나머지는 True로 반환한다.
- int형의 하위타입이기 때문에 False와 True가 각각 0과 1로 간주될 수 있지만 Boolean Type을 int Type 처럼 사용하고자 한다면 `int()`함수를 사용해 분명하게 변환할 것을 권장한다.

```python
print(bool(None), bool(False), bool(0), bool(0.0), bool(0j), bool(""), bool(()), bool([]), bool({}), bool(set()), bool(range(0)))

print(True + True)
print(int(True) + int(True))
```

### 6-1. Boolean 연산자(논리 연산자)

- 비트 연산자에 대응되더라도 논리 연산자를 사용할 것을 권장
- Python의 논리 연산자는 short-circuit operator로 앞의 값이 결정되면 뒤의 값을 검사하지 않는다.
  - `x or y`에 대해 x가 참이면 y의 참/거짓을 검사하지 않는다.
  - `x and y`에 대해 x가 거짓이면 y의 참/거짓을 검사하지 않는다.
- not 연산자에 대해서는 다음을 주의해야 한다.
  - 다른 연산자보다 우선순위가 낮기 때문에 `not a == b`는 `(not a) == b`가 아니며 `not (a == b)`이다.
   `~`연산자는 3.12부터 deprcated되며 3.14에서는 에러가 발생하도록 업데이트할 예정이다.

|논리 연산자|비트 연산자|결과|
|:-:|:-:|:-:|
|`x or y`|&|x가 참이면 x를, 아니면 y를 반환|
|`x and y`|\||x가 거짓이면 x를, 아니면 y를 반환|
|`not x`|~|x가 거짓이면 `True`를, 아니면 `False`를 반환|

```python
print(True or False)
print(True and False)
print(not True)
```

### 6-2. 비교 연산자

- 비교 연산자 간의 우선순위는 모두 동일함
- Python은 비교 연산자를 연속으로 쓸 수 있다.

|연산자|의미|
|:-:|:-:|
|<|보다 작다|
|<=|작거나 같다|
|>|보다 크다|
|>=|크거나 같다|
|==|같다|
|!=|같지 않다|
|is|object identity|
|is not|negated object identity|

- int와 float을 제외한 다른 타입 간에는 비교 연산자를 사용할 수 없다.
- complex는 크기 비교 연산이 불가능하다.

```python
print(10 < 10, 10 <= 10, 10 > 10, 10 >= 10, 10 == 10, 10 != 10)
```

## 7. Condition Statement (조건문)

- [사용자가 정의한 식의 참과 거짓을 평가해 다른 계산이나 행동으로 수행하는 명령](https://en.wikipedia.org/wiki/Conditional_(computer_programming))
  - `if statement: code_block` 형태로 사용한다.
- `else: code`는 `if`문의 `statement`를 만족하지 않을 때 실행한다. `else`문이 없다면 다음 코드블럭을 실행한다.
- `if`문의 `statement`를 만족하지 않을 때 `elif statement: code`가 있다면 `else`문보다 먼저 실행한다.
- `if`, `elif`, `else`문을 여러 개 조합하는 복합 조건문을 한 구문으로 나타낼 수 있는 `match-case`문도 있다.
  - 3.10부터 지원하며 다른 언어의`switch-case`문과 비슷한 것 같지만 [공식문서에서는 Rust나 Haskell의 패턴 매칭 구문과 더 비슷하다고 소개한다.](https://docs.python.org/3/tutorial/controlflow.html#match-statements)
  - *하위버전 호환성을 고려해야 한다면 사용하지 않는 것을 권장한다.*

```python
if 102958372 % 2 == 0:
    print("This is even number.")

if 102958371 % 2 == 0:
    print("This is even number.")
print("This is odd number.")

if 102958371 % 2 == 0:
    print("This is even number.")
else:
    print("This is odd number.")

if 102958371 % 2 == 0:
    print("This is even number.")
elif 102958371 % 2 == 1:
    print("This is odd number.")
else: print("Is this 0?")
```
