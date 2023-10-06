command = input()

while not command == "Finish":
    current_movie = command
    total_seats = int(input())
    available_seats = total_seats

    while available_seats >= 0:
        current_ticket_type = input()

        if current_ticket_type == "End":
            break

        if current_ticket_type == "student":
            pass
        if current_ticket_type == "standart":
            pass
        if current_ticket_type == "kid":
            pass
    percent_full = (total)
    print(f"{current_movie} - {}")