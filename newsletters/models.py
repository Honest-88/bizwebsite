from django.db import models
from django.urls import reverse
from tinymce.models import HTMLField




class NewsLetters(models.Model):
    title = models.CharField(max_length=200)
    content = HTMLField()
    timestamp = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(blank=True, null=True, upload_to='letters/images')
    upload_letter = models.FileField(upload_to='letters/', blank=True)
    previous_post = models.ForeignKey('self', related_name='previous', on_delete=models.SET_NULL, blank=True, null=True)
    next_post = models.ForeignKey('self', related_name='next', on_delete=models.SET_NULL, blank=True, null=True)
    

    class Meta:
        verbose_name = ' News Letter'
        verbose_name_plural = 'News Letters'



    def __str__(self):
        return self.title

    
    def get_absolute_url(self):
        return reverse('newsletters:letters_detail', kwargs={
            'id': self.id
        })
