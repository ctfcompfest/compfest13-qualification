from accmanager.models import AccountModel

from captcha.fields import CaptchaField
from django import forms
from django.contrib.auth.hashers import make_password, check_password
from django.forms import ModelForm, Form

class RegisterForm(ModelForm):
    captcha = CaptchaField()
    username = forms.CharField(
        error_messages = {'unique': "Username has been used."}
    )

    class Meta:
        model = AccountModel
        fields = ['username', 'password', 'transaction_password']
        exclude = ['balance']
    
    def save(self, commit = True):
        super(RegisterForm, self).save(commit=False)

        plain_pwd = self.cleaned_data['password']
        plain_trxpwd = self.cleaned_data['transaction_password']
        self.instance.password = make_password(plain_pwd)
        self.instance.transaction_password = make_password(plain_trxpwd)
        
        return super(RegisterForm, self).save(commit)

class LoginForm(Form):
    username = forms.CharField(max_length=20, required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)

    def authenticate(self):
        if super(LoginForm, self).is_valid():
            try:
                acc = AccountModel.objects.get(username = self.cleaned_data['username'])
                sttPwd = check_password(self.cleaned_data['password'], acc.password)
                if sttPwd:
                    return acc
            except:
                self.add_error('username', 'The username or password is incorrect.')
                return None
                
        self.add_error('username', 'The username or password is incorrect.')
        return None