from datetime import datetime
date1_str = input("Enter the first date (YYYY-MM-DD HH:MM:SS): ")
date2_str = input("Enter the second date (YYYY-MM-DD HH:MM:SS): ")

date_format = "%Y-%m-%d %H:%M:%S"
date1 = datetime.strptime(date1_str, date_format)
date2 = datetime.strptime(date2_str, date_format)


difference_seconds = abs((date2 - date1).total_seconds())

print("The difference between the two dates is", difference_seconds, "seconds.")
