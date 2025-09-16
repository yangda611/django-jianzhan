from django.http import Http404
from django.shortcuts import render
from django.views.decorators.cache import cache_page

from page.models import Page
from sx_cms.contexts import cache_time
from tuwen.models import TuWen
from web import single_page, single_page_01, contact


@cache_page(cache_time)
def page(request, page_item):
    try:
        page_obj = Page.objects.get(url=page_item)
    except Exception as e:
        raise Http404
    page_dict = {'page_obj': page_obj}

    strength_List = TuWen.objects.filter(tuwen_catalog=15).order_by('-sort', '-created_time', '-id')[:8]
    page_dict['strength_List'] = strength_List

    honorary_List = TuWen.objects.filter(tuwen_catalog=14).order_by('-sort', '-created_time', '-id')[:8]
    page_dict['honorary_List'] = honorary_List

    p_time = page_obj.updated_time
    if p_time:
        p_time = p_time
    else:
        p_time = datetime.datetime(1970, 1, 1)
        page_dict['p_time'] = p_time
    if page_obj.id == 12:
        return render(request, single_page_01, page_dict)
    elif page_obj.id == 13:
        return render(request, contact, page_dict)
    elif page_obj.id == 14:
        return render(request, 'single_server.html', page_dict)
    else:
        return render(request, single_page, page_dict)
