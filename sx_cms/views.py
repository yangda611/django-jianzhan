import datetime
from django.db.models import Max
from django.http import HttpResponse
from django.shortcuts import render

from goods.models import Goods
from links.models import Links
from news.models import News
from page.models import Page
from slide_set.models import PCSlide
from sx_cms import search
from tuwen.models import TuWen
from web import index
from django.views.decorators.cache import cache_page
from sx_cms.contexts import cache_time


@cache_page(cache_time)
def home(request):
    home_dict = {}

    pro_list = Goods.objects.filter().order_by('-sort', '-created_time')[:8]
    home_dict['pro_list'] = pro_list

    new_list = News.objects.filter(news_catalog=18).order_by('-sort', '-created_time')[:3]
    home_dict['new_list'] = new_list

    new_list1 = News.objects.filter(news_catalog=19).order_by('-sort', '-created_time')[:4]
    home_dict['new_list1'] = new_list1

    case_List = TuWen.objects.filter(tuwen_catalog=13).order_by('-sort', '-created_time', '-id')[:4]
    home_dict['case_List'] = case_List

    about_us = Page.objects.get(id=12)
    home_dict['about_us'] = about_us
    link_queryset = Links.objects.all()
    home_dict['link_queryset'] = link_queryset
    pc_queryset = PCSlide.objects.order_by('sort')
    home_dict['pc_queryset'] = pc_queryset

    search_value = request.GET.get('q', '')
    if search_value:
        return search.search(request)

    sjn_time = new_list.aggregate(Max('updated_time'))['updated_time__max']
    if sjn_time:
        new_time = sjn_time
    else:
        new_time = datetime.datetime(1970, 1, 1)

    index_time = new_time
    home_dict['index_time'] = index_time
    home_dict['h_name'] = 1

    return render(request, index, home_dict)

def sitemap(request):
    sitemap_dict = {}
    return render(request, 'sitemap.html', sitemap_dict)
