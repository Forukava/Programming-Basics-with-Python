number_groups = int(input())
musala = 0
monblan = 0
kilimandjaro = 0
k2 = 0
everest = 0

for _ in range(number_groups):
    number_tourists = int(input())
    if number_tourists < 6:
        musala += number_tourists
    elif number_tourists < 13:
        monblan += number_tourists
    elif number_tourists < 26:
        kilimandjaro += number_tourists
    elif number_tourists <= 40:
        k2 += number_tourists
    elif number_tourists >= 41:
        everest += number_tourists

all_people = musala + monblan + kilimandjaro + k2 + everest
p_musala = musala / all_people * 100
p_monblan = monblan / all_people * 100
p_kilimandjaro = kilimandjaro / all_people * 100
p_k2 = k2 / all_people * 100
p_everest = everest / all_people * 100

print(f"{p_musala:.2f}%")
print(f"{p_monblan:.2f}%")
print(f"{p_kilimandjaro:.2f}%")
print(f"{p_k2:.2f}%")
print(f"{p_everest:.2f}%")


