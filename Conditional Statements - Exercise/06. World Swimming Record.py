from math import floor
record_v_secundi = float(input())
raztoqnie_v_metri = float(input())
vreme_za_1_metur = float(input())

ivan_trqbva_da_prepluva = raztoqnie_v_metri * vreme_za_1_metur
dobavq_na_vseki_15_metra = raztoqnie_v_metri // 15.00

dobavq_12_secundi = dobavq_na_vseki_15_metra * 12.50

obshto_vreme_1 = ivan_trqbva_da_prepluva + dobavq_12_secundi
obshto_vreme = round(obshto_vreme_1, 2)

if record_v_secundi <= obshto_vreme:
    nedostigashti_secundi = obshto_vreme - record_v_secundi
    print(f"No, he failed! He was {nedostigashti_secundi:.2f} seconds slower.")
else:
    print(f"Yes, he succeeded! The new world record is {obshto_vreme:.2f} seconds.")