# Sequence Type
- iterator를 지원하는 타입
## Sequence Type 함수
|     연산자     | 결과                                                                                                            | 비고 |
|:--------------:| --------------------------------------------------------------------------------------------------------------- |:----:|
|     x in s     | x가 s에 존재하면 True, 아니면 False                                                                             |      |
|   x not in s   | x가 s에 존재하지 않으면 True, 아니면 False                                                                      |      |
|     s + t      | s와 t를 연결                                                                                                    |immutable sequence 타입은 새로운 객체를 생성하기 때문에<br>$O(n^2)$의 시간복잡도를 가짐<br>range 등의 일부 sequence type은 지원되지 않음      |
|     s \* n or n \* s      | s를 n번 연결                                                                                                    |range 등의 일부 sequence type은 지원되지 않음      |
|     s\[i\]     | s의 i번째 요소 반환                                                                                             |      |
|     len(s)     | s의 길이                                                                                                        |      |
|     min(s)     | s에서 가장 작은 요소 반환                                                                                       |      |
|     max(s)     | s에서 가장 큰 요소 반환                                                                                         |      |
| s.index(x,i,j) | s에서 첫 번째로 나타나는 x를 찾아 그 index를 반환<br>i와 j는 선택사항이며 설정하면 i번째부터 j-1번째까지에서 탐색 |x를 찾지 못했다면 ValueError 발생<br>s\[i:j\].index(x)와 동치이지만 슬라이싱된 리스트 기준의 index를 반환      |
|s.count(x)                |s에서 x가 나타난 횟수를 반환                                                                                                                 |      |
```python
country_list = ["Angola", "Begium", "Chile", "Denmark", "England"]
print(country_list.index("Chile", 1), country_list[1:].index("Chile"))
#Output:2 1
```
## slicing
- Ada, Go, Python 등 일부 언어에서 지원하는 배열에 대한 독특한 기능
- `s[i:j:k]`로 표시하며 i에서 j-1까지의 요소를 반환
	- k는 선택 사항이며 설정하면 k만큼 건너뛰면서 반환
	- i나 j가 음수라면 마지막 요소부터 역순으로 가리킴
		- 그러나 -0은 0으로 취급하기 때문에 가장 마지막의 요소는 음수로 -1임
## list
- mutable sequence type, 일반적으로 비슷한 요소의 집합을 저장함
- 아래와 같이 선언할 수 있음
```python
using_bracket_pair = []
using_bracket_comma = ["a", "b", "c"]
using_list_comprehension = [x for x in [1,2,3]]
using_constructor = list("list")
```
- `list()`를 이용한 list 선언은 아래와 같이 이뤄짐
```python
str_to_list = list("abc") #["a", "b", "c"]
tuple_to_list = list((1, 2, 3)) #[1, 2, 3]
blank_list = list() #[]
```
### list 함수
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
|  s.pop() or s.pop(i)  | s에서 i번째 요소를 반환하고 제거함<br>i가 주어지지 않았다면 마지막 값 |                                             |
|      s.remove(x)      | s에서 첫 번째로 나타난 x를 제거함                                     |                                             |
|      s.reverse()      | s를 뒤집은 값으로 바꿈                                                |                                             |
### list comprehension(리스트 표현식)
- list를 생성할 때 식, for문, if문을 한 문장으로 묶어 생성하는 것
- `[expression for variable in list if statement]` 혹은 `list(expression for variable in list if statement)`형태로 표현할 수 있음
```python
university_list = ["Seoul National", "Korea", "Yonsei", "Sugang", "Sungkyunkwan", "Hanyang", "Chungang", "KyungHee", "HUFS", "Seoul", "Konkuk", "Dongguk", "Hongik", "Kookmin", "Soongsil", "Sejong", "Dankook", "Kwangwoon", "Myongji", "Sangmyung", "Gachon", "Hansung", "Seokyeong", "Sahmyook"]
print([university for university in university_list if "k" in university])
#Ouput:['Sungkyunkwan', 'Konkuk', 'Dongguk', 'Hongik', 'Kookmin', 'Dankook', 'Seokyeong', 'Sahmyook']
```
### [list == array?](https://stackoverflow.com/questions/176011/python-list-vs-array-when-to-use)
- 자료구조 상으로 list와 배열은 엄연히 다른 존재이고 Python에서 `array`모듈을 별도로 지원
- 정의 상 다른 개념이지만 사용에 있어서는 거의 동치임
	- Python에서 list는 상수시간에 작동할 수 있도록 구현되었지만 그 대가로 배열보다 많은 공간을 필요로 함
	- `array`모듈은 C로 구현되었기 때문에 빠른 연산과 적은 메모리(특히 수학)가 필요할 때 사용
