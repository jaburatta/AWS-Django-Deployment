
from django.urls import path
from .apiviews import api_register, api_dashboard, api_login, api_record, api_botresponse, api_history, api_income, api_expense, api_histbydate
from .appviews import register, login, logout, dashboard, record, history, income, expense, histbydate, chatpage, botresponse


urlpatterns = [
    # api endpoints
    path('api/register/', api_register),
    path('api/login/', api_login),
    path('api/dashboard/', api_dashboard),
    path('api/record/', api_record),
    path('api/botresponse/', api_botresponse),
    path('api/history/', api_history),
    path('api/income/', api_income),
    path('api/expense/', api_expense),
    path('api/histbydate/', api_histbydate),

    # app endpoints
    path('register/', register),
    path('login/', login),
    path('logout/', logout),
    path('dashboard/', dashboard),
    path('record/', record),
    path('history/', history),
    path('income/', income),
    path('expense/', expense),
    path('histbydate/', histbydate),
    path('chat/', chatpage),
    path('botresponse/', botresponse),
]
