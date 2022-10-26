from django.db import models


class  Slider(models.Model):
    tagline_one = models.CharField(max_length=200, null=True, blank=True)
    tagline_two = models.CharField(max_length=200, null=True, blank=True)
    tagline_three = models.CharField(max_length=200, null=True, blank=True)
    tagline_four = models.CharField(max_length=200, null=True, blank=True)

    tagline_five = models.CharField(max_length=200, null=True, blank=True)
    tagline_six = models.CharField(max_length=200, null=True, blank=True)
    tagline_seven = models.CharField(max_length=200, null=True, blank=True)
    tagline_eight = models.CharField(max_length=200, null=True, blank=True)

    tagline_nine = models.CharField(max_length=200, null=True, blank=True)
    tagline_ten = models.CharField(max_length=200, null=True, blank=True)
    tagline_eleven = models.CharField(max_length=200, null=True, blank=True)
    tagline_twelve = models.CharField(max_length=200, null=True, blank=True)

    image_one = models.ImageField(upload_to='images/', null=True, blank=True)
    image_two = models.ImageField(upload_to='images/', null=True, blank=True)
    image_three = models.ImageField(upload_to='images/', null=True, blank=True)
    image_four = models.ImageField(upload_to='images/', null=True, blank=True)
    image_five = models.ImageField(upload_to='images/', null=True, blank=True)

    class Meta:
        verbose_name = 'Sliders'
        verbose_name_plural = 'Sliders'

    def __str__(self):
        return self.tagline_one

class Our_Mission(models.Model):
    title = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField(max_length=500, null=True, blank=True)


    class Meta:
        verbose_name = 'Our Mission'
        verbose_name_plural = 'Our Mission'

    def __str__(self):
        return self.title


class Our_Activities(models.Model):
    heading = models.CharField(max_length=200, null=True, blank=True)
    title_one = models.CharField(max_length=200, null=True, blank=True)
    title_two = models.CharField(max_length=200, null=True, blank=True)
    description_one = models.TextField(max_length=500, null=True, blank=True)
    description_two = models.TextField(max_length=500, null=True, blank=True)


    
    class Meta:
        verbose_name = 'Our Activities'
        verbose_name_plural = 'Our Activities'

    def __str__(self):
        return self.heading

class Our_Classes(models.Model):
    title = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField(max_length=500, null=True, blank=True)

    
    class Meta:
        verbose_name = 'Our Class'
        verbose_name_plural = 'Our Class'

    def __str__(self):
        return self.title

class Images(models.Model):
    title = models.CharField(max_length=200, null=True, blank=True)
    image_one = models.ImageField(upload_to='images/', null=True, blank=True)
    image_two = models.ImageField(upload_to='images/', null=True, blank=True)
    image_three = models.ImageField(upload_to='images/', null=True, blank=True)
    

    class Meta:
        verbose_name = 'Images'
        verbose_name_plural = 'Images'

    def __str__(self):
        return self.title



