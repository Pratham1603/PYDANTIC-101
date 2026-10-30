from pydantic import BaseModel
from typing import List, Dict, Optional

class Patient(BaseModel):

    name: str
    age: int
    weight: float
    married: bool
    allergies: Optional[List[str]] = None
    contact_details: Dict[str, str]

def insert_patient_data(patient: Patient):

    print(patient.name)
    print(patient.age)
    print(patient.weight)
    print(patient.married)
    print(patient.allergies)
    print(patient.contact_details)
    print("Inserted")

patient_data = {'name': 'pratham', 'age': 20, 'weight': 70.5, 'married': False, 'contact_details': {'email': 'pratham@example.com', 'phone': '123-456-7890'}}

patient1 = Patient(**patient_data)

insert_patient_data(patient1)