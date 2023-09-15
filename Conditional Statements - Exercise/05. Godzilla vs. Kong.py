budget_for_film = float(input())
broi_na_statisti = int(input())
price_for_clothes_for_one_statist = float(input())

dekor = budget_for_film * 0.10

if broi_na_statisti > 150:
    discount_for_statisti = price_for_clothes_for_one_statist * 0.90
    all_needed_for_film = dekor + (discount_for_statisti * broi_na_statisti)
else:
    all_needed_for_film = dekor + (price_for_clothes_for_one_statist * broi_na_statisti)

if all_needed_for_film > budget_for_film:
    nedostigashti_pari_za_filma = all_needed_for_film - budget_for_film
    print("Not enough money!")
    print(f"Wingard needs {nedostigashti_pari_za_filma:.2f} leva more.")
elif all_needed_for_film <= budget_for_film:
    leftover_money = budget_for_film - all_needed_for_film
    print("Action!")
    print(f"Wingard starts filming with {leftover_money:.2f} leva left.")
