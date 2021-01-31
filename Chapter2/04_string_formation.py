#.format 메소드
print("저는 {}, {}, {}를 좋아합니다!".format("김남준","김석진","민윤기"))
print("저는 {1}, {0}, {2}를 좋아합니다!".format("김남준","김석진","민윤기"))

num_1 = 1
num_2 = 3
print("{0} 나누기 {1}은 {2} 입니다.".format(num_1, num_1, num_1/num_2))
print("{0} 나누기 {1}은 {2:.2f} 입니다.".format(num_1, num_1, num_1/num_2)) #.2는 소수점 둘째 자리로 반올림
print("{0} 나누기 {1}은 {2:.0f} 입니다.".format(num_1, num_1, num_1/num_2)) #정수로 반환

#f-string
name = "김석진"
age = 30
print(f"제 이름은 {name}이고 {age}살입니다.")

#%기호
print("제 이름은 %s이고 %d살입니다." %(name, age))

#실습과제
wage = 5
exchange_rate = 1142.16
print("{}시간에 {}{} 벌었습니다.".format(1,wage*1,"달러"))
print("{}시간에 {}{} 벌었습니다.".format(1,wage*5,"달러"))
print("{}시간에 {:.1f}{} 벌었습니다.".format(1,wage*1*exchange_rate,"원"))
print("{}시간에 {:.1f}{} 벌었습니다.".format(5,wage*5*exchange_rate,"원"))