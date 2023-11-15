# Sequence Type
- iterator를 지원하는 타입
## Sequence Type 함수
|     연산자     | 결과                                                                                                            | 비고 |
|:--------------:| --------------------------------------------------------------------------------------------------------------- |:----:|
|     x in s     | x가 s에 존재하면 True, 아니면 False                                                                             |      |
|   x not in s   | x가 s에 존재하지 않으면 True, 아니면 False                                                                      |      |
|     s + t      | s와 t를 연결                                                                                                    |immutable sequence 타입은 새로운 객체를 생성하기 때문에<br>$O(n^2)$의 시간복잡도를 가짐<br>range 등의 일부 sequence type은 지원되지 않음      |
|     s \* n or n \* s      | s를 n번 연결                                                                                                    |range 등의 일부 sequence type은 지원되지 않음      |
|     s\[i\]     | s의 i번째 요소 반환                                                                                             |      |
|     len(s)     | s의 길이                                                                                                        |      |
|     min(s)     | s에서 가장 작은 요소 반환                                                                                       |      |
|     max(s)     | s에서 가장 큰 요소 반환                                                                                         |      |
| s.index(x,i,j) | s에서 첫 번째로 나타나는 x를 찾아 그 index를 반환<br>i와 j는 선택사항이며 설정하면 i번째부터 j-1번째까지에서 탐색 |x를 찾지 못했다면 ValueError 발생<br>s\[i:j\].index(x)와 동치이지만 슬라이싱된 리스트 기준의 index를 반환      |
|s.count(x)                |s에서 x가 나타난 횟수를 반환                                                                                                                 |      |
```python
country_list = ["Angola", "Begium", "Chile", "Denmark", "England"]
print(country_list.index("Chile", 1), country_list[1:].index("Chile"))
#Output:2 1
```
## slicing
- Ada, Go, Python 등 일부 언어에서 지원하는 배열에 대한 독특한 기능
- `s[i:j:k]`로 표시하며 i에서 j-1까지의 요소를 반환
	- k는 선택 사항이며 설정하면 k만큼 건너뛰면서 반환
	- i나 j가 음수라면 마지막 요소부터 역순으로 가리킴
		- 그러나 -0은 0으로 취급하기 때문에 가장 마지막의 요소는 음수로 -1임
