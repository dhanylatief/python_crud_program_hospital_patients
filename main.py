# ===================================
# [Ophthalmology Patient Database]
# ===================================
# Developed by. [Muhammad Dhany Latief]
# JCDS - [JCDS 0412]
import mysql.connector
from utils import menu, create, read, update, delete
from utils import connecting_to_db
# /===== Main Program =====/
# Create your main program here
def main():
    """Function for main program
    """
    menu.crud_menu()
    input_user = input("Insert option number (1-5): ")
    if input_user == "1":
        read.show_patientdb(database)
    elif input_user == "2":
        create.new_patient_data(database)
    elif input_user == "3":
        update.edit_patient(database)
    elif input_user == "4":
        delete.remove_patient(database)
    elif input_user == "5":
        print("Leaving the database...")
        exit()
    else:
        print("Invalid Input.")


if __name__ == "__main__":
    database = "ophthalmology_patients"
    while True:   
        main()
    else:
        print("Invalid input.")
        exit()