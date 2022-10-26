from django.shortcuts import render, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404, redirect, reverse 
from django.http import HttpResponse
from .models import Project


def projects(request):
    projects = Project.objects.order_by('-created')

    paginator = Paginator(projects, 20)
    page_request_var = 'page'
    page = request.GET.get(page_request_var)
    try:
        paginated_queryset = paginator.page(page)
    except PageNotAnInteger:
        paginated_queryset = paginator.page(1)
    except EmptyPage:
        paginated_queryset = paginator.page(paginator.num_pages)

    context = {'projects' : projects,
       #         'queryset' : paginated_queryset,
                'page_request_var': page_request_var,
                }
    return render(request, 'projects/projects.html', context)


def project(request, id):
    project = get_object_or_404(Project, id=id)

    context = {'project' : project,
                         }
    return render(request, 'projects/single-project.html', context)