## list
- mutable sequence type, 일반적으로 비슷한 요소의 집합을 저장함
- 아래와 같이 선언할 수 있음
```python
using_bracket_pair = []
using_bracket_comma = ["a", "b", "c"]
using_list_comprehension = [x for x in [1,2,3]]
using_constructor = list("list")
```
- `list()`를 이용한 list 선언은 아래와 같이 이뤄짐
```python
str_to_list = list("abc") #["a", "b", "c"]
tuple_to_list = list((1, 2, 3)) #[1, 2, 3]
blank_list = list() #[]
```
### list 함수
- 공식 문서에서는 `collections.abc.MutableSequence`에 속한 자료형들에서 가능한 연산이라고 했으나 내장 타입 중에는 list밖에 없어 list 함수 항목으로 나타냄
- `list.sort()`는 정렬된 list로 바꿔줌
	- 정렬된 리스트를 값으로 받고 싶다면 [sorted()함수를 사용](https://github.com/Indigo-Coder-github/Python_Lecture/tree/main/%EC%A4%91%EA%B8%89%EB%B0%98%203%EC%A3%BC%EC%B0%A8#sortediterable-keynone-reversefalse)

|        연산자         | 결과                                                                  |                    비고                     |
|:---------------------:| --------------------------------------------------------------------- |:-------------------------------------------:|
|      s\[i\] = x       | i 위치의 요소를 x로 대체                                              |                                             |
|     s\[i:j\] = t      | i에서 j-1까지를 iterable한 t로 대체                                   |                                             |
|     del s\[i:j\]      | s\[i:j\] = \[\]와 동치                                                |                                             |
|    s\[i:j:k\] = t     | s\[i:j:k\]를 iterable한 t로 대체                                      | t의 길이는 대체하려는 요소의 수와 같아야 함 |
|    del s\[i:j:k\]     | s[i:j:k]의 요소 삭제                                                  |                                             |
|      s.append(x)      | s의 가장 마지막에 x를 이어붙임                                        |                                             |
|       s.clear()       | s의 모든 요소를 삭제                                                  |                                             |
|       s.copy()        | s의 얕은 복사본을 생성                                                |                                             |
| s.extend(t) or s += t | s의 가장 마지막에 t의 요소들을 이어붙임                               |                                             |
|        s \*= n        | s를 n번 반복한 값으로 바꿈                                            |                                             |
|     s.insert(i,x)     | s의 i 위치 바로 직후에 x를 삽입함                                               |                                             |
|  s.pop() or s.pop(i)  | s에서 i번째 요소를 반환하고 제거함<br>i가 주어지지 않았다면 마지막 값 |                                             |
|      s.remove(x)      | s에서 첫 번째로 나타난 x를 제거함                                     |                                             |
|      s.reverse()      | s를 뒤집은 값으로 바꿈                                                |                                             |
### list comprehension(리스트 표현식)
- list를 생성할 때 식, for문, if문을 한 문장으로 묶어 생성하는 것
- `[expression for variable in list if statement]` 혹은 `list(expression for variable in list if statement)`형태로 표현할 수 있음
```python
university_list = ["Seoul National", "Korea", "Yonsei", "Sugang", "Sungkyunkwan", "Hanyang", "Chungang", "KyungHee", "HUFS", "Seoul", "Konkuk", "Dongguk", "Hongik", "Kookmin", "Soongsil", "Sejong", "Dankook", "Kwangwoon", "Myongji", "Sangmyung", "Gachon", "Hansung", "Seokyeong", "Sahmyook"]
print([university for university in university_list if "k" in university])
#Ouput:['Sungkyunkwan', 'Konkuk', 'Dongguk', 'Hongik', 'Kookmin', 'Dankook', 'Seokyeong', 'Sahmyook']
```
### [list == array?](https://stackoverflow.com/questions/176011/python-list-vs-array-when-to-use)
- 자료구조 상으로 list와 배열은 엄연히 다른 존재이고 Python에서 `array`모듈을 별도로 지원
- 정의 상 다른 개념이지만 사용에 있어서는 거의 동치임
	- Python에서 list는 상수시간에 작동할 수 있도록 구현되었지만 그 대가로 배열보다 많은 공간을 필요로 함
	- `array`모듈은 C로 구현되었기 때문에 빠른 연산과 적은 메모리(특히 수학)가 필요할 때 사용
### 다차원 list 생성 주의
- `[[] for i in range(x)]`와 `[[]] * x`는 다르게 작동함
	- sequence type의 `*`연산자는 복사가 되는 것이 아닌 여러 번 참조하는 연산자임
```python
multiple_list = [[None, None]] * 3
multiple_list[0][0] = 1
print(multiple_list)
#Output:[[1, None],[1, None],[1, None]]
comprehension_list = [[None, None] for _ in range(3)]
comprehension_list[0][0] = 1
print(comprehension_list)
#Output:[[1, None],[None, None],[None, None]]
```
## tuple
- immutable sequence type
## range
# Text Sequence Type
## string
- immutable sequence type이지만 mutable sequence type같은 행동을 보이는 독특한 자료형
# Set Type
## set
# Mapping Type
## dict
# Loop(반복문)
## for
- Sequence type의 요소를 순서대로 반복하는 구문
- `for *variables in *sequences:`형태로 사용
- [zip 함수에 대해서는 중급반 3주차 자료를 참조](https://github.com/Indigo-Coder-github/Python_Lecture/tree/main/%EC%A4%91%EA%B8%89%EB%B0%98%203%EC%A3%BC%EC%B0%A8#zipiterables-strictfalse)
```python
for i in range(5):
    print(i, end="")
#Output:12345
#변수의 수만큼 sequence 자료가 있다면
#zip 함수를 이용해 unpacking 할 수 있음
president_list = ["이승만", "박정희", "최규하", "전두환", "노태우", "김영삼", "김대중", "노무현", "이명박", "박근혜", "문재인", "윤석열"]
for i, name in zip((range(1, len(president_list)+1), president_list)):
    print(f"대한민국 {i}번째 대통령은 {name}이다.")
```
## while
- 조건식만 만족하면 무한히 반복하는 구문
- `while condition:`형태로 사용하면 condition이 True라면 while문을 실행, False이면 다음 코드를 실행
	- 만약 condition을 True 값으로 주면 무한루프
	- 무한루프가 상황에 따라 필요(ex. 기기 간 통신 등 상황 유지가 필요한 경우)할 수도, 의도치 않은 상황일 수도 있음(ex. 잘못된 조건으로 인한 무한 출력 등)
```python
my_list = [4,9,3,8,1,6,4]
while my_list:
    print(my_list.pop(my_list.index(max(my_list))))
#my_list의 요소를 큰 것부터 차례로 pop하면서 출력
```
## break, else, pass, continue
- break는 가장 가까운 반복문을 종료시킴
	- else문이 있다면 else도 생략함
- else는 반복문이 모두 종료된 뒤 실행됨
	- 즉, break가 발생했다면 실행되지 않고 break가 발생하지 않았다면 실행되기 때문에 break 발생 여부를 따로 검사할 필요가 없음
- pass는 실행할 코드가 없음을 나타냄
	- 반복문뿐 아니라 코드블록이 있는 곳 어디든 실행할 코드가 없음을 나타내기 위해서 사용할 수 있음
- continue는 현재의 상태를 종료하고 반복문의 시작 위치로 돌아가 다음 상태를 실행함
### else-break 코드 예시
```python
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, "equals", x, "*", n//x)
            break
    else:
        print(n, "is a prime number")
    #else문을 없애면 모든 수가 소수라고 출력됨
```
### pass, continue 코드 예시
```python
for i in range(10):
    if i % 2 == 0:
        pass #continue로 바꾼 것과 결과가 다름
        print(i)
```