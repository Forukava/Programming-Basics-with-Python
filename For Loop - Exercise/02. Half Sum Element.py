import sys

n = int(input())

max = -sys.maxsize
sum = 0

for i in range(0, n):
    num = int(input())
    if num > max:
        max = num
        sum += num
    if max == sum - max:
        print("Yes")
        print(f"Sum={sum}")
    else:
        print("No")
        print(f"Diff = {abs(max - sum)}")
