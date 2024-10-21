import _mysql_connector
from utils import connecting_to_db
def remove_patient(patient_data: dict):
    """Function for delete the data
    """
    read_query = f"""SELECT p.patientid, p.patient_name, qd.waitingtime, qd.examtime, qd.caretime, qd.subspecialty, qd.insurance 
    FROM patient p JOIN queue q ON p.patientid = q.patientid JOIN queuedetail qd ON q.registrationid = qd.registrationid;"""
    data, column_names = connecting_to_db.exec_query(connecting_to_db.conn, read_query)
    print(f"\n{column_names}")
    for i in range(len(data)):
        print(f'{data[i]}')
    id_del = input("Enter patient ID of the patient you want to delete (type C to cancel): ")
    if id_del.upper() == "C":
        print("Returning to main menu.")
    else:
        try:
            del_query1 = f"""DELETE FROM patient WHERE patientid = '{id_del}'"""
            connecting_to_db.exec_query(connecting_to_db.conn, del_query1)
            read_query = f"""SELECT p.patientid, p.patient_name, qd.waitingtime, qd.examtime, qd.caretime, qd.subspecialty, qd.insurance 
                            FROM patient p JOIN queue q ON p.patientid = q.patientid JOIN queuedetail qd ON q.registrationid = qd.registrationid;"""
            data, column_names = connecting_to_db.exec_query(connecting_to_db.conn, read_query)
            print(f"\n{column_names}")
            for i in range(len(data)):
                print(f'{data[i]}')
            confirm_del_patient = input("Are you sure (Y/N)? ")
            if confirm_del_patient.upper() == "Y":
                connecting_to_db.conn.commit()
                print("Patient data deleted.")
            elif confirm_del_patient.upper() == "N":
                print("Patient data not deleted.")
            else:
                print("Invalid entry")
        except Exception:
                print("Input not recognized")
    return