# Use When: custom validation and transformation a MULTIPLE fields in a model 

from pydantic import BaseModel, EmailStr, AnyUrl, Field, model_validator #model_validator
from typing import List, Dict, Optional, Annotated

class Patient(BaseModel):

    name: str
    email: EmailStr
    age: int
    weight: float
    married: bool
    allergies: List[str]
    contact_details: Dict[str, str]


    # Here we go!
    @model_validator(mode='after') # mode = 'after' means this validation will be applied after all the field validations are done
    @classmethod
    def validate_patient_emergency_contact(cls, model):

        if model.age > 60 and 'emergency' not in model.contact_details:
            raise ValueError('Emergency contact is required for patients above 60 years of age')
        return model


def update_patient_data(patient: Patient):

    print(patient.name)
    print(patient.email)
    print(patient.age)
    print(patient.weight)
    print(patient.allergies)
    print(patient.married)
    print('updated')

patient_info = {'name':'Pratham', 'email':'abc@icici.com', 'age': 20, 'weight': 75.2, 'married': True, 'allergies': ['pollen', 'dust'], 'contact_details':{'phone':'2353462'}} # this will not throw error coz @icici.com is a valid domain

# cross check by changing the age to 70 and removing 'emergency' from contact_details --> Error expected
# patient_info = {'name':'Pratham', 'email':'abc@icici.com', 'age': 70, 'weight': 75.2, 'married': True, 'allergies': ['pollen', 'dust'], 'contact_details':{'phone':'2353462'}}

# patient_info = {'name':'Pratham', 'email':'abc@icici.com', 'age': 70, 'weight': 75.2, 'married': True, 'allergies': ['pollen', 'dust'], 'contact_details':{'phone':'2353462', 'emergency':'1234567890'}} # this will not throw error coz 'emergency' is present in contact_details

patient1 = Patient(**patient_info) # validation -> type coercion

update_patient_data(patient1) # funtion call 