from rest_framework import serializers
from acctapp.models import Users, TransactionHistory


class Serializeusers(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = '__all__'

class Serializelogin(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ['email', 'pass_field']

class Serializetrans(serializers.ModelSerializer):
    class Meta:
        model = TransactionHistory
        fields = '__all__'

# class SerializeTransHist(serializers.ModelSerializer):
#     class Meta:
#         model = TransactionHistory
#         fields = ['userid', 'trans_id', 'trans_statement', 'item', 'qty', 'amount', 'trans_type','trans_date']