from django.shortcuts import render
from . models import NewsLetters
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger



def newsletters(request):
    news_letters = NewsLetters.objects.order_by('-timestamp')

    paginator = Paginator(news_letters, 12)
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
        'news_letters' : news_letters ,
    }
    return render(request, 'letters/letters_list.html', context)




def letters(request, id):
    news_letters = get_object_or_404(NewsLetters, id=id)

    context = {
        'news_letters': news_letters,
        
    }
    return render(request, 'letters/letters_detail.html', context)



