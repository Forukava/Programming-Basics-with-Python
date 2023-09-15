degrees = int(input())
status = input()

outfits = ""
shoes = ""

if degrees >= 10 and degrees <= 18 and status == "Morning":
    outfits = "Sweatshirt"
    shoes = "Sneakers"
    print(f"It's {degrees} degrees, get your {outfits} and {shoes}.")
elif degrees >= 10 and degrees <= 18 and status == "Afternoon" or status == "Evening":
    outfits = "Shirt"
    shoes = "Moccasins"
    print(f"It's {degrees} degrees, get your {outfits} and {shoes}.")
elif degrees > 18 and degrees <= 24 and status == "Morning" or status == "Evening":
    outfits = "Shirt"
    shoes = "Moccasins"
    print(f"It's {degrees} degrees, get your {outfits} and {shoes}.")
elif degrees > 18 and degrees <= 24 and status == "Afternoon":
    outfits = "T-Shirt"
    shoes = "Sandals"
    print(f"It's {degrees} degrees, get your {outfits} and {shoes}.")
elif degrees >= 25 and status == "Morning":
    outfits = "T-Shirt"
    shoes = "Sandals"
    print(f"It's {degrees} degrees, get your {outfits} and {shoes}.")
elif degrees >= 25 and status == "Afternoon":
    outfits = "Swim Suit"
    shoes = "Barefoot"
    print(f"It's {degrees} degrees, get your {outfits} and {shoes}.")
elif degrees >= 25 and status == "Evening":
    outfits = "Shirts"
    shoes = "Moccasins"
    print(f"It's {degrees} degrees, get your {outfits} and {shoes}.")