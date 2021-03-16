def is_evenly_divisible(number):
    return number%2 == 0

#테스트
print(is_evenly_divisible(3))
print(is_evenly_divisible(7))
print(is_evenly_divisible(8))
print(is_evenly_divisible(218))
print(is_evenly_divisible(317))

def calculate_change(payment, cost):
    change = payment-cost
    print("50000원 지폐 : {}장".format(change // 50000))
    change %= 50000
    print("10000원 지폐 : {}장".format(change // 10000))
    change %= 10000
    print("5000원 지폐 : {}장".format(change // 5000))
    change %= 5000
    print("1000원 지폐 : {}장".format(change // 1000))
    change %= 1000
#테스트
calculate_change(100000, 33000)
print()
calculate_change(500000, 378000)
