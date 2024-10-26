import _mysql_connector
from utils import connecting_to_db

def show_patientdb(patient_data: dict):
    """Function for read the data
    """
    print("\nPatient Record:")
    read_query = "SELECT p.patientid, p.patient_name, qd.waitingtime, qd.examtime, qd.caretime, qd.subspecialty, qd.insurance FROM patient p JOIN queue q ON p.patientid = q.patientid JOIN queuedetail qd ON q.registrationid = qd.registrationid;"
    data, column_names = connecting_to_db.exec_query(connecting_to_db.conn, read_query)
    print(column_names)
    for i in range(len(data)):
        print(f'{data[i]}')
    search_input = input("\nWould you like to search for a patient [Y/N]? ")
    if search_input.upper() == "Y":
        try:
            patient_search = input("\nPut in patient id or name you want to search: ")
            search_query = f"""SELECT p.patientid, p.patient_name, qd.waitingtime, qd.examtime, qd.caretime, qd.subspecialty, qd.insurance 
            FROM patient p JOIN queue q ON p.patientid = q.patientid JOIN queuedetail qd ON q.registrationid = qd.registrationid 
            WHERE p.patientid = '{patient_search}' OR p.patient_name LIKE '%{patient_search}%';"""
            search_data, column_names = connecting_to_db.exec_query(connecting_to_db.conn, search_query)
            print(column_names)
            for i in range(len(search_data)):
                print(f'{search_data[i]}')
        except Exception:
            print("Input not recognized")
    elif search_input.upper() == "N":
        print("\nReturning to main menu")
    else:
        print("Invalid Input.")
        show_patientdb(data)
    return