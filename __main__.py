
from phone import ContactDetails

def menu():
    print("Choose any action from Given List")
    print("_"*20)
    print("1. Add Contact Details")
    print("2. List contact")
    print("3. Delete Contact Details")
    print("4. Update Conatct Details")
    print("5. Exit")
    print("_"*20)

if __name__ == "__main__":
    # print("Do you want to continue y/n:")
    # user_choice = input("Enter your choice")
    # while user_choice == "y" or user_choice =="Y":
    menu()
    choice = int (input("Please Enter your Choice!!:"))
    if choice == 1:
        c1 = ContactDetails("","","")
        c1.add_Contact()

    if choice == 2:
        c = ContactDetails(" "," "," ")
        c.read_Contacts()

    if choice == 3:
        c = ContactDetails ("","","")
        c.delete_contact()

    if choice == 4:
        c= ContactDetails("","","")
        c.update_contact()
    
    if choice == 5:
        exit(1)
