# [Match-Case 문](https://github.com/Indigo-Coder-github/Python_Lecture/tree/main/초급반%203%2C%204주차#condition-statement조건문)
# [Type Hint](https://docs.python.org/3.12/library/typing.html)
- python 3.5에서부터 지원하는 사항
- **python 실행 환경에서는 함수와 변수의 자료형에 대해 강제하지 않기 때문에 type checker, IDE, linter 등에서 사용되는 third party tool의 성격이다.**
	- IDE에서 변수에 type hint를 적용하면 해당 변수에서 불러올 수 있는 내부 요소를 바로 파악할 수 있다.
- `def function_name(parameter: type) -> return_type`으로 표기한다.
```python
def sqrt(val: int) -> float:
    return val**0.5

#type hint는 자료형을 강제하지 않음
print(sqrt(1), sqrt(1.0))
#Output 1 1.0
```
## Type aliases(타입 별칭)
- `TypeAliasType`의 instance로써 type 구문을 이용해 사용자 지정 타입을 만들 수 있음
	- 다만 버전 호환성 때문에 3.12 이전의 호환성을 위해서는 문법이 조금 상이함
	- Python 3.9 이전에는 typing class의 하위 클래스로 중복되어 존재했지만 현재는 내장 타입과 호환되도록 변경되었음
```python
#Python 3.12
type Vector = list[float]
#~Python 3.11
from typing import TypeAlias
Vector: TypeAlias = list[float]
#혹은 Vector = list[float]
```
- 이러한 타입별칭은 복잡한 타입힌트를 생성하는데 도움이 됨
```python
#구버전의 호환성을 위해 type 키워드를 사용하지 않음
Coordinate = list[float, float]
BuildingName = str
BuildingInfo = tuple[BuildingName, Coordinate]

def search_address(building_info: BuildingInfo) -> str:
	pass
#Type aliases를 사용하지 않았다면
#def search_address(building_info: tuple[str,list[float, float]]) -> str:
```
## Typing Module
- Python의 Type Hint와 관련하여 지원하는 모듈로써 `NewType`, `Generic`, `Any` 등의 구문을 지원함
	- *Python이 동적 언어이기 때문에 사실 이렇게까지 자세한 Type Hint를 사용해야 하나라는 개인적인 생각*
