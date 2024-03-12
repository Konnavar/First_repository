import re

def normalize_phone(phone_number):
    normalized_number = re.sub(r'\D', '', phone_number) # Видаляємо всі символи, крім цифр та '+'
      
    if len(normalized_number) == 12 and normalized_number[0] == '3' and normalized_number[1] == '8' and normalized_number[2] == '0':  # Перевіряємо, чи відповідає номер критеріям
        return '+' + normalized_number  # Якщо так, повертаємо номер без зайвих символів
    elif len(normalized_number) == 10:  # Якщо номер без міжнародного коду, додаємо '+38' та повертаємо
        return '+38' + normalized_number
    else:  # Якщо номер не відповідає критеріям, повертаємо порожній рядок
        return ''

raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
] # Приклад з завдання

sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)