
achtor = input()
a_points = float(input())
num_evaluative = int(input())

for _ in range(num_evaluative):
    name_evaluative = input()
    points_evaluative = float(input())
    eva = len(name_evaluative)
    a_points += ((eva * points_evaluative) / 2)

    if a_points > 1250.5:
        break

if a_points > 1250.5:
    print(f"Congratulations, {achtor} got a nominee for leading role with {a_points:.1f}!")
else:
    needed = 1250.5 - a_points
    print(f"Sorry, {achtor} you need {needed:.1f} more!")
