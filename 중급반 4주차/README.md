# [break, continue, pass](https://github.com/Indigo-Coder-github/Python_Lecture/tree/main/%EC%B4%88%EA%B8%89%EB%B0%98%205%2C%206%EC%A3%BC%EC%B0%A8#break-else-pass-continue)
# Assignment Expression(:=)
- Python 3.8부터 지원하는 기능
	- `:=`가 바다코끼리를 닮았다고 해서 Walrus Operator라고도 불림
- `variable := expression`으로 선언
	- 변수의 재사용성과 가독성을 높이고 코드 줄 수를 줄임
	- 아래와 같은 형태로 작성할 수 있음
```python
import requests
#request에 대한 코드를 받아와 할당시키면서 값이 200이 넘는지 검사
#넘는다면 response를 출력
if (response := requests.get("https://www.naver.com")) > 200:
    print(response)
#아래는 위의 코드와 동치인 코드
response = requests.get("https://www.naver.com")
if response > 200: print(response)
#list comprehension 예시
#데이터의 합을 구하고 평균과 분산을 각각 구한 list
data = [1,2,3,4,5,6]
[y := sum(data), y//len(data), sum([i**2 for i in data])//len(data) - (y//len(data))**2]
#Output:[21, 3, 6]
def f(x): return x%2
even_data = [y for x in data if(y := f(x) == 0)]
#Output:[2, 4, 6]
```
- 다만, 단순 할당이나 재할당 형태는 모호성이나 혼란을 피하기 위해 무효한 구문으로 설정되어있거나 유효하더라도 권장하지 않음
```python
def f(x): pass
#아래 예시들은 불가능한 assignment expression임
y := f(x)
y0 = y1 := f(x)
g(x=y:=f(x))
```
# Iterator(반복자)
- 클래스에 구현된 `__iter__`메서드를 호출해 반환된 객체
	- 내장 라이브러리인 [itertools](https://docs.python.org/3/library/itertools.html)는 iterator에 대한 더 효율적이고 다양한 기능을 지원함
## Iterable Object(반복 가능한 객체)
- `__iter__`와 `__next__` 메서드를 가진 객체
	- iterator protocol을 지원한다고 말하기도 함
- `__iter__`메서드를 호출해 반환된 iterator는 `__next__`메서드를 통해 값에 차례대로 접근할 수 있음
	- 더 이상 꺼낼 값이 없을 때 `__next__`메서드를 호출하면 StopIteration 예외가 발생함
	- 즉, 반복문이 Iterable Object에 접근할 때 `__iter__` 메서드로 Iterator를 생성하고 `__next__`메서드를 이용해 순차적으로 접근함
- `__getitem__`메서드를 구현하면 index로 접근할 수 있음
- Iterator는 그 자체로 하나의 객체 형태이기 때문에 iterable object와 용어를 분리해서 사용할 필요가 있음
```python
class CityMap:
    def __init__(self, stop):
        self.city_list = ["Seoul", "Busan", "Incheon", "Jeonju"]
        self.current = 0#현재 값/위치를 나타낼 값
        self.stop = stop #iterating을 끝낼 값

    def __iter__(self):
        return self #인스턴스 자체를 반환

    def __next__(self):
        if self.current < self.stop:
            r = self.city_list[self.current]
            self.current += 1
            return r
        else: raise StopIteration

    def __getitem__(self, index):
        if index < self.stop: return self.city_list[index]
        else: raise IndexError

for i in CityMap(4):
    print(i)
#Output:Seoul
#       Busan
#       Incheon
#       Jeonju
print(CityMap(4)[0])
	#Output:Seoul
```
## 반환값 무시
- unpacking을 하는데 있어서 `_`를 사용하면 해당 위치의 값을 반환받는 것을 무시할 수 있음
```python
_, t = range(2)
print(t) #Output:1
#아래와 같이 반복문의 변수를 사용하지 않고
#단순히 반복하고자 한다면 _를 이용해 응용할 수 있음
for _ in range(10):
    my_input = input()
```
## lazy evaluation(지연 평가)
- 실행할 때 값을 계산하는 방식
- 메모리를 절약하거나 성능 상의 이점을 가질 수 있음
- [비교 연산이 그 예시 중 하나](https://github.com/Indigo-Coder-github/Python_Lecture/tree/main/%EC%B4%88%EA%B8%89%EB%B0%98%203%2C%204%EC%A3%BC%EC%B0%A8#%EB%B9%84%EA%B5%90-%EC%97%B0%EC%82%B0%EC%9E%90)
# Generator(발생자)
- iterator를 생성해주는 함수
	- class 단에서 구현하고자 하면 iterator를, 함수 단에서 구현하고자 하면 generator를 사용
	- 또한 generator와 달리 `__next__()`메서드의 반환 값이 yield의 값으로 정해져 있음
- return 부분을 `yield value`나 `yield from iterable_object`로 대체하여 구현함
	- return의 성격을 지니기 때문에 값이 반환된 이후 다시 generator를 호출하기 전까지 함수 바깥의 코드가 실행됨
- 일반 함수, 혹은 다른 방식으로 비슷한 방식을 구현할 수 있지만 [매우 큰 메모리가 필요한 작업을 lazy한 방식으로 실행할 수 있음](https://stackoverflow.com/questions/102535/what-can-you-use-generator-functions-for/)
```python
def extract_text_in_html(html: str):
    return_list = list()
    while "<t>" in html:
        start_idx, end_idx = html.index("<t>"), html.index("</t>")
        return_list.append(html[start_idx+3:end_idx])
	    html = html[end_idx+4:]
	yield from return_list
html = "<h1>This is first header</h1><t>This is first paragraph</t><h2>This is second header</h2><t>This is second paragraph</t>"

for text in extract_text_in_html(html):
    print(text)
    print("Here is not in function")
#Output:This is first paragraph
#       Here is not in function
#       This is second paragraph
#       Here is not in function
```
# Lambda(람다식, 익명함수)
- 이름을 붙이지 않은 객체가 마치 함수 객체처럼 행동한다고 하여 익명함수라고도 함
- `lambda paramters: expression`형태로 표현
	- 익명함수이기 때문에 이 식은 객체 자체이고 반환 값을 받고자 하면 변수를 선언해야 함
		- 혹은 `(lambda paramters: expression)(parameter_value)`를 통해 바로 값을 받을 수도 있음
	- expression은 한 줄로만 표현이 가능해야 함
```python
for string in "this sentence needs upper function":
    print((lambda x: x.upper())(string), end="")
#Output:THIS SENTENCE NEEDS UPPER FUNCTION
#function을 paramter로 받는 함수와 결합해 사용할 수 있음
person_list = ["John: Male", "Elizabeth: Female", "Henry: Male", "Jessica: Female"]
male_list = (list(filter(lambda x: x if "Male" in x else None, person_list)))
print(male_list)
#Output:["John: Male", "Henry: Male"]
```
# Closure
- 자신을 둘러싼 scope의 상태 값을 기억하는 함수
- 아래의 세 가지 조건을 만족해야 함, 만족하지 않는다면 단순히 중첩 함수에 해당함
	1. 어떤 함수의 내부 함수이어야 함(중첩 함수)
		- lambda를 반환하는 함수도 closure에 해당함
	2. 외부 함수의 변수 반드시 참조하고 있음
	3. 외부 함수는 이 내부 함수를 반환해야 함
```python
def shoot(bullet: int):
    maganize = bullet
    def burst():
        print(maganize - 3)
    return burst
f = shoot(40)
f() #Output:37
```
- f가 shoot을 호출하면 burst를 반환받으며 shoot이 종료되는데 burst는 shoot의 로컬 변수를 참조하고 있음
	- closure은 내부 함수가 이런 환경을 동적으로 저장하도록 하는 역할
- closure은 전역변수를 남발하지 않게 하고 데이터 은닉의 효과도 지님
	- 특정 scope나 코드블럭에서만 특정 변수를 사용할 수 있게 하는 기능이 없다면 전역변수의 책임소재가 불명확해짐
## scope
- 접근할 수 있는 변수의 범위
	- global scope면 코드 전체에서 접근할 수 있고 이러한 변수는 global variable(전역 변수)
	- local scope면 변수가 생성된 범위에서만 접근할 수 있고 이러한 변수는 local variable(지역 변수)
### global
- local scope에서 global variable을 호출하기 위해 사용하는 구문
	- global을 남발하면 변수의 사용 범위가 꼬이면 코드의 가독성이 떨어지고 버그가 많이 생김
		- 때문에 이러한 구문을 남발하지 않도록 설계하는 것이 중요함
		- 이를 가능하게 하는 것이 closure
```python
maganize = 40
def shoot():
    global maagnize
    maganize -= 1
shoot()
shoot()
print(maganize)#Output: 38
#global을 선언하지 않으면 local variable인 magnize를 찾을 수 없다는 오류 발생
```
## 중첩 함수
- 함수 내 함수를 정의하면 외부 함수가 내부 함수를 호출해야 내부 함수가 정상적으로 작동함
	- 함수 자체를 호출할 때 내부 함수는 호출할 수 없기 때문에 외부 함수를 호출해야 함
- 한편, 내부 함수는 외부 함수의 지역변수에 접근할 수 있음
	- read-only이기 때문에 값의 수정은 불가능
```python
def shoot():
    def show_remain_bullet():
        maganize = 39
        print(maganize)
    return show_remain_bullet
f = shoot()
f() #Output:39
```
### nonlocal
- 내부 함수가 외부 함수의 local variable을 접근하기 위해 사용하는 구문
```python
def shoot():
    maganize = 40
    def burst():
        nonlocal maganize
        maganize -= 3
    shoot()
    return maganize
print(shoot())#Output:37
```
## First Class Object(일급 객체)
- 아래의 조건을 모두 만족하는 객체
	1. 할당 명령문의 대상
	2. `==`연산의 대상
	3. 함수의 파라미터가 될 수 있음
	4. 함수의 반환 값이 될 수 있음
- Python에서 함수 또한 일급객체이기 때문에 위의 조건을 만족함
# Decorator(장식자)
- 함수를 장식하는, @로 시작하는 구문
- 함수를 매개변수로 받아 이를 실행하는 내부 함수인 wrapper 함수가 정의되어 있음
	- 메서드에 Decorator를 사용하고자 하면 wrapper 함수와 내부 함수의 첫 번째 매개변수는 self를 줘야 함
- 한 함수에 대해 Decorator를 여러 개 지정해줄 수 있음
	- 실행되는 Decorator는 위에서부터 아래임
- Decorator 또한 함수이기 때문에 매개변수를 받을 수 있음
	- 매개변수를 받는 함수가 맨 처음에 정의되고 그 내부에 함수를 매개변수로 받는 함수가 정의됨
```python
import time

#만드려는 데코레이터가 매개변수를 받는다면
#데코레이터를 상위함수로 하는 
#def run_iteratonally(num_iteration: int)
def estimate_execution_time(func):
    #인자로 받는 함수에 매개변수(가변인수, 키워드인수도 포함)가 있다면
    #wrapper와 내부 함수도 마찬가지로 작성
    def wrapper(needed_sorting):
        start = time.time()
        sorted_list = func(needed_sorting)
        end = time.time()
        print(end-start)
        #함수의 return이 있다면 wrapper함수에도
        #반드시 return을 작성해야함
        return sorted_list
	return wrapper

@estimate_execution_time
def selection_sort(arr: list) -> list:
	last_idx = len(arr)-1
	while last_idx > 0:
		max_value, max_idx = max(arr[:last_idx]), arr.index(max(arr[:last_idx]))
		arr[last_idx], arr[max_idx] = max_value, arr[last_idx]
		last_idx -= 1
	return arr

needed_sorting = [6,1,5,2,4,3]
print(selection_sort(needed_sorting))
#선택정렬의 결과가 출력되고 실행시간이 출력됨
```
## `__call__`
- 클래스 단에서 Decorator를 생성해주는 매직 메서드
- 사용 방법은 함수 단에서 Decorator를 생성하는 것과 대동소이하며 더 자세한 내용은 [링크를 참고](https://dojang.io/mod/page/view.php?id=2431)
```python
import time

class EstimateTime:
    def __init__(self, func):W
        self.func = func

    def __call__(self, *args, **kwargs):
        start = time.time()
        sorted_list = self.func(*args, **kwargs)
        end = time.time()
        print(end-start)
        return sorted_list

@EstimateTime
def selection_sort(arr: list) -> list:
	last_idx = len(arr)-1
	while last_idx > 0:
		max_value, max_idx = max(arr[:last_idx]), arr.index(max(arr[:last_idx]))
		arr[last_idx], arr[max_idx] = max_value, arr[last_idx]
		last_idx -= 1
	return arr

needed_sorting = [6,1,5,2,4,3]
print(selection_sort(needed_sorting))
```
## Property
- 객체지향의 [접근 제한자](https://github.com/Indigo-Coder-github/Python_Lecture/tree/main/%EC%A4%91%EA%B8%89%EB%B0%98%202%EC%A3%BC%EC%B0%A8%2C%20%EC%B4%88%EA%B8%89%EB%B0%98%208%EC%A3%BC%EC%B0%A8#visibility%EA%B0%80%EC%8B%9C%EC%84%B1-%EC%A0%91%EA%B7%BC-%EC%A0%9C%ED%95%9C%EC%9E%90)에 대해 객체의 속성 접근은 getter와 setter라는 메서드를 통해 이뤄짐
	- getter는 속성의 값을 read, setter는 속성의 값을 write
- 그러나 앞서 설명한 바와 같이 Python에 접근 제한자라는 개념이 없기 때문에 getter, setter를 쓰는 것은 Pythonic하지 않으나 사용하고자 한다면 `@property` decorator를 통해 구현할 수 있음
	- 결국 모든 속성에 대해 getter와 setter를 모두 작성해줘야 하기 때문에 property를 사용하는 것도 재사용성이 좋지 않음
	- 재사용성을 극단적으로 높이기 위해서는 [getattr, setattr](https://github.com/Indigo-Coder-github/Python_Lecture/tree/main/%EC%A4%91%EA%B8%89%EB%B0%98%203%EC%A3%BC%EC%B0%A8#delattrgetattrhasattrsetattrobject-name)을 사용해 구현할 수 있으며 [이를 극단적으로 줄일 수 있는 방법에 대해서는 이 링크를 참조](https://dojinkimm.github.io/python/2019/08/24/effective-python-5.html)
	- 이에 대한 자세한 설명은 [링크의 질문의 두 번째 답변을 참조](https://stackoverflow.com/questions/2627002/whats-the-pythonic-way-to-use-getters-and-setters)
```python
class Database:
    def __init__(self):
        self.__total_data = 0 #name mangling

    @property
    def total_data(self):
        return self.__total_data

    @property.setter
    def total_data(self, value):
        self.__total_data = value

db = DataBase()
print(db.total_data) #Output:0
db.total_data = 10
```
# Meta Class
- 클래스를 만드는 클래스로 두 가지의 구현 방법이 있음
	- type을 사용하여 동적으로 클래스를 생성
	- type을 상속받아서 메타클래스를 구현
- 추상 클래스도 메타 클래스 방식 중 하나
- Python의 Singleton Pattern을 구현하고자 할 때 Meta Class를 사용할 수 있으며 이에 대해서는 [코딩도장과](https://dojang.io/mod/page/view.php?id=2468) [이러한 글들을 참고](https://jh-bk.tistory.com/43)
## type을 사용해 동적을 생성
- `class_name = type("class_name", parent_class: tuple, attr_and_methods: dict)`로 클래스를 지정해 instance를 생성
	- 메서드는 람다식으로 작성할 수 있음
```python
def return_db_size(self):
    return self.total_data
Database = type("Database", (), {"total_data": 0, "return_db_size": return_db_size})
db = Database()
print(db.return_db_size())
#Output 0
```
## type을 상속받은 메타클래스
### `__new__`
- 메타클래스로 새 클래스를 만들 때 호출되는 메서드
```python
class MetaDatabase(type):
	#메타 클래스 자체를 인자로 주기 때문에
	#self가 아닌 metacls를 관습적으로 사용
    def __new__(metacls, name, bases, namespace):
        namespace["total_data"] = 0
        #lambda를 사용하고자 하면 parameter로 self를 줘야 함
        namespace["return_db_size"] = lambda self: self.total_data
        return type.__new__(metacls, name, bases, namespace)

DataBase = MetaDatabase("DataBase",(),{}) #먼저 메타클래스로 클래스를 생성
db = DataBase() #그 후에 클래스로 객체 생성
print(db.return_db_size()) #Output:0
```