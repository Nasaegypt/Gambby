from django.urls import path, include
from . import views

app_name = 'service'
urlpatterns = [
    path('', views.service_list, name='service_list'),
    path('add', views.add_service, name='add_service'),
    path('<str:slug>', views.service_detail, name='service_detail'),

]
