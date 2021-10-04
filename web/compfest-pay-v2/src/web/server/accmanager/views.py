from captcha.models import CaptchaStore
from django.contrib.auth import logout, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from compfestpay2.secret import FLAG_PRICE

from accmanager.forms import RegisterForm, LoginForm
from accmanager.models import AccountModel
from compfestpay2.secret import FLAG_PRICE
from transaction.models import TransactionModel

from random import choice
from string import ascii_letters
from os import urandom

def create_new_transaction():
    username = "fakeacc-" + urandom(4).hex() + str(AccountModel.objects.all().count())
    password = ''.join([choice(ascii_letters) for _ in range(12)])

    bos = AccountModel.objects.get(username = 'richGuy')
    tmp = AccountModel(username = username, password = password, transaction_password = password, balance = FLAG_PRICE + 5)
    tmp.save()
    trx = TransactionModel(amount=FLAG_PRICE, sender=bos, recipient=tmp, msg="Steal me!")
    trx.save()

def register_handler(req):
    if req.user.is_authenticated:
        return redirect('accmanager:dashboard')
    context = {
        'captcha_key': CaptchaStore.generate_key(),
    }
    if req.method == 'POST':
        regForm = RegisterForm(req.POST)
        context['form'] = regForm
        if regForm.is_valid():
            regForm.save()
            create_new_transaction()
            return redirect('accmanager:login')
        
    return render(req, 'accmanager/register.html', context)

def login_handler(req):
    if req.user.is_authenticated:
        return redirect('accmanager:dashboard')
    context = {}
    if req.method == 'POST':
        loginForm = LoginForm(req.POST)
        context['form'] = loginForm
        acc = loginForm.authenticate()
        if acc is not None:
            login(req, acc)
            return redirect('accmanager:dashboard')
    return render(req, 'accmanager/login.html', context)

def logout_handler(req):
    logout(req)
    return redirect('accmanager:login')
    
@login_required(login_url='accmanager:login')
def dashboard(req):
    context = {}
    acc = AccountModel.objects.get(username = req.user.username)
    sent = TransactionModel.objects.filter(sender = acc).count()
    received = TransactionModel.objects.filter(recipient = acc).count()

    context['flagprice'] = FLAG_PRICE
    context['balance'] = acc.balance
    context['transaction_sent'] = sent
    context['transaction_received'] = received
    return render(req, 'transaction/dashboard.html', context)