
fruit = input()
d_of_week = input()
quantity = float(input())

if d_of_week == "Monday" or d_of_week == "Tuesday" or d_of_week == "Wednesday" or d_of_week == "Thirsday" or d_of_week == "Friday":
    if fruit == "banana":
        bu = quantity * 2.50
        print(f"{bu:.2f}")
    elif fruit == "apple":
        ap = quantity * 1.20
        print(f"{ap:.2f}")
    elif fruit == "orange":
        ora = quantity * 0.85
        print(f"{ora:.2f}")
    elif fruit == "grapefruit":
        gr = quantity * 1.45
        print(f"{gr:.2f}")
    elif fruit == "kiwi":
        ki = quantity * 2.70
        print(f"{ki:.2f}")
    elif fruit == "pineapple":
        pi = quantity * 5.50
        print(f"{pi:.2f}")
    elif fruit == "grapes":
        gr = quantity * 3.85
        print(f"{gr:.2f}")
    else:
        print("error")
elif d_of_week == "Saturday" or d_of_week == "Sunday":
        if fruit == "banana":
            ba = quantity * 2.70
            print(f"{ba:.2f}")
        elif fruit == "apple":
            app = quantity * 1.25
            print(f"{app:.2f}")
        elif fruit == "orange":
            oran = quantity * 0.90
            print(f"{oran:.2f}")
        elif fruit == "grapefruit":
            grap = quantity * 1.60
            print(f"{grap:.2f}")
        elif fruit == "kiwi":
            kiw = quantity * 3.00
            print(f"{kiw:.2f}")
        elif fruit == "pineapple":
            pin = quantity * 5.60
            print(f"{pin:.2f}")
        elif fruit == "grapes":
            gra = quantity * 4.20
            print(f"{gra:.2f}")
        else:
            print("error")
else:
    print("error")