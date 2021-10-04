# AWS-Django-Deployment

This repo contains files and folders deployed on AWS. 
Five (5) AWS services was used for this deployment: 
- AWS EFS - tol hold project files and folder and also to install python packages to be called in AWS Lambda. 
- AWS EC2 - This was used to mount the EFS and also to deploy the web app. 
- AWS Lambda - this is where the serveless fucntion ivocked by the API gaetway resides. The AWS lambda also had the EFS attached to it and then configured to acomodate django requirements.
- AWS API Gateway - Resources and methods were created and invocked lambda in its backend.
- AWS RDS (MySQL DB) - This is where the DB for the project was hosted 

# About The Project

The project utilizes:
- A Named Entity Recognition (NER Model) built with Spacy 3
- Chatbot built with chatterbot
- Machine Learning classification model 
- MySQL database as its backend
