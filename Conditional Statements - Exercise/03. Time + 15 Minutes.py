hours = int(input())
minutes = int(input())

bonus = minutes + 15
if bonus >= 60:
    bonus = bonus - 60
    hours = hours + 1
if hours > 23:
    hours = 0
if bonus < 10:
    print(f"{hours}:0{bonus}")
else:
    print(f"{hours}:{bonus}")