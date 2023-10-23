# Workflow Code Description
Code Challenge solution to create CI/CD approach using Github Pull and PUSH Request actions and deploy the code to AWS cloud server.


# Github Actions
GitHub actions helps to perform the CI/CD operations based on PR creation and any push to the main branch.


## Code Build 
After creating pull request code build and checks are performed on the PR, once the code build completes successfully PR is ready for review and then merge. Below status shows the status of latest code build performed.

[![Python Application Code Build](https://github.com/Pallavi-Sharma12/code_challenge/actions/workflows/python-app.yml/badge.svg)](https://github.com/Pallavi-Sharma12/code_challenge/actions/workflows/python-app.yml)


## Code Deploy
Once any code is merged or pushed to the `main` branch, corresponding code is deployed to the respective AWS EC2 environment. Below status shows the status of latest code deploy performed.

[![Deploy to Amazon Linux EC2](https://github.com/Pallavi-Sharma12/code_challenge/actions/workflows/main.yml/badge.svg)](https://github.com/Pallavi-Sharma12/code_challenge/actions/workflows/main.yml)


# Application Overview
This application uses SQLite and Python to Fetch and Add Employee ID and Name in the SQLite database created using Flask GET and POST API method technique.
- With `GET` request, code fetches all the employee data [employee-id] or [employee-name] from the database and return.
- With `POST` request, employee data like ID and Name is inserted in the database for further use.


# Tools Used 
- AWS EC2
- Github


# Technology Used
- Python Flask
- SQLite
- Github Action


# How to Execute the GET and POST request
Use below commands to run GET and POST request ->


## GET Request
Execute GET request using "curl http://127.0.0.1:5000/result" command on the system to check the employee details returned by the employee database from SQLite.


## POST Request
Execute mentioned POST request to insert user detail in the SQLite "test.db" using command -> curl --header "Content-Type: application/json" --request POST --data '{"Emp_Id":{employee_id},"Emp_Name":"{employee_name}"}' http://127.0.0.1:5000/results