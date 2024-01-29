# 기초반 3차시

## 1. Condition Statement(조건문)

- 기본적으로 if문을 통해 조건검사를 하고 elif를 통해 추가적인 분기, else를 통해 나머지를 처리
- `match`는 3.10부터 지원하며 `switch-case`문과 비슷하지만 [공식문서에서는 Rust나 Haskell의 패턴 매칭 구문과 더 비슷하다고 소개함](https://docs.python.org/3/tutorial/controlflow.html#match-statements)
- *하위버전 호환성을 고려해야 한다면 사용하지 말 것*

## 2. Loop(반복문)

### 2-1. for

- Sequence type의 요소를 순서대로 반복하는 구문
- `for *variables in *sequences:`형태로 사용
- [zip 함수에 대해서는 중급반 3주차 자료를 참조](https://github.com/Indigo-Coder-github/Python_Lecture/tree/main/%EC%A4%91%EA%B8%89%EB%B0%98%203%EC%A3%BC%EC%B0%A8#zipiterables-strictfalse)

### 2-2. while

- 조건식만 만족하면 무한히 반복하는 구문
- `while condition:`형태로 사용하면 condition이 True라면 while문을 실행, False이면 다음 코드를 실행
  - 만약 condition을 True 값으로 주면 무한루프
  - 무한루프가 상황에 따라 필요(ex. 기기 간 통신 등 상황 유지가 필요한 경우)할 수도, 의도치 않은 상황일 수도 있음(ex. 잘못된 조건으로 인한 무한 출력 등)

### 2-3. break, else, pass, continue

- break는 가장 가까운 반복문을 종료시킴
  - else문이 있다면 else도 생략함
- else는 반복문이 모두 종료된 뒤 실행됨
  - 즉, break가 발생했다면 실행되지 않고 break가 발생하지 않았다면 실행되기 때문에 break 발생 여부를 따로 검사할 필요가 없음
- pass는 실행할 코드가 없음을 나타냄
  - 반복문뿐 아니라 코드블록이 있는 곳 어디든 실행할 코드가 없음을 나타내기 위해서 사용할 수 있음
- continue는 현재의 상태를 종료하고 반복문의 시작 위치로 돌아가 다음 상태를 실행함
