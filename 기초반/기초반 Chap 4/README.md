# Function(함수)
- 같은 기능을 제공하는 코드에 이름을 정의하여 반복해 사용할 수 있도록 하는 것
- `def function_name(parameters):`로 선언하고 내부에 작성한다.
	- parameter는 매개변수이며 argument와 혼용된다.
	- return은 선택 사항이다.
- python은 return 값을 복수로 받을 수 있으며 이 경우 tuple 형태로 반환된다.
	- return하는 값의 수와 이를 받는 변수의 수가 일치하면 각각에 대입된다.
		- return 값을 list로 줘도 적용된다. 
- parameter은 초기값을 지정해줄 수 있다.
	- 초기값을 지정한 parameter은 가장 마지막에 선언한다.
	- 해당 parameter에 지정된 값이 아닌 다른 값을 줄 수 있다.
- 함수를 호출할 때 `function_name(parameter_name=parameter_value)`형식으로 호출할 수 있다.
- 최종적으로 함수는 `def function_name(args, args=values, *args, **kwargs)`의 형태로 parameter를 선언한다.
## 가변 인수
- 함수의 인수를 가변적으로 사용할 수 있는 기능
	- 가변 인수라도 함수가 주어진 parameter를 모두 수용할 수 없거나 반대로 주어진 parameter가 모자라면 TypeError가 발생한다.
	- 가변 인수를 구현할 때 parameter 앞에 `*`를 붙이며 관습적으로는 `*args`로 표기한다.
	- 고정 인수와 함께 사용하고자 할 때는 고정 인수를 먼저 선언하고 가변 인수를 선언한다.
## 키워드 인수
- 함수의 인수를 key-value 쌍으로 사용할 수 있는 기능
	- parameter은 parameter 이름과 해당 parameter에 들어갈 값의 쌍으로 이뤄진 dictionary로 주어져야 한다.
	- 키워드 인수를 구현할 때 parameter 앞에 `**`를 붙이며 관습적으로는 `**kwargs`로 표기한다.
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
#### Immutable Object
- 데이터 값이 바뀔 때 현재 메모리에 대한 내용을 삭제하고 다른 위치에 새로 생성하는 객체
- mutable object를 제외한 모든 타입은 immutable object에 해당한다.
#### Mutable Object
- 데이터 값이 바뀔 때 현재 메모리에 대한 값을 수정하는 객체
	- 객체를 독립적으로 복사하려면 copy 함수를 사용하거나 `copy.deepcopy`를 통해 깊은 복사를 해줘야 한다.
	- `copy.deepcopy`가 `copy`에 비해 안전하게 깊은 복사를 한다.
-  list, set, dictionary, `@dataclass(frozen=True)`로 선언하지 않은 사용자 class가 해당한다.
### Instance(인스턴스)
- Class를 실체화한, 메모리에 실제로 할당된 실체
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
## Method(메서드)
- 객체의 행위를 정의한 것
	- 혹은 객체에게 전달할 수 있는 메시지를 나타내기도 한다.
	- operation, member function, instance method라는 용어와 혼용된다.
