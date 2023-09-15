age = float(input())
pol = input()
if pol == "m":
    if age >= 16:
        print("Mr.")
    else:
        print("Master")
else:
    if age >= 16:
        print("Ms.")
    else:
        print("Miss")