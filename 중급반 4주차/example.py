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

#def f(x): pass
##아래 예시들은 불가능한 assignment expression임
#y := f(x)
#y0 = y1 := f(x)
#g(x=y:=f(x))

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
 
_, t = range(2)
print(t) #Output:1
#아래와 같이 반복문의 변수를 사용하지 않고
#단순히 반복하고자 한다면 _를 이용해 응용할 수 있음
for _ in range(10):
    my_input = input()
    
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

for string in "this sentence needs upper function":
    print((lambda x: x.upper())(string), end="")
#Output:THIS SENTENCE NEEDS UPPER FUNCTION
#function을 paramter로 받는 함수와 결합해 사용할 수 있음
person_list = ["John: Male", "Elizabeth: Female", "Henry: Male", "Jessica: Female"]
male_list = (list(filter(lambda x: x if "Male" in x else None, person_list)))
print(male_list)
#Output:["John: Male", "Henry: Male"]

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

def shoot(bullet: int):
    maganize = bullet
    def burst():
        print(maganize - 3)
    return burst
f = shoot(40)
f() #Output:37

maganize = 40
def shoot():
    global maagnize
    maganize -= 1
shoot()
shoot()
print(maganize)#Output: 38
#global을 선언하지 않으면 local variable인 magnize를 찾을 수 없다는 오류 발생

def shoot():
    def show_remain_bullet():
        maganize = 39
        print(maganize)
    return show_remain_bullet
f = shoot()
f() #Output:39

def shoot():
    maganize = 40
    def burst():
        nonlocal maganize
        maganize -= 3
    shoot()
    return maganize
print(shoot())#Output:37

class Database:
    def __init__(self):
        self.__total_data = 0 #name mangling
        
    @property
    def total_data(self):
        return self.__total_data
    
    @property.setter
    def total_data(self, value):
        self.__total_data = value

db = Database()
print(db.total_data) #Output:0
db.total_data = 10

def return_db_size(self):
    return self.total_data
Database = type("Database", (), {"total_data": 0, "return_db_size": return_db_size})
db = Database()
print(db.return_db_size())
#Output 0

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