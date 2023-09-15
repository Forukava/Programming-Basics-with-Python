chas_ot_denonoshtieto = int(input())
den_ot_sedmicata = input()

if den_ot_sedmicata == "Sunday":
    print("closed")

if den_ot_sedmicata == "Monday" or den_ot_sedmicata == "Tuesday" or den_ot_sedmicata == "Wednesday" or den_ot_sedmicata == "Thursday" or den_ot_sedmicata == "Friday" or den_ot_sedmicata == "Saturday":
        if 10 <= chas_ot_denonoshtieto <= 17:
            print("open")
        else:
            print("closed")