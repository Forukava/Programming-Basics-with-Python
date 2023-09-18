age = int(input())
price_l = float(input())
one_toy = int(input())

toy = 0
cash = 0
for birthday in range (1, age + 1):
    if birthday % 2 == 0:
        cash += birthday * 5
    else:
        toy += one_toy

final = toy + cash
total = final - (age // 2)
if price_l > total:
    diff = price_l - total
    print(f"No! {diff:.2f}")
else:
    diff = total - price_l
    print(f"Yes! {diff:.2f}")


