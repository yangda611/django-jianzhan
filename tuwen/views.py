import datetime
from django.db.models import Max
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import HttpResponse, Http404
from django.shortcuts import render
from django.views.decorators.cache import cache_page

from goods.models import Goods
from sx_cms.contexts import cache_time
from tuwen.models import TuWenCatalog, TuWen
from web import tuwen_list, tuwen_page


@cache_page(cache_time)
def tuwen_catalog(request, tuwen_c):
    try:
        t_c_obj = TuWenCatalog.objects.get(url=tuwen_c)
    except Exception as e:
        raise Http404

    tuwen_queryset = t_c_obj.tuwen_set.filter(tuwen_catalog=t_c_obj).order_by('-sort', '-id')

    data = []
    for item in tuwen_queryset:
        image_queryset = item.tuwenimage_set.filter(goods=item)
        lists = [item, image_queryset]
        data.append(lists)

    paginator = Paginator(data, 6)
    cur_page = request.GET.get('page', 1)
    try:
        page = paginator.page(cur_page)
    except PageNotAnInteger:
        page = paginator.page(1)
    except EmptyPage:
        page = paginator.page(paginator.num_pages)
    is_paginated = True if paginator.num_pages > 1 else False

    page_range = paginator.get_elided_page_range(cur_page, on_each_side=1, on_ends=0)
    t_c_queryset = TuWenCatalog.objects.order_by('-sort', '-id')

    tuwen_c_dict = {'page': page, 'paginator': paginator, 'page_range': page_range, 'is_paginated': is_paginated, 't_c_queryset': t_c_queryset, 't_c_obj': t_c_obj}

    tuwen_up = tuwen_queryset.aggregate(Max('updated_time'))['updated_time__max']
    if tuwen_up:
        tuwen_time = tuwen_up
    else:
        tuwen_time = datetime.datetime(1970, 1, 1)
    tuwen_c_dict['t_time'] = tuwen_time

    return render(request, tuwen_list, tuwen_c_dict)


@cache_page(cache_time)
def tuwen(request, tuwen_c, tuwen_p):
    try:
        t_c_obj=TuWenCatalog.objects.get(url=tuwen_c)
        tuwen_obj = TuWen.objects.get(url=tuwen_p)
    except Exception as e:
        raise Http404
    if t_c_obj.is_sitemap == 0 or tuwen_obj.is_sitemap == 0:
        raise Http404
    n_prev = TuWen.objects.filter(tuwen_catalog_id=t_c_obj, id__lt=tuwen_obj.id).order_by('-id')[:1]
    n_next = TuWen.objects.filter(tuwen_catalog_id=t_c_obj, id__gt=tuwen_obj.id).order_by('id')[:1]
    tuwen_dict = {'tuwen_obj': tuwen_obj,'t_c_obj':t_c_obj, 'n_prev': n_prev, 'n_next': n_next}
    t_tag = tuwen_obj.tuwen_tag.all()
    for item in t_tag:
        same_tag_goods = Goods.objects.filter(tuwen_tag=item).exclude(url=tuwen_p)[:4]
        tuwen_dict['same_tag_goods'] = same_tag_goods

        same_tag_tuwen = TuWen.objects.filter(tuwen_tag=item)[:10]
        tuwen_dict['same_tag_tuwen'] = same_tag_tuwen

    t_c_queryset = TuWenCatalog.objects.order_by('sort')
    tuwen_dict['t_c_queryset'] = t_c_queryset

    return render(request, tuwen_page, tuwen_dict)
