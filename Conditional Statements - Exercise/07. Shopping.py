budget = float(input())
broi_vga = int(input())
broi_cpu = int(input())
broi_ram = int(input())

price_vga = 250 * broi_vga
price_cpu = (0.35 * price_vga) * broi_cpu
price_ram = (0.10 * price_vga) * broi_ram

sum = price_vga + price_cpu + price_ram

if broi_vga > broi_cpu:
    sum = sum - (sum * 0.15)

if budget >= sum:
    over = budget - sum
    print(f"You have {over:.2f} leva left!")
elif sum >= budget:
    nedeed = sum - budget
    print(f"Not enough money! You need {nedeed:.2f} leva more!")