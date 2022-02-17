"""
CLI in python to manage an Artifactory SaaS instance via its API.
"""

import argparse
import requests
import json


parser = argparse.ArgumentParser(description='JFrog Production Engineering Academy - Alex Scherbakov Home Assignments.')
parser.add_argument("-p", "--system_ping", action="store_true",help="Return ping from the system") # store_true : storing the values True or False
parser.add_argument("-v", "--system_version", action="store_true",help="Return system version")
parser.add_argument("-cu", "--create_user", action="store_true",help="Create user") 
parser.add_argument("-du", "--delete_user", action="store_true",help="Delete user") 
parser.add_argument("-gsi", "--get_storage_info", action="store_true",help="Get storage info")
args = parser.parse_args()



def main():
    flag_dic = {"system_ping": False, "system_version": False}
    if args.system_ping:
        flag_dic["system_ping"] = True
        respod_from_the_server("api/system/ping", flag_dic)
    elif args.system_version:
        flag_dic["system_version"] = True
        respod_from_the_server("api/system/version", flag_dic)
    elif args.create_user:
        create_user(input("Enter username: "), input("Enter password: "), input("Enter email: "))
    elif args.delete_user:
        respod_from_the_server("api/security/users/delete")
    elif args.get_storage_info:
        respod_from_the_server("api/storage/info")
    else:
        print("Please enter a valid argument")

def respod_from_the_server(api="", flag_dic={}):
    """
    This function is used to get the response from the server.
    """
    username = "alexscher"
    password = "Alex0246802"
    artifactory = "https://alexscher.jfrog.io/artifactory/" #artifactory URL
    
    url = artifactory + api
    r = requests.get(url, auth = (username, password)) #this script is only for API methods that use GET

    if r.status_code == 200 and flag_dic["system_ping"]:
        print("Ping status: " + r.content.decode('utf-8'))
    elif r.status_code == 200 and flag_dic["system_version"]:
        print(r.headers.get('X-JFrog-Version'))
    else:
        print("Fail")
        response = json.loads(r.content)
        print(response["errors"])

        print("x-request-id : " + r.headers['x-request-id'])
        print("Status Code : " + r.status_code)

def create_user(username, password, email="", admin=False):
    """
    Create a user in Artifactory.
    """
    url = f"https://alexscher.jfrog.io/artifactory/api/security/users/{username}"
    data = {
        "name": username,
        "password": password,
        "admin": admin,
        "email": email
    }
    r = requests.put(url, data=data)
    print(r.content)



if __name__ == "__main__":
    main()