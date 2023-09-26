bad_score = int(input())
name_it = input()
grades = int(input())

count_objects = 0
count_grades = 0

bad_grades = 0
last_object = ""

has_failed = True


while bad_grades < bad_score:
    name_it = input()
    if name_it == "Enough":
        has_failed = False
        break

    grades = int(input())
    if grades < 4:
        bad_grades += 1
        count_grades += grades
        count_objects += 1
        last_object = name_it

    if has_failed:
        print(f"You need a break, {bad_score} poor grades.")
        break
    else:
        average = count_grades / count_objects
        print(f"Average score: {average}")
        print(f"Number of problem: {count_objects}")
        print(f"Last problem: {last_object}")