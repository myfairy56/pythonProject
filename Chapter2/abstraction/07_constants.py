#상수(constants-변하지 않는 값
#일반변수와 상수를 구분짓기 위하여 대문자로 표현
PI = 3.14 #원주율 파이

#반지름을 받아서 원 넓이 계산
def calculate_area(r):
    return PI * r * r

radius = 4 #반지름
print("반지름이 {}면, 넓이는 {}".format(radius, calculate_area(radius)))

#PI = 0 수정할 수 있지만 좋지 않은 코드
radius = 6
print("반지름이 {}면, 넓이는 {}".format(radius, calculate_area(radius)))

radius = 7
print("반지름이 {}면, 넓이는 {}".format(radius, calculate_area(radius)))