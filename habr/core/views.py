from django.shortcuts import render, HttpResponse, redirect
from django.db.models import Q
from .models import Article, Author
# from django.views.generic import #Templateview


# Create your views here.

def article_page(request, id):
    article = Article.objects.get(id=id)
    article.views += 1
    article.save()
    return render(
        request,
        'article.html',
        {'article':article}
    )

def edit_article(request, pk):
    article = Article.objects.get(id=pk)

    if request.method == "POST":
        title = request.POST.get("title")
        text = request.POST.get("text")
        article.title = title
        article.text = text
        article.save()
        return redirect(article_page, pk)
    return render (request, "update.html", {"article": article})


def add(request):
    if request.method == "GET":
        return render(request, "add_article.html")
    elif request.method == "POST":
        form = request.POST
        title = form.get("title")
        text = form.get("text")

        
        # new_article = Article(title=title, text=text)
        # new_article.save()

        new_article = Article()
        new_article.title = title
        new_article.text = text
        user = request.user

        if user.is_authenticated:
            if not Author.objects.filter(user=user).exists():
                author = Author(user=user, nik=user.username)
                author.save()
            author = user.author
            new_article.author = author
        
        new_article.save()
        return redirect(article_page, new_article.pk)


# def article_form(request):
#     context = {}
    
#     if request.method == 'POST':
#         form = ArticleForm(request.POST, requset.FILES)
#         if form.is_valid():
#             article = form.save()
#             return redirect(article_page, article_id)

#     form = ArticleForm()
#     context["form"] = form
#     return render(request, "form.html", context)
        

def delete_article(request, id):
    article = Article.objects.get(pk=id)
    article.delete()
    return HttpResponse('???????????? ??????????????')

def articles(request):
    articles = Article.objects.filter(is_active = True)
    return render(request, "articles.html", {"articles":articles})

def authors(request):
    authors = Author.objects.all()
    return render(request, "authors.html", {"authors":authors})

def about(request):
    return render(request, 'about.html')

def hide_article(request, id):
    article = Article.objects.get(pk=id)
    article.is_active = False
    article.save()
    return redirect(articles)


# class TestView(TemplateView):
#     template_name = "test.html" 

def search(request):
    word = request.GET.get('word')
    articles = Article.objects.filter (Q (title__icontains = word) | Q(text__icontains = word), 
                                      is_active=True)
    return render(request, 'articles.html', {'articles':articles})