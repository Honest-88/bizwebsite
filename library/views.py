


from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.http import HttpResponseRedirect
from .models import *


def library(request):
    library_list = Library.objects.order_by('-timestamp')

    paginator = Paginator(library_list, 6)
    page_request_var = 'page'
    page = request.GET.get(page_request_var)
    try:
        paginated_queryset = paginator.page(page)
    except PageNotAnInteger:
        paginated_queryset = paginator.page(1)
    except EmptyPage:
        paginated_queryset = paginator.page(paginator.num_pages)


    context = {
        'queryset' : paginated_queryset,
        'page_request_var': page_request_var,

    }
    return render(request, 'lib/library.html', context)


def library_detail(request, id):
    library_detail = get_object_or_404(Library, id=id)

    context = {
        'library_detail': library_detail,
        
    }
    return render(request, 'lib/library_detail.html', context)
