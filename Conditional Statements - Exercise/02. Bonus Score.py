number = int(input())
bonus = 0
if number % 2 == 0:
    bonus += 1
if number % 10 == 5:
    bonus += 2
if number <= 100:
    bonus += 5
    print(bonus)
    print(bonus + number)
elif number < 1000:
    bonus1 = (number * 0.2) + bonus
    print(bonus1)
    print(bonus1 + number)
else:
    bonus2 = (number * 0.1) + bonus
    print(bonus2)
    print(bonus2 + number)