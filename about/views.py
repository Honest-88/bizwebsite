from django.shortcuts import render
from .models import About_Us, Our_Staff, History



def about(request):
    about_us = About_Us.objects.all()
    our_staff = Our_Staff.objects.order_by('-name')
    history = History.objects.all()

    context = {
        'about_us' : about_us,
        'our_staff' : our_staff,
        'history': history,

    }

    return render(request, 'about/about.html', context)


