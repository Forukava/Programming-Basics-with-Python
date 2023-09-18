r1 = 0
r2 = 0
r3 = 0
r4 = 0
r5 = 0
num_count = int(input())

for _ in range(num_count):
    num = int(input())

    if num < 200:
        r1 += 1
    elif 200 <= num <= 399:
        r2 += 1
    elif 400 <= num <= 599:
        r3 += 1
    elif 600 <= num <= 799:
        r4 += 1
    elif num >= 800:
        r5 += 1

r1_percent = r1 / num_count * 100
r2_percent = r2 / num_count * 100
r3_percent = r3 / num_count * 100
r4_percent = r4 / num_count * 100
r5_percent = r5 / num_count * 100

print(f"{r1_percent:.2f}%")
print(f"{r2_percent:.2f}%")
print(f"{r3_percent:.2f}%")
print(f"{r4_percent:.2f}%")
print(f"{r5_percent:.2f}%")