### 다차원 list 생성 주의
- `[[] for i in range(x)]`와 `[[]] * x`는 다르게 작동함
	- sequence type의 `*`연산자는 복사가 되는 것이 아닌 여러 번 참조하는 연산자임
```python
multiple_list = [[None, None]] * 3
multiple_list[0][0] = 1
print(multiple_list)
#Output:[[1, None],[1, None],[1, None]]
comprehension_list = [[None, None] for _ in range(3)]
comprehension_list[0][0] = 1
print(comprehension_list)
#Output:[[1, None],[None, None],[None, None]]
```
## tuple
- immutable sequence type, 일반적으로 서로 무관한 데이터의 집합을 저장
	- immutable하다는 것은 내부의 값이 수정될 수 없다는 것
		- 때문에 `O = (0,0)`에 대해 `O[0] = 1`이 오류를 일으킴
		- 하지만 `linear = ([0,0], [1,1])`에 대해 `O[0][1] = 1`은 가능함
	- tuple은 immutable하고 일반적으로 unpacking이나 indexing으로 접근할 수 있는 요소들의 무관한 sequence라면, list는 mutable하고 요소들이 일반적으로 동질적이며 iterating을 통해 접근할 수 있음
- 아래와 같이 선언할 수 있음
```python
using_parenthese_pair = ()
using_trailing_comma = "a",
using_trailing_comma = ("a",)
using_commas_itmes = "a","b","c"
using_commas_itmes = ("a","b","c")
#생성자의 매개변수는 iterable한 자료형이라면 무관함
using_constructor = tuple("tuple") #("t","u","p","l","e")
```
- tuple을 생성하는 것은 괄호가 아니고 comma임
	- 즉 빈 tuple을 생성하는 경우나 구문의 모호성을 피하기 위한 경우(함수 등 괄호를 사용하는 구문들에서)를 제외하면 괄호는 선택사항
	- 만약 `a = "hello",`등으로 tuple을 선언했다면 그 크기는 1임
## range
- 수들의 immutable sequence를 나타내는 자료형
	- for문에서 특정 횟수만큼 반복하기 위해 사용함
- range의 최대 장점은 같은 기능의 list와 tuple과 달리 메모리를 매우 적게 차지함
	- start, stop, step만 저장하고 필요할 때 계산함
- `range(stop)`혹은 `range(start=0, stop, step=1)`
	- 매개변수들은 반드시 정수형
	- step이 0이면 `ValueError`가 발생
	- `start + step*i`인 요소들을 반환하는데 step이 양수면 stop보다 작을 때까지, 음수면 클 때까지 반복
