numPacksPen = int(input())
numPacksSharpee = int(input())
LPCLEAN = int(input())
discount = int(input())
pricePackPen = numPacksPen * 5.80
price_pack_sharpee = numPacksSharpee * 7.20
price_clean = LPCLEAN * 1.20
all_price = pricePackPen + price_pack_sharpee + price_clean
dis = discount / 100
total_price_w_discount = all_price - (all_price * dis)
print(total_price_w_discount)