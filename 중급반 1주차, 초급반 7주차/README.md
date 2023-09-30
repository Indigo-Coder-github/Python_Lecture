# Function(함수)
 - 같은 기능을 제공하는 코드에 이름을 정의하여 반복해 사용할 수 있도록 하는 것
 - `def function_name(parameters):`로 선언하고 내부에 작성한다.
	 - parameter는 매개변수이며 argument와 혼용된다.
	 - return은 선택 사항이다.
```python
def making_bread(ingredient):
	if ingredient == "egg": return "egg bread"
	elif ingredient == "apple": return "apple pie"
def bread_recipe():
	print("Put an ingredient you want!")

bread_recipe()
print(making_bread("egg"))
#Output: "Put an ingredient you want!" "egg bread"
```
 - python은 return 값을 복수로 받을 수 있으며 이 경우 tuple 형태로 반환된다.
	 - return하는 값의 수와 이를 받는 변수의 수가 일치하면 각각에 대입된다.
		 - return 값을 list로 줘도 적용된다. 
```python
def making_all_bread():
	return "egg bread", "apple pie"
print(making_all_bread())
#Output:("egg bread", "apple pie")
kims_bread, kangs_bread = making_all_bread()
print(kims_bread,kangs_bread)
#Output:"egg bread", "apple pie"
```
 - parameter은 초기값을 지정해줄 수 있다.
	 - 초기값을 지정한 parameter은 가장 마지막에 선언한다.
	 - 해당 parameter에 지정된 값이 아닌 다른 값을 줄 수 있다.
 - 함수를 호출할 때 `function_name(parameter_name=parameter_value)`형식으로 호출할 수 있다.
```python
def show_food_list(ingredients, food="sushi"):
	for ingredient in ingredients: print("{}_{}".format(ingredient, food))
show_food_list(["salmon", "tuna", "shrimp"], "sashimi")
#Output:salmon_sashimi tuna_sashimi shrimp_sashimi
```
 - 최종적으로 함수는 `def function_name(args, args=values, *args, **kwargs)`의 형태로 parameter를 선언한다.
## 가변 인수
 - 함수의 인수를 가변적으로 사용할 수 있는 기능
	 - 가변 인수라도 함수가 주어진 parameter를 모두 수용할 수 없거나 반대로 주어진 parameter가 모자라면 TypeError가 발생한다.
	 - 가변 인수를 구현할 때 parameter 앞에 `*`를 붙이며 관습적으로는 `*args`로 표기한다.
	 - 고정 인수와 함께 사용하고자 할 때는 고정 인수를 먼저 선언하고 가변 인수를 선언한다.
```python
def show_food_list(food, *args):
	for ingredient in args: print("{}_{}".format(ingredient, food))
show_food_list("sushi", "salmon", "tuna", "shrimp")
#Output:salmon_sushi tuna_sushi shrimp_sushi
ingredient_list = ["salmon", "tuna", "shrimp"]
show_food_list("sushi", *ingredient_list)
#Output:salmon_sushi tuna_sushi shrimp_sushi
```
## 키워드 인수
 - 함수의 인수를 key-value 쌍으로 사용할 수 있는 기능
	 - parameter은 parameter 이름과 해당 parameter에 들어갈 값의 쌍으로 이뤄진 dictionary로 주어져야 한다.
	 - 키워드 인수를 구현할 때 parameter 앞에 `**`를 붙이며 관습적으로는 `**kwargs`로 표기한다.
```python
def show_food_list(**kwargs):
	if "food" in kwargs and "ingredient" in kwargs:
		print("{}_{}".format(kwargs["ingredient"], kwargs["food"]))
show_food_list(**{"food":"pizza", "ingredient":"pineapple"})
#Output:pineapple_pizza
```
# Objected Oriented Programming (OOP)
 - 프로그래밍 패러다임의 하나
 - 절차지향 언어로 객체지향 언어를 흉내내려면 GOTO문을 남발해야 했고 이는 코드의 가독성을 해치고 버그가 늘어나는 원인이 됐다.
 - [좋은 라이브러리 문서들은 클래스의 파라미터, 속성, 메서드, 예제 코드 등을 잘 정리하여 보여준다.](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html)
## Class(클래스)
 - 같은 attribute와 method를 가진 객체들을 추상화한 것
	 - 다시 말해 instance를 정의한 프로그램
### Object(객체)
 - Class가 실체화할 대상
 - Python의 모든 것은 객체이다! 다른 언어는 primitive type과 객체 타입이 구분되어있는 것과는 차이점이 있다.
	 - C++, Java 등은 primitive type과 이에 대한 wrapper class가 따로 구분된다.
		 - numpy도 wrapper class를 사용했으나 신규 사용자들의 혼동으로 인해 1.20부터 deprecated되어 python의 data type으로 통합됐다.
	 - 때문에 python에서 형변환을 하면 입력 값에 대해 해당하는 class의 새로운 instance를 생성한다.
		 - 이 부분은 일본에서 개발된 프로그래밍 언어인 Ruby와 일맥상통한다.
	 - 인터프리터라는 점과 더불어 python의 속도가 느린 이유 중 하나로 꼽는다.
