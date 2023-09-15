broi_pileshki_menu = int(input())
broi_menu_w_fish = int(input())
broi_vege_menu = int(input())
price_pileshki_menuta = broi_pileshki_menu * 10.35
price_menu_fish = broi_menu_w_fish * 12.40
price_vege_menu = broi_vege_menu * 8.15
total_price_menu = price_pileshki_menuta + price_menu_fish + price_vege_menu
desert_price = 0.20 * total_price_menu
delivery_price = 2.50
total_price = total_price_menu + desert_price + delivery_price
print(total_price)