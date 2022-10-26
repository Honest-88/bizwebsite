from django.db import models



class About_Us(models.Model):
    title = models.CharField(max_length=200, null=True, blank=True)
    director_welcome = models.TextField(max_length=5000, null=True, blank=True)
    image_one = models.ImageField(upload_to='images/', null=True, blank=True)

    
    class Meta:
        verbose_name = 'About Us'
        verbose_name_plural = 'About Us'

    def __str__(self):
        return self.title


class History(models.Model):
    title = models.CharField(max_length=200, null=True, blank=True)
    content_one = models.TextField(max_length=5000, null=True, blank=True)

    title_one = models.CharField(max_length=5000, null=True, blank=True)
    content_two = models.TextField(max_length=5000, null=True, blank=True)

    title_two = models.CharField(max_length=5000, null=True, blank=True)
    content_three = models.TextField(max_length=5000, null=True, blank=True)

    title_three = models.CharField(max_length=5000, null=True, blank=True)
    content_four = models.TextField(max_length=5000, null=True, blank=True)
    image_one = models.ImageField(upload_to='images/', null=True, blank=True)


    
    
    class Meta:
        verbose_name = 'Brief History'
        verbose_name_plural = 'Brief History'

    def __str__(self):
        return self.title


class Our_Staff(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    role = models.CharField(max_length=200, null=True, blank=True)
    image_one = models.ImageField(upload_to='images/', null=True, blank=True)
    
    
    class Meta:
        verbose_name = 'Our Staff'
        verbose_name_plural = 'Our Staff'

    def __str__(self):
        return self.name