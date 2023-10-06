x, y, z = 1, 2, 3
print(x, y, z)
#Output:1 2 3
#이를 응용해 변수의 값을 쉽게 바꿀 수 있음
x, y = y, x
print(x, y)
#Output:2 1
del z

#입력 값에 반점이 있다면 이를 기준으로 분할
x, y = input().split(",")
x, y = int(x), int(y)
print(x+y)
#Output:x+y 값

#파일 확장자는 쓸 수만 있다면 어떤 것이든 가능
#읽기 위해선 파일이 존재해야함
file = open("data.txt", "r", encoding="UTF-8")
my_text = file.read()
print(my_text)
#open함수를 사용했다면 반드시 close함수로 닫아야 함
#하지 않을 경우 메모리 누수가 발생
file.close()

file = open("data.txt", "r", encoding="UTF-8")
my_text = file.readlines()
#Output:[line 1, line 2, line 3, ...]
#rstrip함수는 string의 함수로써 가장 오른쪽에 있는 문자를 제거함
for line in file: print(line.rstrip())
#Output:line 1
#       line 2
#       line 3
#       ...
file.close()

#"w"mode는 파일 전체를 덮어쓰기 때문에 기존 내용을 유지하려면 "a"로 설정
#"a"mode는 마지막 줄을 줄바꿈한 위치에서부터 쓰기 시작
#파일을 불러오기 전 존재하지 않는다면 파일을 새로 생성
string = "I have a pen. I have a pineapple."
list_string = ["pen", "pineapple\n", "apple", "pen"]
with open("data.txt", "w", encoding="UTF-8") as f:
    f.write(string)
    #Output:"I have a pen. I have a pineapple."
with open("data.txt", "w", encoding="UTF-8") as f:
    for line in string.split(" "): f.write(line+"\n")
    #Output:I
	#       have
	#       a
	#       pen.
	#       I
	#       have
	#       a
	#       pineapple.
with open("data.txt", "w", encoding="UTF-8") as f:
    f.writelines(list_string)
	#Output:penpineapple
	#       applepen

try:
    x = int(input("젯수: "))
    print(10/x)
except ZeroDivisionError as e: #0으로 나누기 예외만 처리함
    print("Exception raised because of ".format(e))
else:
	print("{} can divide any number.".format(x))
finally:
	print("{} is number.".format(x))
 
print(1.0+0.5)
print(1.0-0.5)
print(1.0/0.5)
print(1.0*0.5)
print(1.0//0.5)
print(1.0%0.5)
print(1.0**0.5)