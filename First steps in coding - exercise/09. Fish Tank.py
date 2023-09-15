lenght_in_cm = int(input())
width_in_cm = int(input())
height_in_cm = int(input())
procent = float(input())
obem_na_akvarium = lenght_in_cm * width_in_cm * height_in_cm
obem_v_litri = obem_na_akvarium * 0.001
zaeto_mqsto = procent / 100
nushni_litri = obem_v_litri * (1 - zaeto_mqsto)
print(nushni_litri)