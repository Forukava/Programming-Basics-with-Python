age = int(input("What is your current age?\n"))
last_day = 90 * 365
current_age = age * 365
final = last_day - current_age
months = final / 30
weeks = final / 7
print(f"You have {final} days, {weeks:.0f} weeks, and {months:.0f} months left.")