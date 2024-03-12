from datetime import datetime
date = '1814-02-23' #для перевірки
def get_days_from_today(date):
    try:
        selected_date = datetime.strptime(date, '%Y-%m-%d')
        present_date = datetime.today()
        result = present_date - selected_date
        return result.days
    except ValueError:
        return "Невірний формат введених даних. Введіть дату в форматі YYYY-MM-DD"
print(get_days_from_today(date)) #для перевірки