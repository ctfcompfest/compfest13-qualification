from django.urls import path
import api.views as views

app_name = 'api'

urlpatterns = [
    path('v1/history/sent/', views.api_sent, name='sent'),
    path('v1/history/received/', views.api_received, name='received'),
]
