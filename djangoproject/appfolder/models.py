# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
import datetime

class TransactionHistory(models.Model):
    trans_id = models.IntegerField(primary_key=True)
    userid = models.ForeignKey('Users', on_delete=models.CASCADE, db_column='userid')
    trans_statement = models.CharField(max_length=1000)
    item = models.CharField(max_length=1000)
    qty = models.CharField(max_length=10, blank=True, null=True)
    amount = models.FloatField()
    trans_type = models.CharField(max_length=10)
    trans_date = models.DateTimeField(default=datetime.datetime.now())

    class Meta:
        managed = False
        db_table = 'transaction_history'


class Users(models.Model):
    userid = models.IntegerField(primary_key=True)
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    businessname = models.CharField(max_length=50)
    phone = models.CharField(max_length=11)
    address = models.CharField(max_length=70)
    email = models.CharField(max_length=50)
    pass_field = models.CharField(db_column='pass', max_length=200)  # Field renamed because it was a Python reserved word.
    datejoined = models.DateTimeField(default=datetime.datetime.now())
    secretkey = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'users'



# python manage.py inspectdb > models.py
