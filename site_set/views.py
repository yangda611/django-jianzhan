import datetime
import re
import urllib
import urllib.request

import pymysql
import requests
from django.core.cache import caches
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render
from site_set.baidu_ts import BaiduTS
from site_set.models import MinGan, Site, BaiduFanHuiZhi


def site_set(request, site):
    pass


def get_ban_keyword_page(request):
    return render(request, "admin/get_mingan.html")

def ban_keyword(request):
    kwargs = {
        'host': '122.114.165.105',
        'port': 3306,
        'user': 'sxerp_sxglpx_com',
        'password': '6HPYTwB5p2rAwHTE',
        'database': 'sxerp_sxglpx_com',
        'charset': 'utf8'
    }
    db = pymysql.connect(**kwargs)
    cur = db.cursor()

    sql = "select name from web_nokeyword;"
    cur.execute(sql)
    all_in = cur.fetchall()

    if MinGan.objects.filter():
        mgc = MinGan.objects.filter()
        mgc.delete()

    for item in all_in:
        MinGan.objects.create(name=item[0])

    cur.close()
    db.close()

    return render(request, "admin/mingan.html")


def all_tui(request):
    home = request.META['HTTP_HOST']
    request_http = 'http://'
    url = request_http + home + '/sitemap.xml'
    num = requests.get(url=url)
    lists = []
    success = 0
    html = urllib.request.urlopen(url).read()
    html = html.decode('utf-8')
    url = re.findall(f'({request_http}{home}/.*?</loc>)', html)
    for item in url:
        ok_url = re.sub('<.*>', '', item, 2)
        lists.append(ok_url)

    paginator = Paginator(lists, 3)
    cur_page = request.GET.get('page', 1)
    page = paginator.page(cur_page)

    try:
        site_obj = Site.objects.get(id=1)
        site_url = site_obj.url
        token = site_obj.baidu_api
        send_baidu = BaiduTS(site_url, token)
        result = send_baidu.push(lists)

        success = result['success']
        remain = result['remain']
        BaiduFanHuiZhi.objects.create(content=success)
    except Exception as e:
        return HttpResponse('站点网址与token配置信息不存在，请添加后再推送')

    return render(request, "admin/all_tuisong.html", locals())

def all_tui_view(request):
    lists = ['只显示当前推送的链接，不显示历史信息']
    paginator = Paginator(lists, 3)
    cur_page = request.GET.get('page', 1)
    page = paginator.page(cur_page)
    return render(request, "admin/all_tuisong.html", locals())

def view_tui(request):

    all_day = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    today = datetime.date.today()
    tomorrow = today + datetime.timedelta(days=1)
    num = 0
    for i in range(len(all_day) - 1, -1, -1):
        num += 1
        date_time = tomorrow - datetime.timedelta(days=num)
        all_day[i] = str(date_time)

    all_num = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    data = BaiduFanHuiZhi.objects.all()
    for item in data:
        for i in range(len(all_day)):
            if item.created_time.strftime('%Y-%m-%d') == all_day[i]:
                all_num[i] = item.content

    return render(request, "admin/view_tuisong.html", {'all_day': all_day, 'all_num': all_num})


def cache_view_page(request):
    return render(request, "admin/cache_view_page.html")


def cache_set(request):
    caches['default'].clear()
    return render(request, "admin/cache_set.html")

