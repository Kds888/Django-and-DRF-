import requests
from datetime import datetime

def get_data():
    first_name=input("Enter the First name\n")
    last_name=input("Enter the Last name\n")
    dob=input("Enter the DOB in YYYY-MM-DD format\n")
    amount_due=float(input("Enter the AMOUNT_Due \n"))
    data ={
        'first_name':first_name,
        'last_name':last_name,
        'dob':dob,
        'amount_due':amount_due
    }
    return data

data=get_data()
get_create=requests.post("http://localhost:8000/api/students/", json=data)
print(get_create.json()) 