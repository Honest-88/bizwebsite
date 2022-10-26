from django.urls import path
from . import views


app_name = 'madrassa'


urlpatterns = [
    path('madrassa/', views.madrassa, name='madrassa'),

]