## Phonebook App using PostgresSQL database
import pg

db = pg.DB(dbname='phonebook_db')
# db.debug = True

def menu():
    print '''
    Electronic Phone Book
    =====================
    1\. Look up an entry
    2\. Set an entry
    3\. Delete an entry
    4\. List all entries
    5\. Save entries
    6\. Quit
    What do you want to do (1-5)?
    '''
    answer = int(raw_input("> "))
    return answer

def lookup_entry():


def set_entry():


def delete_entry():


def list_all_entries():


def save_entries():


def quit():
    # Not necessary to do this in a function, but did it to practice

is_using = True

while is_using == True:

    choice = menu()

    if choice == 1:
        lookup_entry()
    elif choice == 2:
        set_entry()
    elif choice == 3:
        delete_entry()
    elif choice == 4:
        list_all_entries()
    elif choice == 5:
        save_entries()
    elif choice == 6:
        is_using = quit() # Not necessary to do this in a function, but did it to practice
    else:
        print "Please choose a number from 1 to 5!"
