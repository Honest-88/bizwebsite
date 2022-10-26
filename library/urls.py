from django.contrib import admin
from django.urls import path,include
from library import views


app_name = 'library'


urlpatterns = [
    path("library",views.library, name='library'),
    path('library_detail/<id>/', views.library_detail, name='library_detail'),

]
