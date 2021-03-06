from django.shortcuts import render, HttpResponse
from .models import Article

# Create your views here.
def homepage(request):
    # return HttpResponse('<h2>Hello world!<h2>')
    return render(request, 'index.html')

def first_article(request):
    article = Article.objects.first()
    return render(
        request,
        'article_page.html',
        {'article':article}
    )