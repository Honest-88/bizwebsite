from django.urls import path
from . import views

app_name = 'gallery'


urlpatterns = [
    path('gallery/', views.gallery, name='gallery'),
    path('green_club_gallery/', views.green_club_gallery, name='green_club_gallery'),
    path('school_gallery/', views.school_gallery, name='school_gallery'),
    path('grade_r/', views.grade_r, name='grade_r'),
    path('madrassa/', views.madrassa, name='madrassa'),
 
]
