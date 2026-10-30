from pydantic import BaseModel

class Patient(BaseModel):

    name: str
    age: int

def insert_patient_data(patient: Patient):

    print(patient.name)
    print(patient.age)
    print("Inserted")

patient_data = {'name': 'pratham', 'age': 20}

patient1 = Patient(**patient_data)

insert_patient_data(patient1)