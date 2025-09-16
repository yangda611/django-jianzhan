import datetime
from django.db.models import Max
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import Http404
from django.shortcuts import render
from django.views.decorators.cache import cache_page

from goods.models import Goods
from news.models import NewsCatalog, News
from page.models import NewsTag
from sx_cms.contexts import cache_time
from web import news_list, news_page


@cache_page(cache_time)
def news_catalog(request, news_c):
    try:
        news_c_obj = NewsCatalog.objects.get(url=news_c)
    except Exception as e:
        raise Http404

    if news_c_obj.id == 17:
        news_queryset = News.objects.filter(news_catalog_id__in=[18,19]).order_by('-sort', '-id')
    else:
        news_queryset = news_c_obj.news_set.filter(news_catalog=news_c_obj).order_by('-sort', '-id')

    paginator = Paginator(news_queryset, 6)
    cur_page = request.GET.get('page', 1)
    currentPage = int(cur_page)
    if currentPage<0 or currentPage >  paginator.num_pages:
        raise Http404
    if paginator.num_pages < 4:
        pageRange = range(1, paginator.num_pages + 1)
    else:
        if currentPage - 2 < 1:
            pageRange = range(1, 5)
        elif currentPage + 1 == paginator.num_pages:
            pageRange = range(currentPage - 2, paginator.num_pages + 1)
        elif currentPage == paginator.num_pages:
            pageRange = range(currentPage - 3, paginator.num_pages + 1)
        else:
            pageRange = range(currentPage - 2, currentPage + 2)
    try:
        page = paginator.page(cur_page)
    except PageNotAnInteger:
        page = paginator.page(1)
    except EmptyPage:
        page = paginator.page(paginator.num_pages)
    is_paginated = True if paginator.num_pages > 1 else False

    n_c_queryset = NewsCatalog.objects.order_by('-sort', '-id')

    news_c_dict = {'page': page, 'paginator': paginator, 'page_range': pageRange, 'is_paginated': is_paginated,
                   'n_c_queryset': n_c_queryset, 'news_c_obj': news_c_obj, 'news_queryset': news_queryset}

    new_obj = news_queryset.aggregate(Max('updated_time'))['updated_time__max']
    if new_obj:
        new_time = new_obj
    else:
        new_time = datetime.datetime(1970, 1, 1)
    news_c_dict['n_time'] = new_time

    return render(request, news_list, news_c_dict)

@cache_page(cache_time)
def news(request, news_c, news_p):
    try:
        c = NewsCatalog.objects.get(url=news_c)
        p = News.objects.get(url=news_p)
    except Exception as e:
        raise Http404
    if p.is_sitemap == 0:
        raise Http404
    news_tj = News.objects.filter(is_topping=1).order_by('-id')[:5]
    n_prev = News.objects.filter(news_catalog_id=c, id__lt=p.id).order_by('-id')[:1]
    n_next = News.objects.filter(news_catalog_id=c, id__gt=p.id).order_by('id')[:1]
    news_dict = {'news_obj': p, 'news_c_obj': c, 'n_prev': n_prev, 'n_next': n_next, 'news_tj': news_tj}
    pb_tag = NewsTag.objects.filter().order_by('?')[:12]
    news_dict['pb_tag'] = pb_tag
    news_tag = p.news_tag.all()
    news_dict['news_tag'] = news_tag
    same_tag_news = News.objects.filter(news_tag__in=list(news_tag)).exclude(url=news_p)[:10]
    news_dict['same_tag_news'] = same_tag_news

    same_tag_goods = Goods.objects.filter(news_tag__in=list(news_tag)).order_by('-sort', '-updated_time')[:4]
    news_dict['same_tag_goods'] = same_tag_goods
    n_c_queryset = NewsCatalog.objects.order_by('sort')
    news_dict['n_c_queryset'] = n_c_queryset

    return render(request, news_page, news_dict)
