import sys
num = input()

min_number = sys.maxsize

while num != "Stop":
    total = float(num)
    if total < min_number:
        min_number = total
    num = input()
print(f"{min_number:.0f}")