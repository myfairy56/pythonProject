#Scope
'''
def my_function():
    x = 3 #로컬변수
    print(x)

my_function()
#print(x) #x는 my_function 함수 내에서 정의한 것이므로 이름오류 발생
'''

y = 2 #글로벌변수-모든 곳에서 사용 가능
def my_scope():
    print(y)

my_scope()
print(y)

x = 3 #글로벌변수
def my_function():
    x = 4 #로컬변수
    print(x)

my_function()
print(x) #글로벌변수

#파라미터도 로컬 변수
def square(x):
    return x * x

print(square(3))

