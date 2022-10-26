from django.db.models import Count, Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404, redirect, reverse 
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from .forms import CommentForm, PostForm
from .models import Post, Comment, Author, Category
from home_page.models import Slider, Welcome, Our_Mission, Mid_Page, Impression, Testimonials
from projects.models import Project
from django.views.generic import (CreateView, DeleteView, DetailView, ListView, UpdateView, View)


def get_author(user):
    qs = Author.objects.filter(user=user)
    if qs.exists():
        return qs[0]
    return None


class SearchView(View):
    def get(self, request, *args, **kwargs):
        q = request.GET.get("q", "")
        search_result = Post.objects.filter(
            Q(title__icontains=q) | Q(overview__icontains=q)
        ).all()
        context = {"search_result": search_result}
        return render(request, "search_results.html", context=context)


class CategoryListView(ListView):
    def get(self, request, *args, **kwargs):
        category_posts = Post.objects.order_by("-timestamp")[0:4]
        
        context = {"category_posts": category_posts}
        return render(request, "category_list.html", context=context)


class IndexView(View):
    def get(self, request, *args, **kwargs):
        latest_posts = Post.objects.order_by("-timestamp")[0:3]
        recent_projects = Project.objects.order_by("-created")[0:6]

        testimonials = Testimonials.objects.all()
        sliders = Slider.objects.all()
        welcome = Welcome.objects.all()
        our_mission = Our_Mission.objects.all()
        mid_page = Mid_Page.objects.all()
        impression = Impression.objects.all()

        context = {
            "latest_posts": latest_posts,
            "recent_projects": recent_projects,
            "testimonials": testimonials,
            "sliders": sliders,
            "welcome": welcome,
            "our_mission": our_mission,
            "mid_page": mid_page,
            "impression": impression,
            }
        return render(request, "main.html", context=context)


class PostListView(ListView):
    model = Post
    template_name = "post/post_list.html"
    paginate_by = 18

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["latest_posts"] = Post.objects.all().order_by("-timestamp")[0:3]
        context["categories"] = Category.objects.all()
        return context


class PostDetailView(DetailView):
    model = Post
    template_name = "post/post_detail.html"
    _comment_form = CommentForm()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["latest_posts"] = Post.objects.all().order_by("-timestamp")[0:4]
        context["categories"] = Category.objects.all()
        context["comment_form"] = self._comment_form
        return context

    def post(self, request, *args, **kwargs):
        _post = self.get_object()
        _comment_form = CommentForm(request.POST)
        if _comment_form .is_valid():
            _comment_form.instance.user = request.user.author
            _comment_form.instance.post = _post
            _comment_form.save()
            return redirect(_post)