```python
a=1
type(a)
#Ouput:<class 'int'>
b=str(a)
#b와 a의 자료형도 다르고 메모리 주소도 다름
#python에서는 형변환보단 객체의 클래스가 바뀌었다고 하는 것이 엄밀한 표현
print(id(a)==id(b))
#Output:False
help(int)
#int형에 대한 도움말
```
#### Immutable Object
 - 데이터 값이 바뀔 때 현재 메모리에 대한 내용을 삭제하고 다른 위치에 새로 생성하는 객체
 - mutable object를 제외한 모든 타입은 immutable object에 해당한다.
```python
a=(1,2,3)
a[0]=2
#Output:TypeError
```
#### Mutable Object
 - 데이터 값이 바뀔 때 현재 메모리에 대한 값을 수정하는 객체
	 - 객체를 독립적으로 복사하려면 copy 함수를 사용하거나 `copy.deepcopy`를 통해 깊은 복사를 해줘야 한다.
	 - `copy.deepcopy`가 `copy`에 비해 안전하게 깊은 복사를 한다.
 -  list, set, dictionary, `@dataclass(frozen=True)`로 선언하지 않은 사용자 class가 해당한다.
```python
from copy import deepcopy
a=[1,2]
b, c = a, deepcopy(a)
b+=[3,4]
c+=[5,6]
print(a,b,c)
#Output:[1,2,3,4],[1,2,3,4],[1,2,5,6]
```
### Instance(인스턴스)
 - Class를 실체화한, 메모리에 실제로 할당된 실체
```python
#PEP8에서 클래스 이름을 UpperCamelCase를 따를 것을 권장
#구체적으로 정확하게 지칭할 수 있는 단수형 명사를 사용할 것을 권장
#다만 시스템에서 많이 사용하는 단어는 지양
class Stock:
	def __init__(self):
		pass
	def buy(self):
		pass
	def sell(self):
		pass

samsung = Stock()
lg = Stock()
posco = Stock()
```
 - `samsung`, `lg`, `posco`는 모두 `Stock`이라는 클래스의 Object이다.
	 - 이 Object들을 추상화하면 `Stock`이라는 클래스를 만들 수 있다.
 - 동시에 각각은 `Stock` 클래스의 instance이다.
```python
from sklearn.cluster import KMeans

two_split_kmeans = KMeans(n_clusters=2)
three_split_kmeans = KMeans(n_clusters=3)
four_split_kmeans = KMeans(n_clusters=4)
```
 - `two_split_kmeans`, `three_split_kmeans`, `four_split_kmeans` 모두 KMeans라는 클래스의 Object이다.
	 - 이 Object들을 추상화하면 KMeans라는 클래스를 만들 수 있다.
 - 동시에 각각은 `KMeans` 클래스의 instance이다.
## Attribute(속성)
 - 객체에 저장된 자료의 특성과 이름을 정의한 것
	 - instance의 상태, 정보를 나타낸다.
	 - property, member variable, instance variable 이라는 용어와 혼용된다.
 - instance의 속성을 불러고자 하면 `instance.attribute_name`형식으로 불러온다.
```python
class Stock:
	def __init__(self, code):
		self.code = code
		self.price = 68400
samsung = Stock("005930")
print(samsung.code, samsung.price)
#Output:005930, 68400
```
 - `Stock` 클래스에는 `code`와 `price`라는 자료가 저장되어있다.
	 - `samsung`이라는 instance의 `code`는 005930으로 입력했고 `price`는 68400으로 초기화한다.
```python
print(two_split_kmeans.n_clusters)
#Output:2
```
 - `KMeans`클래스에는 `n_clusters`라는 자료가 저장되어있다.
	 - 위의 코드에서 `two_split_kmeans`라는 instance의 `n_clusters`는 2로 입력했다.
### Constructor(생성자)
 - `__init__`함수는 Python에서 생성자인 특별 함수이며 instance가 생성될 때 그 instance의 속성들을 초기화한다.
 - `*args`와 `*kwargs`으로 초기화할 수 있다.
### Destructor(소멸자)
 - `__del__`함수를 통해 구현하며 `del samsung`을 통해 불러온다.
	 - 대부분의 프로그래밍 언어에서 그렇듯이 Python도 Garbage Collector를 통해 객체가 관리된다.
