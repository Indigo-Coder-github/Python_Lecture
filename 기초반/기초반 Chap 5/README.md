# 기초반 5차시

## TOC

- [1. Objected Oriented Programming](#1-objected-oriented-programming-oop-객체지향-프로그래밍)
  - [1-1. Class(클래스)](#1-1-class클래스)
  - [1-2. Object(객체)](#1-2-object객체)
    - [1-2-1. Immutable Object](#1-2-1-immutable-object)
    - [1-2-2. Mutable Object](#1-2-2-mutable-object)
      - [shallow copy, deep copy(얕은 복사, 깊은 복사)](#shallow-copy-deep-copy얕은-복사-깊은-복사)
  - [1-3. Instance(인스턴스)](#1-3-instance인스턴스)
    - [1-3-1. Constructor(생성자)](#1-3-1-constructor생성자)
    - [1-3-2. Desrtructor(소멸자)](#1-3-2-destructor소멸자)
  - [1-4. Property(속성)](#1-4-property속성)
    - [1-4-1. Class Variabel(클래스 속성)](#1-4-1-class-variable클래스-속성)
  - [1-5. Method(메서드)](#1-5-method메서드)
    - [1-5-1. Static Method(정적 메서드)](#1-5-1-static-method정적-메서드)
    - [1-5-2. Class Method(클래스 메서드)](#1-5-2-class-method클래스-메서드)
    - [1-5-3. Magic Method(Special Method)](#1-5-3-magic-methodspecial-method)
  - [1-6. self](#1-6-self)

## 1. Objected Oriented Programming (OOP, 객체지향 프로그래밍)

- 프로그래밍 패러다임의 하나
  - 절차 형태의 코드와 필드 형태의 코드와 데이터를 담을 수 있는 객체라는 것을 기반으로 하는 패러다임이다.

### 1-1. Class(클래스)

- 공통의 속성과 행위를 가진 객체들을 추상화한 것
  - 다시 말해 instance를 정의한 코드이다.
- `class ClassName`으로 정의한다.`

### 1-2. Object(객체)

- Class가 실체화할 대상
- Python의 모든 것은 객체이다! 다른 언어는 Primitive Type과 Object Type이 구분되어있는 것과는 차이점이 있다.
  - C++, Java 등은 Primitive type과 이에 대한 wrapper class가 따로 구분된다.
    - numpy도 wrapper class를 사용했으나 신규 사용자들의 혼동으로 인해 1.20부터 deprecated되어 python의 data type으로 통합됐다.
  - 때문에 Python에서 형변환은 입력 값에 자료형이 단순히 바뀌는 것이 아니라 해당 자료형의 새로운 instance를 생성한다.
    - 이 부분은 일본에서 개발된 프로그래밍 언어인 Ruby와 일맥상통한다.
  - 인터프리터라는 점과 더불어 Python의 속도가 느린 이유 중 하나로 꼽는다.

#### 1-2-1. Immutable Object

- 데이터 값이 바뀔 때 현재 메모리 위치의 내용을 삭제하고 다른 위치에 새로 생성하는 객체
- Mutable Object를 제외한 모든 타입은 Immutable Object에 해당한다.
  - 때문에 tuple은 요소를 수정할 수 없다.

#### 1-2-2. Mutable Object

- 데이터 값이 바뀔 때 현재 메모리에 대한 값을 수정하는 객체
- list, set, dictionary, `@dataclass(frozen=True)`로 선언하지 않은 사용자 class가 해당한다.

##### shallow copy, deep copy(얕은 복사, 깊은 복사)

- Mutable Object는 객체가 저장된 위치와 객체 내부의 값이 저장된 위치가 서로 다르기 때문에 등호, slicing, `mutable_object.copy()`, `copy.copy(mutable_object)`을 사용하면 얕은 복사가 이뤄진다.
  - 얕은 복사는 원래의 변수와 새로 생성한 변수 모두 같은 객체가 저장되어 있다.
  - 때문에 한 변수의 내용을 수정하면 다른 변수의 내용도 똑같이 수정된다.
  - Immutable Object는 그 특징 때문에 얕은 복사와 깊은 복사에 대해 다루지 않아도 된다.
- `copy.deepcopy(mutable_obejct)`를 사용하면 깊은 복사가 이뤄진다.
  - 깊은 복사는 새로 생성된 변수가 원래의 변수 내용을 전부 다른 위치에 복사시킨다.

### 1-3. Instance(인스턴스)

- Class를 실체화한, 메모리에 실제로 할당된 객체
- `instance_name = ClassName(arguments)`로 정의한다.

#### 1-3-1. Constructor(생성자)

- instance가 생성될 때 그 instance의 속성들을 초기화하는 method
- `__init__()`은 Python에서 생성자인 magic method이다.

#### 1-3-2. Destructor(소멸자)

- instance가 소멸할 때 작동하는 method
  -`__del__()`은 Python에서 소멸자인 magic method이며 `del samsung`형태로 호출한다.
  - 대부분의 프로그래밍 언어처럼 Python도 Garbage Collector를 통해 객체의 소멸 시점을 관리하기 때문에 특별한 사유가 없는 한 소멸자를 임의로 사용하지 않아도 된다.

### 1-4. Property(속성)

- 객체에 저장된 자료의 특성과 이름을 정의한 것
  - instance의 상태와 정보를 나타낸다.
- attribute, member variable, instance variable 등의 용어와 혼용된다.
- class의 생성자에 `self.property_name = arg_name`으로 정의하며 `instance.property_name`으로 호출한다.

#### 1-4-1. Class Variable(클래스 속성)

- 한 클래스에서 탄생한 모든 instance가 공유하는 공통의 속성
  - 쉽게 얘기해 클래스 버전의 전역변수이다.
- class가 생성될 때 생성되는 속성이기 때문에 `class_name().class_variable_name`으로 참조할 수 있다.

### 1-5. Method(메서드)

- 객체의 행위를 정의한 것 혹은 객체에게 전달할 수 있는 메시지
  - operation, member function, instance method 등의 용어와 혼용된다.
- class 내 함수를 선언하고 `instance.method_name(args)`형태로 호출한다.

#### 1-5-1. Static Method(정적 메서드)

- instance를 생성하지 않아도 접근할 수 있는 메서드
  - 인자로 `self`를 받지 않는다.
- 메서드를 정의한 코드 위에 `@staticmethod`를 써서 해당 메서드가 정적 메서드임을 나타낸다.
  - 일반적으로 유틸리티 함수를 만드는데 사용한다.

#### 1-5-2. Class Method(클래스 메서드)

- instance를 생성하지 않아도 접근할 수 있으면서 클래스 속성, 클래스 메서드에 접근할 수 있는 메서드
  - 즉, static method는 클래스 속성, 클래스 메서드에 접근할 수 없다.
- 메서드를 정의한 코드 위에 `@classmethod`를 써서 해당 메서드가 클래스 메서드임을 나타낸다.
  - 다른 메서드와 다르게 첫 parameter를 `cls`로 정의한다. `cls`는 클래스 그 자체를 의미한다.

#### 1-5-3. Magic Method(Special Method)

- 특별한 이름으로 정의되어 특별한 구문으로 호출하는 메서드
  - 오버라이딩을 통해 커스터마이징할 수 있다.
- `__function_name__()`형태이며 생성자와 소멸자인 `__init__()`, `__del__()`도 매직 메서드이다.
  - 경우에 따라서 `__del__()`을 `del`로 바꿔 쓰는 등 wrapping된 구문도 있다.

### 1-6. self

- python에서 자기 자신을 가리키는 구문
  - 즉, instance 자체를 말하며 메서드가 호출될 때 첫 번째 인자로 넘겨주거나 클래스 내에서 `self.property` 형태로 사용함으로써 어떤 instance의 요소가 호출됐는지 구분한다.
