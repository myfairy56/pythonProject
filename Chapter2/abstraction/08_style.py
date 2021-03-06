#모든 변수와 함수 이름은 소문자 (여러 단어일 경우 _로 분리)
#모든 상수 이름은 대문자(여러 단어일 경우 _로 분리)

print(6.28 * 4)
print(3.14 * 4 * 4)
print(6.28 * 8)
print(3.14 *8 *8)
'''
PI = 3.14

radius = 4 #반지름
print(2 * PI * radius)
print(PI * radius * radius)

radius=8
print( 2 * PI * radius)
print(PI * radius * radius)
'''
PI = 3.14

#반지름이 r인 원의 둘레 계산
def calculate_circumference(r):
    return 2 * PI * r

#반지름이 r인 원의 넓이 계산
def calculate_area(r):
    return PI * r * r

radius = 4
print(calculate_circumference((radius)))
print(calculate_area((radius)))

radius = 8
print(calculate_circumference(radius))
print(calculate_area(radius))