import sys
sum = 0
max = -sys.maxsize
n = int(input())

for i in range(n):
    num = int(input())
    if num > max:
        max = num
    sum += num
rest_sum = sum - max
if max == rest_sum:
    print("Yes")
    print(f"Sum = {max}")
else:
    diff = abs(max - rest_sum)
    print(f"No\nDiff = {diff}")
