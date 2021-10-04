from django.urls import path
import history.views as views

app_name = 'history'

urlpatterns = [
    path('sent/', views.history_sent, name='sent'),
    path('received/', views.history_received, name='received'),
]
