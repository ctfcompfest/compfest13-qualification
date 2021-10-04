from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db import models

def balance_nonnegative(v):
    if v < 0:
        raise ValidationError('Balance cannot be negative.')

class AccountModel(User):
    balance = models.IntegerField(default=50, validators=[balance_nonnegative])
    transaction_password = models.CharField(null=False, max_length=100)
