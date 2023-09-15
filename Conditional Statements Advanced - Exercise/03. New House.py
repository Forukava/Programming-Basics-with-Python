flowers = input()
count = int(input())
budget = int(input())

total = 0

if flowers == "Roses":
    if count > 80:
        total = (count * 5) * 0.90
    else:
        total = count * 5
if flowers == "Dahlias":
    if count > 90:
        total = (count * 3.80) * 0.85
    else:
        total = count * 3.80
if flowers == "Tulips":
    if count > 80:
        total = (count * 2.80) * 0.85
    else:
        total = count * 2.80
if flowers == "Narcissus":
    if count < 120:
        total = (count * 3) * 1.15
    else:
        total = count * 3
if flowers == "Gladiolus":
    if count < 80:
        total = (count * 2.50) * 1.20
    else:
        total = count * 2.50

if budget >= total:
    final = budget - total
    print(f"Hey, you have a great garden with {count} {flowers} and {final:.2f} leva left.")
else:
    final = total - budget
    print(f"Not enough money, you need {final:.2f} leva more.")
