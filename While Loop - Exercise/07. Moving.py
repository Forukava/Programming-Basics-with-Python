width = int(input())
length = int(input())
heiht = int(input())

area = width * length * heiht
total = 0
final = 0
while True:
    numbers = input()
    if numbers != "Done":
        current = int(numbers)
        total += current
        final = area - total
        if final < 0:
            break
    elif numbers == "Done":
        break

if final < 0:
    print(f"No more free space! You need {-final} Cubic meters more.")
else:
    print(f"{final} Cubic meters left.")