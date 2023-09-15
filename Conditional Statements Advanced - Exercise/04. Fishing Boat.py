budget = int(input())
season = input()
fisherman = int(input())

total = 0

if season == "Spring":
    if fisherman > 0 and fisherman <= 6:
        total = 3000 * 0.90
    elif fisherman > 7 and fisherman <= 11:
        total = 3000 * 0.85
    elif fisherman > 12:
        total = 3000 * 0.75
if season == "Summer":
    if fisherman > 0 and fisherman <= 6:
        total = 4200 * 0.90
    elif fisherman > 7 and fisherman <= 11:
        total = 4200 * 0.85
    elif fisherman > 12:
        total = 4200 * 0.75
if season == "Autumn":
    if fisherman > 0 and fisherman <= 6:
        total = 4200 * 0.90
    elif fisherman > 7 and fisherman <= 11:
        total = 4200 * 0.85
    elif fisherman > 12:
        total = 4200 * 0.75
if season == "Winter":
    if fisherman > 0 and fisherman <= 6:
        total = 2600 * 0.90
    elif fisherman > 7 and fisherman <= 11:
        total = 2600 * 0.85
    elif fisherman > 12:
        total = 2600 * 0.75

if season != 'Autumn' and fisherman % 2 == 0:
    total = total * 0.95

if budget - total >= 0:
    final = budget - total
    print(f"Yes! You have {final:.2f} leva left.")
else:
    print(f"Not enough money! You need {abs(total - budget):.2f} leva.")