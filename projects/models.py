from django.db import models
from django.db import models
from embed_video.fields import EmbedVideoField
from tinymce.models import HTMLField
from django.shortcuts import reverse

class  Project(models.Model):
    heading = models.CharField(max_length=500, null=True, blank=True)
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to="project/images", null=True, blank=True)
    video = EmbedVideoField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    description = HTMLField(null=True, blank=True)
    previous_project = models.ForeignKey('self', related_name='previous', on_delete=models.SET_NULL, blank=True, null=True)
    next_project = models.ForeignKey('self', related_name='next', on_delete=models.SET_NULL, blank=True, null=True)
    

    def __str__(self):
        return self.title


    def get_absolute_url(self):
        return reverse('projects:project', kwargs={
            'id': self.id
    })






