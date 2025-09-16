from django.shortcuts import render

from goods.models import Goods
from news.models import News


def search(request):
    search_list = ['name__contains', 'content__contains', 'keywords__contains']
    search_value = request.POST.get('q', '')
    from django.db.models import Q
    conn = Q()
    conn.connector = 'OR'
    if search_value:
        for item in search_list:
            conn.children.append((item, search_value))
    goods_search = Goods.objects.filter(conn)
    news_search = News.objects.filter(conn)
    search_data = [goods_search, news_search]
    return render(request, 'search.html', {'search_data': search_data, "search_value": search_value})
