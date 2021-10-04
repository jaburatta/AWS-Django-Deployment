from appfolder.serialization import Serializetrans, Serializeusers
from rest_framework.response import Response
from rest_framework.decorators import api_view 
import secrets
import datetime

from custompackage.nas import NlpAS
from ChatBot.AgriChat import Responses
from Register.register import User

reg = User()
nas = NlpAS()
res = Responses()


# Create your views here.
# pip install pylint-django

@api_view(['GET', 'POST'])
def api_login(request):

    if request.method == 'POST':
        if 'email' in request.data and 'password' in request.data:

            email = request.data['email']
            password = request.data['password']
            try:
                result = reg.login(email, password)
                if result != None:
                    serialize = Serializeusers(result, many=True)
                    return Response({'message': serialize.data}) 
                return Response({'message':"Provide valid email and password"})
            except Exception as e:
                pass
    return Response({"message":"Provide valid email and password like 'email':'abc@yahoo.com', 'password':'password'"})


@api_view(['GET', 'POST'])
def api_register(request):
    reg = User()
    
    if request.method == 'POST':
        if 'businessname' in request.data and 'email' in request.data:
            
            firstname = request.data['firstname']
            lastname = request.data['lastname']
            businessname = request.data['businessname']
            phone = request.data['phone']
            address = request.data['address']
            email = request.data['email']
            confirm_email = request.data['confirm-email']
            password = request.data['password']
            confirm_password = request.data['confirm-password']
            secretkey = secrets.token_hex(20)
                
            if confirm_email != email:
                return Response({'message': "Emails Must Match!"})

            if confirm_password != password:
                return Response({'message': "Passwords Must Match!"})

            if len(phone) != 11:
                return Response({'message': "Invalid Phone Number!"})

            result = reg.register(firstname, lastname,
                        businessname, phone, address, email, password, secretkey)
            return Response({'message': result})
           
    return Response({'message': 'provide firstname, lastname, businessname, phone, address, email, confirm-email, password, confirm-password'})


@api_view(['GET', 'POST'])
def api_dashboard(request):

    if request.method == 'POST':
        if 'secretkey' in request.data:
            secretkey = request.data["secretkey"]
            try:
                nas = NlpAS(secretkey=secretkey)

                Bus_Val = nas.business_value()
                Income = nas.income_sum()
                Expense = nas.expense_sum()

                return Response({'Business Value':Bus_Val, 'Total Income':Income, 'Total Expense': Expense})
            except Exception as e:
                return Response({'message':'Invalid secret key, go to /login/ to view secret key'})  
    return Response({'message':'Provide a Valid Secret Key'})


@api_view(['GET', 'POST'])
def api_record(request):

    if request.method == 'POST':
        if 'secretkey' in request.data and "transcript" in request.data:
            secretkey = request.data["secretkey"]
            
            try:
                nas = NlpAS(secretkey=secretkey)
                record  = request.data["transcript"]
               
                result = nas.populateDB_SR(record)
                if result == 'Transaction Saved':
                    return Response({'message': result})
                return Response({'message':'Provide a Valid secret key and transcript'})
            except Exception as e:    
                pass
    return Response({'message':'Provide a Valid Transcript'})


@api_view(['GET', 'POST'])
def api_botresponse(request):
    bot_response = ""
    
    if request.method == 'POST':
        if 'secretkey' in request.data and 'text' in request.data:
            secretkey = request.data["secretkey"]
            userText = request.data["text"]
            try:
                bot_response = res.get_bot_response(userText)

                if bot_response == 'Transaction Saved. Thank you.':
                    res.populateDB_ChatBot(secretkey, res.record, res.Trans_type)
                return Response({'message': bot_response})
            except Exception as e:
                # pass
                return Response({'message':'Provide a Valid Secret Key'})
    return Response({'message':"Welcome to LedgerBot, would you like to record a transaction?"})
        
    
@api_view(['GET', 'POST'])
def api_history(request):

    if request.method == 'POST':
        if 'secretkey' in request.data:
            secretkey = request.data["secretkey"]
            try:
                nas = NlpAS(secretkey=secretkey)
                result = nas.Trans_History()
                if result:
                    serialize = Serializetrans(result, many=True)
                    return Response({'message':serialize.data})
                return Response({'message':'No Record Found!'})  
            except Exception as e:
                pass
    return Response({'message':'Provide a Valid Secret Key'})


@api_view(['GET', 'POST'])
def api_income(request):

    if request.method == 'POST':
        if 'secretkey' in request.data:
            secretkey = request.data["secretkey"]
            try:
                nas = NlpAS(secretkey=secretkey)
                result = nas.income()
                if result:
                    serialize = Serializetrans(result, many=True)
                    return Response({'message':serialize.data})
                return Response({'message':'No Record Found!'})
            except Exception as e:
                pass
    return Response({'message':'Provide a Valid Secret Key'})


@api_view(['GET', 'POST'])
def api_expense(request):

    if request.method == 'POST':
        if 'secretkey' in request.data:
            secretkey = request.data["secretkey"]
            try:
                nas = NlpAS(secretkey=secretkey)
                result = nas.expense()
                if result:
                    serialize = Serializetrans(result, many=True)
                    return Response({'message':serialize.data})
                return Response({'message':'No Record Found!'}) 
            except Exception as e:
                pass 
    return Response({'message':'Provide a Valid Secret Key'})


@api_view(['GET', 'POST'])
def api_histbydate(request):

    if request.method == 'POST':
        if 'secretkey' in request.data:
            secretkey = request.data["secretkey"]
            try:
                nas = NlpAS(secretkey=secretkey)

                start_date = request.data["start_date"]
                end_date = request.data["end_date"]

                # To include the end date in the query we add an extra day using timedelta
                # Bcos startdate and enddate are returned as strings, we convert from string to date using strptime
                # then date to string usint strftime

                datetimeobj = datetime.datetime.strptime(
                    end_date, "%Y-%m-%d")+datetime.timedelta(days=1)

                end_date = datetimeobj.strftime("%Y-%m-%d")

                result = nas.hist_by_date(start_date, end_date)
                if result:
                    serialize = Serializetrans(result, many=True)
                    return Response({'message': serialize.data})
                return Response({'message': 'No Record Found!'})
            except Exception as e:  
                pass
    return Response({'message':'Provide a Valid Secret Key, start_date and end_date like 2021-10-5'})
