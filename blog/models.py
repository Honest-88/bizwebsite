from io import BytesIO
from django.core.files.storage import default_storage
from django.db import models
from django.shortcuts import reverse
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _
from PIL import Image
from django.contrib.auth import get_user_model
from tinymce.models import HTMLField

User = get_user_model()


class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField()

    def __str__(self):
        return self.user.username


class Category(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(_("Slug"), blank=True, null=True)

    class Meta:
        verbose_name = ' category'
        verbose_name_plural = 'catogories'


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        #Absolute URL for Post
        return reverse("category_list", kwargs={"slug": self.slug})



class Post(models.Model):
    title = models.CharField(max_length=200)
    content = HTMLField()
    timestamp = models.DateTimeField(auto_now_add=True)
    comment_count = models.IntegerField(default = 0)
    view_count = models.IntegerField(default = 0)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="blog/images")
    category = models.ManyToManyField(Category)
    featured = models.BooleanField()
    previous_post = models.ForeignKey('self', related_name='previous', on_delete=models.SET_NULL, blank=True, null=True)
    next_post = models.ForeignKey('self', related_name='next', on_delete=models.SET_NULL, blank=True, null=True)
    slug = models.SlugField(_("Slug"), blank=True, null=True)

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"


    def __str__(self):
        return self.title


    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"slug": self.slug})

    def get_update_url(self):
        return reverse('post_update', kwargs={"slug": self.slug})

    def get_delete_url(self):
        return reverse('post_delete', kwargs={"slug": self.slug}) 

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)
        # if self.image:
        #     img = Image.open(default_storage.open(self.image.name))
        #     if img.height > 1080 or img.width > 1920: # Pragma:no cover
        #         output_size = (1920, 1080)
        #         img.image(output_size)
        #         buffer = BytesIO()
        #         img.save(buffer, format="JPEG")
        #         default_storage.save(self.image.name, buffer)


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    reply = models.ForeignKey('Comment', null=True, related_name="replies", on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    content = models.TextField(max_length=500)
    post = models.ForeignKey('Post', related_name='comments', on_delete=models.CASCADE)


    class Meta:
        verbose_name = _("comment")
        verbose_name_plural = _("comments")


    def __str__(self):
        return '{}-{}'.format(self.post.title, str(self.user.username))



