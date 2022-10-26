from django.urls import path
from . import views

app_name = 'newsletters'


urlpatterns = [
   
    path('newsletters/', views.newsletters, name='letters_list'),
    path('letters/<id>/', views.letters, name='letters_detail'),

]