- instance의 메스드를 불러고자 하면 `instance.method_name(params)형식으로 불러온다.
- `KMeans`클래스에는 `fit_transform`이라는 메서드를 실행할 수 있다.
	- 위의 코드에서 `three_split_kmeans`라는 instance의 `fit_transform`이라는 행위를 가진다.
	- 혹은 `fit_transform`이라는 메시지를 보낼 수 있다.
### Static Method
- instance를 생성하지 않아도 접근할 수 있는 메서드
	- 인자로 `self`를 받지 않기 때문이다.
- `def`위에 `@staticmethod`구문을 먼저 써서 해당 메서드가 정적 메서드임을 나타낸다.
	- 일반적으로 유틸리티 함수를 만드는데 사용한다.
### Class Method
- instance를 생성하지 않아도 접근할 수 있으면서 클래스 속성, 클래스 메서드에 접근할 수 있는 메서드
- `def`위에 `@classmethod`구문을 먼저 써서 해당 메서드가 클래스 메서드임을 나타낸다.
	- 다른 메서드와 다르게 첫 parameter로 cls를 준다.
		- `cls`의 parameter 값은 클래스이기 때문에 이를 이용해 생성자를 오버로딩할 수 있다.
		- python에서는 생성자의 오버로딩을 지원하지 않기 때문에 `__init__`을 if-else문으로 구성하는 것이 아니라면 클래스 메서드를 이용해 구현한다.
### Magic Method(Special Method)
- 특별한 이름으로 정의되어 특별한 구문으로 호출하는 메서드
	- 오버로딩을 통해 커스터마이징할 수 있다.
- `__function_name__`형태이며 생성자와 소멸자인 `__init__`, `__del__`도 매직 메서드이다.
	- magic method에 따라서 wrapping된 구문이 있기도 하다.
- [공식 문서에 어마어마한 양이 나와있기 때문에 아래 코드에선 쓸만한 것들만 소개한다.](https://docs.python.org/3/reference/datamodel.html#special-method-names)
## self
- 자기자신을 가리키는 메서드의 첫 인자
	- 즉, instance를 말하며 클래스의 메서드가 호출될 때마다 첫 번째 인자로 넘겨줌으로써 어떤 instance의 메서드가 호출됐는지 구분한다.
	- 속성도 마찬가지로 구분한다.
	- 한편, 클래스 내부의 코드에서 같은 이름을 가진 변수에 대해 이것이 외부의 변수인지 아님 class의 변수인지 구분하는 역할을 한다.
# 객체지향 4대 특성
## 1. Encapsulation(캡슐화)
- 속성과 메서드를 하나의 객체 안에 묶는 개념
	- 이를 통해 추상화를 실현시키면서 내부 데이터를 보호하고 은닉한다.
	- 다만, 정보 은닉을 위한 수단으로 캡슐화를 사용할 순 있어도 캡슐화가 정보은닉을 항상 보장하진 않는다.
### Visibility(가시성), 접근 제한자
- 클래스 내부에 접근하는 것을 제한하는 구문
- Python은 공식적으로 접근 제한자를 지원하지 않으며 창시자인 귀도 반 로섬도 [이에 대해 지원하지 않을 것이라고 정확히 얘기함](https://stackoverflow.com/questions/7456807/should-i-use-name-mangling-in-python)
	- 즉, 모든 속성과 메서드는 public이다.
	- [PEP8에서는](https://peps.python.org/pep-0008/#method-names-and-instance-variables) non-public 메서드와 속성을 알려주고 싶다면 이름 앞에`_`를 사용할 수 있고 서브 클래스의 이름 충돌을 피하기 위해 `__`를 이름 앞에 붙일 수 있다고 설명한다.
		- 이름 앞에 `__`을 붙이는 것으로 private 처리를 할 수 있다고 알려져 있으나 실제로 코드를 실행하면 해당 속성을 찾을 수 없다고 나온다.
			- [내부적으로 `InstanceName._ClassName__AttributeName`, `InstanceName._ClassName__MethodName`](https://docs.python.org/3.11/reference/expressions.html?highlight=mangling#index-5)라는 이름으로 바뀌기 때문에 해당 형식에 맞춰 강제로 꺼낼 수 있다.
			- 이를 name mangling이라고 한다.
- 객체지향에서 접근 제한자는 public, private, protected로 나뉜다.
	- public은 어디에서든 클래스의 요소에 접근할 수 있다.
	- private는 클래스 내부에서만 요소에 접근할 수 있다.
	- protected는 클래스 내부, 상속받은 클래스, 같은 패키지 안에서 접근할 수 있다.
- 결론적으로 python의 내부 값 접근에는 제약 사항이 없다. 
## 2. Abstraction(추상화)
- 실세계를 추상화하여 공통적인 것을 추출하는 개념
- 캡슐화를 통해 상태와 행위를 하나로 묶어 추상화하며 이를 구현하고 실행할 떄 비로소 구체화된 객체로 나타난다.
## 3. Inheritance(상속)
- 하위 클래스가 상위 클래스의 속성과 메서드를 묵시적으로 소유한 것
	- 즉, 하위 클래스는 상위 클래스의 속성과 메서드를 불러올 수 있다.
	- 추상화할 수 있는 부분을 계층적으로 추상화하여 코드의 재사용성을 높인다.
	- `class ChildClass(ParentClass)`로 작성한다.
- 상위 개념의 클래스를 parent class(부모 클래스), base class(기반 클래스), super class(슈퍼 클래스), 상위 클래스라고 하며 하위 개념의 클래스를 child class(자식 클래스), derived class(파생 클래스), subclass(서브 클래스), 하위 클래스라고 한다.
	- 해당 자료에서는 상위 클래스와 하위 클래스로 용어를 통일했다.
- 메서드는 아래의 코드와 같이 하위 클래스의 instance가 상위 클래스의 메서드를 호출할 수 있다.
- 속성은 하위 클래스의 생성자에서 상위 클래스의 생성자를 호출해야만 사용할 수 있다.
	- 하위 클래스의 생성자가 생략된다면 상위 클래스의 생성자가 자동으로 호출된다.
### super 함수
- 단일 상속에 대해 상위 클래스의 정의 없이 이를 반환하거나 다중 상속에 대해 호출하고 싶은 상위 클래스를 명백히 하는데 사용하는 함수
	- `super().method_name()`을 하위 클래스에서 사용하여 상위 클래스의 메서드를 호출한다.
	- 다만 `super().method_name()`의 호출 시기에 따라 하위 클래스의 내용이 달라질 수 있는 것에 유의해야 한다.
		- 상위 클래스의 생성자를 호출하고 하위 클래스에서 이 값을 수정한 것은 상위 클래스에 반영되지 않는다.
### Generalization, Specialization(일반화, 상세화)
- 일반화는 하위 클래스로부터 상위 클래스를 추상화하는 방식이고 반대로 상세화는 상위 클래스로부터 하위 클래스를 작성하는 방식이다.
	- 이미 작성된 클래스로부터 공통 사항을 추출해 추상화하는 Bottom-Up 방식이 일반화, 매우 추상화된 클래스로부터 좀 더 구체적인 클래스를 작정하는 Top-Down 방식이 상세화이다.
### 포함 관계
- is-a관계면 상속 관계, has-a관계로 치환할 수 있다면 포함 관계이다.
	- 위에서 예시로 든 코드에서 "Soldier76 is a Champion"은 가능한 문장이므로 상속 관계로 나타낼 수 있다.
	- 예를 들어 내가 ChampionList를 만들고 싶다면 "ChampionList is a Champion"보다는 "ChampionList has a Champion"이 더 자연스러운 문장일 것이다. 이러한 has-a관계는 클래스의 속성에 여러 개의 instance를 저장하는 방식으로 구현한다.
### 다중상속
- 다른 객체지향 언어와 다르게 python은 직접적으로 다중 상속을 지원한다.
- `class ChildClass(ParentClass1, ParentClass2, ...)`로 작성한다.
![|480](https://dojang.io/pluginfile.php/13909/mod_page/content/3/068006.png)
- 문제는 다중상속이 위와 같이 다이아몬드 구조로 생성되면 같은 이름을 가진 메서드가 모든 클래스에 있을 때 가장 하위 클래스가 어떤 상위 클래스의 메서드를 호출해야 하는지 알 수 없다는 문제가 있다.
	- `ClassName.mro()`로 mro함수를 호출하면 메서드 호출 순서를 보여준다. 이를 통해 하위 클래스의 다중 상속 순서를 알 수 있다.
		- `class ChildClass(ParentClass1, ParentClass2, ...)`로 작성되었다면 `ParentClass1`부터 탐색한다.
		- 그러나 설계단계에서 이러한 복잡한 상속을 지양하도록 하는 것이 권장된다.
### Abstract Class(추상 클래스)
 - 메서드 목록만 가진 클래스
	 - 이 클래스를 상속받으면 이 클래스의 메서드 구현이 강제된다.
	 - 또한 추상로 instance를 만들 수 없다. 해당 클래스는 오로지 상속과 메서드 구현을 위한 상위 클래스로써만 작동한다.
	 - python에는 interface구현을 위한 키워드가 없기 때문에 abc로 구현하며 인터페이스라는 용어도 쓰이지 않는다.
 - abc라는 모듈을 불러와 생성하려는 추상클래스가 ABC를 상속받도록 하며 각 메서드는 `@abstractmethod`라는 데코레이터가 붙는다.
	 - 일부 자료에서는 추상클래스가 `metaclass=ABCMeta`로 상속받도록 표기해야 한다고 하지만 [실제 기능상 차이는 없다고 한다.](https://stackoverflow.com/questions/68569239/what-is-the-difference-between-abstractclassmetaclass-abcmeta-and-class-abstra)
## 4. Polymorphism(다형성)
- 객체의 메서드는 그 맥락에 따라 여러 역할을 수행할 수 있다는 개념
	- 다형성은 같은 이름을 가지면서 파라미터가 다른 메서드를 정의할 수 있게 하고 상위 클래스의 메서드를 하위 클래스에서 작성할 수 있도록 해준다.
		- 다형성을 제공하지 않는다면 코드의 낭비가 심할 것이다.
### Overloading
- 같은 클래스에서 이름이 같은 메서드에 대해 매개변수의 수와 유형을 달리하여 여러 개의 메서드로 정의하는 것
	- [[중급반 1주차 & 초급반 7주차#^be66e2|중급반 1주차에서 생성자 오버로딩에서 잠깐 설명했지만]] Python은 메서드 오버로딩을 지원하지 않음
		- python의 가변인자, 키워드인자가 사실 오버로딩의 정의와 일치한다. 다만 그것을 여러 개의 메서드로 정의하지 않았을 뿐이다.
		- python 3.4이상부터는 [`@singledispatch`](https://docs.python.org/3/library/functools.html#functools.singledispatch)라 불리는 데코레이터로 구현할 수 있으며 [`@multidispatch`](https://pypi.org/project/multipledispatch/)는 라이브러리로 있다. python 3.5이상부터는 type hint를 사용했다면 `typing`모듈을 불러와 `@typing.overload`라는 데코레이터를 사용할 수 있다.
			- `@typing.overload`데코레이터는 단순히 type hint이기 때문에 다른 type hint와 마찬가지로 정적 타입을 보장하지 않는다.
		- `@multidispatch`를 사용하여 오버로딩을 구현하는 것은 다른 언어의 오버로딩 구현과 동일하기 때문에 아래 예제 코드는 키워드인자를 이용해 구현했다.
### Overriding(함수 재정의)
- 상위 클래스에서 정의된 메서드가 하위 클래스에서 같은 이름의 다른 내용을 가진 정의로 재정의하는 것
	- 상위 클래스에서 작성한 메서드의 내용은 무시된다.
	- 상위 클래스의 메서드 내용을 활용하고 새로운 내용을 추가하려면 `super().method_name()`을 하위 클래스의 메서드에 추가하면 된다. 