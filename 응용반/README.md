# Git

- 리눅스를 개발한 리누스 토르발스가 기존의 버전 관리 시스템이 맘에 안들어 너무 빡친 나머지 2주만에 개발한 시스템
- 이걸 웹사이트로 만든 것이 Github이며 2010년대부터 인기가 급상승하면서 MS가 인수했음
  - MS 인수 당시 오픈소스 진영의 철학이 침해되지 않을까라는 우려가 있었으나 오히려 MS에서 Github를 지지 및 권장함
- Git의 구조와 명령어가 직관적이지 않아 입문 난이도가 있음
  - Git의 저장소 구조와 Branch 구조에 따라 두 가지로 나눠 볼 예정

## Git 저장소

- [알리바바 클라우드 글을 출처로 함](https://www.alibabacloud.com/blog/a-detailed-explanation-of-the-underlying-data-structures-and-principles-of-git_597391)
![Git Structure.png](./Git%20Structure.png)

## workspace

- 로컬 폴더에서 볼 수 있는 현재 작업 공간

## index

- 파일을 임시 저장하는 공간
- commit은 index에 있는 파일을 local repository로 전달해 대체하는 명령어
- .git 폴더에 저장됨

## local repository

- remote repository로 올리고자 하는 것이 아니라면 오프라인에서도 작업 가능
- index와 마찬가지로 .git 폴더에 저장됨

## remote repository

- Github에 있는 repository

## Git Branch 구조

![Git Structure.png](./Git%20Branch%20Structure.png)

## Git Flow

![Git Flow.png](./Git%20Flow.png)

## Github Flow

![Github Flow.png](./Github%20Flow.png)