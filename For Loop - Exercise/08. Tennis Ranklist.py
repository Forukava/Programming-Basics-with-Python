import math
turnirs = int(input())
ranglist_number = int(input())

W = 0
F = 0
SF = 0

for _ in range(turnirs):
    stage = input()
    if stage == "W":
        W += 2000
    elif stage == "F":
        F += 1200
    elif stage == "SF":
        SF += 720

total_points = ranglist_number + W + F + SF
average_points = (total_points - ranglist_number) / turnirs
won_turnirs = W / 2000
won_turnirs_percent = won_turnirs / turnirs * 100

print(f"Final points: {total_points}")
print(f"Average points: {math.floor(average_points)}")
print(f"{won_turnirs_percent:.2f}%")