from django.contrib import admin
from django.urls import path
from home import views
urlpatterns = [
    path("", views.login,name='login'),
    path("registration",views.registration,name="registration"),
    path("index",views.index,name="index"),
    path("logout",views.index,name="logout")
]