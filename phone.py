import csv

csv_file = "phone.csv"
class ContactDetails:
    def __init__(self,name, phone_number, email):
        self.name = name
        self.phone_number = phone_number
        self.email = email

    def add_Contact(self):
        print("Enter the Details of the person")
        self.name = input("Enter the name of the person")
        self.phone_number = input("Enter the phone number of person")
        self.email = input("Enter the unique email of the person")

        with open("phone.csv","a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([self.name, self.phone_number, self.email])
    
    def read_Contacts(self):
        with open (csv_file,"r") as file:
            reader = csv.reader(file)
            for contact in reader:
                print (contact)

    def delete_contact (self):
        email = input (" Enter a email to delete")
        contacts_to_keep = []
        with open(csv_file,'r') as file:
            reader= csv.reader(file)
            for contact in reader:
                if contact[2].strip() == email.strip():
                    continue
                else:
                    contacts_to_keep.append (contact)
        print(contacts_to_keep)
                    # print ( "Deletion complete!")

        with open (csv_file,"w") as file:
            writer = csv.writer (file)
            writer.writerows(contacts_to_keep)

    def update_contact (self):
        email = input (" Enter a email to update")
        contacts_to_keep = []
        updated_contact = []
        with open(csv_file,'r') as file:
            reader= csv.reader(file)
            for contact in reader:
                if contact[2].strip() == email.strip():
                    name = input("Enter the name of the person")
                    phone_number = input("Enter the phone number of the person")
                    email = input(" Enter the updated email of the person")
                    updated_contact = [name, phone_number, email]
                else:
                    contacts_to_keep.append (contact)
       
        with open (csv_file,"w") as file:
            writer = csv.writer (file)
            writer.writerow (updated_contact)
            writer.writerows(contacts_to_keep)

    
