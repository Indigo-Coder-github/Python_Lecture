# [break, continue, pass](https://github.com/Indigo-Coder-github/Python_Lecture/tree/main/%EC%B4%88%EA%B8%89%EB%B0%98%205%2C%206%EC%A3%BC%EC%B0%A8#break-else-pass-continue)
# Assignment Expression(:=)
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
## global
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
# Meta Class
# Asyncio
# Multithreading