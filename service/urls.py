from django.urls import path, include
from . import views

app_name = 'service'
urlpatterns = [
    path('', views.service_list),
    path('<str:slug>', views.service_detail, name='service_detail'),

]
