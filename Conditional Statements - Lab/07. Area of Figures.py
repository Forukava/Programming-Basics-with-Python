from math import pi
figura = input()

if figura == "square":
    nega = float(input())
    total_nega = nega * nega
    print(f"{total_nega:.3f}")
elif figura == "rectangle":
    negro = float(input())
    negro_1 = float(input())
    total_negro = negro * negro_1
    print(f"{total_negro:.3f}")
elif figura == "circle":
    negri = float(input())
    total_negri = pi * (negri ** 2)
    print(f"{total_negri:.3f}")
elif figura == "triangle":
    negroni = float(input())
    negroni_1 = float(input())
    total_negroni = (negroni * negroni_1) / 2
    print(f"{total_negroni:.3f}")