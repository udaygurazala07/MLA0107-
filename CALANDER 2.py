import calendar

# input from user
year = int(input("Enter year: "))
month = int(input("Enter month (1-12): "))

# display calendar
print("\nCalendar:\n")
print(calendar.month(year, month))
