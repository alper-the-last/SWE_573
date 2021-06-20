from django.shortcuts import render
import urllib
import requests
import urllib.request

from django.db.models import Q
from django.core.paginator import Paginator

from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.contrib.postgres.search import *
from django.contrib.auth import *

from django.contrib import messages


# Create your views here.
def Home(request):
    return render(request, "search-results.html")


def retrieve_article_data(request, pk):
    article = Article.objects.get(PMID=pk)

    return render(request, "article.html", {"article": article})


def Results(request):
    form = SearchForm()
    q = ''
    results = []

    if 'q' in request.GET:
        form = SearchForm(request.GET)
        print("results started")
        if form.is_valid():
            q = form.cleaned_data['q']

            # order by ID to retrieve the most recent article first as I stored the
            # articles_in_db = Article.objects.order_by("-id")
            articles_in_db = Article.objects
            # results = articles_in_db.filter(Q(ArticleTitle__icontains=q))

            # results = articles_in_db.filter(ArticleTitle=q)

            vector = SearchVector("ArticleKeywords", weight='A') + \
                     SearchVector("ArticleTitle", weight='B') + \
                     SearchVector("AbstractText", weight='C')

            query = SearchQuery(q)

            results = articles_in_db.annotate(search=SearchVector("ArticleTitle", "AbstractText", "ArticleKeywords"), ).filter(search=q)

            # results = articles_in_db.annotate(rank=SearchRank(vector, query, cover_density=True)).order_by('-rank').filter(search=query)



        print("results finished")
        print(len(results))
    return render(request, "search-results.html", {"form": form, 'q': q, 'results': results})


def registerPage(request):
    form = createUserForm()

    if request.method == 'POST':
        form = createUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account successfully created")
            return redirect('Login')

    return render(request, 'register.html', {"form": form})


def loginPage(request):
    if request.method == 'POST':
        # get user input for username and password fields
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('Results')
        else:
            messages.info(request, 'username or password is incorrect!')

    return render(request, 'login.html', {})


def logoutPage(request):
    logout(request)
    return redirect('Login')