```python
#parameter에 따른 반환되는 range의 변화
print(list(range(10)))
#Output:[0,1,2,3,4,5,6,7,8,9]
print(list(range(1,10)))
#Output:[1,2,3,4,5,6,7,8,9]
print(list(range(1,10,2)))
#Output:[1,3,5,7,9]
print(list(range(10,1,-1)))
#Output:[10,9,8,7,6,5,4,3,2,1]
print(list(range(10,1,-2)))
#Output:[10,8,6,4,2]
#range slicing
print(list(range(1,10)[1:]))
#Output:[2,3,4,5,6,7,8,9]
```
- sequence type이기 때문에 [Sequence Type 함수](https://github.com/Indigo-Coder-github/Python_Lecture/tree/main/%EC%B4%88%EA%B8%89%EB%B0%98%205%2C%206%EC%A3%BC%EC%B0%A8#sequence-type-%ED%95%A8%EC%88%98), [slicing](https://github.com/Indigo-Coder-github/Python_Lecture/tree/main/%EC%B4%88%EA%B8%89%EB%B0%98%205%2C%206%EC%A3%BC%EC%B0%A8#slicing), 음수를 통한 indexing 모두 지원
	- slicing과 음수를 통한 indexing은 3.2부터 지원
```python
r = range(1,10)
#in 접근
print(11 in r)
#Output:False
print(r.index(5))
#Output:4
print(r[:5])
#Output:range(1,6)
#range의 slicing은 값이 담긴 형태가 아닌 range의 형태를 반환
```
- 3.3부터는 `==`과 `!=`연산도 지원하며 결과 값에 대해 검사함
```python
print(range(10) == range(0,10,1))
#Output:True
```
# Text Sequence Type
## string
- immutable sequence type, UTF-8로 인코딩함
- 아래와 같이 선언할 수 있음
	- python에서 큰 따옴표와 작은 따옴표의 차이는 아래의 경우를 제외하면 없으며 [개인의 취향에 따라 사용하거나 관습을 따르는 것 같음](https://stackoverflow.com/questions/56011/single-quotes-vs-double-quotes-in-python)
```python
single_quote = 'This allows "double quote".'
double_quote = "This allows 'single quote'."
triple_single_quote = '''Triple single quote'''
triple_double_quote = """Triple doulbe quote"""
```
- 세 개의 따옴표로 묶으면 문자열의 줄바꿈도 허용함
- string의 formatting에 대해서는 [1주차의 내용을 참조](https://github.com/Indigo-Coder-github/Python_Lecture/tree/main/%EC%B4%88%EA%B8%89%EB%B0%98%201%EC%A3%BC%EC%B0%A8#format)
### string 함수
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

# Set Type
- hashable한 요소들로 구성된 순서가 없는 집합
- 일반적으로 sequence의 중복요소 제거, 교집합이나 합집합 등의 수학적 연산에 사용
- 다른 집합형 자료형들과 마찬가지로 `x in set`, `len(set)`, `for x in set`등을 지원
	- 삽입 순서에 대한 위치를 기록하지 않기 때문에 indexing, slicing 다른 sequence 같은 행동을 할 수 없음
- 아래와 같이 선언할 수 있음
```python
prime_set = {2,3,5,7,11}
#frozenset의 인자로는 iterable한 자료가 올 수 있음
prime_frozen_set = frozenset({2,3,5,7,11})
even_set_with_comprehension = {i for i in range(20) if i%2 == 0}
#빈 set는 {}로 선언할 수 없음
#{}로 선언하면 빈 dictionary로 인식
empty_set = set()
```
## Set Type 함수
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
## set
- mutable type
## frozenset
- immutable type
	- 생성되고 난 이후 내용을 바꿀 수 없음
	- dict type의 key로 사용할 수 있음
# Mapping Type
- mutable type, 임의의 값을 hashable한 값에 대응시키는 자료구조
	- Python 표준의 mapping type은 dictionary만 있음
	- list, dictionary 혹은 다른 mutable type은 hashable하지 않기 때문에 key로 사용할 수 없음
## dictionary
- Sequence 자료형과 달리 immutable 타입인 key에 대해 indexing이 이뤄짐
	- string, numeric은 항상 key가 될 수 있고 string, numeric, tuple을 요소로 하는 tuple도 key가 될 수 있음
- 아래와 같이 선언할 수 있음
```python
key_value_pair_braces = {"Korea":"Seoul", "USA":"Washington D.C.", "Japan":"Tokyo", "China":"Beijing"}
dict_comprehension = {x: x**2 for x in range(15)}
dict_constructor_1 = dict([("Korea", "Seoul"), ("USA", "Washington D.C."), ("Japan", "Tokyo"), ("China", "Beijing")])
dict_constructor_2 = dict(Korea="seoul", USA="Washington D.C.", Japan="Tokyo", China="Beijing")
```
### hash table(hash map)
- 자료구조의 하나, key-value 쌍으로 구성된 요소에 대해 key에 hash function을 적용한 위치에 value를 저장하는 자료구조
	- hash function은 일반적으로 나머지 연산자(%, mod)를 많이 사용
- 탐색, 삽입, 삭제 모두 시간복잡도가 `O(1)`에 해당하지만 충돌이 발생할 수 있고 해시 함수의 성능에 영향을 많이 받으며 key-value 쌍이 아닌 자료구조에선 부적합할 수 있음
### dictionary 함수
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
|       d.get(key, default)       | d의 key에 해당하는 value를 반환<br>만약 없다면 default로 준 값을 반환하며 주어지지 않았다면 예외 발생 |                                           |
|            d.items()            | d의 모든 요소를 (key, value)쌍 형태로 반환                                                            |        dictview 객체라는 특수 형태        |
|            d.keys()             | d의 key들에 대한 dictview를 반환                                                                      |                                           |
|       d.pop(key, default)       | d의 key에 대한 값을 반환하고 이를 제거                                                                |      default 인자는 get과 같은 역할       |
|           d.popitem()           | LIFO의 순서로 d의 아이템을 (key, value)쌍 형태로 반환                                                 | 3.7 이전에는 LIFO가 아닌 임의의 쌍을 반환 |
|           reversed(d)           | d의 key에 대한 뒤집힌 iterator를 반환                                                                 |             3.8 이상부터 지원             |
| d.setdefault(key, default=None) | d에 key가 있다면 그 값을 반환하고<br>없다면 default를 value로 하는 key를 삽입하고 default를 반환      |                                           |
|         d.update(other)         | d에 대해 other의 내용을 업데이트                                                                      |     other은 dict의 선언 형태를 따라감     |
|           d.values()            | d의 값에 대한 dictview를 반환                                                                         |                                           |
### dictview 함수
- `dict.keys()`, `dict.values()`, `dict.items()`로 도출되는 자료형에 대한 함수

|       연산자       | 결과                                                     |                       비고                        |
|:------------------:| -------------------------------------------------------- |:-------------------------------------------------:|
|   len(dictview)    | dictview의 크기 반환                                     |                                                   |
|   iter(dictview)   | dictview의 iterator를 반환                               | iterating 중에 삽입, 삭제 등을 실행하면 예외 발생 |
|   x in dictview    | x가 dictview에 있다면 True를 반환, 아니라면 False를 반환 |                                                   |
| reversed(dictview) | dictview에 대한 뒤집힌 iterator를 반환                   |                                                   |

# Loop(반복문)
## for
- Sequence type의 요소를 순서대로 반복하는 구문
- `for *variables in *sequences:`형태로 사용
- [zip 함수에 대해서는 중급반 3주차 자료를 참조](https://github.com/Indigo-Coder-github/Python_Lecture/tree/main/%EC%A4%91%EA%B8%89%EB%B0%98%203%EC%A3%BC%EC%B0%A8#zipiterables-strictfalse)
```python
for i in range(5):
    print(i, end="")
#Output:12345
#변수의 수만큼 sequence 자료가 있다면
#zip 함수를 이용해 unpacking 할 수 있음
president_list = ["이승만", "박정희", "최규하", "전두환", "노태우", "김영삼", "김대중", "노무현", "이명박", "박근혜", "문재인", "윤석열"]
for i, name in zip((range(1, len(president_list)+1), president_list)):
    print(f"대한민국 {i}번째 대통령은 {name}이다.")
```
## while
- 조건식만 만족하면 무한히 반복하는 구문
- `while condition:`형태로 사용하면 condition이 True라면 while문을 실행, False이면 다음 코드를 실행
	- 만약 condition을 True 값으로 주면 무한루프
	- 무한루프가 상황에 따라 필요(ex. 기기 간 통신 등 상황 유지가 필요한 경우)할 수도, 의도치 않은 상황일 수도 있음(ex. 잘못된 조건으로 인한 무한 출력 등)
```python
my_list = [4,9,3,8,1,6,4]
while my_list:
    print(my_list.pop(my_list.index(max(my_list))))
#my_list의 요소를 큰 것부터 차례로 pop하면서 출력
```
## break, else, pass, continue
- break는 가장 가까운 반복문을 종료시킴
	- else문이 있다면 else도 생략함
- else는 반복문이 모두 종료된 뒤 실행됨
	- 즉, break가 발생했다면 실행되지 않고 break가 발생하지 않았다면 실행되기 때문에 break 발생 여부를 따로 검사할 필요가 없음
- pass는 실행할 코드가 없음을 나타냄
	- 반복문뿐 아니라 코드블록이 있는 곳 어디든 실행할 코드가 없음을 나타내기 위해서 사용할 수 있음
- continue는 현재의 상태를 종료하고 반복문의 시작 위치로 돌아가 다음 상태를 실행함
### else-break 코드 예시
```python
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, "equals", x, "*", n//x)
            break
    else:
        print(n, "is a prime number")
    #else문을 없애면 모든 수가 소수라고 출력됨
```
### pass, continue 코드 예시
```python
for i in range(10):
    if i % 2 == 0:
        pass #continue로 바꾼 것과 결과가 다름
        print(i)
```