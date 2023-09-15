import math

name_of_serial = input()
produlshitelnost_na_epizod = int(input())
produlshitelnost_na_pochivkata = int(input())

vreme_za_obqd = produlshitelnost_na_pochivkata * 0.125
vreme_za_dishane_na_prudnq = produlshitelnost_na_pochivkata * 0.25
ostanalo_vreme = produlshitelnost_na_pochivkata - vreme_za_dishane_na_prudnq - vreme_za_obqd

if ostanalo_vreme >= produlshitelnost_na_epizod:
    over_time = ostanalo_vreme - produlshitelnost_na_epizod
    print(f"You have enough time to watch {name_of_serial} and left with {math.ceil(over_time)} minutes free time.")
elif produlshitelnost_na_epizod >= ostanalo_vreme:
    needed_time =produlshitelnost_na_epizod - ostanalo_vreme
    print(f"You don't have enough time to watch {name_of_serial}, you need {math.ceil(needed_time)} more minutes.")