pages = int(input())
numberOfPagesPerHour = int(input())
numberOfDays = int(input())
hoursToFin = pages // numberOfPagesPerHour
hoursPerDay = hoursToFin / numberOfDays
print(hoursPerDay)