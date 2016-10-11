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
    5\. Quit

    What do you want to do (1-5)?
    '''
    answer = int(raw_input("> "))
    return answer

# def lookup_entry():

def set_entry():
        name = raw_input("Provide person's name: ").capitalize()
        phone_number = raw_input("Provide person's phone number: ")
        email = raw_input("Provide person's email: ")
        set_person = db.insert('phonebook', name = name, phone_number = phone_number, email = email);
        print "Entry saved for %s." % name

# def delete_entry():

def list_all_entries():
    result_list = db.query('select * from phonebook').namedresult()
    print "\nYour phonebook contains the following information:"
    for result in result_list:
        print "\t %s's phone number is %s" % (result.name, result.phone_number)

# def quit():
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
        is_using = quit() # Not necessary to do this in a function, but did it to practice
    else:
        print "Please choose a number from 1 to 5!"
