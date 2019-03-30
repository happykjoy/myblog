from django.shortcuts import render
from django.http import HttpResponse
from .models import Article
from .models import Category,Banner,Tag,Link


def hello(request):
    return HttpResponse('Welcome to Django!!')

def index(request):
    banner = Banner.objects.filter(is_active = True)[0:4]
    tui = Article.objects.filter(tui_id = 8)[0:3]
    newarticle = Article.objects.all().order_by('-id')[0:8]
    hot = Article.objects.all().order_by('-views')[0:10]
    links = Link.objects.all()
    context = {
        'banner':banner,
        'tui':tui,
        'newarticle':newarticle,
        'hot':hot,
        'links':links,
    }
    return render(request,'index.html',context)

def list(request,lid):
    lists = Article.objects.filter(categary_id = lid)
    cname = Category.objects.get(id = lid)
    context = {
        'lists':lists,
        'cname':cname,
    }
    return render(request,'list.html',context)


def show(request,sid):
    show = Article.objects.get(id = sid)
    hot = Article.objects.all().order_by('?')[0:10]
    previous_blog = Article.objects.filter(created_time__gt=show.created_time,categary = show.categary.id).first()
    next_blog = Article.objects.filter(created_time__lt= show.created_time,categary = show.categary.id).last()
    show.views = show.views + 1
    show.save()
    return render(request,'show.html',locals())

from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
def tag(request,tag):
    list = Article.objects.filter(tags__name = tag)
    tname = Tag.objects.get(name = tag)
    page = request.GET.get('page')
    paginator = Paginator(list,2)
    try:
        list = paginator.page(page)  # 获取当前页码的记录
    except PageNotAnInteger:
        list = paginator.page(1)  # 如果用户输入的页码不是整数时,显示第1页的内容
    except EmptyPage:
        list = paginator.page(paginator.num_pages)  # 如果用户输入的页数不在系统的页码列表中时,显示到最后一页的内容
    print(list)
    return render(request,'tag.html',locals())


def search(request):
    ss = request.GET.get('search')
    list = Article.objects.filter(title__icontains=ss)
    page = request.GET.get('page')
    paginator = Paginator(list,10)
    try:
        list = paginator.page(page)
    except PageNotAnInteger:
        list = paginator.page(1)
    except EmptyPage:
        list = paginator.page(paginator.num_pages)
    return render(request,'search.html',locals())

def about(request):
    recomment = Article.objects.all()[0:6]
    return render(request,'page.html',locals())

def global_variable(request):
    allcategory = Category.objects.all()
    tags = Tag.objects.all()
    recomment = Article.objects.filter(tui__id = 8)[0:6]
    return locals()