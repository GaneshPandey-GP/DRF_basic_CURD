import requests
import json

url="http://127.0.0.1:8000/api/"

def GetStudentInfo():
    Custom_url = url+"stu_info/"
    response = requests.request("GET", Custom_url)
    print(response.text)


# GetStudentInfo()    

def InsertNewStudent():

    Custom_url = url+"insert_new_stu/"

    payload = json.dumps({
    "name": "Ram",
    "rollno": 6,
    "address": "uttarakhand"
    })
    headers = {
    'Content-Type': 'application/json'
    }

    response = requests.request("POST", Custom_url, headers=headers, data=payload)

    print(response.text)

# InsertNewStudent()


def InsertInBulk():

    custom_url=url+"insert_new_stu_in_bulk/"


    payload = json.dumps({
    "data": [
        {
        "name": "John",
        "rollno": 7,
        "address": "new delhi"
        },
        {
        "name": "Ram",
        "rollno": 8,
        "address": "mumbai"
        }
    ]
    })
    headers = {
    'Content-Type': 'application/json'
    }

    response = requests.request("POST", custom_url, headers=headers, data=payload)

    print(response.text)

# InsertInBulk()

def UpdateStudent():
    custom_url=url+"update_info/"

    payload = json.dumps({
    "id": 9,
    "name": "John"
    })
    headers = {
    'Content-Type': 'application/json'
    }

    response = requests.request("POST", custom_url, headers=headers, data=payload)

    print(response.text)

# UpdateStudent()

def DeleteInfo():
    custom_url=url+"delete_info/"

    payload = json.dumps({
    "id": 1
    })
    headers = {
    'Content-Type': 'application/json'
    }

    response = requests.request("DELETE", custom_url, headers=headers, data=payload)

    print(response.text)

DeleteInfo()


