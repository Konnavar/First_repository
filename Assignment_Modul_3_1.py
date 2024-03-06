from datetime import datetime
date = '3033-03-03' #для перевірки
def get_days_from_today(date):
    selected_date = datetime.strptime(date, '%Y-%m-%d')
    present_date = datetime.today()
    result = present_date - selected_date
    return result.days
print(get_days_from_today(date)) #для перевірки