length = int(input())
width = int(input())
pieces = length * width
total = pieces
cake = 0
final = 0

while True:
    numbers = input()
    if numbers != "STOP":
        current = int(numbers)
        cake += current
        final = total - cake
        if final < 0:
            break
    elif numbers == "STOP":
        break

if final < 0:
    print(f"No more cake left! You need {-final} pieces more.")
else:
    print(f"{final} pieces are left.")