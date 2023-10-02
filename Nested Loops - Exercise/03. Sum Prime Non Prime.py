num = input()
sum_prime = 0
sum_non = 0
while num != "stop":
    nums = int(num)
    if nums < 0:
        print("Number is negative.")
        num = input()
        continue
    if nums == 0:
        num = input()
        continue
    if nums == 3:
        sum_prime += nums
        num = input()
        continue
    if nums % 2 == 0 or nums % 3 == 0:
        sum_non += nums
        num = input()
    else:
        sum_prime += nums
        num = input()

print(f"Sum of all prime numbers is: {sum_prime}")
print(f"Sum of all non prime numbers is: {sum_non}")