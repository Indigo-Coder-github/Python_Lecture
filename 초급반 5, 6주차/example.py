country_list = ["Angola", "Begium", "Chile", "Denmark", "England"]
print(country_list.index("Chile", 1), country_list[1:].index("Chile"))
#Output:2 1

using_bracket_pair = []
using_bracket_comma = ["a", "b", "c"]
using_list_comprehension = [x for x in [1,2,3]]
using_constructor = list("list")

str_to_list = list("abc") #["a", "b", "c"]
tuple_to_list = list((1, 2, 3)) #[1, 2, 3]
blank_list = list() #[]

university_list = ["Seoul National", "Korea", "Yonsei", "Sugang", "Sungkyunkwan", "Hanyang", "Chungang", "KyungHee", "HUFS", "Seoul", "Konkuk", "Dongguk", "Hongik", "Kookmin", "Soongsil", "Sejong", "Dankook", "Kwangwoon", "Myongji", "Sangmyung", "Gachon", "Hansung", "Seokyeong", "Sahmyook"]
print([university for university in university_list if "k" in university])
#Ouput:['Sungkyunkwan', 'Konkuk', 'Dongguk', 'Hongik', 'Kookmin', 'Dankook', 'Seokyeong', 'Sahmyook']

multiple_list = [[None, None]] * 3
multiple_list[0][0] = 1
print(multiple_list)
#Output:[[1, None],[1, None],[1, None]]
comprehension_list = [[None, None] for _ in range(3)]
comprehension_list[0][0] = 1
print(comprehension_list)
#Output:[[1, None],[None, None],[None, None]]

for i in range(5):
    print(i, end="")
#Output:12345
#변수의 수만큼 sequence 자료가 있다면
#zip 함수를 이용해 unpacking 할 수 있음
president_list = ["이승만", "박정희", "최규하", "전두환", "노태우", "김영삼", "김대중", "노무현", "이명박", "박근혜", "문재인", "윤석열"]
for i, name in zip((range(1, len(president_list)+1), president_list)):
    print(f"대한민국 {i}번째 대통령은 {name}이다.")
    
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, "equals", x, "*", n//x)
            break
    else:
        print(n, "is a prime number")
    #else문을 없애면 모든 수가 소수라고 출력됨
    
for i in range(10):
    if i % 2 == 0:
        pass #continue로 바꾼 것과 결과가 다름
        print(i)