# Nested Field - use When: you want to have a field in your model that is itself another Pydantic model. 
# useful for complex data and hierarchical data.
# e.g address has various things in int if we create a single varible then it will be difficult to manager(extract e.g city , state, pin etc) but in nested we create a model for address and use it in patient model as a field.

from pydantic import BaseModel

class Address(BaseModel):

    city: str
    state: str
    pin: str

class Patient(BaseModel):

    name: str
    gender: str
    age: int
    address: Address

address_dict = {'city': 'mumbai', 'state': 'maharashtra', 'pin': '421503'}

address1 = Address(**address_dict)   # <------------------------------------------------object of address model

patient_dict = {'name': 'pratham', 'gender': 'male', 'age': 20, 'address': address1}

patient1 = Patient(**patient_dict) # <--------------------------------------------------object of patient model

print(patient1)
print(patient1.address.city) # <--------------------------------------------------accessing nested field
print(patient1.address.state) # <-------------------------------------------------accessing nested field
print(patient1.address.pin) # <---------------------------------------------------accessing nested field



# Better organization of related data (e.g., vitals, address, insurance)

# Reusability: Use Vitals in multiple models (e.g., Patient, MedicalRecord)

# Readability: Easier for developers and API consumers to understand

# Validation: Nested models are validated automatically—no extra work needed