from rest_framework import serializers
from transaction.models import TransactionModel
from accmanager.serializers import AccountSerializer

class TransactionSerializer(serializers.ModelSerializer):
    sender = AccountSerializer(read_only=True)
    recipient = AccountSerializer(read_only=True)

    class Meta:
        model = TransactionModel
        fields = '__all__'