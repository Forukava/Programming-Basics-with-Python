num = input()
total = 0
while num != "NoMoreMoney":

    num = float(num)
    if num > 0:
        total += num
        print(f"Increase: {float(num):.2f}")
        num = input()
    else:
        print("Invalid operation!")
        break
print(f"Total: {total:.2f}")
