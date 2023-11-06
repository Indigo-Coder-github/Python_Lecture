# Numeric Type
- 아래에 표시된 내용 외에 더 많은 기능과 함수는 공식 문서 참조
## int
- `int(x, base=10)`생성자를 통해 int형으로 바꿀 수 있음
- 정확도 제한이 없음
## float
- `float(x=0.0)`생성자를 통해 float형으로 바꿀 수 있음
- C언어의 double형에 해당하는 정확도를 가짐
## complex
- `complex(real=0, imag=0)`이나 `complex(string)`생성자를 통해 complex형으로 바꿀 수 있음
- 실수부와 허수부 모두 부동 소수점 방식을 사용
	- 실수부는 `z.real`로, 허수부는 `z.imag`로 추출하며 실수로 표기됨
```python
x = (3+0j)
print(x.real, x.imag)
#Output: 3.0 0.0
```
## 연산자
- 연산자 우선순위는 [이를 따름](https://docs.python.org/3/reference/expressions.html#operator-summary)

|        연산자         | 결과         |                                  비고                                  |
|:---------------------:|:------------ |:----------------------------------------------------------------------:|
|         `x+y`         | 더하기       |                                                                        |
|         `x-y`         | 빼기         |                                                                        |
|         `x*y`         | 곱하기       |                                                                        |
|         `x/y`         | 나누기       |                                                                        |
|        `x//y`         | 몫           | x,y 모두 정수가 아니라면 반환값은 항상 실수<br>complex는 지원하지 않음 |
|         `x%y`         | 나머지       |                        complex는 지원하지 않음                         |
|         `-x`          | 부정         |                                                                        |
|         `+x`          | 변하지 않음  |                                                                        |
|       `abs(x)`        | 절댓값       |                                                                        |
|    `divmod(x, y)`     | 몫, 나머지쌍 |                        complex는 지원하지 않음                         |
| `pow(x, y, mod=None)` | x의 y제곱    |    mod에 파라미터를 입력하면 나머지 반환<br>0의 0제곱은 1로 정의함     |
|        `x**y`         | x의 y제곱    |                         0의 0제곱은 1로 정의함                         |
```python
print(2+4, 2-4, 2*4, 2/4, 2//4, 2%4, -2, +2, abs(2-4), divmod(2,4), pow(2,4), 2**4)
#Output: 6 -2 8 0.5 0 2 -2 2 2 (0,2) 16 16
```
### int, flaot 연산자
- 더 많은 함수는 [math](https://docs.python.org/3/library/math.html#module-math) 모듈과 [cmath](https://docs.python.org/3/library/cmath.html#module-cmath)모듈에서 정의하고 있음

|     연산자      | 결과                                    |
|:---------------:|:--------------------------------------- |
| `math.trunc(x)` | 정수부 반환                             |
|  `round(x, n)`  | 소수 n번째 자릿수까지 표기되도록 반올림 |
| `math.floor(x)` | x이하의 가장 큰 정수 반환               |
| `math.ceil(x)`  | x이상의 가장 작은 정수 반환             |
### 비트 연산자
- 정수가 주어지면 해당 정수의 모든 비트에 대한 연산을 수행

| 연산자 | 결과                       |            비고            |
|:------:| -------------------------- |:--------------------------:|
|  x\|y  | x or y 비트연산            |                            |
| `x^y`  | x xor y 비트연산           |                            |
| `x&y`  | x and y 비트연산           |                            |
| `x<<n` | 왼쪽으로 n비트만큼 shift   | n은 음수값을 허용하지 않음 |
| `x>>n` | 오른쪽으로 n비트만큼 shift | n은 음수값을 허용하지 않음 |
|  `~x`  | 비트를 반전                |                            |
```python
print(25|14, 25^14, 25&14, 25<<2, 25>>2, ~25)
#Output: 31 23 8 100 6 -26
#25의 bit는 11001, 14의 bit는 01110
```
# Boolean Type
- True, False라는 두 개의 상수로 구성된 타입
- 내장 함수 `bool(value)`를 사용하면 value의 Boolean 타입을 반환해줌
	- 이때 `None`, `False`, `0`, `0.0`,` 0j`, `''`, `()`, `[]`, `{}`, `set()`, `range(0)`은 False로, 나머지는 True로 반환함
- [[초급반 3,4주차#int|int]]형의 하위타입이기 때문에 False와 True가 각각 0과 1로 간주될 수 있지만 `int()`함수를 사용해 분명하게 변환할 것을 권장함
## Boolean 연산자(논리 연산자)
- 논리 연산자는 아래 표와 같음
	- 비트 연산자에 대응되더라도 논리 연산자를 사용할 것을 권장함
- Python의 논리 연산자는 short-circuit operator로
	- `x or y`에 대해 x가 참이면 y의 참/거짓을 검사하지 않음
	- `x and y`에 대해 x가 거짓이면 y의 참/거짓을 검사하지 않음
- not 연산자에 대해서는 다음과 같은 주의사항이 있음
	- 다른 연산보다 우선순위가 낮아서 `not a==b`는 `not (a==b)`와 동치이며 `a == not b`가 아닌 `a == (not b)`로 표기해야 함
	- `~`연산자는 3.12부터 deprcated되며 3.14에서는 에러를 발생시키도록 업데이트할 예정임

| 논리 연산자 | 비트 연산자 |                    결과                    |
|:-----------:|:-----------:|:------------------------------------------:|
|  `x or y`   |      &      |      x가 참이면 x를, 아니면 y를 반환       |
|  `x and y`  |     \|      |     x가 거짓이면 x를, 아니면 y를 반환      |
|   `not x`   |      ~      | x가 거짓이면 `True`를, 아니면 False를 반환 |                                    |
```python
print(not(True|False)&(False|False))
#Output: True
```
## 비교 연산자
- 비교 연산자 간의 우선순위는 모두 동일함
- Python은 비교 연산자를 연속으로 쓸 수 있음

| 연산자 | 의미                    |
|:------:|:----------------------- |
|   <    | 보다 작다               |
|   <=   | 작거나 같다             |
|   >    | 보다 크다               |
|   >=   | 크거나 같다             |
|   ==   | 같다                    |
|   !=   | 같지 않다               |
|   is   | object identity         |
| is not | negated object identity |
- Numeric type을 제외하고 다른 타입 간에는 비교 연산자를 사용할 수 없음
	- complex는 크기 비교 연산이 불가능함
- instance 간의 비교는 [[중급반 1주차 & 초급반 7주차#Magic Method(Special Method)|magic method]]를 구현하여 정의할 수 있음
	- `is`, `is not`은 사용자 설정이 불가능함
```python
print(2<4, 2<=4, 2>4, 2>=4, 2==4, 2!=4, 2 is 4, 2 is not 4)
#Output: True True False False False True False True
#2 is 4, 2 is not 4에 대해서 Warning이 발생하는데 값의 비교에서는 ==, !=을 사용할 것을 권장
#객체에서는 is, is not을 사용할 것을 권장
```
# Condition Statement(조건문)
- 기본적으로 if문을 통해 조건검사를 하고 elif를 통해 추가적인 분기, else를 통해 나머지를 처리
```python
x = int(input())
if x > 0:
    print("positive number")
    if x % 2 == 0: print("even number")
    else: print("odd number")
elif x < 0: print("negative number")
else: print("zero")
```
 - `match`는 3.10부터 지원하며 `switch-case`문과 비슷하지만 [공식문서에서는 Rust나 Haskell의 패턴 매칭 구문과 더 비슷하다고 소개함](https://docs.python.org/3/tutorial/controlflow.html#match-statements)
 - *하위버전 호환성을 고려해야 한다면 사용하지 말 것*
```python
point = map(int, input().split(" "))
match point:
    case (0,0):
        print("Origin Point")
	#y와 x는 변수로써 case문 내에서 사용할 수 있음
    case (0, y) | (x, 0):
	    print("Point is on the axes")
	#case 뒤에 붙는 if문은 guard라고 함
	#guard가 거짓이면 다음 case문으로 진행
	case (x, y) if x == y:
	    print("The point is on the y=x")
	case (x, y):
	    print("{}, {}".format(x,y))
	#case의 조건에 "_"주면 else문과 같은 역할
    case _:
        print("unexpected input")
```