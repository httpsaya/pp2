from datetime import datetime, timedelta

current_date = datetime.now()

new_date = current_date.replace(microsecond=0)

print("Текущая дата и время:", new_date)
