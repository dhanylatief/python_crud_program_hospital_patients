def edit_patient(patient_data: dict):
    """Function for updating data
    """
    try:
        for i in range(len(patient_data["Name"])):
            print(f"ID: {patient_data['Patient ID'][i]} | Name: {patient_data['Name'][i]} | Waiting Time: {patient_data['Waiting Time'][i]} | Care Time: {patient_data['Care Time'][i]} | Exam Time: {patient_data['Exam Time'][i]} | Subspecialty: {patient_data['Subspecialty'][i]} | Insurance: {patient_data['Insurance'][i]}")
        id_edited = input("\nEnter patient ID of the patient you want to edit (or type C to cancel editing): ")
        if id_edited.upper() == "C":
            print("\nOperation aborted. Returning to main menu")
        elif id_edited in patient_data["Patient ID"]:
            edit_index = patient_data["Patient ID"].index(id_edited)
            edit_name = input("Enter new patient name (leave blank to keep current): ")
            edit_waiting_time = input("Enter new waiting time (leave blank to keep current): ")
            edit_exam_time = input("Enter new exam time (leave blank to keep current): ")
            edit_care_time = input("Enter new care time (leave blank to keep current): ")
            edit_subspecialty = input("Enter new subspecialty (leave blank to keep current): ")
            edit_insurance = input("Enter new insurance (leave blank to keep current): ")

            patient_data_temp = {f"Name":[{patient_data["Name"][edit_index]}],
                    "Waiting Time":[{patient_data["Waiting Time"][edit_index]}],
                    "Exam Time": [{patient_data["Exam Time"][edit_index]}],
                    "Care Time":[{patient_data["Care Time"][edit_index]}], 
                    "Subspecialty": [{patient_data["Subspecialty"][edit_index]}],
                    "Insurance": [{patient_data["Insurance"][edit_index]}]}
            
            if edit_name:
                patient_data_temp["Name"] = edit_name
            if edit_waiting_time:
                patient_data_temp["Waiting Time"] = int(edit_waiting_time)
            if edit_exam_time:
                patient_data_temp["Exam Time"]= int(edit_exam_time)
            if edit_care_time:
                patient_data_temp["Care Time"] = int(edit_care_time)
            if edit_subspecialty:
                patient_data_temp["Subspecialty"] = edit_subspecialty
            if edit_insurance:
                patient_data_temp["Insurance"] = edit_insurance
                
            print("Edited patient data", end="\n")
            print(f"ID: {patient_data['Patient ID'][edit_index]} | Name: {patient_data_temp['Name']} | Waiting Time: {patient_data_temp['Waiting Time']} | Care Time: {patient_data_temp['Care Time']} | Exam Time: {patient_data_temp['Exam Time']} | Subspecialty: {patient_data_temp['Subspecialty']} | Insurance: {patient_data_temp['Insurance']}")
            confirm_edit_patient = input("Is the data correct (Y/N)? ")
            if confirm_edit_patient.upper() == "Y":
                if edit_name:    
                    patient_data["Name"][edit_index] = patient_data_temp["Name"]
                if edit_waiting_time:
                    patient_data["Waiting Time"][edit_index] = patient_data_temp["Waiting Time"]
                if edit_exam_time:
                    patient_data["Exam Time"][edit_index] = patient_data_temp["Exam Time"]
                if edit_care_time:
                    patient_data["Care Time"][edit_index] = patient_data_temp["Care Time"]
                if edit_subspecialty:
                    patient_data["Subspecialty"][edit_index] = patient_data_temp["Subspecialty"]
                if edit_insurance:
                    patient_data["Insurance"][edit_index] = patient_data_temp["Insurance"]
                print("Patient data updated.")
            elif confirm_edit_patient.upper() == "N":
                print("Patient data not updated.")
        else:
            print("Invalid patient ID.")
    except:
        print("Error occured")
    return