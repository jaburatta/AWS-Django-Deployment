import json
import os 
import sys

# Mount EFS to have access to files and libraries
sys.path.append('/mnt/access')

# DJANGO_SETTINGS_MODULE nasapi.settings - Include DJANGO_SETTINGS_MODULE projectname.settings as environment variable to solve  ImproperlyConfigured Settings error

import django
django.setup() # include to solve AppRegistryNotReady: Apps aren't loaded yet. error

import secrets
import datetime

### Import our custom built packages from AWS EFS
from custompackage.nas import NlpAS
from ChatBot.AgriChat import Responses
from Register.register import User 

reg = User()
nas = NlpAS()
res = Responses()


def lambda_handler(event, context):
    
     # get API Gateway event invocation parameters - e.g. path, queryStringParameters etc. based on needs
    path = event["path"]
    
    if path =='/login':
        email = event["queryStringParameters"]["email"]
        password = event["queryStringParameters"]["password"]
        return {
            'statusCode': 200,
            'body': json.dumps(api_login(email, password))
        }
        

    
    if path=='/register':
        firstname = event["queryStringParameters"]["firstname"]
        lastname = event["queryStringParameters"]["lastname"]
        businessname = event["queryStringParameters"]["businessname"]
        phone = event["queryStringParameters"]['phone']
        address = event["queryStringParameters"]['address']
        email = event["queryStringParameters"]['email']
        confirm_email = event["queryStringParameters"]['confirm-email']
        password = event["queryStringParameters"]['password']
        confirm_password = event["queryStringParameters"]['confirm-password']
        secretkey = secrets.token_hex(20)
        
        if confirm_email != email:
            return {
            'statusCode': 200,
            'body': json.dumps({'message': "Emails Must Match!"})
        }

        if confirm_password != password:
            return {
            'statusCode': 200,
            'body': json.dumps({'message': "Passwords Must Match!"})
        }
           
        if len(phone) != 11:
            return {
            'statusCode': 200,
            'body': json.dumps({'message': "Invalid Phone Number!"})
        }
            
        return {
            'statusCode': 200,
            'body': json.dumps(api_register(firstname, lastname,
                    businessname, phone, address, email, password, secretkey))
        }   
        
    if path=='/dashboard':
        secretkey = event["queryStringParameters"]["secretkey"]
        return {
            'statusCode': 200,
            'body': json.dumps(api_dashboard(secretkey))
        } 
    
    if path=='/record':
        secretkey = event["queryStringParameters"]["secretkey"]
        record = event["queryStringParameters"]["transcript"]
        
        return {
            'statusCode': 200,
            'body': json.dumps(api_record(secretkey, record))
        }
        
    if path=='/history':
        secretkey = event["queryStringParameters"]["secretkey"]
        return {
            'statusCode': 200,
            'body': json.dumps(api_history(secretkey))
        }
        
    if path=='/income':
        secretkey = event["queryStringParameters"]["secretkey"]
        return {
            'statusCode': 200,
            'body': json.dumps(api_income(secretkey))
        }
        
    if path=='/expense':
        secretkey = event["queryStringParameters"]["secretkey"]
        return {
            'statusCode': 200,
            'body': json.dumps(api_expense(secretkey))
        }
        
    if path=='/histbydate':
        secretkey = event["queryStringParameters"]["secretkey"]
        start_date = event["queryStringParameters"]["start_date"]
        end_date = event["queryStringParameters"]["end_date"]
        
        return {
            'statusCode': 200,
            'body': json.dumps(api_histbydate(secretkey, start_date, end_date))
        }
    
    if path =='/chat':
        secretkey = event["queryStringParameters"]["secretkey"]
        userText = event["queryStringParameters"]["text"]
        
        return {
            'statusCode': 200,
            'body': json.dumps(api_botresponse(secretkey, userText))
        }


# import django json serializer
from django.core import serializers

### Login Endpoint
def api_login(email, password):

    if email!= None and password!=None:
        try:
            result = reg.login(email, password)
            if result !=None:
                tmpJson = serializers.serialize("json", result) # Needed to handle Object of type RawQuerySet is not JSON serializable error
                tmpObj = json.loads(tmpJson)
                return tmpObj
            return ("Provide valid email and password")
        except Exception as e:
            pass
    return ("Provide valid email and password like 'email':'abc@yahoo.com', 'password':'password'") 
    
