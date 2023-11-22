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
        
using_parenthese_pair = ()
using_trailing_comma = "a",
using_trailing_comma = ("a",)
using_commas_itmes = "a","b","c"
using_commas_itmes = ("a","b","c")
#생성자의 매개변수는 iterable한 자료형이라면 무관함
using_constructor = tuple("tuple") #("t","u","p","l","e")

#parameter에 따른 반환되는 range의 변화
print(list(range(10)))
#Output:[0,1,2,3,4,5,6,7,8,9]
print(list(range(1,10)))
#Output:[1,2,3,4,5,6,7,8,9]
print(list(range(1,10,2)))
#Output:[1,3,5,7,9]
print(list(range(10,1,-1)))
#Output:[10,9,8,7,6,5,4,3,2,1]
print(list(range(10,1,-2)))
#Output:[10,8,6,4,2]
#range slicing
print(list(range(1,10)[1:]))
#Output:[2,3,4,5,6,7,8,9]

r = range(1,10)
#in 접근
print(11 in r)
#Output:False
print(r.index(5))
#Output:4
print(r[:5])
#Output:range(1,6)
#range의 slicing은 값이 담긴 형태가 아닌 range의 형태를 반환

print(range(10) == range(0,10,1))
#Output:True

single_quote = 'This allows "double quote".'
double_quote = "This allows 'single quote'."
triple_single_quote = '''Triple single quote'''
triple_double_quote = """Triple doulbe quote"""

prime_set = {2,3,5,7,11}
#frozenset의 인자로는 iterable한 자료가 올 수 있음
prime_frozen_set = frozenset({2,3,5,7,11})
even_set_with_comprehension = {i for i in range(20) if i%2 == 0}
#빈 set는 {}로 선언할 수 없음
#{}로 선언하면 빈 dictionary로 인식
empty_set = set()

key_value_pair_braces = {"Korea":"Seoul", "USA":"Washington D.C.", "Japan":"Tokyo", "China":"Beijing"}
dict_comprehension = {x: x**2 for x in range(15)}
dict_constructor_1 = dict([("Korea", "Seoul"), ("USA", "Washington D.C."), ("Japan", "Tokyo"), ("China", "Beijing")])
dict_constructor_2 = dict(Korea="seoul", USA="Washington D.C.", Japan="Tokyo", China="Beijing")