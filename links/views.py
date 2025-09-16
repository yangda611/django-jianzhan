

import re
from django.shortcuts import render

from goods.models import Goods
from links.models import Mode, LinkInner
from news.models import News
from tuwen.models import TuWen


def inner_link(request):
    one = Goods.objects.all()
    two = News.objects.all()
    three = TuWen.objects.all()

    lists = []

    for item in one:
        a1_lst = []
        a1_lst.append(item.name)
        url_host = request.get_host()
        url_postfix = '/' + item.c_url + '/' + item.url + '.html'
        url = url_host + url_postfix
        a1_lst.append(url)
        if '</a>' in item.content:
            result = re.findall(r'<a\b[^>]+\bhref="([^"]*)"[^>]*>([\s\S]*?)</a>', item.content)
            for i in range(len(result)):
                if '>' in result[i][1]:
                    res = re.findall('[\u4e00-\u9fa5]+', result[i][1])
                    item = (result[i][0], res[0])
                    result[i] = item

            a1_lst.append(result)
        else:
            a1_lst.append([])
        lists.append(a1_lst)

    for items in two:
        lst = []
        lst.append(items.name)
        url_host = request.get_host()
        url_postfix = '/' + 'a' + '/' + items.c_url + '/' + items.url + '.html'
        url = url_host + url_postfix
        lst.append(url)
        if '</a>' in items.content:
            result = re.findall(r'<a\b[^>]+\bhref="([^"]*)"[^>]*>([\s\S]*?)</a>', items.content)
            for i in range(len(result)):
                if '>' in result[i][1]:
                    res = re.findall('[\u4e00-\u9fa5]+', result[i][1])
                    item = (result[i][0], res[0])
                    result[i] = item
            lst.append(result)
        else:
            lst.append([])
        lists.append(lst)

    for items in three:
        lst = []
        lst.append(items.name)
        url_host = request.get_host()
        url_postfix = '/' + 'c' + '/' + items.c_url + '/' + items.url + '.html'
        url = url_host + url_postfix
        lst.append(url)
        if '</a>' in items.content:
            result = re.findall(r'<a\b[^>]+\bhref="([^"]*)"[^>]*>([\s\S]*?)</a>', items.content)
            for i in range(len(result)):
                if '>' in result[i][1]:
                    res = re.findall('[\u4e00-\u9fa5]+', result[i][1])
                    item = (result[i][0], res[0])
                    result[i] = item
            lst.append(result)
        else:
            lst.append([])
        lists.append(lst)

    if Mode.objects.filter():
        links = Mode.objects.filter()
        links.delete()

    for i in range(len(lists)):
        num = 0
        for ii in range(len(lists)):
            if i == ii:
                continue
            if lists[i][1] in str(lists[ii][2]):
                num += 1

        Mode.objects.create(name=lists[i][0], url=lists[i][1], number=len(lists[i][2]), vote_number=num,
                            content=lists[i][2])

    obj = Mode.objects.all()
    for item in obj:
        for items in lists:
            for inner in items[2]:
                if item.url in inner[0]:
                    LinkInner.objects.create(vote_url=items[1], vote_keyword=inner[1], name=items[0], mode=item)

    return render(request, "admin/links.html")
