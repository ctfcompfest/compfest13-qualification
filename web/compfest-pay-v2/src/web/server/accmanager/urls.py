from django.urls import path
import accmanager.views as views

app_name = 'accmanager'

urlpatterns = [
    path('login/', views.login_handler, name='login'),
    path('logout/', views.logout_handler, name='logout'),
    path('register/', views.register_handler, name='register'),
    path('dashboard/', views.dashboard, name='dashboard'),
]
