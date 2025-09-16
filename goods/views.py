from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
import datetime
from django.db.models import Max
from django.http import Http404, HttpResponse
from django.shortcuts import render
from django.views.decorators.cache import cache_page

from goods.models import GoodsCatalog, Goods
from news.models import NewsCatalog, News
from sx_cms.contexts import cache_time

from tuwen.models import TuWenCatalog, TuWen
from web import goods_list, goods_page


@cache_page(cache_time)
def goods_catalog(request, goods_c):
    try:
        goods_c_obj = GoodsCatalog.objects.get(url=goods_c)
    except Exception:
        raise Http404
        
    g_c = GoodsCatalog.objects.filter(category=goods_c_obj.id).values("id").order_by('-sort', '-id')
    if g_c:
        g_list = Goods.objects.filter(goods_catalog__in=g_c).order_by('-sort', '-created_time')
    else:
        g_list = Goods.objects.filter(goods_catalog=goods_c_obj).order_by('-sort', '-created_time')

    paginator = Paginator(g_list, 12)
    cur_page = request.GET.get('page', 1)
    try:
        page = paginator.page(cur_page)
    except PageNotAnInteger:
        page = paginator.page(1)
    except EmptyPage:
        page = paginator.page(paginator.num_pages)
    is_paginated = True if paginator.num_pages > 1 else False

    page_range = paginator.get_elided_page_range(cur_page, on_each_side=1, on_ends=0)

    goods_c_dict = {'page': page, 'paginator': paginator, 'page_range': page_range, 'is_paginated': is_paginated, 'goods_c_obj': goods_c_obj, 'g_list': g_list}

    pxg_news = News.objects.filter().order_by('-sort', '-id')[:8]
    goods_c_dict['pxg_news'] = pxg_news

    good_up = g_list.aggregate(Max('updated_time'))['updated_time__max']
    if good_up:
        good_time = good_up
    else:
        good_time = datetime.datetime(1970, 1, 1)
    goods_c_dict['g_time'] = good_time

    if goods_c_obj.id == 31:
        return render(request, 'goods_catalog01.html', goods_c_dict)
    else:
        return render(request, goods_list, goods_c_dict)


@cache_page(cache_time)
def goods(request, goods_c, goods_p):
    try:
        g_p = GoodsCatalog.objects.get(url=goods_c)
        goods_obj = Goods.objects.get(url=goods_p)
    except Exception:
        raise Http404
    if goods_obj.is_sitemap == 0:
        raise Http404
    n_prev = Goods.objects.filter(goods_catalog_id=g_p, id__lt=goods_obj.id).order_by('-id')[:1]
    n_next = Goods.objects.filter(goods_catalog_id=g_p, id__gt=goods_obj.id).order_by('id')[:1]
    goods_dict = {'goods_obj': goods_obj, 'goods_c_obj': g_p, 'n_prev': n_prev, 'n_next': n_next}
    p_tag = goods_obj.goods_tag.all()
    for item in p_tag:
        same_tag_goods = Goods.objects.filter(goods_tag=item).exclude(url=goods_p)[:4]
        goods_dict['same_tag_goods'] = same_tag_goods

        same_tag_news = News.objects.filter(goods_tag=item)[:10]
        goods_dict['same_tag_news'] = same_tag_news

        same_tag_tuwen = TuWen.objects.filter(goods_tag=item)[:4]
        goods_dict['same_tag_tuwen'] = same_tag_tuwen

    g_c_queryset = GoodsCatalog.objects.order_by('sort')
    goods_dict['g_c_queryset'] = g_c_queryset
    
    p_xgcp = Goods.objects.filter(goods_catalog=goods_obj.goods_catalog_id).exclude(id=goods_obj.id).order_by('-sort', '-created_time')[:6]
    goods_dict['p_xgcp'] = p_xgcp

    return render(request, goods_page, goods_dict)
