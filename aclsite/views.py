from django.http import Http404
from django.shortcuts import render

from .models import Article
# Create your views here.

def index(request):
    latest_article_list = Article.objects.order_by('-pub_date')[:5]
    context = {'latest_article_list': latest_article_list}
    return render(request, 'aclsite/index.html', context)

def details(request, article_id):
    try:
        article = Article.objects.get(pk=article_id)
        detail = article.description
    except Article.DoesNotExist:
        raise Http404('Article does not exist')
    return render(request, 'aclsite/detail.html', {
        'article': article,
        'detail': detail
        })

def content(request, article_id):
    article = Article.objects.get(pk=article_id)
    title = article.title
    content = article.content
    return render(request, 'aclsite/content.html', {
        'title': title,
        'content': content 
        })
