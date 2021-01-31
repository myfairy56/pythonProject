#형변환(Type Conversion) - 값을 한 자료형에서 다른 자료형으로 바꾸는 것
# 정수 > 소수 or 문자열 > 소수

#int 정수
print(int(3.8))

#float 소수
print(float(3))

#문자열 > 정수형 / 문자열 > 소수형
print(int("2") + int("5"))
print(float("1.1")+float("2.5"))

print(str(2) + str(5))

age = 7
print("제 나이는 " + str(age) +"살입니다.")

#print(int("Hello World")) 문자열을 숫자로 바꿀 수 없기 때문에 에러가 남