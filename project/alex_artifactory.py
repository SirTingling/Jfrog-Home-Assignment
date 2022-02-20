# !/usr/bin/env python3

import argparse
import requests
import json
import sys

def parser_args():
    """
    This function is used to parse the arguments.
    """
    parser = argparse.ArgumentParser(description='JFrog Production Engineering Academy - Alex Scherbakov Home Assignments.')
    parser.add_argument("-p",   "--system_ping",       action="store_true", help="Return ping from the system") # store_true : storing the values True or False
    parser.add_argument("-v",   "--system_version",    action="store_true", help="Return system version")
    parser.add_argument("-si",  "--storage_info",      action="store_true", help="Get storage info")
    parser.add_argument("-lr",  "--list_repositories", action="store_true", help="List repositories") 
    parser.add_argument("-cr",  "--create_repository", action="store_true", help="Create repository")
    parser.add_argument("-ur",  "--update_repository", action="store_true", help="Update repository")
    parser.add_argument("-cu",  "--create_user",       action="store_true", help="Create user")
    parser.add_argument("-du",  "--delete_user",       action="store_true", help="Delete user") 
    args = parser.parse_args()
    return args

class Artifactory:
    def __init__(self):
        self.username, self.artifactory_url, self.token = self.user_authentication()
        self.args = parser_args()
        
    def user_authentication(self):
        """
        Get username and password from the user.
        """
        user_dict = {}
        print("Welcome to jfrog Artifactory")
        user_dict["username"] = input("Please input your username: ") #"alexscherba" 
        user_dict["password"] = input("please Input your password: ") #"Alex0246802" 
        user_dict["scope"] = "member-of-groups:*"

        headers_dict = {"Content-Type": "application/x-www-form-urlencoded"}

        artifactory_url = f"https://{user_dict['username']}.jfrog.io/artifactory/"
        token_api = f"api/security/token"
        r = requests.post(artifactory_url + token_api, data=user_dict, headers=headers_dict, auth = (user_dict['username'], user_dict['password']))
        if r.status_code == 200:
            print("Authentication successful")
            return user_dict["username"], artifactory_url, r.json()["access_token"]
        else:
            print("Authentication failed"+ r.content.decode('utf-8'))
            sys.exit()

    def pass_args(self):
        """
        Pass the arguments to the functions.
        """
        if self.args.system_ping:
            self.system_ping()
        elif self.args.system_version:
            self.system_version()
        elif self.args.storage_info:
            self.storage_info()
        elif self.args.list_repositories:
            self.list_repositories()
        elif self.args.create_user:
            self.create_user()
        elif self.args.delete_user:
            self.delete_user()
        elif self.args.create_repository:
            self.create_repository()
        elif self.args.update_repository:
            self.update_repository()
        else:
            print("Please enter a valid argument")

    def system_ping(self):
        """
        Ping the server.
        """
        r = requests.get(self.artifactory_url + "api/system/ping", auth = (self.username, self.token))
        if r.status_code == 200:
            print("Ping status: " + r.content.decode('utf-8'))
        else:
            print("Ping failed")
    
    def system_version(self):
        """
        Get the version of the server.
        """
        r = requests.get(self.artifactory_url + "api/system/version", auth = (self.username, self.token))
        if r.status_code == 200:
            print("Version: " + r.content.decode('utf-8'))
        else:
            print("Version failed")
    
    def storage_info(self):
        """
        Get the storage info.
        """
        r = requests.get(self.artifactory_url + "api/storageinfo", auth = (self.username, self.token))
        if r.status_code == 200:
            print(json.dumps(r.json(), indent = 4))
        else:
            print("Storage info failed")
    
    def list_repositories(self):
        """
        List all repositories.
        """
        r = requests.get(self.artifactory_url + "api/repositories", auth = (self.username, self.token))
        if r.status_code == 200:
            print(json.dumps(r.json(), indent = 4))
        else:
            print("List repositories failed")

    def create_user(self):
        """
        Create a user in Artifactory.
        """
        create_user_dict = {}
        create_user_dict["username"] = input("Input username: ")
        create_user_dict["password"] = input("Input password: ")
        create_user_dict["admin"] = False
        create_user_dict["email"] = input("Input email: ")
        headers = {'Content-Type': 'application/json'}
        r = requests.put(self.artifactory_url + "api/security/users/" + create_user_dict["username"], headers=headers, data=json.dumps(create_user_dict).encode('utf-8'), auth = (self.username, self.token))
        if r.status_code == 201:
            print("User created")
        else:
            print("User creation failed \n" + r.content.decode('utf-8'))

    def delete_user(self):
        """
        Delete a user in Artifactory.
        """
        user_name = input("Input user name: ")
        r = requests.delete(self.artifactory_url + "api/security/users/" + user_name, auth = (self.username, self.token))
        if r.status_code == 200:
            print("User deleted successfully")
        else:
            print("User deletion failed \n" + r.content.decode('utf-8'))
    
    def create_repository(self):
        """
        Create a repository in Artifactory.
        """
        create_reprepository_dict = {}
        create_reprepository_dict["key"] = input("Input repository name: ")
        create_reprepository_dict["rclass"] = "local"
        create_reprepository_dict["packageType"] = input("Package type: ")# "maven"
        create_reprepository_dict["description"] = input("Input repository description: ")
        headers = {'Content-Type': 'application/json'}
        r = requests.put(self.artifactory_url + "api/repositories/" + create_reprepository_dict["key"], headers=headers, data=json.dumps(create_reprepository_dict).encode('utf-8'), auth = (self.username, self.token))
        if r.status_code == 200:
            print("Repository created successfully")
        else:
            print("Repository creation failed \n" + str(r.status_code) + "\n" + str(r.content.decode('utf-8')))
    
    def update_repository(self):
        """
        Update the description of the repository.
        """
        update_repository_dict = {}
        update_repository_dict["key"] = input("Input repository name: ")
        update_repository_dict["description"] = input("Input repository description: ")
        headers = {'Content-Type': 'application/json'}
        r = requests.post(self.artifactory_url + "api/repositories/" + update_repository_dict["key"], headers=headers, data=json.dumps(update_repository_dict).encode('utf-8'), auth = (self.username, self.token))
        if r.status_code == 200:
            print("Repository updated successfully")
        else:
            print("Repository update failed\n" + str(r.status_code) + " " + str(r.content.decode('utf-8')))
    
if __name__ == "__main__":
    artifactory = Artifactory()
    artifactory.pass_args()