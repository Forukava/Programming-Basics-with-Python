month = input()
nights = int(input())

price_s = 0
price_a = 0

if month == "May" or month == "October":
    price_s = nights * 50
    price_a = nights * 65
    if 7 < nights < 14:
        price_s *= 0.95
    elif nights > 14:
        price_s *= 0.7

if month == "July" or month == "August":
        price_s = nights * 76
        price_a = nights * 77

if month == "June" or month == "September":
        price_s = nights * 75.20
        price_a = nights * 68.70
        if nights > 14:
            price_s *= 0.8
if nights > 14:
    price_a *= 0.90

print(f"Apartment: {price_a:.2f} lv.")
print(f"Studio: {price_s:.2f} lv.")
