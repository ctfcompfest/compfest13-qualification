from django.shortcuts import render

def index_handler(req):
    return render(req, 'index.html')