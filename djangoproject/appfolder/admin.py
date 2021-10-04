from django.contrib import admin
from appfolder.models import Users, TransactionHistory

# Register your models here.
admin.site.register(Users)
admin.site.register(TransactionHistory)
