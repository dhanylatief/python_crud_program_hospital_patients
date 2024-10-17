def edit_patient(patient_data: dict):
    """Function for updating data
    """
    for i in range(len(patient_data["Name"])):
        print(f"ID: {patient_data['Patient ID'][i]} | Name: {patient_data['Name'][i]} | Waiting Time: {patient_data['Waiting Time'][i]} | Care Time: {patient_data['Care Time'][i]} | Exam Time: {patient_data['Exam Time'][i]} | Subspecialty: {patient_data['Subspecialty'][i]} | Insurance: {patient_data['Insurance'][i]}")
    id_edited = input("Enter patient ID of the patient you want to update: ")
    
    if id_edited in patient_data["Patient ID"]:
        edit_index = patient_data["Patient ID"].index(id_edited)
        edit_name = input("Enter new patient name (leave blank to keep current): ")
        edit_waiting_time = input("Enter new waiting time (leave blank to keep current): ")
        edit_exam_time = input("Enter new exam time (leave blank to keep current): ")
        edit_subspecialty = input("Enter new subspecialty (leave blank to keep current): ")
        edit_insurance = input("Enter new insurance (leave blank to keep current): ")

        if edit_name:
            patient_data["Name"][edit_index] = edit_name
        if edit_waiting_time:
            patient_data["Waiting Time"][edit_index] = int(edit_waiting_time)
        if edit_exam_time:
            patient_data["Exam Time"][edit_index] = int(edit_exam_time)
        if edit_waiting_time and edit_exam_time:
            patient_data["Care Time"][edit_index] = int(edit_waiting_time+edit_exam_time)
        if edit_subspecialty:
            patient_data["Subspecialty"][edit_index] = edit_subspecialty
        if edit_insurance:
            patient_data["Insurance"][edit_index] = edit_insurance
        print("Patient data updated", end="\n")
        for i in range(len(patient_data["Name"])):
            print(f"ID: {patient_data['Patient ID'][i]} | Name: {patient_data['Name'][i]} | Waiting Time: {patient_data['Waiting Time'][i]} | Care Time: {patient_data['Care Time'][i]} | Exam Time: {patient_data['Exam Time'][i]} | Subspecialty: {patient_data['Subspecialty'][i]} | Insurance: {patient_data['Insurance'][i]}")
        # confirm_edit_patient = input("Is the data correct (Y/N)? ")
        # if confirm_edit_patient.upper() == "Y":
        #     print("Patient data updated.")
        # elif confirm_edit_patient.upper() == "N":
            
        #     print("Patient data not updated.")
    else:
        print("Invalid patient ID.")
    return