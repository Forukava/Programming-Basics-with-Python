tab = int(input())
salary = int(input())

for i in range(tab):
    vt = input()

    if vt == "Facebook":
        salary -= 150
    elif vt == "Instagram":
        salary -= 100
    elif vt == "Reddit":
        salary -= 50

    if salary <= 0:
        break
if salary > 0:
    print(f"{salary}")
else:
    print("You have lost your salary")

