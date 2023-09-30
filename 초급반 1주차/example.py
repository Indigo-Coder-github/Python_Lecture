import os
my_input = input("이곳에 입력하세요: ")
for i in range(1,5):
    print("{}회: {}\n{}".format(i, input, os.listdir()))
 
print("This","is","Σπάρτη", sep="!")
#Output:This!is!Σπάρτη
#sep를 활용한 출력
print("I have a pen", end=". ")
print("I have a pineapple")
#Ouput:I have a pen. I have a pineapple
#end를 활용한 출력
print("start\tend\thigh\tlow")
#Output:start    end    high    low
#제어문자를 활용한 출력

var1 = "format specifiers"
var2 = "formatting"
var3 = "f-string"
print("This is %s"%var1) #서식 지정자를 활용
print("This is {}".format(var2)) #format 함수를 활용
print(f"This is {var3}") #f-string을 활용