# 기초반 2차시

## TOC

- [1. Numeric Type](#1-numeric-type)
  - [1-1. int](#1-1-int)
  - [1-2. float](#1-2-float)
  - [1-3. complex](#1-3-complex)
  - [1-4. 연산자](#1-4-연산자)
    - [1-4-1. int, float 연산자](#1-4-1-int-flaot-연산자)
    - [1-4-2. 비트 연산자](#1-4-2-비트-연산자)
- [2. Boolean Type](#2-boolean-type)
  - [2-1. Boolean 연산자](#2-1-boolean-연산자논리-연산자)
  - [2-2. 비교 연산자](#2-2-비교-연산자)
- [3. Sequence Type](#3-sequence-type)
  - [3-1. Iterator(반복자)](#3-1-iterator반복자)
  - [3-2. Sequence Type 함수](#3-2-sequence-type-함수)
  - [3-3. slicing](#3-3-slicing)
- [4. list](#4-list)
  - [4-1. list 함수](#4-1-list-함수)
  - [4-2. list comprehension(리스트 표현식)](#4-2-list-comprehension리스트-표현식)
  - [4-3. list == array?](#4-3-list--array)
  - [4-4. 다차원 list 생성 주의](#4-4-다차원-list-생성-주의)
- [5. tuple](#5-tuple)
- [6. range](#6-range)
- [7. string(Text Sequence Type)](#7-string-text-sequence-type)
  - [7-1. string 함수](#7-1-string-함수)
- [8. Set Type](#8-set-type)
  - [8-1. Hash Table(Hashmap, Hashable)](#8-1-hash-tablehashmap-hashable)
  - [8-2. Set 함수](#8-2-set-함수)
- [9. dictionary(Mapping Type)](#9-dictionarymapping-type)
  - [9-1. dictionary 함수](#9-1-dictionary-함수)
  - [9-2. dictview 함수](#9-2-dictview-함수)

## 1. Numeric Type

### 1-1. int

- `int(x, base=10)`생성자를 통해 int형으로 바꿀 수 있음
- 크기 제한이 없다.

### 1-2. float

- `float(x=0.0)`생성자를 통해 float형으로 바꿀 수 있음
- C언어의 double형에 해당하는 정확도를 가진다.

### 1-3. complex

- `complex(real=0, imag=0)`이나 `complex(string)`생성자를 통해 complex형으로 바꿀 수 있음
- 실수부와 허수부 모두 부동 소수점 방식을 사용한다.
  - 실수부는 `z.real`로, 허수부는 `z.imag`로 추출하며 실수로 표기된다.

### 1-4. 연산자

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

#### 1-4-1. int, float 연산자

- 더 많은 함수는 [math](https://docs.python.org/3/library/math.html#module-math) 모듈과 [cmath](https://docs.python.org/3/library/cmath.html#module-cmath)모듈에서 정의하고 있음

|연산자|결과|
|:-:|:-:|
|`math.trunc(x)`|정수부 반환|
|`round(x, n)`|소수 n번째 자릿수까지 표기되도록 반올림|
|`math.floor(x)`|x이하의 가장 큰 정수 반환|
|`math.ceil(x)`|x이상의 가장 작은 정수 반환|

#### 1-4-2. 비트 연산자

- 정수가 주어지면 해당 정수의 모든 비트 값에 대한 연산을 수행

|연산자|결과|비고|
|:-:|:-:|:-:|
|`x\|y`|x or y 비트연산||
|`x^y`|x xor y 비트연산||
|`x&y`|x and y 비트연산||
|`x<<n`|왼쪽으로 n비트만큼 shift|n은 음수값을 허용하지 않음|
|`x>>n`|오른쪽으로 n비트만큼 shift|n은 음수값을 허용하지 않음|
|`~x`|비트를 반전||

## 2. Boolean Type

- True, False라는 두 개의 상수로 구성된 타입
- 내장 함수 `bool(value)`를 사용하면 value의 Boolean 타입을 반환해준다.
  - `None`, `False`, `0`, `0.0`, `0j`, `''`, `()`, `[]`, `{}`, `set()`, `range(0)`은 False로, 나머지는 True로 반환한다.
- int형의 하위타입이기 때문에 False와 True가 각각 0과 1로 간주될 수 있지만 Boolean Type을 int Type 처럼 사용하고자 한다면 `int()`함수를 사용해 분명하게 변환할 것을 권장한다.

### 2-1. Boolean 연산자(논리 연산자)

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

### 2-2. 비교 연산자

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

## 3. Sequence Type

- iterator를 지원하는 타입
- 앞서 설명한 타입들은 Sequence Type이 아닌 타입들로 iterator를 지원하지 않는다.

### 3-1. Iterator(반복자)

- `__iter__()`함수와 `__next__()` 함수를 내부적으로 갖고 처리하는 자료형(클래스)
  - `__iter__()` 함수는 Iterator 타입의 객체를 반환한다.
  - `__next__()` 함수는 다음 요소에 접근한다.

### 3-2. Sequence Type 함수

|연산자|결과|비고|
|:-:|:-:|:--:|
|`x in s`|x가 s에 존재하면 True, 아니면 False||
|`x not in s`|x가 s에 존재하지 않으면 True, 아니면 False||
|`s + t`|s와 t를 연결|immutable sequence 타입은 새로운 객체를 생성하기 때문에</br>$O(n^2)$의 시간복잡도를 가짐</br>range 등의 일부 sequence type은 지원되지 않음|
|`s * n or n * s`|s를 n번 연결|range 등의 일부 sequence type은 지원되지 않음|
|`s[i]`| s의 i번째 요소를 반환||
|`len(s)`|s의 길이를 반환||
|`min(s)`|s에서 값이 가장 작은 요소를 반환||
|`max(s)`| s에서 값이 가장 큰 요소 반환를 반환||
|`s.index(x,i,j)`| s에서 첫 번째로 나타나는 x를 찾아 그 index를 반환</br>i와 j는 선택사항이며 설정하면 i번째부터 j-1번째까지에서 탐색|x를 찾지 못했다면 ValueError 발생</br>`s[i:j].index(x)`와 동치같지만 slicing 한 위치를 기준으로 index를 반환|
|`s.count(x)`|s에서 x가 나타난 횟수를 반환||

### 3-3. slicing

- Ada, Go, Python 등 일부 언어에서 지원하는 list에 대한 독특한 기능
- `s[i:j:k]`로 표시하며 i에서 j-1까지의 요소를 동일한 Sequence Type으로 반환한다.
  - k는 선택 사항이며 설정하면 k를 간격으로 반환한다.
  - i나 j가 음수라면 마지막 요소부터 역순으로 가리킴
    - -0은 0으로 취급하기 때문에 가장 마지막의 요소는 -1부터 시작한다.
- 예제코드를 보는 것이 이해하기 쉽다.

## 4. list

- 일반적으로 비슷한 요소를 저장하는 Mutable Sequence Type

### 4-1. list 함수

- 공식 문서에서는 `collections.abc.MutableSequence`에 속한 자료형들에서 가능한 연산이라고 했으나 내장 타입 중에는 list밖에 없어 list 함수 항목으로 나타냄

|연산자|결과|비고|
|:-:|:-:|:-:|
|`s[i] = x`|i 위치의 요소를 x로 대체||
|`s[i:j] = t`|i에서 j-1까지를 iterable한 t로 대체||
|`del s[i:j]`|`s[i:j] = []`와 동치||
|`s[i:j:k] = t`|`s[i:j:k]`를 iterable한 t로 대체|t의 길이는 대체하려는 요소의 수와 같아야 함|
|`del s[i:j:k]`|s[i:j:k]의 요소 삭제||
|`s.append(x)`|s의 가장 마지막에 x를 이어붙임||
|`s.clear()`|s의 모든 요소를 삭제||
|`s.copy()`|s의 얕은 복사본을 생성||
|`s.extend(t)` or `s += t`|s의 가장 마지막에 t의 요소들을 이어붙임||
|`s *= n`|s를 n번 반복한 값으로 바꿈||
|`s.insert(i,x)`|s의 i 위치 바로 직후에 x를 삽입함||
|`s.pop(i)`|s에서 i번째 요소를 반환하고 제거함</br>i가 주어지지 않았다면 마지막 값||
|`s.remove(x)`|s에서 첫 번째로 나타난 x를 제거함||
|`s.reverse()`|s를 뒤집은 값으로 바꿈||
|`s.sort()`|s를 정렬한 list로 바꿈|정렬한 list를 다른 변수에 할당하려면 `t=s.sorted()`를 사용할 것|

### 4-2. list comprehension(리스트 표현식)

- list를 생성할 때 식, for문, if문을 한 문장으로 묶어 생성하는 것
  - tuple, set, dictionary에도 적용할 수 있다.
- `[variable_expression for variable in iterator if condition]` 혹은 `list(expression for variable in iterator if condition)`형태로 표현할 수 있다.
  - if-else문을 사용하려면 `[variable_expression if condition else statement for variable in iterator]` 형태로 작성한다.
- 예제코드를 보는 것이 이해하기 쉽다.

### 4-3. [list == array?](https://stackoverflow.com/questions/176011/python-list-vs-array-when-to-use)

- 자료구조 상으로 list와 배열은 엄연히 다른 존재이고 Python에서 `array`모듈을 별도로 지원
- 정의 상 다른 개념이지만 사용에 있어서는 거의 동치임
- Python에서 list는 상수시간에 작동할 수 있도록 구현되었지만 그 대가로 배열보다 많은 공간을 필요로 함
- `array`모듈은 C로 구현되었기 때문에 빠른 연산과 적은 메모리(특히 수학)가 필요할 때 사용

### 4-4. 다차원 list 생성 주의

- `[[] for i in range(x)]`와 `[[]] * x`는 다르게 작동함
  - Sequence Type의 `*`연산자는 복사가 되는 것이 아닌 여러 번 참조하는 연산자이다.

## 5. tuple

- 일반적으로 서로 무관한 데이터를 저장하는 Immutable Sequence Type
  - immutable하다는 것은 내부의 값이 수정될 수 없는 것을 의미한다.
- tuple을 선언하는 것은 괄호가 아니고 comma이다.
  - 즉, 빈 tuple을 생성하는 경우나 구문의 모호성을 피하기 위한 경우(함수 등 괄호를 사용하는 구문들에서)를 제외하면 tuple을 나타내기 위해 괄호를 사용하는 것은 선택사항이다.

## 6. range

- 숫자들을 순서대로 나열하는 Immutable Sequence Type
  - 일반적으로 for문에서 특정 횟수만큼 반복하기 위해 사용한다.
- range의 최대 장점은 같은 기능의 list와 tuple과 달리 메모리를 매우 적게 차지한다는 것이다.
  - 값을 저장하지 않고 실행할 때 계산하여 반환하는 것을 lazy evaluation(지연평가)라고 한다.
  - range는 start, stop, step만 저장하고 필요할 때 계산한다.
- `range(stop)`혹은 `range(start=0, stop, step=1)` 형태로 작성한다.
  - 매개변수들은 반드시 정수형이어야 한다.
  - step이 0이면 `ValueError`가 발생한다.
  - `start`부터 `stop`까지 `step`을 0부터 증가시키면서 `start*step`을 반환한다.
- sequence type이기 때문에 [Sequence Type 함수](https://github.com/Indigo-Coder-github/Python_Lecture/tree/main/%EC%B4%88%EA%B8%89%EB%B0%98%205%2C%206%EC%A3%BC%EC%B0%A8#sequence-type-%ED%95%A8%EC%88%98), [slicing](https://github.com/Indigo-Coder-github/Python_Lecture/tree/main/%EC%B4%88%EA%B8%89%EB%B0%98%205%2C%206%EC%A3%BC%EC%B0%A8#slicing), 음수를 통한 indexing 모두 지원한다.
  - 단, slicing과 음수를 통한 indexing은 3.2 이상부터 지원한다.
  - 3.3 이상부터는 결과값에 대한 `==`과 `!=`연산도 지원한다.

## 7. string (Text Sequence Type)

- 문자열을 담는 Immutable Sequence Type
- UTF-8로 인코딩한다.
- Python에서 문자열을 선언할 때 문자열 내 따옴표로 문자열을 묶는 것을 피해야 하는 경우만 제외하면 큰 따옴표와 작은 따옴표의 차이는 없으며 [개인의 취향에 따라 사용하거나 관습을 따른다.](https://stackoverflow.com/questions/56011/single-quotes-vs-double-quotes-in-python)
- 세 개의 따옴표로 묶으면 문자열의 줄바꿈을 허용한다.

### 7-1. string 함수

- Sequence Type의 함수도 사용할 수 있다.

|연산자|결과|비고|
|:-:| :-: |:-:|
|`str.capitalize()`|첫 글자만 대문자로 바꿔 반환||
|`str.casefold()`|`str.lower()`와 동치이지만 좀 더 엄격한 변환을 거침(ex. 독일어 ß를 ss로)|자세한 사항은 Unicode 표준 문서를 참조할 것|
|`str.center(width, fillchar)`|str을 가운데에 놓고 str의 길이가 width가 될 때까지 양옆으로 fillchar을 채워 반환||
|`str.count(sub, start, end)`|str에서 sub의 갯수를 계산함</br>start와 end는 선택 사항으로 `str[start:end].count(sub)`와 동치||
|`str.encode(encoding="utf-8", errors="strict")`|str을 byte로 인코딩</br>encoding은 현재 str의 인코딩 방식</br>errors는 [공식문서 참조](https://docs.python.org/3/library/stdtypes.html#str.encode)||
|`str.endswith(suffix, start, end)`|str이 suffix로 끝난다면 True를, 아니면 False를 반환</br>찾고자 하는 것이 여러개라면 suffix는 tuple일 수 있음</br>start와 end는 선택 사항으로 slicing한 것으로 해석||
|`str.expandtabs(tabsize=8)`|str의 모든 tab을 tabsize만큼의 공백으로 바꿔 반환||
|`str.find(sub, start, end)`|`str[start:end]`에서 처음 찾은 sub의 위치를 반환, 찾지 못했다면 -1을 반환|sub의 위치를 알고 있을 때 이 함수를 사용할 것을 권장하며 단순히 sub가 있는지 확인하려면 `in`을 사용할 것을 권장|
|`str.format()`|formatting 메서드로 string은 {}을 갖고 있어야 함</br>채워야 할 각 필드는 위치 인수의 index나 키워드 인수의 이름이어야 하며 일치하는 인수의 문자열 값으로 대체된 str을 반환||
|`str.index(sub, start, end)`|`find()`와 동치이지만 sub를 찾지 못하면 ValueError 발생||
|`str.isalnum()`|str의 모든 문자들이 알파벳과 숫자로 이뤄졌다면 True를, 아니면 False를 반환|str이 `isalpha()`, `isdecimal()`, `isdigit()`, `isnumeric()` 중 하나 이상에 대해 True를 반환했다면 이 함수는 True를 반환|
|`str.isalpha()`|str의 모든 문자들이 알파벳이면 True를, 아니면 False를 반환||
|`str.isascii()`|str이 비었거나 모든 문자가 ASCII라면 `True`를, 아니면 `False`를 반환</br>Unicode로는 0000~007F에 해당함|3.7 이상부터 지원|
|`str.isdecimal()`|str의 모든 문자들이 decimal이라면 `True`를, 아니면 `False`를 반환|Unicode에서 Nd 카테고리로 분류된 모든 문자가 해당|
|`str.isdigit()`|str의 모든 문자들이 digit이라면 `True`를, 아니면 `False`를 반환|[True를 반환하는 digit의 Unicode는 위키백과를 참조할 것](https://en.wikipedia.org/wiki/Numerals_in_Unicode)|
|`str.isidentifier()`|str이 변수명으로 사용할 수 있는 문자의 조합이라면 `True`를 반환|예약어 여부는 알 수 없음|
|`str.islower()`|str의 적어도 한 문자가 대문자/소문자 체계이고 그 문자들이 모두 소문자이면 `True`를, 아니면 `False를 반환||
|`str.isnumeric()`|str의 모든 문자가 숫자이면 `True`를, 아니면 `False`를 반환|[True를 반환하는 숫자의 Unicode는 위키백과를 참조할 것](https://en.wikipedia.org/wiki/Numerals_in_Unicode)|
|`str.isprintable()`|str의 모든 문자가 출력할 수 있거나 비었다면 `True`를, 아니면 `False`를 반환|Unicode에서 공백을 제외한 separator나 other로 분류된 문자는 출력 불가능한 문자로 정의|
|`str.isspace()`|str이 모두 공백으로 이뤄졌다면 `True`를, 아니면 `False`를 반환||
|`str.istitle()`|str이 titlecase(각 어절이 대문자)면 `True`를, 아니면 `False`를 반환||
|`str.isupper()`|str의 적어도 한 문자가 대문자/소문자 체계이고 그 문자들이 모두 대문자이면 `True`를, 아니면 `False`를 반환||
|`str.join(iterable)`|iterable 요소를 str로 연결하여 반환</br>즉, str이 iterable 요소 사이의 구분자|iterable의 요소 중 string이 아닌 값이 있다면 TypeError 발생|
|`str.ljust(width, fillchar=" ")`|str의 길이가 width가 될 때까지 fillchar로 오른쪽을 채움</br>width가 원래 str의 길이보다 작거나 같으면 str을 반환||
|`str.lower()`|str을 모두 소문자로 변환해 반환||
|`str.lstrip(chars)`|chars에 해당하는 문자들이 발견되지 않을 때까지 str의 앞부분부터 제거</br>chars를 주지 않거나 None인 경우 공백이 제거됨|chars를 접두사로 인식하지 않음|
|`str.maketrans()`|`str.translate()`에서 사용할 수 있는 table을 반환하는 정적 메서드로 `str.maketrans()`로 호출</br>인자가 하나뿐이라면 글자-글자 쌍의 dict를 줘야하며 key에 해당하는 글자는 Unicode 10진 값으로 바뀌어 저장</br>인자가 둘뿐이라면 두 인자는 같은 길이의 문자열이어야 하며 첫 인자의 모든 문자가 두 번째 인자의 모든 문자에 대응하는 dict를 생성</br>인자가 셋뿐이라면 둘뿐일때와 마찬가지이며 세 번째 인자의 모든 문자는 None에 대응||
|`str.partition(sep)`|str에 첫 번째로 나타난 sep를 기준으로 분할해 sep 전의 str, sep, sep 후의 str, 총 3개를 요소로 하는 tuple을 반환|sep를 찾지 못했다면 str과 두 개의 빈 string, 총 3개를 요소로 하는 tuple을 반환|
|`str.removeprefix(prefix)`|str이 prefix로 시작하면 `str[len(prefix):]`를, 아니면 str을 반환||
|`str.removesuffix(suffix)`|str이 suffix로 끝나면 `str[:len(suffix)]`를, 아니면 str을 반환||
|`str.replace(old, new, count)`|str 내의 모든 old를 new로 바꿔 반환|count는 선택사항으로 처음으로 count만큼 발생한 old만 new로 바꿈|
|`str.rfind(sub, start, end)`|`str[start:end]`에서 마지막으로 찾은 sub의 위치를 반환, 찾지 못했다면 -1을 반환||
|`str.rindex()`|`rfind()`와 동치이지만 sub를 찾지 못하면 ValueError 발생||
|`str.rjust(width, fillchar)`|str의 길이가 width가 될 때까지 fillchar로 왼쪽을 채움</br>width가 원래 str의 길이보다 작거나 같으면 str을 반환||
|`str.rpartition(sep)`|str에 마지막로 나타난 sep를 기준으로 분할해 sep 전의 str, sep, sep 후의 str, 총 3개를 요소로 하는 tuple을 반환|sep를 찾지 못했다면 str과 두 개의 빈 string, 총 3개를 요소로 하는 tuple을 반환|
|`str.rsplit(sep=None, maxsplit=-1)`|sep를 구분자로 하여 문자열 내 단어들의 리스트를 반환</br>sep가 주어지지 않거나 `None`인 경우 어떤 공백이든지 구분자로 간주</br>maxsplit이 주어지면 가장 오른쪽부터 maxsplit에 해당하는 횟수만큼 분할|오른쪽부터 분할한다는 점을 제외하면 `split()`과 동치|
|`str.rstrip(chars)`|chars에 해당하는 문자들이 발견되지 않을 때까지 str의 뒷부분부터 제거</br>chars를 주지 않거나 None인 경우 공백이 제거됨|chars를 접미사로 인식하지 않음|
|`str.split(sep=None, maxsplit=-1)`|sep를 구분자로 하여 문자열 내 단어들의 리스트를 반환</br>sep가 주어지지 않거나 `None`인 경우 연속된 공백을 단일 구분자로 간주, 앞 뒤의 모든 공백도 제거하여 반환</br>maxsplit이 주어지면 해당 횟수만큼 분할, 주어지지 않거나 -1인 경우 가능한 한 최대로 분할|sep는 복수의 문자일 수 있음</br>str 내 sep가 연속으로 나타나면 하나로 묶어 취급하지 않으며 구분자 사이에 빈 문자가 있는 것으로 간주|
|`str.splitlines(keepends=False)`|str내 줄 바꿈을 없애고 이들을 요소로 하는 list를 반환</br>keepends가 주어졌거나 `True`인 경우 줄 바꿈 문자도 포함해 반환|[줄 바꿈에 해당하는 문자는 링크를 참조](https://docs.python.org/3/library/stdtypes.html#str.splitlines)|
|`str.startswith(prefix, start, end)`|str이 prefix로 시작하면 `True`를, 아니면 `False`를 반환|찾으려는 prefix가 여러 개라면 tuple로 줄 수 있음</br>start와 end는 선택사항으로 start부터 end에 해당하는 index에 대해서만 검사|
|`str.strip(chars)`|str의 선행/후행 문자에서 chars의 모든 문자를 제거해 반환|`None`을 주거나 아무것도 주지 않으면 공백을 제거함|
|`str.swapcase()`|str의 모든 대문자/소문자를 소문자/대문자로 바꿔 반환||
|`str.title()`|str의 title case(어절의 첫 번째 문자만 대문자)을 반환|'(apostrophe) 뒤의 첫 문자도 대문자로 변환|
|`str.translate(table)`|str 내 각 문자열에 대해 주어진 table에 대응하는 문자열로 변환하여 반환|table은 일반적으로 dict나 Sequence Type|
|`str.upper()`|str을 모두 대문자로 변환해 반환|str에 대문자/소문자 개념이 없는 문자열이 포함되있다면 `str.upper().isupper()`의 결과가 `False`일 수 있음|
|`str.zfill(width)`|반환하는 문자열의 길이가 width가 될 때까지 str의 왼쪽에 0을 채워 반환|str에 부호가 포함되어 있다면 0은 부호 뒤부터 채워짐|

## 8. Set Type

- hashable한 요소들로 구성된 순서가 없는 집합
  - Set와 Dictionary Type은 Sequence Type이 아니다! collection이라는 타입에 Sequence, Set, Dictionary가 종속된다.
  - set는 mutable하며 immutable한 set인 frozenset을 지원한다.
- 일반적으로 sequence의 중복요소 제거, 교집합이나 합집합 등의 수학적 연산에 사용한다.
  - 수학에서 말하는 집합을 지원하는 자료형이라고 생각하면 된다.
- 다른 집합형 자료형들과 마찬가지로 `x in set`, `len(set)`, `for x in set`등을 지원한다.
  - 삽입 순서에 대한 위치를 기록하지 않기 때문에 indexing, slicing 등은 할 수 없다.

### 8-1. Hash Table(Hashmap, Hashable)

- key-value 쌍으로 구성된 요소에 대해 key에 대한 hash function 값의 위치에 value를 저장하는 자료구조
  - key는 hash function에 대한 입력값으로 주어지기 때문에 Python에서는 Immutable Type만 사용할 수 있다.
    - Numeric Type, string은 항상 key가 될 수 있는 자료형이다.
    - Numeric Type, string, tuple을 요소로 하는 typle도 key가 될 수 있는 자료형이다.
  - hash function은 일반적으로 나머지 연산자(%, mod)를 사용한다.
- 탐색, 삽입, 삭제 모두 시간복잡도가 `O(1)`이라는 강력한 장점을 갖고 있지만 충돌이 발생할 수 있고 해시 함수의 성능에 영향을 많이 받으며 key-value 쌍이 아닌 자료구조에선 부적합할 수 있다는 단점을 갖고 있다.

### 8-2. Set 함수

|연산자|결과|비고|
|:-:|:-:|:-:|
|`len(s)`|s의 요소 수를 반환|s의 cardinality|
|`x in s`|s가 x의 멤버십인지 테스트||
|`x not in s`|s가 x의 멤버십이 아닌지 테스트||
|`s.isdisjoint(t)`|s가 t와 공통 원소가 없다면 True를 반환|두 집합이 서로소 집합이기 때문에 교집합이 공집합임|
|`s.issubset(t)`|s가 t의 부분집합이면 True 반환|`s<=t`, `s<t`와 동치|
|`s.issuperset(t)`|s가 t의 상위집합이면 True 반환|`s>=t`, `s>t`와 동치|
|`s.union(t)`|s와 t의 합집합을 반환|`s\|t`와 동치|
|`s.intersection(t)`|s와 t의 교집합을 반환|`s&t`와 동치|
|`s.difference(t)`|s와 t의 차집합을 반환|`s-t`와 동치|
|`s.symmetric_difference(t)`|s와 t의 대칭차집합을 반환|`s^t`와 동치|
|`s.copy()`|s의 얕은 복사를 반환||
|`s.update(t)`|s와 t의 합집합으로 s를 업데이트|`s\|=t`와 동치|
|`s.intersection_update(*t)`|s와 t의 교집합으로 s를 업데이트|`s&=t`와 동치|
|`s.difference_update(*t)`|s와 t의 차집합으로 s를 업데이트|`s-=t`와 동치|
|`s.symmetric_difference_update(t)`|s와 t에 모두 있는 원소 외의 원소들로 s를 업데이트 |`s^=t`와 동치|
|`s.add(x)`|s에 x를 추가||
|`s.remove(x)`|s에서 x를 제거|x가 없다면 KeyError가 발생|
|`s.discard(x)`|s에 x가 있다면 x를 제거||
|`s.pop()`|s에서 임의의 요소를 반환하고 제거|s가 비었다면 KeyError가 발생|
|`s.clear()`|s의 모든 요소를 제거||

## 9. dictionary(Mapping Type)

- 임의의 값을 hashable한 값에 대응시키는 Mutable Type
  - Python 표준 Mapping Type은 dictionary만 있다.
- Sequence 자료형과 달리 immutable 타입인 key를 index로 value에 접근할 수 있다.

### 9-1. dictionary 함수

- 3.7 이상부터는 삽입 순서에 따른 순서를 보장하며 value가 바뀌었다고 순서가 바뀌진 않는다.
- [3.9 이상부터는 `|`연산과 `|=`연산을 지원하며 dictionary를 서로 비교한 결과를 새로운 dictionary로 반환한다.](https://docs.python.org/3/library/stdtypes.html#mapping-types-dict)

|연산자|결과|비고|
|:-:|:-:|:-:|
|`list(d)`|d의 key를 요소로 하는 list 반환||
|`len(d)`|d의 요소의 수를 반환||
|`d[key]`|key를 key로 하는 d의 요소 반환||
|`d[key] = value`|`d[key]`를 value로 설정||
|`del d[key]`|`d[key]`를 d에서 제거||
|`key in d`|d의 key에 key가 있다면 True 반환, 아니면 False 반환||
|`key not in d`|not (key in d)와 동치||
|`iter(d)`|d의 key에 대한 iterator를 반환||
|`d.clear()`|d의 모든 요소를 제거||
|`d.copy()`|d의 모든 요소를 얕은 복사해 반환||
|`d.get(key, default)`|d의 key에 해당하는 value를 반환</br>만약 없다면 default로 준 값을 반환하며 주어지지 않았다면 예외 발생||
|`d.items()`|d의 모든 요소를 (key, value)쌍 형태로 반환|dictview 객체라는 특수 형태|
|`d.keys()`|d의 key들에 대한 dictview를 반환||
|`d.pop(key, default)`|d의 key에 대한 값을 반환하고 이를 제거|default 인자는 get과 같은 역할|
|`d.popitem()`| LIFO의 순서로 d의 아이템을 (key, value)쌍 형태로 반환|3.7 이전에는 LIFO가 아닌 임의의 쌍을 반환|
|`reversed(d)`|d의 key에 대한 뒤집힌 iterator를 반환|3.8 이상부터 지원|
|`d.setdefault(key, default=None)`|d에 key가 있다면 그 값을 반환하고</br>없다면 default를 value로 하는 key를 삽입하고 default를 반환||
|`d.update(other)`|d에 대해 other의 내용을 업데이트|other은 dict의 선언 형태를 따라감|
|`d.values()`|d의 값에 대한 dictview를 반환||

### 9-2. dictview 함수

- `dict.keys()`, `dict.values()`, `dict.items()`로 도출되는 자료형에 대한 함수

|연산자|결과|비고|
|:-:|:-:|:-:|
|`len(dictview)`|dictview의 크기 반환||
|`iter(dictview)`|dictview의 iterator를 반환| iterating 중에 삽입, 삭제 등을 실행하면 예외 발생|
|`x in dictview`|x가 dictview에 있다면 True를 반환, 아니라면 False를 반환||
|`reversed(dictview)`|dictview에 대한 뒤집힌 iterator를 반환||
