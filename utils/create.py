def new_patient_data(patient_data: dict):
    """Function for create the data
    """
    try:
        new_confirm = input("\nDo you want to add a new patient data (Type Y to proceed, type any other key to cancel)? ")
        if new_confirm.upper() == "Y":
            patient_id = input("Enter patient ID (8 digits): ")
            name = input("Enter new patient name: ")
            waiting_time = int(input("Enter waiting time: "))
            exam_time = int(input("Enter exam time: "))
            subspecialty = input("Enter subspecialty: ")
            insurance = input("Enter insurance type: ")
            
            patient_data["Patient ID"].append(patient_id)
            patient_data["Name"].append(name)
            patient_data["Waiting Time"].append(waiting_time)
            patient_data["Exam Time"].append(exam_time)
            patient_data["Care Time"].append(waiting_time+exam_time)
            patient_data["Subspecialty"].append(subspecialty)
            patient_data["Insurance"].append(insurance)
            for i in range(len(patient_data["Name"])):
                print(f"ID: {patient_data['Patient ID'][i]} | Name: {patient_data['Name'][i]} | Waiting Time: {patient_data['Waiting Time'][i]} | Care Time: {patient_data['Care Time'][i]} | Exam Time: {patient_data['Exam Time'][i]} | Subspecialty: {patient_data['Subspecialty'][i]} | Insurance: {patient_data['Insurance'][i]}")
            confirm_new_patient = input("Is the data correct (Y/N)? ")
            if confirm_new_patient.upper() == "Y":
                print("New patient added.")
            elif confirm_new_patient.upper() == "N":
                patient_data["Patient ID"].remove(patient_id)
                patient_data["Name"].remove(name)
                patient_data["Waiting Time"].remove(waiting_time)
                patient_data["Exam Time"].remove(exam_time)
                patient_data["Care Time"].remove(waiting_time+exam_time)
                patient_data["Subspecialty"].remove(subspecialty)
                patient_data["Insurance"].remove(insurance)
                print("New patient not added.")
            else:
                print("Invalid entry")
                new_patient_data(patient_data)
        else:
            print("Operation aborted. Returning to main menu.")
    except:
        print("Error occured")
    return 
