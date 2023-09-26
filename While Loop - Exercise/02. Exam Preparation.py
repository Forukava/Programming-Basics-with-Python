poorGradeLimit = int(input())
poorGradeCount = 0
problemCount = 0
gradesSum = 0
lastProblemName = ""
problemName = ""
grade = 0

while True:
    problemName = input()
    if problemName != "Enough":
        grade = int(input())
        gradesSum += grade
        problemCount += 1

        if grade <= 4:
            poorGradeCount += 1

        if poorGradeCount >= poorGradeLimit:
            print(f"You need a break, {poorGradeCount} poor grades.")
            break

        lastProblemName = problemName
    else:
        if problemCount == 0:
            print("No problems solved yet.")
        else:
            print(f"Average score: {gradesSum / problemCount:.2f}")
            print(f"Number of problems: {problemCount}")
            print(f"Last problem: {lastProblemName}")
        break