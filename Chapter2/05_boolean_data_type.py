#불대수 - 일상적인 논리를 수학적으로 표현한 것
#불 대수의 값 = 진리값 (True, False)
#불린(Boolean) - 따옴표 없이 써야 함
print(True)
print(False,"\n")
#불 대수의 연산 = AND, OR, NOT
#AND연산 : x와 y가 모두 참일 때만 x AND y가 참
print(True and True)
print(True and False)
print(False and True)
print(False and False,"\n")
#OR연산 :  x와 y 중 하나라도 참이면 x OR y는 참
print(True or True)
print(True or False)
print(False or True)
print(False or False,"\n")
#NOT : 반대로 뒤집어 주는 역할 참 > 거짓으로 거짓 > 참으로
print(not True)
print(not False)

#명제
print(2>1)
print(3>=2)
print(2==2)
print(2!=2)
print("Hello"=="Hello")
print("Hello"!="Hello","\n")

print(2>1 and "Hello" == "Hello") #True and True > True
print(not not True) #not False > True
print(not not False) #not True > False
print( 7==7 or (4<3 and 12>10)) #True or (False and True) > True

x=3
print(x>4 or not (x<2 or x==3)) #False or not True > False