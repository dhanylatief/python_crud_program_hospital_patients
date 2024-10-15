# ===================================
# [Ophthalmology Patient Database]
# ===================================
# Developed by. [Muhammad Dhany Latief]
# JCDS - [JCDS 0412]

from utils import menu, create, read, update, delete
import db
# /************************************/
# /===== Feature Program =====/
# Create your feature program here
# def read(patient_data: dict):
#     """Function for read the data
#     """
#     return

# def create(patient_data: dict):
#     """Function for create the data
#     """
#     return

# def update(patient_data: dict):
#     """Function for update the data
#     """
#     return

# def delete(patient_data: dict):
#     """Function for delete the data
#     """
#     return

# /===== Main Program =====/
# Create your main program here
def main():
    """Function for main program
    """
    while True:
        menu.crud_menu()
        input_user = input("Insert option number (1-5): ")
        if input_user == "1":
            read.read(db.patient_data)
        elif input_user == "2":
            create.create(db.patient_data)
        elif input_user == "3":
            update.update(db.patient_data)
        elif input_user == "4":
            delete.delete(db.patient_data)
        elif input_user == "5":
            print("Leaving the database...")
            break
        else:
            print("Invalid Input.")


if __name__ == "__main__":
        main()