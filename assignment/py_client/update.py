import requests
product_id = int(input("Enter the product_id you want to update \n"))


def get_data():
    print("Leave the fileds blank if you do not want to update them")
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
data = {k: v for k, v in data.items() if v}

get_mixin_update=requests.patch(f"http://localhost:8000/api/students/{product_id}/",json=data)

print(get_mixin_update.json())


