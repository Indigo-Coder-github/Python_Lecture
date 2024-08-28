# 기초반 7차시

## TOC

- [1. Type Hint](#1-type-hint)
- [2. Type Hint](#2-iterator반복자)
  - [2-1. Iterable Object(반복 가능한 객체)](#2-1-iterable-object반복-가능한-객체)
  - [2-2. 반환값 무시](#2-2-반환값-무시)
  - [2-3. lazy evaluation(지연 평가)](#2-3-lazy-evaluation지연-평가)
- [3. Generator(발생자)](#3-generator발생자)
- [4. Lambda(람다식, 익명함수)](#4-lambda람다식-익명함수)

## 1. Type Hint

- python 3.5에서부터 지원하는 사항
- **python 실행 환경에서는 함수와 변수의 자료형에 대해 강제하지 않기 때문에 type checker, IDE, linter 등에서 사용되는 third party tool의 성격이다.**
  - IDE에서 변수에 type hint를 적용하면 해당 변수에서 불러올 수 있는 내부 요소를 바로 파악할 수 있다.
- `def function_name(parameter: type) -> return_type`으로 표기한다.

## 2. Iterator(반복자)

- 클래스에 구현된 `__iter__`메서드를 호출해 반환된 객체
  - 내장 라이브러리인 [itertools](https://docs.python.org/3/library/itertools.html)는 iterator에 대한 더 효율적이고 다양한 기능을 지원함

### 2-1. Iterable Object(반복 가능한 객체)

- `__iter__`와 `__next__` 메서드를 가진 객체
  - iterator protocol을 지원한다고 말하기도 함
- `__iter__`메서드를 호출해 반환된 iterator는 `__next__`메서드를 통해 값에 차례대로 접근할 수 있음
  - 더 이상 꺼낼 값이 없을 때 `__next__`메서드를 호출하면 StopIteration 예외가 발생함
  - 즉, 반복문이 Iterable Object에 접근할 때 `__iter__` 메서드로 Iterator를 생성하고 `__next__`메서드를 이용해 순차적으로 접근함
- `__getitem__`메서드를 구현하면 index로 접근할 수 있음
- Iterator는 그 자체로 하나의 객체 형태이기 때문에 iterable object와 용어를 분리해서 사용할 필요가 있음

### 2-2. 반환값 무시

- unpacking을 하는데 있어서 `_`를 사용하면 해당 위치의 값을 반환받는 것을 무시할 수 있음

### 2-3. lazy evaluation(지연 평가)

- 실행할 때 값을 계산하는 방식
- 메모리를 절약하거나 성능 상의 이점을 가질 수 있음
- [비교 연산이 그 예시 중 하나](https://github.com/Indigo-Coder-github/Python_Lecture/tree/main/%EC%B4%88%EA%B8%89%EB%B0%98%203%2C%204%EC%A3%BC%EC%B0%A8#%EB%B9%84%EA%B5%90-%EC%97%B0%EC%82%B0%EC%9E%90)

## 3. Generator(발생자)

- iterator를 생성해주는 함수
  - class 단에서 구현하고자 하면 iterator를, 함수 단에서 구현하고자 하면 generator를 사용
  - 또한 generator와 달리 `__next__()`메서드의 반환 값이 yield의 값으로 정해져 있음
- return 부분을 `yield value`나 `yield from iterable_object`로 대체하여 구현함
  - return의 성격을 지니기 때문에 값이 반환된 이후 다시 generator를 호출하기 전까지 함수 바깥의 코드가 실행됨
- 일반 함수, 혹은 다른 방식으로 비슷한 방식을 구현할 수 있지만 [매우 큰 메모리가 필요한 작업을 lazy한 방식으로 실행할 수 있음](https://stackoverflow.com/questions/102535/what-can-you-use-generator-functions-for/)

## 4. Lambda(람다식, 익명함수)

- 이름을 붙이지 않은 객체가 마치 함수 객체처럼 행동한다고 하여 익명함수라고도 함
- `lambda paramters: expression`형태로 표현
  - 익명함수이기 때문에 이 식은 객체 자체이고 반환 값을 받고자 하면 변수를 선언해야 함
    - 혹은 `(lambda paramters: expression)(parameter_value)`를 통해 바로 값을 받을 수도 있음
  - expression은 한 줄로만 표현이 가능해야 함
