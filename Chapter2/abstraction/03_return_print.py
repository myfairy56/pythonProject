def print_square(x):
    print(x * x)

def get_square(x):
    return x * x

#get_square(3) #print 문이 없기 때문에 출력되지 않은 상태로 종료
#print(get_square(3)) #9출력
print(print_square(3)) #9, None 출력
#파이썬에서는 return 값이 없으면 none 출력