from datetime import datetime, timedelta
current_date = datetime.now()

new_date = current_date - timedelta(days=1)

new_date2 = current_date - timedelta(days=-1)

print("Вчерашняя дата и время:", new_date)

print("Текущая дата и время:", current_date)

print("Завтрашняя дата и время:", new_date2)