# User Defined Exception
- Python에서 정의한 Exception을 `raise`를 통해 발생시킬 수 있음
- Numpy, Pandas 등의 라이브러리 소스코드에서 많이 보게 되는 코드
```python
def validate_probability(x: float) -> bool:
    if 0 <= x <= 1: return True
    else: raise ValueError("The variable of probability must be 0 to 1.")

any_numbers = [0.1, 0.3, 0.5, 1.2]
#try-except 구문을 사용하지 않는다면 사용자가 정의한 에러 메시지 출력
for i in any_numbers:
    validate_probability(i)
#Output: The variable of probability must be 0 to 1.
#raise의 최대 장점은 try-except에서 예외 처리를 위한 코드를 작성하지 않아도 됨
#다시 말해, 예외처리가 필요한 부분에 일일이 try-except를 작성하지 않아도 됨
try:
    for i in any_numbers:
        validate_probability(i)
except Exception as e:
    print("다음과 같은 예외가 발생: ", e)
#Output: 다음과 같은 예외가 발생: The variable of probability must be 0 to 1.
```
- 혹은 Exception class를 상속 받아 사용자 지정 class를 만들 수 있음
```python
class ValidateProbability(Exception):
    def __init__(self):
        super().__init__("The variable of probability must be 0 to 1.")

any_numbers = [0.1, 0.3, 0.5, 1.2]

try:
    for i in any_numbers:
        if not (0<=i<=1): raise ValidateProbability
except Exception as e:
    print("다음과 같은 예외가 발생: ", e)
#Output: 다음과 같은 예외가 발생: The variable of probability must be 0 to 1.
```
# Assert
- raise를 좀 더 간소화한듯한 버전
- `assert condition, message if condition is False`형태로 작성하며 `AssertionError`가 발생함
```python
def validate_probability(x: float) -> bool:
    assert 0 <= x <= 1, "The variable of probability must be 0 to 1."
    return True
```
## [Raise, Assert, Try의 차이와 활용](https://stackoverflow.com/questions/40182944/whats-the-difference-between-raise-try-and-assert)
- Assert는 주어진 조건문이 웬만하면 지켜질 것이라는 믿음이 있기 때문에 빠르게 반례를 잡기 위해 사용
- Raise는 사용자 지정 예외를 만들 수 있다는 점, [re-Raise를 발생시킬 수 있는 점이 있음](https://dojang.io/mod/page/view.php?id=2400)
- Try-Except는 프로그램을 강제 종료하지 않고도 (혹은 다른 코드를 실행하고자 한다면) 예외처리를 할 수 있음
# [내장 함수](https://docs.python.org/3/library/functions.html)
- [초급반 3,4주차](https://github.com/Indigo-Coder-github/Python_Lecture/tree/main/초급반%203%2C%204주차)와 [5,6주차](https://github.com/Indigo-Coder-github/Python_Lecture/tree/main/초급반%205%2C%206주차) 자료에서 소개된 함수들 중 일부도 내장함수에 해당함
- 외워놓는다면 유용하겠지만 반드시 그럴 필요는 없음
	- 구글링과 ChatGPT만으로도 괜찮은 코드가 나옴
- 공식문서에서는 해당 함수와 동치인 코드도 달아두었음
## `all(iterable)`
- parameter는 iterable 객체를 받으며 이 객체에 요소가 하나라도 없다면 False를, 요소가 모두 있다면 True를 반환
## `any(iterable)`
- parameter 는 iterable 객체를 받으며 이 객체에 요소가 하나라도 있으면 True를, 하나도 없다면 False를 반환
## `delattr/getattr/hasattr/setattr(object, name)`
- `delattr(object, name: str)`은 instance인 object의 name인 속성을 제거
	- instance의 속성을 제거하기 때문에 다른 instance에 영향을 미치지 않는다.
- `getattr(object, name: str, default=None)`는 instance인 object에 name인 속성이 있다면 그 값을 반환하고 없다면 default로 준 값을 반환함
	- default가 None이라면 `Attribute`에러가 발생함
- `hasattr(object, name: str) -> Boolean`은 instance인 object에 name인 속성이 있다면 True를 반환하고 그렇지 않다면 False를 반환함
	- `getattr`로 구현했음
- `setattr(obejct, name: str, value)`는 instance인 object에 name인 속성을 만들고 value를 할당함
## `dir()/dir(object)`
- `__dir__()`을 구현했다면 해당 함수의 return을 반환
	- 구현하지 않았다면 `__dict__` 속성을 통해 가능한 한 정보를 취합하며 정확하지 않을 수 있음
## `enumerate(iterable, start=0)`
- iterable 객체의 전체 요소에 대해 start 값으로 시작하는 enumerate 객체를 반환
	- 이를 list로 변환하면 `[(start, iterable[start]), (start+1, iterable[start+1])...]`형태로 변환됨
	- `range`를 쓰는 것보다 pythonic한 방식
## `eval(expression)/exec(object)`
- eval 함수는 expression에 python에서 작동할 수 있는 식을 입력해 실행할 수 있음
	- 그러나 디버깅하기 난해하고 injection attack의 위험이 있어 권장되지 않음
- exec 함수는 object에 python에서 작동할 수 있는 코드를 입력해 동적으로 실행할 수 있음
## `filter(function, iterable)`
- iterable 객체 function의 결과가 참인 경우의 요소만 가지는 iterator를 구축함
## `id(object)`
- 객체의 id를 반환
	- id는 객체가 살아있는 동안 부여되는 독특한 int 상수
## `map(function, iterable)`
- iterable 객체의 모든 요소에 function을 적용한 iterator를 반환
## `reversed(seq)`
- `__reversed__()`메서드를 반드시 가지거나 [시퀀스 규약을](https://docs.python.org/3/library/functions.html#reversed)지키는 객체를 뒤집은 iterator를 반환함
## `sorted(iterable, key=None, reverse=False)`
- iterable 객체의 요소들이 오름차순으로 정렬된 새로운 list를 반환
	- key로 정렬의 기준을 내장 함수나 lambda 등의 함수로 정의함
	- reverse로 True를 주면 내림차순으로 정렬
## `zip(*iterables, strict=False)`
- 파라미터로 제공한 iterable 객체들을 동시에 순회하여 tuple로 반환함
	- 길이가 가장 짧은 iterable 객체를 따라감
		- strict 값을 True로 준다면 ValueError를 발생시킴
- lazy하기 때문에 iterate를 처리하기 전까지 zip 함수가 실제로 실행되지 않음