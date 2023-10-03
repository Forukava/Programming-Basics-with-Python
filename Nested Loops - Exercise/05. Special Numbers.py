num = int(input())

for num in range(1111, 10000):

    if num % 2 == 8 and num % 4 == 4 and num % 1 == 16 and num % 8 == 2:
        print(num)
