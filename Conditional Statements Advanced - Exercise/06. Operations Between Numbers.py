n1 = int(input())
n2 = int(input())
operator = input()
result = 0
need = 0
eo = ""
if operator == "+":
    result = n1 + n2
    if result % 2 != 0:
        eo = "odd"
    else:
        eo = "even"
if operator == "-":
    result = n1 - n2
    if result % 2 != 0:
        eo = "odd"
    else:
        eo = "even"
if operator == "*":
    result = n1 * n2
    if result % 2 != 0:
        eo = "odd"
    else:
        eo = "even"
if operator == "/":
    if n2 == 0:
        print(f"Cannot divide {n1} by zero")
    else:
        result = n1 / n2
if operator == "%":
    if n2 == 0:
        print(f"Cannot divide {n1} by zero")
    else:
        need = n1 % n2

if operator == "+" or operator == "-" or operator == "*":
    print(f"{n1} {operator} {n2} = {result} - {eo}")
if operator == "/" and n2 != 0:
    print(f"{n1} {operator} {n2} = {result:.2f}")
if operator == "%" and n2 != 0:
    print(f"{n1} {operator} {n2} = {need}")