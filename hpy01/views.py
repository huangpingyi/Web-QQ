#
# @author huangpingyi
# coding;utf-8
from django.shortcuts import render,HttpResponseRedirect
from hpy01 import models
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import authenticate, login, logout
from hpy01.forms import ArticleForm
from  hpy01.models import UserProfilehpy
# Create your views here.


def index(request):

    articles = models.Articlehpy.objects.all()
    return render(request, 'index.htm', {'articles': articles})
#用render才能检测


def category(request, category_id):

    articles = models.Articlehpy.objects.filter(category_id=category_id)
    return render(request, 'index.htm', {'articles': articles})

def article_detail(request,article_id):
    try:
        article_obj = models.Articlehpy.objects.get(id=article_id)
    except ObjectDoesNotExist as e:
         return render(request, '404.html', {'err_msg': u'文章不存在！'})
    return render(request, 'article.html', {'article_obj': article_obj})
def acc_logout(request):
    logout(request)
    return HttpResponseRedirect('/')
#跳转首页
def acc_login(request):

    print(request.POST)
    err_msg = " "
    if request.method == "POST":
        print('user authention...')
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request,user)
            #生成session
            return HttpResponseRedirect('/')
        else:
            err_msg = "Wrong username or password!"
    return render(request, 'login.html', {'err_msg':err_msg})

def new_article(request):
    #选取板块p
    if request.method == 'POST':
        print(request.POST)
        form = ArticleForm(request.POST,request.FILES)
        if form.is_valid():
            print("---from data:", form.cleaned_data)
            form_data = form.cleaned_data
            form_data['author_id'] = UserProfilehpy.objects.create(user=request.user).id
            ############
            #form_data['author_id'] = request.user.userprofilehpy.id
            #form_data['author_id'] = request.user.id
            new_article_obj = models.Articlehpy(**form_data)
            #new_article_obj = models.Articlehpy.objects.create()
            #在后台创建完数据库后返回id,直接传字典进去
            new_article_obj.save()
            #返回新创建的文章上面
            return render(request, 'new_article.html', {'new_article_obj': new_article_obj})

        else:
            print("err:", form.errors)
    category_list = models.Category.objects.all()
    return render(request,'new_article.html', {'category_list': category_list})