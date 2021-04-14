from django.shortcuts import render, HttpResponse, redirect
from django.db.models import Q
from .models import Article, Author


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

def edit_article(request, pk):
    article = Article.objects.get(id=pk)

    if request.method == "POST":
        article.title = request.POST.get("title")
        article.text = request.POST.get("text")
        article.save()
        return redirect(article_page, pk)
    return render (request, "update.html", {"article": article})

def add_article(request):
    if request.method == "GET":
        return render(request, "add.html")
    elif request.method == "POST":
        form = request.POST
        title = form.get("title")
        text = form.get("text")
        
        # new_article = Article(title=title, text=text)
        # new_article.save()

        new.article = Article()
        new_article.title = title
        new_article.text = text
        user = request.user
        author = user.author

        new_article.save()
        return redirect(article_page, new_article.pk)
        

def delete_article(request, id):
    article = Article.object.get(pk=id)
    article.delete()