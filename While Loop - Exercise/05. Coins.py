coin = float(input())
current_count = 0
current_remainder = 0
current_1 = 0
current_2 = 0
current_50 = 0
current_20 = 0
current_10 = 0
current_05 = 0
current_02 = 0
current_01 = 0

if (coin / 2) >= 0:
    current_2 = coin // 2
    current_count += current_2
    current_2 = coin % 2
if (current_2 / 1) >= 0:
    current_1 = current_2 // 1
    current_count += current_1
    current_1 = current_2 % 1
    current_1 = round(current_1, 2)
if (current_1 / 0.50) >= 0:
    current_50 = current_1 // 0.50
    current_count += current_50
    current_50 = current_1 % 0.50
    current_50 = round(current_50, 2)
if (current_50 / 0.20) >= 0:
    current_20 = current_50 // 0.20
    current_count += current_20
    current_20 = current_50 % 0.20
    current_20 = round(current_20, 2)
if (current_20 / 0.10) >= 0:
    current_10 = current_20 // 0.1
    current_count += current_10
    current_10 = current_20 % 0.10
    current_10 = round(current_10, 2)
if (current_10 / 0.05) >= 0:
    current_05 += current_10 // 0.05
    current_count += current_05
    current_05 = current_10 % 0.05
    current_05 = round(current_05, 2)
if (current_05 / 0.02) >= 0:
    current_02 = current_05 // 0.02
    current_count += current_02
    current_02 = current_05 % 0.02
    current_02 = round(current_02, 2)
if (current_02 / 0.01) >= 0:
    current_01 = current_02 // 0.01
    current_count += current_01
    current_01 = current_02 % 0.01
    current_01 = round(current_01, 2)

    if current_2 == 0:
        print(f"{current_count:.0f}")
    elif current_1 == 0:
        print(f"{current_count:.0f}")
    elif current_50 == 0:
        print(f"{current_count:.0f}")
    elif current_20 == 0:
        print(f"{current_count:.0f}")
    elif current_10 == 0:
        print(f"{current_count:.0f}")
    elif current_05 == 0:
        print(f"{current_count:.0f}")
    elif current_02 == 0:
        print(f"{current_count:.0f}")
    elif current_01 == 0:
        print(f"{current_count:.0f}")