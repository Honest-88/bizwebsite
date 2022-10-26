from django.urls import path
from . import views

app_name = 'grade_r'


urlpatterns = [
    path("grade_r", views.grade_r, name='grade_r'),

]
