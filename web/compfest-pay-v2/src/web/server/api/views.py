from django.contrib.auth.decorators import login_required
from django.core.paginator import EmptyPage, Paginator
from django.http.response import JsonResponse
from django.views.decorators.http import require_GET

from accmanager.models import AccountModel
from transaction.models import TransactionModel

from transaction.serializers import TransactionSerializer

def get_paginator(request, data, n = 25):
    try:
        page = Paginator(data, n)
        numPage = request.GET.get('page', '1')
        if not numPage.isdigit():
            numPage = 1
        numPage = int(numPage)
        return list(page.page(numPage).object_list)
    except EmptyPage:
        return None

@require_GET
@login_required(login_url='accmanager:login')
def api_sent(req):
    acc = AccountModel.objects.get(username = req.user.username)
    trxsent = TransactionModel.objects.filter(sender = acc).order_by('-date')
    data = get_paginator(req, trxsent)
    serialize = TransactionSerializer(data, many=True).data
    return JsonResponse({"status": "ok", "data": serialize})

@require_GET
@login_required(login_url='accmanager:login')
def api_received(req):
    acc = AccountModel.objects.get(username = req.user.username)
    trxrec = TransactionModel.objects.filter(recipient = acc).order_by('-date')
    data = get_paginator(req, trxrec)
    serialize = TransactionSerializer(data, many=True).data
    return JsonResponse({"status": "ok", "data": serialize})