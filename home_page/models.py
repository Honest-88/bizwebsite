from django.db import models


class  Slider(models.Model):
    title = models.CharField(max_length=200, null=True, blank=True)
    image_one = models.ImageField(upload_to='images/', null=True, blank=True)
    tagline_one = models.TextField(max_length=200, null=True, blank=True)
    tagline_two = models.CharField(max_length=200, null=True, blank=True)

    title_one = models.CharField(max_length=200, null=True, blank=True)
    image_two = models.ImageField(upload_to='images/', null=True, blank=True)
    tagline_three = models.TextField(max_length=200, null=True, blank=True)
    tagline_four = models.CharField(max_length=200, null=True, blank=True)

    title_two = models.CharField(max_length=200, null=True, blank=True)
    image_three = models.ImageField(upload_to='images/', null=True, blank=True)
    tagline_five = models.TextField(max_length=200, null=True, blank=True)
    tagline_six = models.CharField(max_length=200, null=True, blank=True)

   
    class Meta:
        verbose_name = 'Sliders'
        verbose_name_plural = 'Sliders'

    def __str__(self):
        return self.title

class Welcome(models.Model):
    title = models.CharField(max_length=200, null=True, blank=True)
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    tagline_one = models.CharField(max_length=200, null=True, blank=True)
    content = models.TextField(max_length=500, null=True, blank=True)
    application_form = models.FileField(upload_to='applications', null=True, blank=True)

    class Meta:
        verbose_name = 'Welcome'
        verbose_name_plural = 'Welcome'

    def __str__(self):
        return self.title

class Our_Mission(models.Model):
    title = models.CharField(max_length=200, null=True, blank=True)
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    tagline_one = models.TextField(max_length=500, null=True, blank=True)
    tagline_two = models.TextField(max_length=500, null=True, blank=True)
    tagline_three = models.TextField(max_length=500, null=True, blank=True)
    tagline_four = models.TextField(max_length=500, null=True, blank=True)
    tagline_five = models.TextField(max_length=500, null=True, blank=True)
    pass_rate = models.CharField(max_length=200, null=True, blank=True)
    achievements = models.CharField(max_length=500, null=True, blank=True)

    class Meta:
        verbose_name = 'Our Mission'
        verbose_name_plural = 'Our Mission'

    def __str__(self):
        return self.title


class Mid_Page(models.Model):
    title = models.CharField(max_length=300, null=True, blank=True)
    description_one = models.TextField(max_length=500, null=True, blank=True)
    heading_one = models.CharField(max_length=300, null=True, blank=True)

    description_two = models.TextField(max_length=500, null=True, blank=True)
    heading_two = models.CharField(max_length=300, null=True, blank=True)
    description_three = models.TextField(max_length=500, null=True, blank=True)
    heading_three = models.CharField(max_length=300, null=True, blank=True)
    description_four = models.TextField(max_length=500, null=True, blank=True)
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    
    class Meta:
        verbose_name = 'Mid Page Image'
        verbose_name_plural = 'Mid Page Image'

    def __str__(self):
        return self.title


class Impression(models.Model):
    title = models.CharField(max_length=200, null=True, blank=True)
    content = models.TextField(max_length=500, null=True, blank=True)
    application_form = models.FileField(upload_to='Application', blank=True)

    class Meta:
        verbose_name = 'Impression'
        verbose_name_plural = 'Impressions'

    def __str__(self):
        return self.title


class Testimonials(models.Model):
    person_name = models.CharField(max_length=500, null=True, blank=True)
    title = models.CharField(max_length=200, null=True, blank=True)
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    testimony = models.TextField(max_length=500, null=True, blank=True)
    

    class Meta:
        verbose_name = 'Testimonial'
        verbose_name_plural = 'Testimonials'

    def __str__(self):
        return self.person_name
