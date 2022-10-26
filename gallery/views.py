from django.shortcuts import render
from .models import Green_Club, School_Gallery, Grade_R, Madrassa

def gallery(request):
    return render(request, 'gallery/gallery.html')


def green_club_gallery(request):
    green_club = Green_Club.objects.order_by('-timestamp')

    context = {
        'green_club' : green_club,
    }
    return render(request, 'gallery/green_club_gallery.html', context)


def school_gallery(request):
    school_gallery = School_Gallery.objects.order_by('-timestamp')
    context = {
        'school_gallery' : school_gallery,
    }
    return render(request, 'gallery/school_gallery.html', context)


def grade_r(request):
    grade_r = Grade_R.objects.order_by('-timestamp')
    context = {
        'grade_r' : grade_r,
    }
    return render(request, 'gallery/grade_r.html', context)


def madrassa(request):
    madrassa = Madrassa.objects.order_by('-timestamp')
    context = {
        'madrassa' : madrassa,
    }
    return render(request, 'gallery/madrassa.html', context)