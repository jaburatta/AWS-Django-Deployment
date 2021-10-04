from django.shortcuts import render, redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
import requests
import json


@api_view(['GET', 'POST'])
def login(request):

    result = ""

    if request.method == 'POST':

        email = request.POST['email']
        password = request.POST['password']

        # url = 'http://127.0.0.1:8000/api/login/'
        url = 'https://3338l2vnvi.execute-api.us-east-1.amazonaws.com/test/login'

        details = {"email": email,"password":password}

        # result = requests.post(url, json=details)
        try: 
            result = requests.get(url, params=details)
            result = result.json()

            # if result['message'] != "Provide valid email and password":
            if result != "Provide valid email and password":

                request.session["secretkey"] = result[0]['fields']['secretkey']
                request.session['businessname'] = result[0]['fields']['businessname'] 

                return redirect('/dashboard/')  
            return render(request, 'login.html', {"result": result})
        # include this exception for API Gateway Endpoint timeout message
        except Exception as e:
            return render(request, 'login.html')

    return render(request, 'login.html', {"result": result})


@api_view(['GET', 'POST'])
def logout(request):
    request.session.pop('secretkey', None)
    return redirect('/login/')
    


@api_view(['GET', 'POST'])
def register(request):
    
    result = ""

    if request.method == 'POST':

        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        businessname = request.POST['businessname']
        phone = request.POST['phone']
        address = request.POST['address']
        email = request.POST['email']
        confirm_email = request.POST['confirm-email']
        password = request.POST['password']
        confirm_password = request.POST['confirm-password']
            
        # url = 'http://127.0.0.1:8000/api/register/'
        url = 'https://3338l2vnvi.execute-api.us-east-1.amazonaws.com/test/register'

        details = {
            "firstname":firstname ,
            "lastname": lastname,
            "businessname": businessname,
            "phone": phone,
            "address": address,
            "email": email,
            "confirm-email":confirm_email,
            "password":password,
            "confirm-password":confirm_password,
        }

        # result = requests.post(url, json=details)
        try:
            result = requests.get(url, params=details)
            result = result.json()

            if result:
                return render(request, 'registration.html', {"result": result})   
        except Exception as e:
            return render(request, 'registration.html')

    return render(request, 'registration.html', {"result": result})


@api_view(['GET', 'POST'])
def dashboard(request):

    if 'secretkey' in request.session:
        secretkey = request.session["secretkey"]
        businessname = request.session['businessname']

        # url = 'http://127.0.0.1:8000/api/dashboard/'
        url = 'https://3338l2vnvi.execute-api.us-east-1.amazonaws.com/test/dashboard'

        details = {"secretkey":secretkey}

        # result = requests.post(url, json=details)
        try:
            result = requests.get(url, params=details)
            result = result.json()
            if result:
                return render(request, 'dashboard.html', {
                    "Business_Name": businessname, 
                    "Business_value": result["Business Value"], 
                    "Income": result["Total Income"], 
                    "Expense": result["Total Expense"]})

            return redirect('/login/')

        except Exception as e:
            return render(request, 'login.html')



@api_view(['GET', 'POST'])
def record(request):
    result = ""
    if 'secretkey' in request.session:
        secretkey = request.session["secretkey"]
        
        if request.method == 'POST':
            record = request.POST["data"]
            
            # url = 'http://127.0.0.1:8000/api/record/'
            url = 'https://3338l2vnvi.execute-api.us-east-1.amazonaws.com/test/record'

            details = {"secretkey":secretkey, "transcript":record}

            # result = requests.post(url, json=details)
            result = requests.get(url, params=details)
            result = result.json()

            if result:
                return render(request, 'record.html', {"result": result})
            
    return render(request, 'record.html', {'result':result })


@api_view(['GET', 'POST'])
def chatpage(request):
    if 'secretkey' in request.session:
        return render(request, "chatbot.html")
    else:
        return redirect('/login/')
        


@api_view(['GET', 'POST'])
def botresponse(request):
    if 'secretkey' in request.session:
        secretkey = request.session["secretkey"]
        userText = request.GET["msg"]

        # url = 'http://127.0.0.1:8000/api/botresponse/'
        url = 'https://3338l2vnvi.execute-api.us-east-1.amazonaws.com/test/chat'

        details = {"secretkey":secretkey, "text":userText}

        # result = requests.post(url, json=details)
        result = requests.get(url, params=details)
        result = result.json()
    return Response(result)


@api_view(['GET', 'POST'])
def history(request):

    if 'secretkey' in request.session:
        secretkey = request.session["secretkey"]

        # url = 'http://127.0.0.1:8000/api/history/'
        url = 'https://3338l2vnvi.execute-api.us-east-1.amazonaws.com/test/history'

        details = {"secretkey":secretkey}

        # result = requests.post(url, json=details)
        try:
            result = requests.get(url, params=details)
            result = result.json()
            # if result['message'] != "No Record Found!":
            #     return render(request, 'history.html', {'hist': result['message']})
            # return render(request, 'history.html', {'result': result['message']})
            if result != "No Record Found!":
                return render(request, 'history.html', {'hist': result})
            return render(request, 'history.html', {'result':  result})
        except Exception as e:
            return render(request, 'login.html')
        
    return render(request, 'history.html', {'hist': result})


@api_view(['GET', 'POST'])
def income(request):

    if 'secretkey' in request.session:
        secretkey = request.session["secretkey"]

        url = 'https://3338l2vnvi.execute-api.us-east-1.amazonaws.com/test/income'

        details = {"secretkey":secretkey}

        # result = requests.post(url, json=details)
        try:
            result = requests.get(url, params=details)
            result = result.json()
            if result != "No Record Found!":
                return render(request, 'history.html', {'hist': result})
            return render(request, 'history.html', {'result': result})
        except Exception as e:
            return render(request, 'login.html')
  
    return render(request, 'history.html', {'hist': result})


@api_view(['GET', 'POST'])
def expense(request):

    if 'secretkey' in request.session:
        secretkey = request.session["secretkey"]

        url = 'https://3338l2vnvi.execute-api.us-east-1.amazonaws.com/test/expense'

        details = {"secretkey":secretkey}

        try:
            result = requests.get(url, params=details)
            result = result.json()
            if result != "No Record Found!":
                return render(request, 'history.html', {'hist': result})
            return render(request, 'history.html', {'result': result})
        except Exception as e:
            return render(request, 'login.html')
  
    return render(request, 'history.html', {'hist': result})


@api_view(['GET', 'POST'])
def histbydate(request):
    if 'secretkey' in request.session:
        secretkey = request.session["secretkey"]
        
        if request.method == 'POST':
            start = request.POST.get("startdate")
            end = request.POST.get("enddate")
            
            url = 'https://3338l2vnvi.execute-api.us-east-1.amazonaws.com/test/histbydate'

            details = {"secretkey":secretkey,"start_date": start,"end_date": end}

            try:
                result = requests.get(url, params=details)
                result = result.json()
                if result != "No Record Found!":
                    return render(request, 'history.html', {'hist': result})
                return render(request, 'history.html', {'result': result})
            except Exception as e:
                return render(request, 'login.html')      
    return render(request, 'history.html',{'hist': result})
