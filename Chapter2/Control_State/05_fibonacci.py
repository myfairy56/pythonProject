#피보나치 수열의 첫 50개 항을 차례대로 출력하는 프로그램을 작성해 보세요
before = 0
after = 1
i = 1

while i <= 50:
    print(after)
    temp = before
    before = after
    after += temp
    i += 1

