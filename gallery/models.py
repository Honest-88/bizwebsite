from django.db import models
from django.urls import reverse


class Green_Club(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='gallery/club')
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Green Club '
        verbose_name_plural = 'Green Club'


    def __str__(self):
        return self.title


class School_Gallery(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='gallery/school')
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'School_Gallery'
        verbose_name_plural = 'School_Gallery'


    def __str__(self):
        return self.title


class Grade_R(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='gallery/school')
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Grade_R'
        verbose_name_plural = 'Grade_R'


    def __str__(self):
        return self.title


class Madrassa(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='gallery/Madrassa')
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Madrassa'
        verbose_name_plural = 'Madrassa'


    def __str__(self):
        return self.title