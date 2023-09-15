import sys
n = int(input())
max = -sys.maxsize
min = sys.maxsize
for num in range(n):
    current = int(input())
    if current > max:
        max = current
    if current < min:
        min = current
print(f"Max number: {max}")
print(f"Min number: {min}")