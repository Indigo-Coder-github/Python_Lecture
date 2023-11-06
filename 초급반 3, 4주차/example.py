x = (3+0j)
print(x.real, x.imag)
#Output: 3.0 0.0

print(2+4, 2-4, 2*4, 2/4, 2//4, 2%4, -2, +2, abs(2-4), divmod(2,4), pow(2,4), 2**4)
#Output: 6 -2 8 0.5 0 2 -2 2 2 (0,2) 16 16

print(25|14, 25^14, 25&14, 25<<2, 25>>2, ~25)
#Output: 31 23 8 100 6 -26
#25의 bit는 11001, 14의 bit는 01110

print(not(True|False)&(False|False))
#Output: True

print(2<4, 2<=4, 2>4, 2>=4, 2==4, 2!=4, 2 is 4, 2 is not 4)
#Output: True True False False False True False True
#2 is 4, 2 is not 4에 대해서 Warning이 발생하는데 값의 비교에서는 ==, !=을 사용할 것을 권장
#객체에서는 is, is not을 사용할 것을 권장

x = int(input())
if x > 0:
    print("positive number")
    if x % 2 == 0: print("even number")
    else: print("odd number")
elif x < 0: print("negative number")
else: print("zero")

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