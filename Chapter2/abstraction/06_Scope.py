#Scope-변수가 사용 가능한 범위
#로컬변수-변수를 정의한 함수 내에서만 사용 가능
#글로벌변수-모든 곳에서 사용 가능
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

z = 3 #글로벌변수
def my_function():
    z = 4
    print(z)

my_function()
print(z) #글로벌변수

#파라미터도 로컬 변수
def square(x):
    return x * x

print(square(3))

