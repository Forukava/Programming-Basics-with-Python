total = 0
p_count = 0

people = int(input())
text = input()
while not text == "Finish":
    current_present = text
    sum_grades = 0
    for _ in range(people):
        current_score = float(input())
        sum_grades += current_score

    total += sum_grades
    p_count += 1

    average_score = sum_grades / people
    print(f"{current_present} - {average_score:.2f}.")

    text = input()
average_t_score = total / (p_count * people)
print(f"Student's final assessment is {average_t_score:.2f}.")
