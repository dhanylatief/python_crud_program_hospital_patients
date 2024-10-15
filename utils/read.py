def read(patient_data: dict):
    """Function for read the data
    """
    print("\nPatient Records:")
    for i in range(len(patient_data["Name"])):
        print(f"ID: {patient_data['Patient ID'][i]} | Name: {patient_data['Name'][i]} | Waiting Time: {patient_data['Waiting Time'][i]} | Care Time: {patient_data['Care Time'][i]} | Exam Time: {patient_data['Exam Time'][i]} | Subspecialty: {patient_data['Subspecialty'][i]} | Insurance: {patient_data['Insurance'][i]}")
    search_input = input("\nWould you like to search for an entry? (Y/N) ")
    if search_input.upper() == "Y":
    # add search feature here if there's time
        print("Feature incomplete. Returning to main menu")
    elif search_input.upper() == "N":
        print("Returning to main menu")
    else:
        print("Invalid Input. Returning to main menu")
    return