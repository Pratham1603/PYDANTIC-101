from pydantic import BaseModel, EmailStr, AnyUrl, Field, field_validator #field_validator
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
    # 1.use case : Custom Validation - e.g email domain validation - only hdfc.com and icici.com are valid domains

    @field_validator('email')
    @classmethod
    def validate_email(cls, value):

        valid_domains = ['@hdfc.com', 'icici.com']
        # abc@gmail.com
        domain_name = value.split('@')[-1]

        if domain_name not in valid_domains:
            raise ValueError('Not a valid domain')
        return value 


    # 2.use case : Transforming the data - e.g name should be in upper case

    @field_validator('name')
    @classmethod
    def transform_name(cls, value):
        return value.upper()


def update_patient_data(patient: Patient):

    print(patient.name)
    print(patient.email)
    print(patient.age)
    print(patient.weight)
    print(patient.allergies)
    print(patient.married)
    print('updated')

patient_info = {'name':'Pratham', 'email':'abc@icici.com', 'age': '30', 'weight': 75.2, 'married': True, 'allergies': ['pollen', 'dust'], 'contact_details':{'phone':'2353462'}} # this will not throw error coz @icici.com is a valid domain

# cross check by changing the email to 'abc@gmail.com' --> Error expected

patient1 = Patient(**patient_info) # validation -> type coercion

update_patient_data(patient1) # funtion call 