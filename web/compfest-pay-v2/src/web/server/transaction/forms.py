from django import forms
from django.contrib.auth.hashers import check_password
from django.forms import ModelForm

from accmanager.models import AccountModel
from transaction.models import TransactionModel

BLACKLIST = [
    '$', 'jquery', 'function', 'script', 'javascript',
    'document', 'window', 'parent', 'top', 'this', 'frames', 'content', 'Object', 'location', 'href', 'eval', 'exec',
    'xml', 'open', 'send', 'ajax', 'get', 'post', 'put', 'patch', 'fetch',
    'api/', 'history/',
]

def check_blacklist(msg):
    msg = msg.lower()
    for e in BLACKLIST:
        if msg.find(e) != -1:
            msg = msg.replace(e, "[BAD]")
    return msg

class TransactionForm(ModelForm):
    transaction_password = forms.CharField(max_length=100)
    amount = forms.IntegerField(min_value=1,required=False)
    sender = forms.CharField(required=False)
    recipient = forms.CharField(required=False)
    id = forms.UUIDField()
    
    class Meta:
        model = TransactionModel
        fields = ['id', 'sender', 'recipient', 'amount', 'msg']
        exclude = ['date']
    
    def clean_sender(self):
        try:
            sender = self.cleaned_data.get('sender')
            if sender == "" or sender == None:
                return self.instance.sender
            return AccountModel.objects.get(username = sender)
        except Exception as e:
            raise forms.ValidationError(str(e), code='sender')

    def clean_recipient(self):
        try:
            recipient = self.cleaned_data.get('recipient')
            if recipient == None or recipient == "":
                return self.instance.recipient            
            rec = AccountModel.objects.get(username = recipient)
            sender = self.cleaned_data.get('sender')
            if rec.username == sender.username:
                raise Exception('You cannot send money to yourself.')
            return rec
        except Exception as e:
            raise forms.ValidationError(str(e), code='recipient')

    def clean_amount(self):
        try:
            amount = self.cleaned_data.get('amount')
            if amount == None:
                return self.instance.amount
            acc = self.cleaned_data.get('sender')
            if acc.balance < amount:
                raise Exception('Your balance is not enough.')
            return amount
        except Exception as e:
            raise forms.ValidationError(str(e), code='amount')

    def clean_transaction_password(self):
        transaction_password = self.cleaned_data.get("transaction_password")
        acc = self.clean_sender()
        if transaction_password:
            if check_password(transaction_password, acc.transaction_password):
                return transaction_password
        raise forms.ValidationError(
            'You have entered wrong transaction password.',
            code='transaction_password')
    
    def clean_msg(self):
        msg = self.cleaned_data.get("msg")
        return check_blacklist(msg)[:100]
    
    def save(self, commit = True, update = False):
        sender = self.cleaned_data['sender']
        recipient = self.cleaned_data['recipient']
        amount = self.cleaned_data['amount']
        if not update:
            sender.balance -= amount
            sender.save()
            recipient.balance += amount
            recipient.save()
        
        return super(TransactionForm, self).save(commit)
