# A Python Django Example

This repo is intended for use with [Gitpod](httpsL//gitpod.io).

## Basics
When opening a new gitpod with this repo the initial setup should mostly be taken care of for you to get moving with a Django app immediately.

Processes that should run:
1. Automatically get a docker container that creates a PostgresQL database (port 5432) and starts pgAdmin (database tool) on the port 7000. (Credentials for the database can be found in the pgadmin.json file.)
1. After port 7000 starts up, pip should be upgraded and all requirements in the requirements.txt should be installed, including `psycopg2` and `Django` among other packages.

## Changing the Django PROJECT name
1. The current project name is `myproject`. If you would like to change that name you will need to change the directory name as well as all the references to that project throughout the files in the project. That might be worth the time.

## Django Admin
The CSRF_TRUSTED_ORIGINS setting in settings.py should be set to allow `https://*.gitpod.io` for a trusted CSRF token.
