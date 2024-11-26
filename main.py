# ===================================
# [Ophthalmology Patient Database]
# ===================================
# Developed by. [Muhammad Dhany Latief]
# JCDS - [JCDS 0412]

from utils import menu, create, read, update, delete
import db

# /===== Main Program =====/
# Create your main program here
def main():
    """Function for main program
    """
    menu.crud_menu()
    input_user = input("Insert option number (1-5): ")
    if input_user == "1":
        read.show_patientdb(db.patient_data)
    elif input_user == "2":
        create.new_patient_data(db.patient_data)
    elif input_user == "3":
        update.edit_patient(db.patient_data)
    elif input_user == "4":
        delete.delete_patient(db.patient_data)
    elif input_user == "5":
        print("Leaving the database...")
        exit()
    else:
        print("Invalid Input.")

username = "Dhany"
password = "12345"

if __name__ == "__main__":
    usern = input("\nInsert Username: ")
    passw = input("Insert password: ")
    if usern == username and passw == password:
        while True:
            main()
    else:
        print("Username and/or password incorrect")