from rest_framework import serializers
from accmanager.models import AccountModel

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccountModel
        fields = ('username', )