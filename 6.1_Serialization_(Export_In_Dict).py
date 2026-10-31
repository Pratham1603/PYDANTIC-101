# Export pydantic model to dictionary using model_dump() method

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

###########################################################################

temp = patient1.model_dump()
print(temp)
print(type(temp))



temp1 = patient1.model_dump(include={'address'})
print(temp1)

temp2 = patient1.model_dump(exclude=['name', 'gender'])
print(temp2)

temp3 = patient1.model_dump(exclude={'address'})
print(temp3)

temp4 = patient1.model_dump(include={'address': {'city', 'pin'}})
print(temp4)