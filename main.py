# ===================================
# [Ophthalmology Patient Database]
# ===================================
# Developed by. [Muhammad Dhany Latief]
# JCDS - [JCDS 0412]

from utils import menu #, create, read, update, delete
# /************************************/

# /===== Data Model =====/
# Create your data model here
patient_data = {"Name":['Edi','Fatkul','Darmawan','Ibnu','Arif'],
                 "Waiting Time":[534, 555, 294, 159, 508],
                 "Care Time":[645, 641, 579, 517, 510],
                 "Exam Time": [111, 86, 284, 358, 101], 
                 "Subspecialty": ['Rekonstruksi','Rekonstruksi','Retina','Neuro Ophthalmology', 'Glaukoma'],
                 "Insurance": ['BPJS','BPJS','Mandiri','BPJS','BPJS']} # Example data model


# /===== Feature Program =====/
# Create your feature program here
def read(patient_data: dict):
    """Function for read the data
    """
    return

def create():
    """Function for create the data
    """
    return

def update():
    """Function for update the data
    """
    return

def delete():
    """Function for delete the data
    """
    return

# /===== Main Program =====/
# Create your main program here
def main():
    """Function for main program
    """
    menu.crud_menu()
    input_user = input("Insert your option: ")
    if input_user == "1":
        read()
    elif input_user == "2":
        create()
    elif input_user == "3":
        update()
    elif input_user == "4":
        delete()
    elif input_user == "5":
        print("Exiting database...")
    else:
        print("Input invalid !")


if __name__ == "__main__":
    main()