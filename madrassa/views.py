from django.shortcuts import render
from .models import Slider, Welcome, Our_Mission, Impression, Testimonials
from projects.models import Project
from blog.models import Post


def madrassa(request):
    most_recent = Post.objects.order_by('-timestamp')[:6]
    recent_projects = Project.objects.order_by('-created')[:6]

    testimonials = Testimonials.objects.all()
    sliders = Slider.objects.all()
    welcome = Welcome.objects.all()
    our_mission = Our_Mission.objects.all()
    impression = Impression.objects.all()

    context = {
        'sliders' : sliders,
        'welcome' : welcome,
        'our_mission' : our_mission,
        'impression' : impression,
        'recent_projects': recent_projects,
        'testimonials' : testimonials,
        'most_recent' : most_recent,
    }
    return render(request, 'madrassa/madrassa.html', context)

