# Level 029

#  ----------------------------------
#  -- SIMULATOR OF MEDICAL RECORDS --
#  ----------------------------------

print("Here We go simulete some basic questions that  nurses make when a patient goes to the hospital")

full_name = input("The patient full name is: ")
doc = input("The kind of document will be SUS card or CPF?R: ")
document = int(input("Patient documents, please, answer using just numbers: "))
age = int(input("Age of the patient: "))
city = input("City where the patient live: ")
sex = input("Answer F for female and M for male: ")
street = input("The house of the patient stays at: ")
num_house = int(input("Number of the house: "))
neighborhood = input("Neighborhood: ")
phone = int(input("Phone number of the patient, Please answer just with numbers: "))
arrived = float(input("Time patient arrived: "))
day_arrived = input("Insert date that the patient arrived, in this format: 00/00/0000: ")
complaints = input("Insert here the complaints: ")
print("-------------------------------------------------------------------------------------------------------------------------------------------------------")
print("----------------------------------------------------------MEDICAL RECORDS------------------------------------------------------------------------------")
print("-------------------------------------------------------------------------------------------------------------------------------------------------------")
print(f"PATIENT'S FULL NAME: {full_name}") 
print("-------------------------------------------------------------------------------------------------------------------------------------------------------")
print(f"DOCUMENT (CPF OR SUS CARD): {doc}, Number: {document}")
print("-------------------------------------------------------------------------------------------------------------------------------------------------------")
print(f"PATIENT AGE: {age} ---------------------------------------------------------------------------------------------------- SEX: {sex} -------------------------") 
print("-------------------------------------------------------------------------------------------------------------------------------------------------------")
print(f"City: {city} --- Street: {street}, number {num_house}, at neighborhood {neighborhood}")
print(f"-------------------------------------------------------------------------------------------------------------------------------------------------------")
print(f"Phone number for contact: {phone}")
print("-------------------------------------------------------------------------------------------------------------------------------------------------------")
print(f"Time patient arrived: {arrived}")
print("-------------------------------------------------------------------------------------------------------------------------------------------------------")
print(f"Date: {day_arrived}")
print("-------------------------------------------------------------------------------------------------------------------------------------------------------")
print(f"Complaints: {complaints}")
print("-------------------------------------------------------------------------------------------------------------------------------------------------------")


""" ABSTRACTIONS MADE AFTER TALKING TO A NURSE
--> Patient's full name OK
--> Document (Brazilian documents such as SUS card or CPF) OK
--> Phone number OK
--> Date of birth OK
--> Male or female OK
--> Age OK
--> Where the patient lives (wich street, neighborhood, and city) OK
--> Time of arrival OK
--> Date OK
--> Check vital signs
--> What are the patient's complaints?
--> If the patient is allergic to any medication

----------------------------------------------------------------------------------------------
ONCE THIS IS DONE, THE PATIENT IS SENT DIRECTLY TO THE WAITING ROOM OR DIRECTLY TO THE DOCTOR
----------------------------------------------------------------------------------------------
"""