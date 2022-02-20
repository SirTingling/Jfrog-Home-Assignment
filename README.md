# Jfrog Alex Home Assignment
## Description
JFrog Production Engineering Academy - Alex Home Assignment

## Installation
They are two ways to install the project:
The first one:

```cmd
pip3 install alexscherba -i  https://alexscherba.jfrog.io/artifactory/alex_assignment_local/alexscherba
```
username: alexscherba
password: Alex0246802

The second:

``` cmd
git clone https://github.com/alexsherba29/Jfrog-Home-Assignment.git
pip3 install -r requirements.txt
cd project/
```

## Usage
python3 alex_artifactory.py [-h] [-p] [-v] [-si] [-lr] [-cr] [-dr] [-ur] [-cu] [-du]

optional arguments: 

flag | long                | description
---- |---------------------|--------------------------------
-h   | --help              | Show all the optional arguments
-p   | --system_ping       | Health check
-v   | --system_version    | Return system version
-si  | --get_storage_info  | Show storage info
-lr  | --list_repositories | List all repositories
-cr  | --create_repository | Create repository
-dr  | --delete_repository | Delete repository
-ur  | --update_repository | Update repository
-cu  | --create_user       | Create user
-du  | --delete_user       | Delete user

## Resources & decisions 

I began by studying the artifactory environment and create local repositorie.

* https://academy.jfrog.com/jfrog-artifactory-overview-2020/443201
* https://www.jfrog.com/confluence/display/RTF

Next, I built a Python CLI script to manage an Artifactory SaaS instance with all the necessary features.

* https://docs.python.org/3/library/argparse.html
* https://github.com/jfrog/artifactory-scripts/tree/master/REST-API-Examples
* https://www.jfrog.com/confluence/display/JFROG/Artifactory+REST+API

Finally, I create a setup script and upload the project to the repository

* https://packaging.python.org/en/latest/tutorials/installing-packages/