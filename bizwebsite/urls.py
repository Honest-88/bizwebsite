from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from blog import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.IndexView.as_view(), name="main"),
    path('blog/', include('blog.urls')),
    path('projects/', include('projects.urls')),
    path('newsletters/', include('newsletters.urls')),
    path('madrassa/', include('madrassa.urls')),
    path('gallery/', include('gallery.urls')),
    path('application/', include('application.urls')),
    path('library/', include('library.urls')),
    path('grade_r/', include('grade_r.urls')),
    path('about/', include('about.urls')),

    path('tinymce/', include('tinymce.urls')),
    
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


admin.site.site_header = "Mayfair Academy AdminPanel"
admin.site.site_title = "Mayfair Academy App Admin"
admin.site.site_index_title = "Welcome To Mayfair Academy Admin Panel"

