from abc import *

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

class Champion():
    def __init__(self):
        self.health = 200

    def move():
        print("이동")

class Soldier76(Champion):
    def __init__(self):
        super().__init__()
        #상위 클래스의 생성자를 불러와 속성 호출
        print("call from parent class: {}".format(self.health))
        #하위 클래스도 health라는 속성을 가지는 것이기 때문에
        #자신의 속성처럼 접근할 수 있음
        self.health = 300

    def press_W():
        print("W를 누름")

champ = Champion()
soldier76 = Soldier76()
print(soldier76.move())
#Output:"이동"
print(soldier76.press_W())
#Output:"W를 누름"
soldier76 = Soldier76()
print(soldier76.health)
print(champ.health)
#Output:call from parent class: 200
#		300
#		200

class AbstractCampion(ABC):
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

class Reinhardt(AbstractCampion):
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

class OverloadingChampion:
    def left_click(self, **kwargs):
        if "gun" in kwargs: return "bullet", *kwargs.get("gun")
        elif "heal" in kwargs: return "healing", *kwargs.get("heal")
        elif "knife" in kwargs: return "slaying", *kwargs.get("knife")

para = OverloadingChampion()
mercy = OverloadingChampion()
genzi = OverloadingChampion()

para.left_click({"gun":120})
mercy.left_click({"gun":20, "heal":55})
genzi.left_click({"gun":27, "knife":110})