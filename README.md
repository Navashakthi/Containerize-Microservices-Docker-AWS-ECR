# Containerize Microservice Applications using Docker

Step by step process of Containerizing Microservice Applications ( Python Flask APP ) to a Docker container on AWS
### > Microservice Architecture : 

Microservices are an approach to application development in which a large application is built as a suite of modular services that has small multiple services where each module supports a specific business goal and uses a simple, well-defined interface to communicate with other sets of services.

It is an architecture where the software components are independent and loosely coupled.

## Project Use-Case
Invoice-Info-APP is an application built to get invoice data such as
-- Total invoices of the month
-- Invoices Pending payment
-- Invoices with payment processed

## Requirements

- Python 3.9 : https://www.python.org/downloads/

- Docker : https://docs.docker.com/get-docker/

- AWS CLI : https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html

- Visual Studio Code : https://code.visualstudio.com/download

- Python Libraries : requests, Flask == 2.0.3, Jinja2 == 3.1.1

Install all requirements, create an AWS account ( a free tier account is sufficient for this project ), login with credentials, create a user with necessary IAM permissions and download the credentials.csv file. [Check AWS doc](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users_create.html)

## Project Structure:
The python flask App files and dependents are present in this folder structure
- data : Folder contains JSON file with invoice data
- app.py : Flask app to get invoice data
- requirements.txt
- Dockerfile
- .dockerignore

## Configure and Containerize the Application in Local Machine
- Check if docker is successfully installed in the system with : docker --version : Docker version 20.10.16, build aa7e414
- Download the code from GitHub repository to your local environment
- In the Invoice-Info-APP directory run the following commands:
  - docker build -t invoiceapp
  - docker run -p 5000:5000 invoiceapp
 
 This creates the docker build and run in the local machine.

## Configure and Containerize the Application in AWS
- **Step 1:** Open AWS Account with User account
  - Navigate to the **Amazon ECR console**.
  - On the repository page, select *Create Repository* 
  - On creating repository enter repository name and details
  - Once the repository is created select the repository and click on *View push commands* for build and push of docker file.
- **Step 2:** Configure AWS profile with the commands:
  -Access the terminal and check for AWS CLI installed with : aws --version
  aws-cli/2.7.18 Python/3.9.11 Windows/10 exe/AMD64 prompt/off
  - Navigate in terminal to Invoice-Info-APP directory and run the below commands
  -aws configure
  -aws configure set region us-west-1 --profile invoiceuser
  -aws configure list-profiles
  -setx AWS_PROFILE invoiceuser
  For more details on CLI configuration check here [AWS CLI Config](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-quickstart.html#cli-configure-quickstart-precedence)
- **Step 3:** Run Docker Commands 
  - Once aws profile is configured run the below docker commands from the **View push commands**
  - aws ecr-public get-login-password --region us-east-1 | docker login --username AWS --password-stdin public.ecr.aws/<id> (Paste your ECR commands)
  - docker build -t invoiceapp .
  - docker tag invoiceapp:latest public.ecr.aws/<id>/invoiceapp:latest
  - docker push public.ecr.aws/<id>/invoiceapp:latest
  
  This pushes the built docker image of the app into AWS ECR.




