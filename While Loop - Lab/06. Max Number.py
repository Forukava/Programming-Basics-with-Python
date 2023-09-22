import sys
num = input()

max_number = -sys.maxsize

while num != "Stop":
    total = float(num)
    if total > max_number:
        max_number = total
    num = input()
print(f"{max_number:.0f}")