#### Register Endpoint
def api_register(firstname, lastname, businessname, phone, address, email, password, secretkey):
    
    result = reg.register(firstname, lastname,
                businessname, phone, address, email, password, secretkey)
    
    return result
    
### DashBoard Endpoint
def api_dashboard(secretkey):

    if secretkey != None:
        try:
            nas = NlpAS(secretkey=secretkey)

            Bus_Val = nas.business_value()
            Income = nas.income_sum()
            Expense = nas.expense_sum()

            return ({'Business Value':Bus_Val, 'Total Income':Income, 'Total Expense': Expense})
        except Exception as e:
            return ('Invalid secret key, go to /login to view secret key')  
    return ('Provide a Valid Secret Key')
    
### Record Endpoint
def api_record(secretkey, record):
    
    if secretkey!=None and record!= None:
        try:
            nas = NlpAS(secretkey=secretkey)
            result = nas.populateDB_SR(record)
            
            if result == 'Transaction Saved':
                return (result)
            return ('Provide a Valid secret key and transcript')
        except Exception as e:    
            pass
    return ('Provide a Valid Transcript')
    
### History Endpoint
def api_history(secretkey):

    if secretkey!=None:
        try:
            nas = NlpAS(secretkey=secretkey)
            result = nas.Trans_History()
            if result:
                tmpJson = serializers.serialize("json", result) # used to handle Object of type QuerySet is not JSON serializable error
                tmpObj = json.loads(tmpJson)
                return tmpObj
            return ('No Record Found!')  
        except Exception as e:
            pass
    return ('Provide a Valid Secret Key')

### Income Endpoint    
def api_income(secretkey):
    if secretkey!=None:
        try:
            nas = NlpAS(secretkey=secretkey)
            result = nas.income()
            if result:
                tmpJson = serializers.serialize("json", result) # used to handle Object of type QuerySet is not JSON serializable error
                tmpObj = json.loads(tmpJson)
                return tmpObj
            return ('No Record Found!')
        except Exception as e:
            pass
    return ('Provide a Valid Secret Key')

### Expense Endpoint    
def api_expense(secretkey):
    if secretkey!=None:
        try:
            nas = NlpAS(secretkey=secretkey)
            result = nas.expense()
            if result:
                tmpJson = serializers.serialize("json", result) # used to handle Object of type QuerySet is not JSON serializable error
                tmpObj = json.loads(tmpJson)
                return tmpObj
            return ('No Record Found!')
        except Exception as e:
            pass
    return ('Provide a Valid Secret Key')


def api_histbydate(secretkey, start_date, end_date):

    if secretkey!=None:
        try:
            nas = NlpAS(secretkey=secretkey)

            # To include the end date in the query we add an extra day using timedelta
            # Bcos startdate and enddate are returned as strings, we convert from string to date using strptime
            # then date to string usint strftime

            datetimeobj = datetime.datetime.strptime(
                end_date, "%Y-%m-%d")+datetime.timedelta(days=1)

            end_date = datetimeobj.strftime("%Y-%m-%d")

            result = nas.hist_by_date(start_date, end_date)
            if result:
                tmpJson = serializers.serialize("json", result) # used to handle Object of type QuerySet is not JSON serializable error
                tmpObj = json.loads(tmpJson)
                return tmpObj
            return ('No Record Found!')
        except Exception as e:  
            return ('Provide a Valid Secret Key, start_date and end_date like 2021-10-5')
    return ('Provide a Valid Secret Key, start_date and end_date like 2021-10-5')
    
def api_botresponse(secretkey, userText):
    bot_response = ""
    
    if secretkey!=None and userText!= None:
        try:
            bot_response = res.get_bot_response(userText)

            if bot_response == 'Transaction Saved. Thank you.':
                res.populateDB_ChatBot(secretkey, res.record, res.Trans_type)
            return (bot_response)
        except Exception as e:
            pass
            # return Response('Provide a Valid Secret Key')
    return Response("Welcome to LedgerBot, would you like to record a transaction?")