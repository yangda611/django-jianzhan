from django.contrib import admin
from django.contrib.auth.admin import UserAdmin, GroupAdmin
from django.contrib.auth.models import User, Group
from django.http import HttpRequest
from django.template.response import TemplateResponse
from django.views.decorators.cache import never_cache
import datetime

from form.models import Message
from goods.models import Goods, GoodsCatalog
from links.models import Links, Mode
from news.models import News, NewsCatalog
from page.models import Page, Job, GoodsTag, NewsTag, TuWenTag
from site_set.models import Site, MinGan
# from sitemap_set.models import Sitemap
from slide_set.models import PCSlide, MSlide
from sx_cms.settings import ALLOWED_HOSTS

from tuwen.models import TuWen, TuWenCatalog


class MyAdminSite(admin.AdminSite):
    index_template = 'admin/index.html'

    @never_cache
    def index(self, request, extra_context=None):


        import requests
        home = request.META['HTTP_HOST']
        request_http = 'http://'
        url = request_http + home + '/sitemap.xml'
        num = requests.get(url=url)
        lists = []

        for item in num:
            if '<loc>http' in item.decode():
                lists.append('<loc>http')
        sitemap_num = len(lists)

        link_number = Mode.objects.filter(number__gt=0)
        index_link_num = 0
        for item in link_number:
            index_link_num += int(item.number)

        fr_links = Links.objects.all()
        index_friend = 0
        for item in fr_links:
            if item:
                index_friend += 1


        mes = Message.objects.all()
        index_mes = 0
        for item in mes:
            if mes:
                index_mes += 1


        app_list = self.get_app_list(request)

        year = datetime.datetime.now().year
        month = datetime.datetime.now().month
        time = str(year) + '-' + str(month)
        news_update = News.objects.filter(updated_time__contains=time)
        goods_update = Goods.objects.filter(updated_time__contains=time)

        news_num = 0
        goods_num = 0
        for item in news_update:
            if item:
                news_num += 1

        for items in goods_update:
            if items:
                goods_num += 1

        month_nums = news_num + goods_num
        index_num = month - 1
        all_update = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

        for i in range(len(all_update)):
            if i == index_num:
                all_update[i] = month_nums

        now = datetime.datetime.now()
        today_year = now.year
        last_year = int(now.year) - 1
        today_year_months = range(1, now.month + 1)
        last_year_months = range(now.month + 1, 13)
        data_list_lasts = []

        for last_year_month in last_year_months:
            date_list = '%s-%s' % (last_year, last_year_month)
            data_list_lasts.append(date_list)

        data_list_todays = []
        for today_year_month in today_year_months:
            data_list = '%s-%s' % (today_year, today_year_month)
            data_list_todays.append(data_list)
        data_year_month = data_list_lasts + data_list_todays

        goods_tag_num = 0
        goods = GoodsTag.objects.all()
        for item in goods:
            if item:
                goods_tag_num += 1

        news_tag_num = 0
        news = NewsTag.objects.all()
        for item in news:
            if item:
                news_tag_num += 1

        tuwen_tag_num = 0
        tuwen = TuWenTag.objects.all()
        for item in tuwen:
            if item:
                tuwen_tag_num += 1
        tags_number = [goods_tag_num, news_tag_num, tuwen_tag_num]
        print(tags_number)
        print('---------')

        context = {
            **self.each_context(request),
            'app_list': app_list,
            'data': all_update,
            'sitemap_num': sitemap_num,
            'index_link_num': index_link_num,
            'index_friend': index_friend,
            'index_mes': index_mes,
            'tags_number': tags_number,
            'data_year_month': data_year_month,

        }

        request.current_app = self.name

        return TemplateResponse(request, self.index_template or 'admin/index.html', context)


admin_site = MyAdminSite(name='admin')
admin_site.register(User, UserAdmin)
admin_site.register(Group, GroupAdmin)
