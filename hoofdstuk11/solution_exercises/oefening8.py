currentHour = int(input("Enter the current hour: "))
waitTime = int(input("How long do you want to wait: "))

counter = 0

while counter != waitTime:
    if currentHour == 24:
        currentHour = 0
    else:
        counter += 1
        currentHour += 1

print("The alarm will sound at", str(currentHour) + "h.")
