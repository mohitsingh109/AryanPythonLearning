import time
totalmin = int(input("How many minutes do you want?"))
while(totalmin >= 0):
	hour = (totalmin // 60)
	min = (totalmin % 60)
	print(f"You have {hour} hours and {min} minutes")
	time.sleep(30)
	totalmin = totalmin - 1
print("Time is up!")
