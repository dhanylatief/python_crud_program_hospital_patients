def delete_patient(patient_data: dict):
    """Function for delete the data
    """
    for i in range(len(patient_data["Name"])):
        print(f"ID: {patient_data['Patient ID'][i]} | Name: {patient_data['Name'][i]} | Waiting Time: {patient_data['Waiting Time'][i]} | Care Time: {patient_data['Care Time'][i]} | Exam Time: {patient_data['Exam Time'][i]} | Subspecialty: {patient_data['Subspecialty'][i]} | Insurance: {patient_data['Insurance'][i]}")
    id_del = input("Enter patient ID of the patient you want to delete: ")
    
    if id_del in patient_data["Patient ID"]:
        del_index = patient_data["Patient ID"].index(id_del)
        print("Edited patient data", end="\n")
        print(f"ID: {patient_data['Patient ID'][del_index]} | Name: {patient_data['Name'][del_index]} | Waiting Time: {patient_data['Waiting Time'][del_index]} | Care Time: {patient_data['Care Time'][del_index]} | Exam Time: {patient_data['Exam Time'][del_index]} | Subspecialty: {patient_data['Subspecialty'][del_index]} | Insurance: {patient_data['Insurance'][del_index]}")
        confirm_delete_patient = input("Do you want to delete this patient data (Y/N)? ")
        if confirm_delete_patient.upper() == "Y":
            del patient_data["Patient ID"][del_index]
            del patient_data["Name"][del_index]
            del patient_data["Waiting Time"][del_index]
            del patient_data["Care Time"][del_index]
            del patient_data["Exam Time"][del_index]
            del patient_data["Subspecialty"][del_index]
            del patient_data["Insurance"][del_index]
            print("\nPatient data deleted")
        elif confirm_delete_patient.upper() == "N":
            print("\nPatient data not deleted.")
    else:
        print("Invalid patient ID.")
    return