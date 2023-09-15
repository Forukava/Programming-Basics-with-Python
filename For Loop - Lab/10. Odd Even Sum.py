n = int(input())

sum_left = 0
sum_right = 0

for i in range(1, n + 1):
    num = int(input())
    if i % 2 == 0:
        sum_left += num
    else:
        sum_right += num

if sum_left == sum_right:
    print('Yes')
    print(f'Sum = {sum_left}')
else:
    print('No')
    print(f'Diff = {abs(sum_left - sum_right)}')