def new_patient_data(patient_data: dict):
    """Function for create the data
    """
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
    
    return print("New patient added.")
