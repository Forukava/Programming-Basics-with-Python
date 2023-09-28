steps = input()
count_steps = 0
target = 10000


while steps != "":
    if steps != "Going home" and steps != "":
        count_steps += int(steps)
        steps = input()
    elif steps == "Going home":
        steps = input()
        count_steps += int(steps)
        break
if target > count_steps:
    total = 10000 - count_steps
    print(f"{total} more steps to reach goal.")
else:
    total = count_steps - 10000
    print(f"Goal reached! Good job!\n{total} steps over the goal!")