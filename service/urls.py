from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.service_list),
    path('<int:id>', views.service_detail)
]
