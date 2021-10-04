from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.views.decorators.http import require_GET

def get_paginator(request):
    numPage = request.GET.get('page', '1')
    if not numPage.isdigit():
        numPage = 1
    numPage = int(numPage)
    return {'page': [numPage - 1, numPage, numPage + 1]}

@require_GET
@login_required(login_url='accmanager:login')
def history_sent(req):
    context = {}
    context.update(get_paginator(req))
    return render(req, 'history/sent.html', context)

@require_GET
@login_required(login_url='accmanager:login')
def history_received(req):
    context = {}
    context.update(get_paginator(req))
    return render(req, 'history/received.html', context)