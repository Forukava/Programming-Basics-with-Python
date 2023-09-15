budget = float(input())
seasons = input()
total = 0
county = ""
accommodation = ""
if budget <= 100 and seasons == "summer":
    total = budget * 0.30
    county = "Bulgaria"
    accommodation = "Camp"
elif budget <= 100 and seasons == "winter":
    total = budget * 0.70
    county = "Bulgaria"
    accommodation = "Hotel"
if 100 < budget <= 1000 and seasons == "summer":
    total = budget * 0.40
    county = "Balkans"
    accommodation = "Camp"
elif 100 < budget <= 1000 and seasons == "winter":
    total = budget * 0.80
    county = "Balkans"
    accommodation = "Hotel"
if budget > 1000 and seasons == "summer":
    total = budget * 0.90
    county = "Europe"
    accommodation = "Hotel"
elif budget > 1000 and seasons == "winter":
    total = budget * 0.90
    county = "Europe"
    accommodation = "Hotel"

print(f"Somewhere in {county}")
print(f"{accommodation} - {total:.2f}")