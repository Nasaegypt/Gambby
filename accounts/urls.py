from django.urls import path, include
from . import views

app_name = 'service'
urlpatterns = [
    path('signup', views.signup, name='signup'),
    path('profile', views.profile, name='profile'),
    path('profile/edit', views.profile_edit, name='profile_edit'),
]
