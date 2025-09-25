from django.contrib import admin
from django.contrib.auth.admin import UserAdmin, GroupAdmin
from django.contrib.auth.models import User, Group
from django.template.response import TemplateResponse
from django.views.decorators.cache import never_cache
import datetime

from form.models import Message
from goods.models import Goods, GoodsCatalog
from links.models import Links, Mode
from news.models import News, NewsCatalog
from page.models import GoodsTag, NewsTag, TuWenTag, Page
from tuwen.models import TuWen, TuWenCatalog


class MyAdminSite(admin.AdminSite):
    index_template = 'admin/index.html'
    
    def get_app_list(self, request):
        """
        自定义应用列表顺序和显示
        """
        app_list = super().get_app_list(request)
        
        # 定义新的应用顺序和显示名称
        app_order = [
            ('goods', '🏪 商品中心'),
            ('news', '📰 内容发布'), 
            ('tuwen', '🖼️ 多媒体库'),
            ('links', '🔗 链接资源'),
            ('form', '💬 用户反馈'),
            ('page', '📄 页面管理'),
            ('slide_set', '🎬 轮播展示'),
            ('sitemap_set', '🗺️ 地图配置'),
            ('site_set', '⚙️ 系统设置'),
        ]
        
        # 重新排序应用列表
        ordered_apps = []
        for app_name, display_name in app_order:
            for app in app_list:
                if app['app_label'] == app_name:
                    app['name'] = display_name
                    ordered_apps.append(app)
                    break
        
        return ordered_apps

    @never_cache
    def index(self, request, extra_context=None):

        g = Goods.objects.filter(is_sitemap=True).count()
        n = News.objects.filter(is_sitemap=True).count()
        t = TuWen.objects.filter(is_sitemap=True).count()
        p = Page.objects.filter(is_sitemap=True).count()
        gc = GoodsCatalog.objects.filter(is_sitemap=True).count()
        nc = NewsCatalog.objects.filter(is_sitemap=True).count()
        tc = TuWenCatalog.objects.filter(is_sitemap=True).count()

        sitemap_num = g + n + t + p + gc + nc + tc + 1

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
            if item:
                index_mes += 1

        app_list = self.get_app_list(request)


        year = datetime.datetime.now().year

        a1 = News.objects.filter(updated_time__range=(datetime.date(year, 1, 1), datetime.date(year, 1, 31))).count()
        a2 = News.objects.filter(updated_time__range=(datetime.date(year, 2, 1), datetime.date(year, 2, 28))).count()
        a3 = News.objects.filter(updated_time__range=(datetime.date(year, 3, 1), datetime.date(year, 3, 31))).count()
        a4 = News.objects.filter(updated_time__range=(datetime.date(year, 4, 1), datetime.date(year, 4, 30))).count()
        a5 = News.objects.filter(updated_time__range=(datetime.date(year, 5, 1), datetime.date(year, 5, 31))).count()
        a6 = News.objects.filter(updated_time__range=(datetime.date(year, 6, 1), datetime.date(year, 6, 30))).count()
        a7 = News.objects.filter(updated_time__range=(datetime.date(year, 7, 1), datetime.date(year, 7, 31))).count()
        a8 = News.objects.filter(updated_time__range=(datetime.date(year, 8, 1), datetime.date(year, 8, 31))).count()
        a9 = News.objects.filter(updated_time__range=(datetime.date(year, 9, 1), datetime.date(year, 9, 30))).count()
        a10 = News.objects.filter(updated_time__range=(datetime.date(year, 10, 1), datetime.date(year, 10, 31))).count()
        a11 = News.objects.filter(updated_time__range=(datetime.date(year, 11, 1), datetime.date(year, 11, 30))).count()
        a12 = News.objects.filter(updated_time__range=(datetime.date(year, 12, 1), datetime.date(year, 12, 31))).count()

        all_update = [a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11, a12]


        now = datetime.datetime.now()
        today_year = now.year

        today_year_months = range(1, 13)

        data_list_lasts = []

        for month in today_year_months:
            date_list = '%s-%s' % (today_year, month)
            data_list_lasts.append(date_list)

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

        # 添加文章数量和产品种类数据
        news_count = News.objects.count()  # 文章总数
        goods_count = Goods.objects.count()  # 产品总数
        
        # 添加产品分类、图文分类、图文数量数据
        goods_catalog_count = GoodsCatalog.objects.count()  # 产品分类数量
        news_catalog_count = NewsCatalog.objects.count()  # 图文分类数量
        tuwen_count = TuWen.objects.count()  # 图文数量

        context = {
            **self.each_context(request),
            'app_list': app_list,
            'data': all_update,
            'sitemap_num': sitemap_num,
            'index_link_num': index_link_num,
            'index_friend': index_friend,
            'index_mes': index_mes,
            'tags_number': tags_number,
            'data_year_month': data_list_lasts,
            'news_count': news_count,  # 文章数量
            'goods_count': goods_count,  # 产品种类数量
            'goods_catalog_count': goods_catalog_count,  # 产品分类数量
            'news_catalog_count': news_catalog_count,  # 图文分类数量
            'tuwen_count': tuwen_count,  # 图文数量

        }

        request.current_app = self.name

        return TemplateResponse(request, self.index_template or 'admin/index.html', context)


admin_site = MyAdminSite(name='admin')
admin_site.register(User, UserAdmin)
admin_site.register(Group, GroupAdmin)
