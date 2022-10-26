from django.urls import path
from . import views
from projects.views import project, projects

app_name = 'projects'

urlpatterns = [

    path('projects/', views.projects, name='projects'),
    path('project/<id>/', views.project, name="project"),

]

