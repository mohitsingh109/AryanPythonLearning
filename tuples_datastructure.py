# Tuples

months = ["Jan", "Feb", "Dec"]
months.remove("Jan")
months.append("Hack")
months[2] = "Again Hacked"
print(months)

# Tuples don't allow delete/update/insert
months_tuple = ("Jan", "Feb", "Dec")
#               0        1      2
print(months_tuple[1])

for month in months_tuple:
    print(month)