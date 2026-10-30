def insert_patient_data(name: str, age: int):

    # Suppose this is DB Code
    if type(name) == str and type(age) == int:
        print(name)
        print(age)
        print("Inserted into DB")
    else:
        raise ValueError("Invalid data type for name or age")

def update_patient_data(name: str, age: int):

    # Suppose this is DB Code
    if type(name) == str and type(age) == int:
        print(name)
        print(age)
        print("Updated in DB")
    else:
        raise ValueError("Invalid data type for name or age")