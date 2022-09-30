from os import path
from unicodedata import name
from django.urls import path
from . import views


urlpatterns = [
    path('home/', views.home_view, name='home'),
    path('signup/', views.signup_view, name='signup'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('users/', views.users_view, name='users'),
    path('users/<str:firstname>/', views.user_details_view, name='user')
]
