from datetime import datetime, timedelta
current_date = datetime.now()

new_date = current_date - timedelta(days=5)

print("Текущая дата и время:", current_date)
print("Дата и время пять дней назад:", new_date)
