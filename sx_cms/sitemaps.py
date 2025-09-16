# @Time: 11月 18, 2021
import datetime

from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from goods.models import GoodsCatalog, Goods
from news.models import NewsCatalog, News
from page.models import Page

from sitemap_set.models import Sitemap as Map
from tuwen.models import TuWenCatalog, TuWen


if Map.objects.filter().exists():
    sx_site = Map.objects.get(id=1)

    catalog_w = sx_site.get_catalog_w_display()
    catalog_f = sx_site.get_catalog_f_display()

    index_w = sx_site.get_index_w_display()
    index_f = sx_site.get_index_f_display()

    inner_w = sx_site.get_inner_w_display()
    inner_f = sx_site.get_inner_f_display()

    page_w = sx_site.get_page_w_display()
    page_f = sx_site.get_page_f_display()

else:
    catalog_w = '0.5'
    catalog_f = 'weekly'

    index_w = '1.0'
    index_f = 'always'

    inner_w = '0.8'
    inner_f = 'weekly'

    page_w = '0.5'
    page_f = 'weekly'

class HomeSitemap(Sitemap):
    changefreq = index_f
    priority = index_w

    def items(self):
        return ['home', ]

    def lastmod(self, obj):
        today = datetime.datetime.today()
        return today

    def location(self, item):
        return reverse(item)

class GoodsCatalogSitemap(Sitemap):
    changefreq = catalog_f
    priority = catalog_w

    def items(self):
        p = GoodsCatalog.objects.filter(is_sitemap=True)
        return p

    def lastmod(self, obj):
        return obj.created_time

    def location(self, obj):
        return '/%s.html' % obj.url

class NewsCatalogSitemap(Sitemap):
    changefreq = catalog_f
    priority = catalog_w

    def items(self):
        n = NewsCatalog.objects.filter(is_sitemap=True)
        return n

    def lastmod(self, obj):
        return obj.created_time


class TuWenCatalogSitemap(Sitemap):
    changefreq = catalog_f
    priority = catalog_w

    def items(self):
        t = TuWenCatalog.objects.filter(is_sitemap=True)
        return t

    def lastmod(self, obj):
        return obj.created_time


class GoodsSitemap(Sitemap):
    changefreq = inner_f
    priority = inner_w

    def items(self):
        p = Goods.objects.filter(is_sitemap=True)
        return p

    def lastmod(self, obj):
        return obj.updated_time



class NewsSitemap(Sitemap):
    changefreq = inner_f
    priority = inner_w

    def items(self):
        n = News.objects.filter(is_sitemap=True)
        return n

    def lastmod(self, obj):
        return obj.updated_time


class TuWenSitemap(Sitemap):
    changefreq = inner_f
    priority = inner_w

    def items(self):
        t = TuWen.objects.filter(is_sitemap=True)
        return t

    def lastmod(self, obj):
        return obj.updated_time


class PageSitemap(Sitemap):
    changefreq = page_f
    priority = page_w

    def items(self):
        page = Page.objects.filter(is_sitemap=True)
        return page

    def lastmod(self, obj):
        return obj.created_time
