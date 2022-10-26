from django.contrib import admin
from .models import Project
from embed_video.admin import AdminVideoMixin


class MyModelAdmin(AdminVideoMixin, admin.ModelAdmin):
    pass

admin.site.register(Project, MyModelAdmin)

