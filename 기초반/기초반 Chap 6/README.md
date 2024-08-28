# 기초반 6차시

## TOC

- [1. 객체지향 4대 특성](#1-객체지향-4대-특성)
  - [1-1. Abstraction(추상화)](#1-1-abstraction추상화)
  - [1-2. Encapsulation(캡슐화)](#1-2-encapsulation캡슐화)
    - [1-2-1. Visibililty(가시성), 접근 제한자](#1-2-1-visibility가시성-접근-제한자)
  - [1-3. Inheritance(상속)](#1-3-inheritance상속)
    - [1-3-1. `super()`](#1-3-1-super)
    - [1-3-2. Generalization, Specialization(일반화, 상세화)](#1-3-2-generalization-specialization일반화-상세화)
    - [1-3-3. 포함관계](#1-3-3-포함-관계)
    - [1-3-4. 다중상속](#1-3-4-다중상속)
    - [1-3-5. Abstract Class(추상 클래스)](#1-3-5-abstract-class추상-클래스)
  - [1-4. Polymorphism(다형성)](#1-4-polymorphism다형성)
    - [1-4-1. Overloading](#1-4-1-overloading)
    - [1-4-2. Overriding(함수 재정의)](#1-4-2-overriding함수-재정의)
- [2. API 문서 읽기](#2-api-문서-읽기)

## 1. 객체지향 4대 특성

### 1-1. Abstraction(추상화)

- 실세계를 추상화하여 공통적인 것을 추출하는 개념
- 캡슐화를 통해 상태와 행위를 하나로 묶어 클래스로 추상화하며 이를 구현할 떄 비로소 실체화된 객체로 나타난다.

### 1-2. Encapsulation(캡슐화)

- 속성과 메서드를 하나의 객체 안에 묶는 개념
  - 이를 통해 추상화를 실현시키면서 내부 데이터를 보호하고 은닉한다.
  - 다만, 정보 은닉의 한 방법으로 캡슐화가 있는 것이지 캡슐화가 정보은닉을 항상 보장하는 것은 아니다.

#### 1-2-1. Visibility(가시성), 접근 제한자

- 클래스 내부 요소의 접근을 결정하는 것
  - 객체지향에서 접근 제한자는 public, private, protected로 나뉜다.
    - public은 어디에서든 클래스의 요소에 접근할 수 있다.
    - private는 클래스 내부에서만 요소에 접근할 수 있다.
    - protected는 클래스 내부, 상속받은 클래스, 같은 패키지 안에서 접근할 수 있다.
- Python은 공식적으로 접근 제한자를 지원하지 않으며 창시자인 귀도 반 로섬도 [이에 대해 지원하지 않을 것이라고 정확히 얘기했다.](https://stackoverflow.com/questions/7456807/should-i-use-name-mangling-in-python)
  - 즉, Python에서 모든 속성과 메서드는 public이다.
    - 이 때문에 혹자는 Python을 객체지향 언어로 인정하지 않으나 [캡슐화는 단지 객체지향의 한 특성일뿐 Python은 객체지향 언어가 맞다.](https://stackoverflow.com/questions/3325343/why-is-python-not-fully-object-oriented)
  - [PEP8에서는](https://peps.python.org/pep-0008/#method-names-and-instance-variables) 이름 앞에 `_`를 붙여 non-public 메서드 혹은 속성임을 알려줄 수 있고 서브 클래스의 이름 충돌을 피하기 위해 `__`를 이름 앞에 붙일 수 있다고 설명한다.
    - 이름 앞에 `__`을 붙여 해당 요소를 private로 설정할 수 있다고 알려져 있으나 실제로 코드를 실행하면 해당 요소를 찾을 수 없다는 예외가 발생한다.
      - [내부적으로 `InstanceName._ClassName__AttributeName`, `InstanceName._ClassName__MethodName`](https://docs.python.org/3.11/reference/expressions.html?highlight=mangling#index-5)라는 이름으로 바뀌기 때문에 해당 형식에 맞춰 강제로 꺼낼 수 있다.
      - 이를 name mangling이라고 한다.
- 결론적으로 특별히 지정하지 않는 한 Python에서 모든 요소는 public에 해당한다.

### 1-3. Inheritance(상속)

- 하위 클래스가 상위 클래스의 속성과 메서드를 묵시적으로 소유한 것
  - 즉, 하위 클래스는 상위 클래스의 속성과 메서드를 호출할 수 있다.
  - 추상화할 수 있는 부분을 계층적으로 추상화하여 코드의 재사용성을 높이는 것이 목적이다.
  - `class ChildClass(ParentClass)`로 작성한다.
- 상위 개념의 클래스를 parent class(부모 클래스), base class(기반 클래스), super class(슈퍼 클래스), 상위 클래스라고 하며 하위 개념의 클래스를 child class(자식 클래스), derived class(파생 클래스), subclass(서브 클래스), 하위 클래스라고 한다.
  - 해당 자료에서는 상위 클래스와 하위 클래스로 용어를 통일했다.
- 메서드는 하위 클래스의 instance가 상위 클래스의 메서드를 호출할 수 있다.
- 속성은 하위 클래스의 생성자에서 상위 클래스의 생성자를 호출해야만 사용할 수 있다.
  - 하위 클래스의 생성자를 선언하지 않는다면 상위 클래스의 생성자가 자동으로 호출된다.

#### 1-3-1. `super()`

- 단일 상속에 대해 상위 클래스를 따로 정의하지 않고 사용하거나 다중 상속에 대해 호출하려는 상위 클래스를 명백히 하는데 사용하는 함수
  - `super().method_name()`을 하위 클래스에서 호출하여 상위 클래스의 메서드를 호출한다.
  - 다만, 코드가 위에서 아래로 진행되기 때문에 `super().method_name()`의 호출 시기를 유념해야 한다.
    - 상위 클래스의 생성자를 호출하고 하위 클래스에서 이 값을 수정하면 상위 클래스에는 반영되지 않는다.

#### 1-3-2. Generalization, Specialization(일반화, 상세화)

- 일반화는 하위 클래스로부터 상위 클래스를 추상화하는 방식이고 반대로 상세화는 상위 클래스로부터 하위 클래스를 작성하는 방식이다.
  - 이미 작성된 클래스로부터 공통 사항을 추출해 추상화하는 Bottom-Up 방식이 일반화, 매우 추상화된 클래스로부터 좀 더 구체적인 클래스를 작정하는 Top-Down 방식이 상세화이다.

#### 1-3-3. 포함 관계

- 상속관계의 두 클래스를 문장으로 나타낼 때 is-a관계면 상속 관계, has-a관계로 치환할 수 있다면 포함 관계
  - is-a 관계는 상속관계이지만 has-a관계는 클래스의 속성에 여러 개의 instance를 저장하는 방식으로 구현하는 것이 자연스러울 수 있다.

#### 1-3-4. 다중상속

- 다른 객체지향 언어와 다르게 Python은 다중 상속을 직접적으로 지원한다.
- `class ChildClass(ParentClass1, ParentClass2, ...)`로 작성한다.  
<img src = "https://dojang.io/pluginfile.php/13909/mod_page/content/3/068006.png" width=50%>
- 다중상속의 문제는 위와 같이 다이아몬드 구조를 가지고 같은 이름을 가진 메서드가 모든 클래스에 있을 때 가장 하위 클래스가 어떤 상위 클래스의 메서드를 호출해야 하는지 알 수 없다는 점이다.
  - `ClassName.mro()`를 호출하면 메서드 호출 순서를 보여주며 이를 통해 해당 클래스의 다중 상속 순서를 알 수 있다.
    - `class ChildClass(ParentClass1, ParentClass2, ...)`로 작성되었다면 `ParentClass1`부터 탐색한다.
    - 그러나 설계단계에서부터 이런 복잡한 상속은 지양하는 것이 권장된다.

#### 1-3-5. Abstract Class(추상 클래스)

- 메서드 목록만 가진 클래스
  - 이 클래스를 상속받으면 이 클래스의 메서드 구현이 강제된다.
  - 또한 instance를 만들 수 없다. 해당 클래스는 오로지 상속과 메서드 구현을 위한 상위 클래스로써만 작동한다.
- `abc.ABC` 클래스를 상속받도록 하며 각 메서드에는 `@abstractmethod`라는 데코레이터가 붙여 추상 클래스를 정의한다.
  - 일부 자료에서는 추상클래스가 `metaclass=ABCMeta`로 상속받도록 표기해야 한다고 하지만 [실제 기능상 차이는 없다고 한다.](https://stackoverflow.com/questions/68569239/what-is-the-difference-between-abstractclassmetaclass-abcmeta-and-class-abstra)

### 1-4. Polymorphism(다형성)

- 객체의 메서드는 그 맥락에 따라 여러 역할을 수행할 수 있다는 개념
  - 다형성은 같은 이름의 다른 파라미터 지닌 메서드를 정의할 수 있게 하고 상위 클래스의 메서드를 하위 클래스에서 작성할 수 있도록 해준다.
    - 다형성을 제공하지 않는다면 코드의 낭비가 심할 것이다.

#### 1-4-1. Overloading

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

#### 1-4-2. Overriding(함수 재정의)

- 상위 클래스에서 정의된 메서드를 하위 클래스에서 같은 이름의 다른 내용으로 재정의하는 것
  - 상위 클래스에서 작성한 메서드의 내용은 무시된다.
  - 상위 클래스의 메서드 내용을 활용하하려면 `super().method_name()`을 하위 클래스의 메서드에 추가하면 된다.

## 2. API 문서 읽기

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
