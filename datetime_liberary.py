from datetime import datetime, timedelta

# I want to print date
print(datetime.now())

# Find age based on Birth year
birth_year = 2010
current_year = datetime.now().year
age = current_year - birth_year
print("Age: ", age)

# Find the day of the week for any date
date = datetime(2014, 1, 1)
print(date.strftime("%A")) # Wednesday, Saturday ....
print(date.strftime("%d/%m/%Y")) # Day-Month-Year

# Add or Sub Days from the current date
today = date.today()
# Move 10 days in past
past_date = today - timedelta(days=10)

# Move 10 days in future
future_date = today + timedelta(days=10)

print("Today date: ", today)
print("10 Days ago: ", past_date)
print("10 Days later: ", future_date)

print(today.strftime("%A")) # Wednesday, Saturday ....
print(today.strftime("%d/%m/%Y")) # Day-Month-Year
print(today.strftime("%I:%M %p")) # HH:MM (AM/PM)
print(today.strftime("%A, %d %B %Y"))

print("Year: ", today.year)
print("Month: ", today.month)
print("Day: ", today.day)
print("Hour: ", today.hour)
print("Minute: ", today.minute)
print("Second: ", today.second)



