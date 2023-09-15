price_ekskurziq = float(input())
broi_puzeli = int(input())
broi_govoreshti_kukli = int(input())
broi_plusheni_mecheta = int(input())
broi_minioni = int(input())
broi_kamioncheta = int(input())

sumo = broi_puzeli * 2.60 + broi_govoreshti_kukli * 3 \
      + broi_plusheni_mecheta * 4.10 + broi_minioni * 8.20 + broi_kamioncheta * 2
broi_igrachki = broi_kamioncheta + broi_minioni + broi_puzeli + broi_plusheni_mecheta + broi_govoreshti_kukli

if broi_igrachki > 50:
    broi_igrachki_discount = sumo * 0.75
    pechalba = broi_igrachki_discount * 0.90
    if pechalba >= price_ekskurziq:
        ostanali_pari = pechalba - price_ekskurziq
        print(f"Yes! {ostanali_pari :.2f} lv left.")
    elif price_ekskurziq >= pechalba:
        nedostigashti_pari = price_ekskurziq - pechalba
        print(f"Not enough money! {nedostigashti_pari :.2f} lv needed.")
if broi_igrachki < 50:
    pechalba_no_otstupka = sumo * 0.90
    if pechalba_no_otstupka >= price_ekskurziq:
        ostanali_pari_1 = pechalba_no_otstupka - price_ekskurziq
        print(f"Yes! {ostanali_pari_1 :.2f} lv left.")
    elif price_ekskurziq >= pechalba_no_otstupka:
        nedostigashti_pari_1 = price_ekskurziq - pechalba_no_otstupka
        print(f"Not enough money! {nedostigashti_pari_1 :.2f} lv needed.")
