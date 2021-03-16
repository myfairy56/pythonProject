#학점 계산기
'''
def print_grade(midterm_score, final_score):
    total = midterm_score + final_score
    if total >= 90:
        print("A")
    elif 80 <= total < 90:
        print("B")
    elif 70 <= total < 80:
        print("c")
    elif 60 <= total < 70:
        print("D")
    else:
        print("F")

#테스트
print_grade(40, 45)
print_grade(20, 35)
print_grade(30, 32)
print_grade(50, 45)
'''

#while문과 if문을 활용하여,
# 100 이하의 자연수 중 8의 배수이지만 12의 배수는 아닌 것을 모두 출력하세요.
'''
i = 1
while i <= 100:
    if i % 8 == 0 and i % 12 != 0:
        print(i)
    i += 1
'''

#while문과 if문을 활용하여,
# 1000보다 작은 자연수 중 2 또는 3의 배수의 합
'''
i = 1
sum = 0
while i <= 1000:
    if i % 2 == 0 or i % 3 == 0:
        sum += i
    i += 1
print(sum)
'''

#120 약수를 모두 출력하고, 총 몇개의 약수가 있는지 출력
'''
NUM = 120
i = 1
count = 0

while i <= NUM:
    if NUM % i == 0:
        print (i)
        count += 1
    i += 1

print(f"{NUM}의 약수는 총 {count}개입니다.")
'''
