# 기초반 2차시

## Numeric Type

### int

- `int(x, base=10)`생성자를 통해 int형으로 바꿀 수 있음
- 크기 제한이 없다.

### float

- `float(x=0.0)`생성자를 통해 float형으로 바꿀 수 있음
- C언어의 double형에 해당하는 정확도를 가진다.

### complex

- `complex(real=0, imag=0)`이나 `complex(string)`생성자를 통해 complex형으로 바꿀 수 있음
- 실수부와 허수부 모두 부동 소수점 방식을 사용한다.
  - 실수부는 `z.real`로, 허수부는 `z.imag`로 추출하며 실수로 표기된다.

### 연산자

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

#### int, flaot 연산자

- 더 많은 함수는 [math](https://docs.python.org/3/library/math.html#module-math) 모듈과 [cmath](https://docs.python.org/3/library/cmath.html#module-cmath)모듈에서 정의하고 있음

|연산자|결과|
|:-:|:-:|
|`math.trunc(x)`|정수부 반환|
|`round(x, n)`|소수 n번째 자릿수까지 표기되도록 반올림|
|`math.floor(x)`|x이하의 가장 큰 정수 반환|
|`math.ceil(x)`|x이상의 가장 작은 정수 반환|

#### 비트 연산자

- 정수가 주어지면 해당 정수의 모든 비트 값에 대한 연산을 수행

|연산자|결과|비고|
|:-:|:-:|:-:|
|`x\|y`|x or y 비트연산||
|`x^y`|x xor y 비트연산||
|`x&y`|x and y 비트연산||
|`x<<n`|왼쪽으로 n비트만큼 shift|n은 음수값을 허용하지 않음|
|`x>>n`|오른쪽으로 n비트만큼 shift|n은 음수값을 허용하지 않음|
|`~x`|비트를 반전||

## Boolean Type

- True, False라는 두 개의 상수로 구성된 타입
- 내장 함수 `bool(value)`를 사용하면 value의 Boolean 타입을 반환해준다.
  - `None`, `False`, `0`, `0.0`, `0j`, `''`, `()`, `[]`, `{}`, `set()`, `range(0)`은 False로, 나머지는 True로 반환한ㄷ.
- int형의 하위타입이기 때문에 False와 True가 각각 0과 1로 간주될 수 있지만 Boolean Type을 int Type 처럼 사용하고자 한다면 `int()`함수를 사용해 분명하게 변환할 것을 권장한다.

### Boolean 연산자(논리 연산자)

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
|`not x`|~|x가 거짓이면 `True`를, 아니면 False를 반환|

### 비교 연산자

- 비교 연산자 간의 우선순위는 모두 동일함
- Python은 비교 연산자를 연속으로 쓸 수 있다.

| 연산자 | 의미                    |
|:------:|:-----------------------:|
|   <    | 보다 작다               |
|   <=   | 작거나 같다             |
|   >    | 보다 크다               |
|   >=   | 크거나 같다             |
|   ==   | 같다                    |
|   !=   | 같지 않다               |
|   is   | object identity         |
| is not | negated object identity |

- int와 float을 제외한 다른 타입 간에는 비교 연산자를 사용할 수 없다.
- complex는 크기 비교 연산이 불가능하다.

## Sequence Type

- iterator를 지원하는 타입
- 앞서 설명한 타입들은 Sequence Type이 아닌 타입들로 iterator를 지원하지 않는다.

### Sequence Type 함수

|연산자|결과| 비고 |
|:-:| --------------------------------------------------------------------------------------------------------------- |:----:|
|     x in s     | x가 s에 존재하면 True, 아니면 False                                                                             |      |
|   x not in s   | x가 s에 존재하지 않으면 True, 아니면 False                                                                      |      |
|     s + t      | s와 t를 연결                                                                                                    |immutable sequence 타입은 새로운 객체를 생성하기 때문에</br>$O(n^2)$의 시간복잡도를 가짐</br>range 등의 일부 sequence type은 지원되지 않음      |
|     s \* n or n \* s      | s를 n번 연결                                                                                                    |range 등의 일부 sequence type은 지원되지 않음      |
|     s\[i\]     | s의 i번째 요소 반환                                                                                             |      |
|     len(s)     | s의 길이                                                                                                        |      |
|     min(s)     | s에서 가장 작은 요소 반환                                                                                       |      |
|     max(s)     | s에서 가장 큰 요소 반환                                                                                         |      |
| s.index(x,i,j) | s에서 첫 번째로 나타나는 x를 찾아 그 index를 반환</br>i와 j는 선택사항이며 설정하면 i번째부터 j-1번째까지에서 탐색 |x를 찾지 못했다면 ValueError 발생</br>s\[i:j\].index(x)와 동치이지만 슬라이싱된 리스트 기준의 index를 반환      |
|s.count(x)                |s에서 x가 나타난 횟수를 반환                                                                                                                 |      |

### slicing

- Ada, Go, Python 등 일부 언어에서 지원하는 배열에 대한 독특한 기능
- `s[i:j:k]`로 표시하며 i에서 j-1까지의 요소를 반환
  - k는 선택 사항이며 설정하면 k만큼 건너뛰면서 반환
  - i나 j가 음수라면 마지막 요소부터 역순으로 가리킴
    - 그러나 -0은 0으로 취급하기 때문에 가장 마지막의 요소는 음수로 -1임

### list

- mutable sequence type, 일반적으로 비슷한 요소의 집합을 저장함
- 아래와 같이 선언할 수 있음

#### list 함수

- 공식 문서에서는 `collections.abc.MutableSequence`에 속한 자료형들에서 가능한 연산이라고 했으나 내장 타입 중에는 list밖에 없어 list 함수 항목으로 나타냄
- `list.sort()`는 정렬된 list로 바꿔줌
  - 정렬된 리스트를 값으로 받고 싶다면 [sorted()함수를 사용](https://github.com/Indigo-Coder-github/Python_Lecture/tree/main/%EC%A4%91%EA%B8%89%EB%B0%98%203%EC%A3%BC%EC%B0%A8#sortediterable-keynone-reversefalse)

|        연산자         | 결과                                                                  |                    비고                     |
|:---------------------:| --------------------------------------------------------------------- |:-------------------------------------------:|
|      s\[i\] = x       | i 위치의 요소를 x로 대체                                              |                                             |
|     s\[i:j\] = t      | i에서 j-1까지를 iterable한 t로 대체                                   |                                             |
|     del s\[i:j\]      | s\[i:j\] = \[\]와 동치                                                |                                             |
|    s\[i:j:k\] = t     | s\[i:j:k\]를 iterable한 t로 대체                                      | t의 길이는 대체하려는 요소의 수와 같아야 함 |
|    del s\[i:j:k\]     | s[i:j:k]의 요소 삭제                                                  |                                             |
|      s.append(x)      | s의 가장 마지막에 x를 이어붙임                                        |                                             |
|       s.clear()       | s의 모든 요소를 삭제                                                  |                                             |
|       s.copy()        | s의 얕은 복사본을 생성                                                |                                             |
| s.extend(t) or s += t | s의 가장 마지막에 t의 요소들을 이어붙임                               |                                             |
|        s \*= n        | s를 n번 반복한 값으로 바꿈                                            |                                             |
|     s.insert(i,x)     | s의 i 위치 바로 직후에 x를 삽입함                                               |                                             |
|  s.pop() or s.pop(i)  | s에서 i번째 요소를 반환하고 제거함</br>i가 주어지지 않았다면 마지막 값 |                                             |
|      s.remove(x)      | s에서 첫 번째로 나타난 x를 제거함                                     |                                             |
|      s.reverse()      | s를 뒤집은 값으로 바꿈                                                |                                             |

#### list comprehension(리스트 표현식)

- list를 생성할 때 식, for문, if문을 한 문장으로 묶어 생성하는 것
- `[expression for variable in list if statement]` 혹은 `list(expression for variable in list if statement)`형태로 표현할 수 있음

#### [list == array?](https://stackoverflow.com/questions/176011/python-list-vs-array-when-to-use)

- 자료구조 상으로 list와 배열은 엄연히 다른 존재이고 Python에서 `array`모듈을 별도로 지원
- 정의 상 다른 개념이지만 사용에 있어서는 거의 동치임
- Python에서 list는 상수시간에 작동할 수 있도록 구현되었지만 그 대가로 배열보다 많은 공간을 필요로 함
- `array`모듈은 C로 구현되었기 때문에 빠른 연산과 적은 메모리(특히 수학)가 필요할 때 사용

#### 다차원 list 생성 주의

- `[[] for i in range(x)]`와 `[[]] * x`는 다르게 작동함
  - sequence type의 `*`연산자는 복사가 되는 것이 아닌 여러 번 참조하는 연산자임

### tuple

- immutable sequence type, 일반적으로 서로 무관한 데이터의 집합을 저장
  - immutable하다는 것은 내부의 값이 수정될 수 없다는 것
    - 때문에 `O = (0,0)`에 대해 `O[0] = 1`이 오류를 일으킴
    - 하지만 `linear = ([0,0], [1,1])`에 대해 `O[0][1] = 1`은 가능함
  - tuple은 immutable하고 일반적으로 unpacking이나 indexing으로 접근할 수 있는 요소들의 무관한 sequence라면, list는 mutable하고 요소들이 일반적으로 동질적이며 iterating을 통해 접근할 수 있음
- 아래와 같이 선언할 수 있음
- tuple을 생성하는 것은 괄호가 아니고 comma임
  - 즉 빈 tuple을 생성하는 경우나 구문의 모호성을 피하기 위한 경우(함수 등 괄호를 사용하는 구문들에서)를 제외하면 괄호는 선택사항
  - 만약 `a = "hello",`등으로 tuple을 선언했다면 그 크기는 1임

### range

- 수들의 immutable sequence를 나타내는 자료형
  - for문에서 특정 횟수만큼 반복하기 위해 사용함
- range의 최대 장점은 같은 기능의 list와 tuple과 달리 메모리를 매우 적게 차지함
  - start, stop, step만 저장하고 필요할 때 계산함
- `range(stop)`혹은 `range(start=0, stop, step=1)`
  - 매개변수들은 반드시 정수형
  - step이 0이면 `ValueError`가 발생
  - `start + step*i`인 요소들을 반환하는데 step이 양수면 stop보다 작을 때까지, 음수면 클 때까지 반복
- sequence type이기 때문에 [Sequence Type 함수](https://github.com/Indigo-Coder-github/Python_Lecture/tree/main/%EC%B4%88%EA%B8%89%EB%B0%98%205%2C%206%EC%A3%BC%EC%B0%A8#sequence-type-%ED%95%A8%EC%88%98), [slicing](https://github.com/Indigo-Coder-github/Python_Lecture/tree/main/%EC%B4%88%EA%B8%89%EB%B0%98%205%2C%206%EC%A3%BC%EC%B0%A8#slicing), 음수를 통한 indexing 모두 지원
  - slicing과 음수를 통한 indexing은 3.2부터 지원

## Text Sequence Type

### string

- immutable sequence type, UTF-8로 인코딩함
- 아래와 같이 선언할 수 있음
  - python에서 큰 따옴표와 작은 따옴표의 차이는 아래의 경우를 제외하면 없으며 [개인의 취향에 따라 사용하거나 관습을 따르는 것 같음](https://stackoverflow.com/questions/56011/single-quotes-vs-double-quotes-in-python)
- 세 개의 따옴표로 묶으면 문자열의 줄바꿈도 허용함
- string의 formatting에 대해서는 [1주차의 내용을 참조](https://github.com/Indigo-Coder-github/Python_Lecture/tree/main/%EC%B4%88%EA%B8%89%EB%B0%98%201%EC%A3%BC%EC%B0%A8#format)

#### string 함수

- sequence type의 함수를 사용할 수 있고 아래의 함수들을 추가적으로 지원함

|       연산자       | 결과 | 비고 |
|:------------------:| ---- |:----:|
|  str.capitalize()  |      |      |
|   str.casefold()   |      |      |
|    str.center()    |      |      |
|    str.count()     |      |      |
|    str.encode()    |      |      |
|   str.endswith()   |      |      |
|  str.expandtabs()  |      |      |
|     str.find()     |      |      |
|    str.format()    |      |      |
|  str.format_map()  |      |      |
|    str.index()     |      |      |
|   str.isalnum()    |      |      |
|   str.isalpha()    |      |      |
|   str.isascii()    |      |      |
|  str.isdecimal()   |      |      |
|   str.isdigit()    |      |      |
| str.isidentifier() |      |      |
|   str.islower()    |      |      |
|  str.isnumeric()   |      |      |
| str.isprintable()  |      |      |
|   str.isspace()    |      |      |
|   str.istitle()    |      |      |
|   str.isupper()    |      |      |
|     str.join()     |      |      |
|    str.ljust()     |      |      |
|    str.lower()     |      |      |
|    str.lstrip()    |      |      |
|  str.partition()   |      |      |
| str.removeprefix() |      |      |
| str.removesuffix() |      |      |
|   str.replace()    |      |      |
|    str.rfind()     |      |      |
|    str.rindex()    |      |      |
|    str.rjust()     |      |      |
|  str.rpartition()  |      |      |
|    str.rsplit()    |      |      |
|    str.rstrip()    |      |      |
|    str.split()     |      |      |
|  str.splitlines()  |      |      |
|  str.startswith()  |      |      |
|    str.strip()     |      |      |
|   str.sapcase()    |      |      |
|    str.title()     |      |      |
|  str.translate()   |      |      |
|    str.upper()     |      |      |
|    str.zfill()     |      |      |

## Set Type

- hashable한 요소들로 구성된 순서가 없는 집합
- 일반적으로 sequence의 중복요소 제거, 교집합이나 합집합 등의 수학적 연산에 사용
- 다른 집합형 자료형들과 마찬가지로 `x in set`, `len(set)`, `for x in set`등을 지원
  - 삽입 순서에 대한 위치를 기록하지 않기 때문에 indexing, slicing 다른 sequence 같은 행동을 할 수 없음
- 아래와 같이 선언할 수 있음

### Set Type 함수

|            연산자             | 결과                                   |                        비고                        |     |
|:-----------------------------:| -------------------------------------- |:--------------------------------------------------:| --- |
|            len(s)             | s의 요소 수를 반환                     |                  s의 cardinality                   |     |
|            x in s             | s가 x의 멤버십인지 테스트              |                                                    |     |
|          x not in s           | s가 x의 멤버십이 아닌지 테스트         |                                                    |     |
|        s.isdisjoint(t)        | s가 t와 공통 원소가 없다면 True를 반환 | 두 집합이 서로소 집합이기 때문에 교집합이 공집합임 |     |
|         s.issubset(t)         | s가 t의 부분집합이면 True반환          |                  s<=t, s<t와 동치                  |     |
|        s.issuperset(t)        | s가 t의 상위집합이면 True반환          |                  s>=t, s>t와 동치                  |     |
|          s.union(t)           | s와 t의 합집합을 반환                  |                    s\|t와 동치                     |     |
|       s.intersection(t)       | s와 t의 교집합을 반환                  |                     s&t와 동치                     |     |
|        s.difference(t)        | s와 t의 차집합을 반환                  |                     s-t와 동치                     |     |
|   s.symmetric_difference(t)   | s와 t의 대칭차집합을 반환              |                     s^t와 동치                     |     |
|            copy()             |                                        |                                                    |     |
|           update()            |                                        |                                                    |     |
|     intersection_update()     |                                        |                                                    |     |
|      difference_update()      |                                        |                                                    |     |
| symmetric_difference_update() |                                        |                                                    |     |
|             add()             |                                        |                                                    |     |
|           remove()            |                                        |                                                    |     |
|           discard()           |                                        |                                                    |     |
|             pop()             |                                        |                                                    |     |
|            clear()            |                                        |                                                    |     |

### set

- mutable type

### frozenset

- immutable type
  - 생성되고 난 이후 내용을 바꿀 수 없음
  - dict type의 key로 사용할 수 있음

## Mapping Type

- mutable type, 임의의 값을 hashable한 값에 대응시키는 자료구조
  - Python 표준의 mapping type은 dictionary만 있음
  - list, dictionary 혹은 다른 mutable type은 hashable하지 않기 때문에 key로 사용할 수 없음

### dictionary

- Sequence 자료형과 달리 immutable 타입인 key에 대해 indexing이 이뤄짐
  - string, numeric은 항상 key가 될 수 있고 string, numeric, tuple을 요소로 하는 tuple도 key가 될 수 있음
- 아래와 같이 선언할 수 있음

#### hash table(hash map)

- 자료구조의 하나, key-value 쌍으로 구성된 요소에 대해 key에 hash function을 적용한 위치에 value를 저장하는 자료구조
  - hash function은 일반적으로 나머지 연산자(%, mod)를 많이 사용
- 탐색, 삽입, 삭제 모두 시간복잡도가 `O(1)`에 해당하지만 충돌이 발생할 수 있고 해시 함수의 성능에 영향을 많이 받으며 key-value 쌍이 아닌 자료구조에선 부적합할 수 있음

#### dictionary 함수

- [3.9 이상부터는 `|`연산과 `|=`연산을 지원하며 비교한 결과를 새로운 dictionary로 반환](https://docs.python.org/3/library/stdtypes.html#mapping-types-dict)
- 3.7 이상부터는 삽입 순서에 따른 순서를 보장하며 value가 바뀌었다고 순서가 바뀌진 않음

|             연산자              | 결과                                                                                                  |                   비고                    |
|:-------------------------------:| ----------------------------------------------------------------------------------------------------- |:-----------------------------------------:|
|             list(d)             | d의 key를 요소로 하는 list 반환                                                                       |                                           |
|             len(d)              | d의 요소의 수를 반환                                                                                  |                                           |
|            d\[key\]             | key를 key로 하는 d의 요소 반환                                                                        |                                           |
|        d\[key\] = value         | d\[key\]를 value로 설정                                                                               |                                           |
|          del d\[key\]           | d\[key\]를 d에서 제거                                                                                 |                                           |
|            key in d             | d의 key에 key가 있다면 True 반환, 아니면 False 반환                                                   |                                           |
|          key not in d           | not (key in d)와 동치                                                                                 |                                           |
|             iter(d)             | d의 key에 대한 iterator를 반환                                                                        |                                           |
|            d.clear()            | d의 모든 요소를 제거                                                                                  |                                           |
|            d.copy()             | d의 모든 요소를 얕은 복사해 반환                                                                      |                                           |
|       d.get(key, default)       | d의 key에 해당하는 value를 반환</br>만약 없다면 default로 준 값을 반환하며 주어지지 않았다면 예외 발생 |                                           |
|            d.items()            | d의 모든 요소를 (key, value)쌍 형태로 반환                                                            |        dictview 객체라는 특수 형태        |
|            d.keys()             | d의 key들에 대한 dictview를 반환                                                                      |                                           |
|       d.pop(key, default)       | d의 key에 대한 값을 반환하고 이를 제거                                                                |      default 인자는 get과 같은 역할       |
|           d.popitem()           | LIFO의 순서로 d의 아이템을 (key, value)쌍 형태로 반환                                                 | 3.7 이전에는 LIFO가 아닌 임의의 쌍을 반환 |
|           reversed(d)           | d의 key에 대한 뒤집힌 iterator를 반환                                                                 |             3.8 이상부터 지원             |
| d.setdefault(key, default=None) | d에 key가 있다면 그 값을 반환하고</br>없다면 default를 value로 하는 key를 삽입하고 default를 반환      |                                           |
|         d.update(other)         | d에 대해 other의 내용을 업데이트                                                                      |     other은 dict의 선언 형태를 따라감     |
|           d.values()            | d의 값에 대한 dictview를 반환                                                                         |                                           |

#### dictview 함수

- `dict.keys()`, `dict.values()`, `dict.items()`로 도출되는 자료형에 대한 함수

|       연산자       | 결과                                                     |                       비고                        |
|:------------------:| :--------------------------------------------------------: |:-------------------------------------------------:|
|   len(dictview)    | dictview의 크기 반환                                     |                                                   |
|   iter(dictview)   | dictview의 iterator를 반환                               | iterating 중에 삽입, 삭제 등을 실행하면 예외 발생 |
|   x in dictview    | x가 dictview에 있다면 True를 반환, 아니라면 False를 반환 |                                                   |
| reversed(dictview) | dictview에 대한 뒤집힌 iterator를 반환                   |                                                   |