### Class Variable
 - 한 클래스에서 탄생한 모든 instance가 공유하는 공통의 속성
	 - 쉽게 얘기해 클래스 버전의 전역변수이다.
	 - 클래스 속성이라는 용어와 혼용된다.
 - instance가 생성될 때 생성되는 것이 아니므로 `class_name.variable_name`으로 참조할 수 있다.
```python
class Stock:
	market = "KOSPI"
print(samsung.market, lg.market, posco.market)
#Output:"KOSPI" "KOSPI" "KOSPI"
Stock.market = "KOSDAQ"
print(samsung.market, lg.market, posco.market)
#Output:"KOSDAQ", "KOSDAQ", "KOSDAQ"
```
## Method(메서드)
 - 객체의 행위를 정의한 것
	 - 혹은 객체에게 전달할 수 있는 메시지를 나타내기도 한다.
	 - operation, member function, instance method라는 용어와 혼용된다.
 - instance의 메스드를 불러고자 하면 `instance.method_name(params)형식으로 불러온다.
```python
class Stock:
	def sell(self, count):
		return self.price*count
	def buy(self, price):
		return self.price//price
print(samsung.sell(100), samsung.buy(68400))
#Ouput:6840000 1
```
 - `Stock`이라는 클래스는 `sell`과 `buy`라는 행위를 할 수 있다.
	 - 혹은 `samsung` instance에 `sell`과 `buy`라는 메시지를 보낼 수 있다.
```python
three_split_kmeans.fit_transform()
#Output:2
```
 - `KMeans`클래스에는 `fit_transform`이라는 메서드를 실행할 수 있다.
	 - 위의 코드에서 `three_split_kmeans`라는 instance의 `fit_transform`이라는 행위를 가진다.
	 - 혹은 `fit_transform`이라는 메시지를 보낼 수 있다.
### Static Method
 - instance를 생성하지 않아도 접근할 수 있는 메서드
	 - 인자로 `self`를 받지 않기 때문이다.
 - `def`위에 `@staticmethod`구문을 먼저 써서 해당 메서드가 정적 메서드임을 나타낸다.
	 - 일반적으로 유틸리티 함수를 만드는데 사용한다.
```python
class Math:
	@staticmethod
	def tan(x,y):
		return y/x
```
### Class Method
 - instance를 생성하지 않아도 접근할 수 있으면서 클래스 속성, 클래스 메서드에 접근할 수 있는 메서드
 - `def`위에 `@classmethod`구문을 먼저 써서 해당 메서드가 클래스 메서드임을 나타낸다.
	 - 다른 메서드와 다르게 첫 parameter로 cls를 준다.
		 - `cls`의 parameter 값은 클래스이기 때문에 이를 이용해 생성자를 오버로딩할 수 있다.
		 - python에서는 생성자의 오버로딩을 지원하지 않기 때문에 `__init__`을 if-else문으로 구성하는 것이 아니라면 클래스 메서드를 이용해 구현한다.
```python
Class Stock:
	@classmethod
	def from_tuple(cls, tup):
		return cls(tup[0])
	@classmethod
	def from_list(cls, lis):
		return cls(lis[0])
	@classmethod
	def show_market(cls):
		return cls.market
samsung_from_tuple = Stock.from_tuple(("005930"))
samsung_from_list = Stock.from_list(["005930"])
print(Stock.show_market())
#Output:"KOSPI"
```
### Magic Method(Special Method)
 - 특별한 이름으로 정의되어 특별한 구문으로 호출하는 메서드
	 - 오버로딩을 통해 커스터마이징할 수 있다.
 - `__function_name__`형태이며 생성자와 소멸자인 `__init__`, `__del__`도 매직 메서드이다.
	 - magic method에 따라서 wrapping된 구문이 있기도 하다.
 - [공식 문서에 어마어마한 양이 나와있기 때문에 아래 코드에선 쓸만한 것들만 소개한다.](https://docs.python.org/3/reference/datamodel.html#special-method-names)
```python
class Stock:
	def __add__(self, target):
		return self.price + target.price
	def __sub__(self, target):
		return self.price - target.price
	def __mul__(self, target):
		return self.price * target.price
	def __truediv__(self, target):
		return self.price/target.price
lg = Stock("066570");lg.price=100900
print(samsung+lg, samsung-lg, samsung*lg, samsung/lg)
#Output:169300 -32500 6901560000 0.6778989098116948
```
## self
 - 자기자신을 가리키는 메서드의 첫 인자
	 - 즉, instance를 말하며 클래스의 메서드가 호출될 때마다 첫 번째 인자로 넘겨줌으로써 어떤 instance의 메서드가 호출됐는지 구분한다.
	 - 속성도 마찬가지로 구분한다.
	 - 한편, 클래스 내부의 코드에서 같은 이름을 가진 변수에 대해 이것이 외부의 변수인지 아님 class의 변수인지 구분하는 역할을 한다.