from django.urls import path, include
import transaction.views as views

app_name = 'transaction'

urlpatterns = [
    path('send/', views.create_trx, name='send'),
    path('<str:id>/update/', views.update_trx, name='update'),
    path('<str:id>/delete/', views.delete_trx, name='delete'),
    path('flag/', views.buyflag, name='flag'),
]
