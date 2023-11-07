def sqrt(val: int) -> float:
    return val**0.5

#type hint는 자료형을 강제하지 않음
print(sqrt(1), sqrt(1.0))
#Output 1 1.0

#Python 3.12
#type Vector = list[float]
#~Python 3.11
from typing import TypeAlias
Vector: TypeAlias = list[float]
#혹은 Vector = list[float]

#구버전의 호환성을 위해 type 키워드를 사용하지 않음
Coordinate = list[float, float]
BuildingName = str
BuildingInfo = tuple[BuildingName, Coordinate]

def search_address(building_info: BuildingInfo) -> str:
	pass
#Type aliases를 사용하지 않았다면
#def search_address(building_info: tuple[str,list[float, float]]) -> str:

#예외처리 실습코드이므로 필요할 때만 주석을 해제하고 실행할 것
#def validate_probability(x: float) -> bool:
#    if 0 <= x <= 1: return True
#    else: raise ValueError("The variable of probability must be 0 to 1.")
#
#any_numbers = [0.1, 0.3, 0.5, 1.2]
##try-except 구문을 사용하지 않는다면 사용자가 정의한 에러 메시지 출력
#for i in any_numbers:
#    validate_probability(i)
##Output: The variable of probability must be 0 to 1.
##raise의 최대 장점은 try-except에서 예외 처리를 위한 코드를 작성하지 않아도 됨
##다시 말해, 예외처리가 필요한 부분에 일일이 try-except를 작성하지 않아도 됨
#try:
#    for i in any_numbers:
#        validate_probability(i)
#except Exception as e:
#    print("다음과 같은 예외가 발생: ", e)
##Output: 다음과 같은 예외가 발생: The variable of probability must be 0 to 1.
#
#class ValidateProbability(Exception):
#    def __init__(self):
#        super().__init__("The variable of probability must be 0 to 1.")
#
#any_numbers = [0.1, 0.3, 0.5, 1.2]
#
#try:
#    for i in any_numbers:
#        if not (0<=i<=1): raise ValidateProbability
#except Exception as e:
#    print("다음과 같은 예외가 발생: ", e)
##Output: 다음과 같은 예외가 발생: The variable of probability must be 0 to 1.
#
#def validate_probability(x: float) -> bool:
#    assert 0 <= x <= 1, "The variable of probability must be 0 to 1."
#    return True