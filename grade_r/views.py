from django.shortcuts import render
from .models import Slider, Our_Mission, Our_Activities, Our_Classes, Images


def grade_r(request):
    sliders = Slider.objects.all()
    our_mission = Our_Mission.objects.all()
    our_activities = Our_Activities.objects.all()
    our_classes = Our_Classes.objects.all()
    images = Images.objects.all()



    context = {
        'sliders' : sliders,
        'our_mission' : our_mission,
        'our_activities': our_activities,
        'our_classes' : our_classes,
        'images' : images,
    } 
    return render(request, 'grade_r/grade_r.html', context)
