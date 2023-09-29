one = int(input())
two = int(input())
magic = int(input())
counter = 0
combination_is_found = False
for x in range(one, two + 1):
    for y in range(one, two + 1):
        counter += 1
        if x + y == magic:
            combination_is_found = True
            sum = x + y
            break
    if combination_is_found:
        break
if combination_is_found:
    print(f"Combination N:{counter} ({x} + {y} = {sum})")
else:
    print(f"{counter} combinations - neither equals {magic}")