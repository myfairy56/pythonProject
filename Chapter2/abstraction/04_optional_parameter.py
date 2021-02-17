#옵셔널 파라미터
#파라미터 기본값을 설정한 후 함수 호출할 때 파라미터에 값을 안 넘겨도 되는 것
#옵셔널 파라미터는 모두 마지막에 있어야 한다. (name, nationality=한국, age) 불가
def myself(name, age, nationality="한국"):
    print("내 이름은{}".format(name))
    print("나이는 {}살".format(age))
    print("국적은 {}".format(nationality))

myself("김석진","30","미국") #옵셔널 파라미터를 제공하는 경우
print()
myself("김석진","30") #옵셔널 파라미터를 제공하지 않는 경우