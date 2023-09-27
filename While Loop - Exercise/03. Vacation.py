money_needed = float(input())
money = float(input())

spend_count = 0
day_count = 0

while money < money_needed and spend_count < 5:
    action = input()
    money_change = float(input())
    day_count += 1
    if action == "save":
        money += money_change
        spend_count = 0
    elif action == "spend":
        money -= money_change
        spend_count += 1
        if money < 0:
            money = 0

if spend_count == 5:
    print("You can't save the money.")
    print(day_count)
elif money >= money_needed:
    print(f"You saved the money for {day_count} days.")

