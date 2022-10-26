from django.contrib import admin
from django.urls import path,include
from application import views


app_name = 'application'


urlpatterns = [
    path("apply",views.apply, name='apply'),

]





