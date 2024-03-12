import random

min = 10#int(input("Введіть мінімальне число: "))
max = 20#int(input("Введіть максимальне число: "))
quantity = 5#int(input("Введіть кількість чисел: "))

def get_numbers_ticket(min, max, quantity): 
    if 1 <= quantity <= (max - min + 1) and min >= 1 and max <= 1000:
        lottery_numbers = random.sample(range(min, max + 1), quantity)
        return sorted(lottery_numbers)
    else: 
        print ("Помилка: некоректні вхідні дані")
        return []
       
lottery_numbers = get_numbers_ticket(min, max, quantity)
print("Ваші лотерейні числа:", lottery_numbers)