## Phonebook App using PostgresSQL database
import pg

db = pg.DB(dbname='phonebook_db')
# db.debug = True

def menu():
    print '''
    Electronic Phone Book
    =====================
    1\. Look up a contact
    2\. Create a contact
    3\. Delete a contact
    4\. List all contacts
    5\. Quit

    What do you want to do (1-5)?
    '''
    answer = int(raw_input("> "))
    return answer

def lookup_entry():
    name = raw_input("Enter name to search: ")
    name = name.capitalize()
    result_list = db.query(" select * from phonebook where name = '%s';"  % name).namedresult()
    if len(result_list) > 0:
        for result in result_list:
            print "\n%s's phone number is: %s\n" % (name, result.phone_number)
    else:
        print "\n%s was not found in the phonebook\n" % name

def set_entry():
        name = raw_input("Provide person's name: ").capitalize()
        phone_number = raw_input("Provide person's phone number: ")
        email = raw_input("Provide person's email: ")
        result_list = db.query("select count(id) from phonebook where name = '%s' or email = '%s'" % (name, email)).namedresult()
        if len(result_list) > 0:
            print "\nThis name and/or email information is already in the phonebook."
            print "Please check the phonebook information before adding this entry."
            list_all_entries()
        else:
            set_person = db.insert('phonebook', name = name, phone_number = phone_number, email = email);
            print "Entry saved for %s." % name

def delete_entry():
    name = raw_input("Provide the name of the person to delete from the phonebook: ").capitalize()
    result_list = db.query("select id from phonebook where name ilike '%s';" % name).namedresult()
    if len(result_list) > 0:
        id = result_list[0].id
        db.delete('phonebook', {'id': '%s' % id})
    else:
        print "\n%s was not found in the phonebook" % name

def list_all_entries():
    result_list = db.query('select * from phonebook').namedresult()
    print "\nThe phonebook contains the following information:"
    for result in result_list:
        print "\t %s's phone number is %s" % (result.name, result.phone_number)

def quit():
    # Not necessary to do this in a function, but did it to practice
    print "\nThanks for using the phonebook app\nBye, bye!\n"
    return False

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
