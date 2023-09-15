city = input()
sum = float(input())

if city == "Sofia":
    if sum >= 0 and sum <= 500:
        total = sum * 0.05
        print(f"{total:.2f}")
    elif sum > 500 and sum <= 1000:
        total = sum * 0.07
        print(f"{total:.2f}")
    elif sum > 1000 and sum <= 10000:
        total = sum * 0.08
        print(f"{total:.2f}")
    elif sum > 10000:
        total = sum * 0.12
        print(f"{total:.2f}")
    else:
        print("error")

elif city == "Varna":
    if sum >= 0 and sum <= 500:
        total = sum * 0.045
        print(f"{total:.2f}")
    elif sum > 500 and sum <= 1000:
        total = sum * 0.075
        print(f"{total:.2f}")
    elif sum > 1000 and sum <= 10000:
        total = sum * 0.10
        print(f"{total:.2f}")
    elif sum > 10000:
        total = sum * 0.13
        print(f"{total:.2f}")
    else:
        print("error")

elif city == "Plovdiv":
    if sum >= 0 and sum <= 500:
        total = sum * 0.055
        print(f"{total:.2f}")
    elif sum > 500 and sum <= 1000:
        total = sum * 0.08
        print(f"{total:.2f}")
    elif sum > 1000 and sum <= 10000:
        total = sum * 0.12
        print(f"{total:.2f}")
    elif sum > 10000:
        total = sum * 0.145
        print(f"{total:.2f}")
    else:
        print("error")
else:
    print("error")
