#return 문의 역할
#값 돌려주기, 함수 즉시 종료하기

def square(x):
    print("함수 시작")
    return x * x
    # Dead Code(의미 없는 코드) 앞의 return 문으로 인해 함수가 종료되고 "함수 끝"은 출력 되지 않은 채 넘어간다.
    print("함수 끝")

print(square(3))
print("Hello World!")