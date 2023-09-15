need_kol_nailon = int(input())
need_kol_boq = int(input())
kol_razreditel = int(input())
hours = int(input())
price_nailon = (need_kol_nailon + 2) * 1.50
price_boq = (need_kol_boq + 1.1) * 14.50
price_razreditel = kol_razreditel * 5.00
price_torb = 0.40
total_price_materials = price_nailon + price_boq + price_razreditel + price_torb
price_maistori = (total_price_materials * 0.30) * hours
total_price = total_price_materials + price_maistori
print(total_price)
