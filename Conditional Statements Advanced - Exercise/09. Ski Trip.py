nights = int(input())
room = input()
evaluation = input()

price = 0

if room == "room for one person":
    price = (nights-1) * 18
    if evaluation == "positive":
        price *= 1.25
    elif evaluation == "negative":
        price *= 0.9
if room == "apartment":
    if nights < 10:
        price = (nights -1) * 25
        price = price * 0.70
        if evaluation == "positive":
            price *= 1.25
        elif evaluation == "negative":
            price *= 0.9
    if 10 < nights <15:
        price = (nights -1) * 25
        price = price * 0.65
        if evaluation == "positive":
            price *= 1.25
        elif evaluation == "negative":
            price *= 0.9
    if nights > 15:
        price = (nights - 1) * 25
        price = price * 0.50
        if evaluation == "positive":
            price *= 1.25
        elif evaluation == "negative":
            price *= 0.9
if room == "president apartment":
    if nights < 10:
        price = (nights -1) * 35
        price = price * 0.90
        if evaluation == "positive":
            price *= 1.25
        elif evaluation == "negative":
            price *= 0.9
    if 10 < nights < 15:
        price = (nights -1) * 35
        price = price * 0.85
        if evaluation == "positive":
            price *= 1.25
        elif evaluation == "negative":
            price *= 0.9
    if nights > 15:
        price = (nights - 1) * 35
        price = price * 0.80
        if evaluation == "positive":
            price *= 1.25
        elif evaluation == "negative":
            price *= 0.9

print(f"{price:.2f}")
