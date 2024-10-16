def show_patientdb(patient_data: dict):
    """Function for read the data
    """
    print("\nPatient Records:")
    for i in range(len(patient_data["Name"])):
        print(f"ID: {patient_data['Patient ID'][i]} | Name: {patient_data['Name'][i]} | Waiting Time: {patient_data['Waiting Time'][i]} | Care Time: {patient_data['Care Time'][i]} | Exam Time: {patient_data['Exam Time'][i]} | Subspecialty: {patient_data['Subspecialty'][i]} | Insurance: {patient_data['Insurance'][i]}")
    search_input = input("\nWould you like to search for an entry? (Y/N) ")
    if search_input.upper() == "Y":
        id_search = input("Put in patient id you want to search: ")
        if id_search in patient_data['Patient ID']:
            index = patient_data["Patient ID"].index(id_search)
            print(f"ID: {patient_data['Patient ID'][index]} | Name: {patient_data['Name'][index]} | Waiting Time: {patient_data['Waiting Time'][index]} | Care Time: {patient_data['Care Time'][index]} | Exam Time: {patient_data['Exam Time'][index]} | Subspecialty: {patient_data['Subspecialty'][index]} | Insurance: {patient_data['Insurance'][index]}")
        else:
            print("Patient data not found.")
        # print("Feature unavailable. Please wait for the next update.")
    elif search_input.upper() == "N":
        print("Returning to main menu")
    else:
        print("Invalid Input.")
        show_patientdb(patient_data)
    return