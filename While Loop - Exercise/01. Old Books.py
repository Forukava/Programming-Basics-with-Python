book = input()
current_book = input()
count = 0
the_found_book = False

while True:

    if current_book == book:
        the_found_book = True
        break

        count += 1
        current_book = input()
    if current_book == "No More Books":
        print("The book you search is not here.")
        print(f"You checked {count} books.")

    if current_book != book:
        continue

if the_found_book is True:
    print(f"You checked {count} books and found it.")

if the_found_book is False:
    print("The book you search is not here.")
    print(f"You checked {count} books.")

#---------------------------------------------------------------#

#book = input()
#counter = 0
#current_book = input()
#while current_book != 'No More Books':
    #if current_book == book:
        #print(f'You checked {counter} books and found it.')
        #quit()
    #counter += 1
    #current_book = input()
#print('The book you search is not here!')
#print(f'You checked {counter} books.')