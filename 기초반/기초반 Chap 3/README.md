# 기초반 3차시

## TOC

- [1. Condition Statement (조건문)](#1-condition-statement-조건문)
- [2. Loop (반복문)](#2-loop-반복문)
  - [2-1. for](#2-1-for)
  - [2-2. while](#2-2-while)

## 1. Condition Statement (조건문)

- [사용자가 정의한 식의 참과 거짓을 평가해 다른 계산이나 행동으로 수행하는 명령](https://en.wikipedia.org/wiki/Conditional_(computer_programming))
  - `if statement: code_block` 형태로 사용한다.
- `else: code`는 `if`문의 `statement`를 만족하지 않을 때 실행한다. `else`문이 없다면 다음 코드블럭을 실행한다.
- `if`문의 `statement`를 만족하지 않을 때 `elif statement: code`가 있다면 `else`문보다 먼저 실행한다.
- `if`, `elif`, `else`문을 여러 개 조합하는 복합 조건문을 한 구문으로 나타낼 수 있는 `match-case`문도 있다.
  - 3.10부터 지원하며 다른 언어의`switch-case`문과 비슷한 것 같지만 [공식문서에서는 Rust나 Haskell의 패턴 매칭 구문과 더 비슷하다고 소개한다.](https://docs.python.org/3/tutorial/controlflow.html#match-statements)
  - *하위버전 호환성을 고려해야 한다면 사용하지 않는 것을 권장한다.*

## 2. Loop (반복문)

### 2-1. for

- Sequence Type의 요소를 순서대로 순회하는 구문
- `for *variables in *sequences: code_block`형태로 사용한다.

### 2-2. while

- 조건식을 만족할 동안 계속 반복하는 구문
- `while condition: code_block`형태로 사용하며 condition이 False가 될 때까지 `code_block`을 실행한다.
  - condition을 True로 설정하면 항상 참이므로 무한 루프 상태를 유지한다.
    - 무한루프는 상황에 따라 필요할 수도(ex. 기기 간 통신 등 상황 유지가 필요한 경우), 의도치 않은 상황일 수도(ex. 잘못된 조건으로 인한 무한 출력 등) 있다.

### 2-3. break, else, pass, continue

- `break`는 현재 코드블록의 반복문을 종료시킴
  - `else`문이 있어도 이를 생략한다.
- `else`문은 반복문이 모두 종료된 뒤 실행됨
- `pass`문은 실행할 코드가 없음을 나타냄
  - 반복문 뿐 아니라 코드블록이 있어야 할 곳을 비워놓기 위한 목적이라면 어디든 사용할 수 있다.
- `continue`문은 현재의 상태를 무시하고 반복문의 시작 위치로 돌아가 다음 상태로 진입함
