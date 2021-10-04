from django.core.exceptions import ValidationError
from django.db import models
from accmanager.models import AccountModel

import uuid
from datetime import datetime

def money_positive(v):
    if v <= 0:
        raise ValidationError('You only can transfer positive amounts of money.')

class TransactionModel(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    amount = models.IntegerField(default=1, null=False, validators=[money_positive])
    sender = models.ForeignKey(AccountModel, related_name="transaction_sender", on_delete=models.CASCADE)
    recipient = models.ForeignKey(AccountModel, related_name="transaction_recipient", on_delete=models.CASCADE)
    msg = models.CharField(max_length=100)
    date = models.DateTimeField(default=datetime.now, blank=True)