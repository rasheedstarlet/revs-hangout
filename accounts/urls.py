from django.urls import path
from . import views

urlpatterns = [
    path('register', views.register, name='register'),
    path('registration', views.registration, name='registration'),
    path('login', views.login, name='login'),

]
