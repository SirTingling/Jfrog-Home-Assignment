# Jfrog Alex Home Assignment
## Description
JFrog Production Engineering Academy - Alex Home Assignment

## Installation
pip3 install -r requirements.txt

## Usage
python3 alex_artifactory.py [-h] [-p] [-v] [-gsi] [-lr] [-cr] [-dr] [-ur] [-cu] [-du]

optional arguments: 

  -h, --help            show this help message and exit
  -p, --system_ping     Return ping from the system
  -v, --system_version  Return system version
  -gsi, --get_storage_info
                        Get storage info
  -lr, --list_repositories
                        List repositories
  -cr, --create_repository
                        Create repository
  -dr, --delete_repository
                        Delete repository
  -ur, --update_repository
                        Update repository
  -cu, --create_user    Create user
  -du, --delete_user    Delete user

## Resources
https://academy.jfrog.com/jfrog-artifactory-overview-2020/443201
https://github.com/jfrog/artifactory-scripts/tree/master/
https://github.com/jfrog/artifactory-scripts/blob/master/REST-API-Examples
https://www.jfrog.com/confluence/display/RTF
https://www.jfrog.com/confluence/display/JFROG/Artifactory+REST+APIREST-API-Examples
https://docs.python.org/3/library/argparse.html
