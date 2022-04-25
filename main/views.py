from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from .models import *
from .forms import comment_form,create_article, update_profile


def index(request):
    context = {
        'title': 'Главная'
    }
    return render(request,'main/index.html', context = context)


def user_reg(request):
    data = {}

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            data['form'] = form
            return render(request, 'main/reg_user.html', data)
    else:
        form = UserCreationForm()
        data['form'] = form
        return render(request, 'main/reg_user.html', data)


def news(request):
    post = article.objects.all()

    context = {
        'post': post
    }
    return render(request, 'main/news.html', context = context)


def article_show(request, article_id):
    article_ = article.objects.filter(id=article_id)
    comment = reversed(comments.objects.filter(article_name_id=article_id))
    if request.method == 'POST':
        form = comment_form(request.POST)
        context = {
            'article': article_,
            'title': 'article',
            'comment': comment,
            'form': form,
        }
        if form.is_valid():
            comment = form.save(commit = False)
            comment.author = request.user
            comment.article_name_id = article_id
            comment.save()
            return render(request, 'main/article.html', context=context)

    else:
        form = comment_form()

        context = {
            'article': article_,
            'title': 'article',
            'comment': comment,
            'form': form,
        }
        return render(request, 'main/article.html', context=context)


def profile(request, user_id):
    user = User.objects.filter(id=user_id)
    article_ = article.objects.filter(author_id=user_id)
    user_profile_id = user_profile.objects.filter(User_id=user_id)
    context = {
        'user' : user,
        'article' : article_,
        'profile' : user_profile_id
    }
    return render(request, 'main/profile.html',context = context)


def create_new_article(request):
    if request.method == 'POST':
        form = create_article(request.POST, request.FILES)

        if form.is_valid():
            article = form.save(commit = False)
            article.author = request.user
            article.save()
            return render(request,'main/index.html')
    else:
        form = create_article()
        return render(request,'main/create_article.html',{'form': form})


def update_profiles(request, user_id):
    if request.method == 'POST':
        form = update_profile(request.POST, request.FILES)
        context = {
            'title': 'article',
            'form': form,
        }
        if form.is_valid():
            profile = form.save(commit = False)
            profile.User = request.user
            profile.about = request.about
            profile.photo = request.photo
            profile.save()
            return render(request, 'main/profile.html', context=context)
    else:
        form = update_profile()
        return render(request,'main/update_profile.html',{'form': form})

