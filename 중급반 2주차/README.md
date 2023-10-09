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
```python
class Mercy:
	def __init__(self):
		self.health = 200
		self._shield = 0
		self.__defense = 0
	def _restore_health(self):
		self.health = 200
		print("you call _restore_health method")
	def __restore_shield(self):
		self.shield = 0
		print("you call __restore_shield method")
mercy = Mercy()
print(mercy.health)#public 속성에 대한 직접 접근
#Output:200
print(mercy._shield)#non-public으로 만든 속성에 대한 직접 접근
#Output:0
print(mercy.__defense)#name mangling으로 만든 속성에 대한 접근
#Output:AttributeError
print(mercy._Mercy__defense)#name mangling으로 만든 속성에 대한 강제적 접근
#Output:0
mercy._restore_health()
#Output:you call _restore_health method
mercy.__restore_shield()
#Output:AttributeError
mercy._Mercy__restore_shield()
#Output:you call __restore_shield method
```
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
``` python
class Champion():
    def move():
	    print("이동")

class Soldier76(Champion):
    def press_W():
        print("W를 누름")

soldier76 = Soldier76-()
print(soldier76.move())
#Output:"이동"
print(soldier76.press_W())
#Output:"W를 누름"
```
- 속성은 하위 클래스의 생성자에서 상위 클래스의 생성자를 호출해야만 사용할 수 있다.
	- 하위 클래스의 생성자가 생략된다면 상위 클래스의 생성자가 자동으로 호출된다.
```python
class Champion():
	def __init__(self):
		self.health = 200

class Soldier76(Champion):
	pass

soldier76 = Soldier76()
print(soldier76.health)
#Output:200
```
### super 함수
- 단일 상속에 대해 상위 클래스의 정의 없이 이를 반환하거나 다중 상속에 대해 호출하고 싶은 상위 클래스를 명백히 하는데 사용하는 함수
	- `super().method_name()`을 하위 클래스에서 사용하여 상위 클래스의 메서드를 호출한다.
	- 다만 `super().method_name()`의 호출 시기에 따라 하위 클래스의 내용이 달라질 수 있는 것에 유의해야 한다.
		- 상위 클래스의 생성자를 호출하고 하위 클래스에서 이 값을 수정한 것은 상위 클래스에 반영되지 않는다.
```python
class Champion():
	def __init__(self):
		self.health = 200

class Soldier76(Champion):
	def __init__(self):
		super().__init__()
		#상위 클래스의 생성자를 불러와 속성 호출
		print("call from parent class: {}".format(self.health))
		#하위 클래스도 health라는 속성을 가지는 것이기 때문에
		#자신의 속성처럼 접근할 수 있음
		self.health = 300

champ = Champion()
soldier76 = Soldier76()
print(soldier76.health)
print(champ.health)
#Output:call from parent class: 200
#		300
#		200
```
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
```python
from abc import *

#class Champion(metaclass=ABCMeta)와 동일
class Campion(ABC):
    @abstractmethod
    def left_click(self):
        pass
    @abstractmethod
    def right_click(self):
        pass
    @abstractmethod
    def press_Q(self):
	    pass
	@abstractmethod
	def press_E(self):
	    pass

class Reinhardt(Champion):
    def left_click(self):
        return "hammer"
	def right_click(self):
	    return "barrier"
	def press_Q(self):
	    return "earth shatter"
	def press_E(self):
	    return "fire strike"
reinhardt = Reinhardt()
print(reinhardt.press_Q())
#Output:"earth shatter"
```
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
```python
class Champion:
    def left_click(self, **kwargs):
	    if "gun" in kwargs: return "bullet", *kwargs.get("gun")
	    elif "heal" in kwargs: return "healing", *kwargs.get("heal")
	    elif "knife" in kwargs: return "slaying", *kwargs.get("knife")

para = Champion()
mercy = Champion()
genzi = Champion()

para.left_click({"gun":120})
mercy.left_click({"gun":20, "heal":55})
genzi.left_click({"gun":27, "knife":110})
```
### Overriding(함수 재정의)
- 상위 클래스에서 정의된 메서드가 하위 클래스에서 같은 이름의 다른 내용을 가진 정의로 재정의하는 것
	- 상위 클래스에서 작성한 메서드의 내용은 무시된다.
	- 상위 클래스의 메서드 내용을 활용하고 새로운 내용을 추가하려면 `super().method_name()`을 하위 클래스의 메서드에 추가하면 된다. 
```python
class Champion:
	def _attack(self):
		pass #구현되었다고 가정
	def _heal(self):
		pass #구현되었다고 가정
	def left_click(self):
		return _attack()

class Mercy(Champion):
	def left_click(self, is_wheel_moved):
		if is_wheel_moved == True: return super()._attack()
		else: return super().left_click()
#Mercy 클래스는 Champion 클래스를 상속받음
#Champion 클래스의 left_click 메서드는 기본적으로 _attack() 메서드를 반환
#그러나 Mercy 클래스는 이를 overriding해 if 문으로 상위 클래스의 다른 메서드 반환

mercy = Mercy()
mercy.attack()
#Output: call Champion._heal()
```
# 객체지향 5대 원리
## 디자인 패턴
- 객체 지향 프로그래밍에서 자주 발생하는 문제들을 해결하기 위해 사용하는 패턴
	- 협업이 필요한 규모의 소프트웨어 프로젝트에서 통일된 패턴을 사용하는 것은 효율성을 높인다.
## 1. Single Responsibility Principle(SRP, 단일 책임 원칙)
- 단일 객체는 단일 기능만 담당
## 2. Open Close Principle(OCP, 개방 폐쇄 원칙)
- 기능의 변경과 확장에는 개방적이지만 그 방식이 내부 코드를 수정하는 것으로 이뤄지는 것에는 폐쇄적
## 3. Liskov Substitution Principle(LSP, 리스코프 치환 원칙)
- 상위 객체를 하위 객체로 대체할 수 있음
	- 즉, 상위 객체의 메서드로 하위 객체를 접근해도 같은 기능을 해야 함
	- 다시 말해, 상위 클래스에 대한 하위 클래스의 오버로딩과 오버라이딩의 일관성이 유지되어야 함
## 4. Interface Segregation Principle(ISP, 인터페이스 분리 원칙)
- 목적과 관심이 다른 클라이언트가 있다면 이에 대응하는 인터페이스를 만들어 적절히 대응해야 함
## 5. Dependency Inversion Principle(DIP, 의존성 역전 원칙)
- 상위 클래스가 하위 클래스에 의존하도록 하면 안됨
	- 다시 말해 구체화된 클래스가 상위 클래스의 역할을 하고 있으면 안된다.