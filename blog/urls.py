from django.urls import path
from blog import views

#app_name = 'blog'

urlpatterns = [
    path("", views.IndexView.as_view(), name="main"),
    path("post/", views.PostListView.as_view(), name="post_list"),
    path("post/<slug>/", views.PostDetailView.as_view(), name="post_detail"),
    path("category/<slug>", views.CategoryListView.as_view(), name="category_list"),
    path("search/", views.SearchView.as_view(), name="search"),

]

