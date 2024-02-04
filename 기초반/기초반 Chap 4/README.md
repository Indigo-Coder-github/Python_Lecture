# 기초반 4차시

## 1. Function(함수)

- 반복적으로 사용하는 코드에 이름을 붙여 추상적으로 사용하도록 한 것
- `def function_name(parameters): code_block (with return)`로 선언하며 `function_name(parameters)`로 사용한다.
  - parameter는 매개변수라고 하며 argument와 인자라고 한다.
    - [parameter는 선언할 때 사용하는 변수이고 argument는 함수를 호출할 때 parameter에 전달하는 데이터이다.](https://stackoverflow.com/questions/156767/whats-the-difference-between-an-argument-and-a-parameter) 하지만 두 단어가 일반적으로 혼용된다.
    - 함수를 선언할 때 parameter의 초기값을 선언할 수 있으며 함수를 호출할 때 argument를 전달하지 않았다면 초기값을 값으로 가진다.
  - return은 선택 사항이다.
    - Python에서 함수는 복수의 값을 반환할 수 있으며 이 경우 tuple 형태로 반환한다.
    - 반환하는 값의 수와 이를 받는 변수의 수가 일치하면 unpacking이 이뤄진다. 일치하지 않으면 예외가 발생한다.
- `function_name(parameter_name=parameter_value)`로 호출한다.
- 최종적으로 함수는 `def function_name(args, args=default, *args, **kwargs)`의 형태로 parameter를 가진다.

## 2. Objected Oriented Programming (OOP, 객체지향 프로그래밍)

- 프로그래밍 패러다임의 하나
  - 절차 형태의 코드와 필드 형태의 코드와 데이터를 담을 수 있는 객체라는 것을 기반으로 하는 패러다임이다.

### 2-1. Class(클래스)

- 공통의 속성과 행위를 가진 객체들을 추상화한 것
  - 다시 말해 instance를 정의한 코드이다.

### 2-2. Object(객체)

- Class가 실체화할 대상
- Python의 모든 것은 객체이다! 다른 언어는 Primitive Type과 Object Type이 구분되어있는 것과는 차이점이 있다.
  - C++, Java 등은 Primitive type과 이에 대한 wrapper class가 따로 구분된다.
    - numpy도 wrapper class를 사용했으나 신규 사용자들의 혼동으로 인해 1.20부터 deprecated되어 python의 data type으로 통합됐다.
  - 때문에 Python에서 형변환은 입력 값에 자료형이 단순히 바뀌는 것이 아니라 해당 자료형의 새로운 instance를 생성한다.
    - 이 부분은 일본에서 개발된 프로그래밍 언어인 Ruby와 일맥상통한다.
  - 인터프리터라는 점과 더불어 Python의 속도가 느린 이유 중 하나로 꼽는다.

#### 2-2-1. Immutable Object

- 데이터 값이 바뀔 때 현재 메모리 위치의 내용을 삭제하고 다른 위치에 새로 생성하는 객체
- Mutable Object를 제외한 모든 타입은 Immutable Object에 해당한다.
  - 때문에 tuple은 요소를 수정할 수 없다.

#### 2-2-2. Mutable Object

- 데이터 값이 바뀔 때 현재 메모리에 대한 값을 수정하는 객체
- list, set, dictionary, `@dataclass(frozen=True)`로 선언하지 않은 사용자 class가 해당한다.

##### shallow copy, deep copy(얕은 복사, 깊은 복사)

- Mutable Object는 객체가 저장된 위치와 객체 내부의 값이 저장된 위치가 서로 다르기 때문에 등호, slicing, `mutable_object.copy()`, `copy.copy(mutable_object)`을 사용하면 얕은 복사가 이뤄진다.
  - 얕은 복사는 원래의 변수와 새로 생성한 변수 모두 같은 객체가 저장되어 있다.
  - 때문에 한 변수의 내용을 수정하면 다른 변수의 내용도 똑같이 수정된다.
  - Immutable Object는 그 특징 때문에 얕은 복사와 깊은 복사에 대해 다루지 않아도 된다.
- `copy.deepcopy(mutable_obejct)`를 사용하면 깊은 복사가 이뤄진다.
  - 깊은 복사는 새로 생성된 변수가 원래의 변수 내용을 전부 다른 위치에 복사시킨다.

### 2-3. Instance(인스턴스)

- Class를 실체화한, 메모리에 실제로 할당된 객체

#### 2-3-1. Constructor(생성자)

- instance가 생성될 때 그 instance의 속성들을 초기화하는 method
- `__init__()`은 Python에서 생성자인 magic method이다.

#### 2-3-2. Destructor(소멸자)

- instance가 소멸할 때 작동하는 method
  -`__del__()`은 Python에서 소멸자인 magic method이며 `del samsung`형태로 호출한다.
  - 대부분의 프로그래밍 언어처럼 Python도 Garbage Collector를 통해 객체의 소멸 시점을 관리하기 때문에 특별한 사유가 없는 한 소멸자를 임의로 사용하지 않아도 된다.

### 2-4. Property(속성)

- 객체에 저장된 자료의 특성과 이름을 정의한 것
  - instance의 상태와 정보를 나타낸다.
- attribute, member variable, instance variable 등의 용어와 혼용된다.
- `instance.attribute_name`형태로 호출한다.

#### 2-4-1. Class Variable(클래스 속성)

- 한 클래스에서 탄생한 모든 instance가 공유하는 공통의 속성
  - 쉽게 얘기해 클래스 버전의 전역변수이다.
- class가 생성될 때 생성되는 속성이기 때문에 `class_name().class_variable_name`으로 참조할 수 있다.

### 2-5. Method(메서드)

- 객체의 행위를 정의한 것 혹은 객체에게 전달할 수 있는 메시지
  - operation, member function, instance method 등의 용어와 혼용된다.
- `instance.method_name(params)`형태로 호출한다.

#### 2-5-1. Static Method

- instance를 생성하지 않아도 접근할 수 있는 메서드
  - 인자로 `self`를 받지 않는다.
- 메서드를 정의한 코드 위에 `@staticmethod`를 써서 해당 메서드가 정적 메서드임을 나타낸다.
  - 일반적으로 유틸리티 함수를 만드는데 사용한다.

#### 2-5-2. Class Method

- instance를 생성하지 않아도 접근할 수 있으면서 클래스 속성, 클래스 메서드에 접근할 수 있는 메서드
  - 즉, static method는 클래스 속성, 클래스 메서드에 접근할 수 없다.
- 메서드를 정의한 코드 위에 `@classmethod`를 써서 해당 메서드가 클래스 메서드임을 나타낸다.
  - 다른 메서드와 다르게 첫 parameter를 `cls`로 정의한다. `cls`는 클래스 그 자체를 의미한다.

#### 2-5-3. Magic Method(Special Method)

- 특별한 이름으로 정의되어 특별한 구문으로 호출하는 메서드
  - 오버라이딩을 통해 커스터마이징할 수 있다.
- `__function_name__()`형태이며 생성자와 소멸자인 `__init__()`, `__del__()`도 매직 메서드이다.
  - 경우에 따라서 `__del__()`을 `del`로 바꿔 쓰는 등 wrapping된 구문도 있다.

### 2-6. self

- python에서 자기 자신을 가리키는 구문
  - 즉, instance 자체를 말하며 메서드가 호출될 때 첫 번째 인자로 넘겨주거나 클래스 내에서 `self.property` 형태로 사용함으로써 어떤 instance의 요소가 호출됐는지 구분한다.

## 3. 객체지향 4대 특성

### 3-1. Abstraction(추상화)

- 실세계를 추상화하여 공통적인 것을 추출하는 개념
- 캡슐화를 통해 상태와 행위를 하나로 묶어 클래스로 추상화하며 이를 구현할 떄 비로소 실체화된 객체로 나타난다.

### 3-2. Encapsulation(캡슐화)

- 속성과 메서드를 하나의 객체 안에 묶는 개념
  - 이를 통해 추상화를 실현시키면서 내부 데이터를 보호하고 은닉한다.
  - 다만, 정보 은닉의 한 방법으로 캡슐화가 있는 것이지 캡슐화가 정보은닉을 항상 보장하는 것은 아니다.

#### 3-1-1. Visibility(가시성), 접근 제한자

- 클래스 내부 요소의 접근을 결정하는 것
  - 객체지향에서 접근 제한자는 public, private, protected로 나뉜다.
    - public은 어디에서든 클래스의 요소에 접근할 수 있다.
    - private는 클래스 내부에서만 요소에 접근할 수 있다.
    - protected는 클래스 내부, 상속받은 클래스, 같은 패키지 안에서 접근할 수 있다.
- Python은 공식적으로 접근 제한자를 지원하지 않으며 창시자인 귀도 반 로섬도 [이에 대해 지원하지 않을 것이라고 정확히 얘기했다.](https://stackoverflow.com/questions/7456807/should-i-use-name-mangling-in-python)
  - 즉, Python에서 모든 속성과 메서드는 public이다.
    - 이 때문에 혹자는 Python을 객체지향 언어로 인정하지 않으나 [캡슐화는 단지 객체지향의 한 특성일뿐 Python은 객체지향 언어가 맞다.](https://stackoverflow.com/questions/3325343/why-is-python-not-fully-object-oriented)
  - [PEP8에서는](https://peps.python.org/pep-0008/#method-names-and-instance-variables) 이름 앞에`_`를 붙여 non-public 메서드 혹은 속성임을 알려줄 수 있고 서브 클래스의 이름 충돌을 피하기 위해 `__`를 이름 앞에 붙일 수 있다고 설명한다.
    - 이름 앞에 `__`을 붙여 해당 요소를 private로 설정할 수 있다고 알려져 있으나 실제로 코드를 실행하면 해당 요소를 찾을 수 없다는 예외가 발생한다.
      - [내부적으로 `InstanceName._ClassName__AttributeName`, `InstanceName._ClassName__MethodName`](https://docs.python.org/3.11/reference/expressions.html?highlight=mangling#index-5)라는 이름으로 바뀌기 때문에 해당 형식에 맞춰 강제로 꺼낼 수 있다.
      - 이를 name mangling이라고 한다.
- 결론적으로 특별히 지정하지 않는 한 Python에서 모든 요소는 public에 해당한다.

### 3-3. Inheritance(상속)

- 하위 클래스가 상위 클래스의 속성과 메서드를 묵시적으로 소유한 것
  - 즉, 하위 클래스는 상위 클래스의 속성과 메서드를 호출할 수 있다.
  - 추상화할 수 있는 부분을 계층적으로 추상화하여 코드의 재사용성을 높이는 것이 목적이다.
  - `class ChildClass(ParentClass)`로 작성한다.
- 상위 개념의 클래스를 parent class(부모 클래스), base class(기반 클래스), super class(슈퍼 클래스), 상위 클래스라고 하며 하위 개념의 클래스를 child class(자식 클래스), derived class(파생 클래스), subclass(서브 클래스), 하위 클래스라고 한다.
  - 해당 자료에서는 상위 클래스와 하위 클래스로 용어를 통일했다.
- 메서드는 하위 클래스의 instance가 상위 클래스의 메서드를 호출할 수 있다.
- 속성은 하위 클래스의 생성자에서 상위 클래스의 생성자를 호출해야만 사용할 수 있다.
  - 하위 클래스의 생성자를 선언하지 않는다면 상위 클래스의 생성자가 자동으로 호출된다.

#### 3-3-1. `super()`

- 단일 상속에 대해 상위 클래스를 따로 정의하지 않고 사용하거나 다중 상속에 대해 호출하려는 상위 클래스를 명백히 하는데 사용하는 함수
  - `super().method_name()`을 하위 클래스에서 호출하여 상위 클래스의 메서드를 호출한다.
  - 다만, 코드가 위에서 아래로 진행되기 때문에 `super().method_name()`의 호출 시기를 유념해야 한다.
    - 상위 클래스의 생성자를 호출하고 하위 클래스에서 이 값을 수정하면 상위 클래스에는 반영되지 않는다.

#### 3-3-2. Generalization, Specialization(일반화, 상세화)

- 일반화는 하위 클래스로부터 상위 클래스를 추상화하는 방식이고 반대로 상세화는 상위 클래스로부터 하위 클래스를 작성하는 방식이다.
  - 이미 작성된 클래스로부터 공통 사항을 추출해 추상화하는 Bottom-Up 방식이 일반화, 매우 추상화된 클래스로부터 좀 더 구체적인 클래스를 작정하는 Top-Down 방식이 상세화이다.

#### 3-3-3. 포함 관계

- 상속관계의 두 클래스를 문장으로 나타낼 때 is-a관계면 상속 관계, has-a관계로 치환할 수 있다면 포함 관계
  - is-a 관계는 상속관계이지만 has-a관계는 클래스의 속성에 여러 개의 instance를 저장하는 방식으로 구현하는 것이 자연스러울 수 있다.

#### 3-3-4. 다중상속

- 다른 객체지향 언어와 다르게 Python은 다중 상속을 직접적으로 지원한다.
- `class ChildClass(ParentClass1, ParentClass2, ...)`로 작성한다.  
<img src = "https://dojang.io/pluginfile.php/13909/mod_page/content/3/068006.png" width=50%>
- 다중상속의 문제는 위와 같이 다이아몬드 구조를 가지고 같은 이름을 가진 메서드가 모든 클래스에 있을 때 가장 하위 클래스가 어떤 상위 클래스의 메서드를 호출해야 하는지 알 수 없다는 점이다.
  - `ClassName.mro()`를 호출하면 메서드 호출 순서를 보여주며 이를 통해 해당 클래스의 다중 상속 순서를 알 수 있다.
    - `class ChildClass(ParentClass1, ParentClass2, ...)`로 작성되었다면 `ParentClass1`부터 탐색한다.
    - 그러나 설계단계에서부터 이런 복잡한 상속은 지양하는 것이 권장된다.

#### 3-3-5. Abstract Class(추상 클래스)

- 메서드 목록만 가진 클래스
  - 이 클래스를 상속받으면 이 클래스의 메서드 구현이 강제된다.
  - 또한 instance를 만들 수 없다. 해당 클래스는 오로지 상속과 메서드 구현을 위한 상위 클래스로써만 작동한다.
- `abc.ABC` 클래스를 상속받도록 하며 각 메서드에는 `@abstractmethod`라는 데코레이터가 붙여 추상 클래스를 정의한다.
  - 일부 자료에서는 추상클래스가 `metaclass=ABCMeta`로 상속받도록 표기해야 한다고 하지만 [실제 기능상 차이는 없다고 한다.](https://stackoverflow.com/questions/68569239/what-is-the-difference-between-abstractclassmetaclass-abcmeta-and-class-abstra)

### 3-4. Polymorphism(다형성)

- 객체의 메서드는 그 맥락에 따라 여러 역할을 수행할 수 있다는 개념
  - 다형성은 같은 이름의 다른 파라미터 지닌 메서드를 정의할 수 있게 하고 상위 클래스의 메서드를 하위 클래스에서 작성할 수 있도록 해준다.
    - 다형성을 제공하지 않는다면 코드의 낭비가 심할 것이다.

#### 3-4-1. Overloading

- 같은 클래스에서 이름이 같은 메서드에 대해 매개변수의 수와 유형을 달리하여 여러 개로 정의하는 것
  - Python은 메서드 오버로딩을 지원하지 않는다.
    - Python의 가변인자, 키워드인자가 사실 오버로딩의 정의와 일치한다. 다만 그것을 여러 개의 메서드로 정의하지 않았을 뿐이다.
    - 이외에 오버로딩을 구현한느 몇 가지 다른 방법이 있다.
      - `if-else`구문을 이용한다.
      - class method를 이용한다.
      - [`@multidispatch`](https://pypi.org/project/multipledispatch/)는 라이브러리를 이용한다.
      - Python 3.4이상부터는 [`@singledispatch`](https://docs.python.org/3/library/functools.html#functools.singledispatch)라 불리는 데코레이터로 구현할 수 있있다.
      - Python 3.5이상부터는 `typing`모듈을 불러와 `@typing.overload`라는 데코레이터를 사용할 수 있다.
        - `@typing.overload`는 단순히 Type Hint이기 때문에 다른 Type Hint와 마찬가지로 정적 타입을 보장하지 않는다.

#### 3-4-2. Overriding(함수 재정의)

- 상위 클래스에서 정의된 메서드를 하위 클래스에서 같은 이름의 다른 내용으로 재정의하는 것
  - 상위 클래스에서 작성한 메서드의 내용은 무시된다.
  - 상위 클래스의 메서드 내용을 활용하하려면 `super().method_name()`을 하위 클래스의 메서드에 추가하면 된다.

## 4. API 문서 읽기

- 각 라이브러리의 내용을 추상적인 수준에서 설명한 문서가 API 문서
- 일반적으로 모듈-클래스-속성-메서드 순으로 이뤄지며 필요에 따라 매개변수, 반환 타입에 대해서도 설명한다.
- 구글링과 GPT를 통해 탐색하지 못하면 결국 공식 API 문서를 통해 직접 해결 방법을 찾아야 한다.
- 아무래도 당연하겠지만 영어 독해 실력과 전문 용어에 대한 지식을 갖추고 있어야 한다.
- 아래의 몇몇 유명 라이브러리들의 공식 API 문서 예제를 통해 알아보자.

### [`sklearn.linear_model.LinearRegression`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html)

- 클래스에 대한 간단한 설명과 기본 형태를 서술한다.
- 이후 매개변수, 속성의 타입과 기본값, 내용을 서술한다.
  - 선언에 대한 예제 코드를 제시한다.
- 메서드는 각각의 매개변수 내용과 반환 내용을 서술한다.

### [`pandas.DataFrame`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html)

- 클래스에 대한 간단한 설명과 기본 형태를 서술한다.
- 이후 매개변수의 타입과 내용을 서술한다.
  - 선언에 대한 예제 코드를 제시한다.
- 속성과 메서드는 다른 페이지의 문서에 자세한 사항이 나오며 추상적인 부분만 서술한다.

### [`seaborn.scatterplot`](https://seaborn.pydata.org/generated/seaborn.scatterplot.html)

- 함수에 대한 설명과 기본 형태를 서술한다.
- 이후 매개변수의 타입과 내용을 서술하고 반환 내용에 대해 서술한다.
  - 예제 코드를 집중적으로 제시한다.
