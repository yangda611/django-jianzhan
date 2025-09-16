import os

from django.conf import settings
from django.contrib import admin, sites
from django.contrib.admin import models
from django.http import HttpResponse
from django.utils.safestring import mark_safe

from goods.models import GoodsImage, Goods, GoodsCatalog

from news.models import NewsCatalog, News
from page.models import GoodsTag, NewsTag, TuWenTag
from site_set.baidu_ts import BaiduTS
from site_set.models import MinGan, Site, BaiduFanHuiZhi
from sxkj_admin.admin import admin_site


class ViewOnSiteMixin(object):
    def view_on_site(self, obj):
        return mark_safe("<a href='%s' target='_blank'>现场查看</a>" % obj.get_absolute_url())

    view_on_site.allow_tags = True
    view_on_site.short_description = "前台页面"


class GoodsCatalogAdmin(ViewOnSiteMixin, admin.ModelAdmin):
    list_display = ['id', 'name', 'view_on_site', 'category', 'sort', 'created_time']
    list_display_links = ['id', 'name']
    list_editable = ('sort',)
    list_per_page = 20
    ordering = ('created_time',)
    search_fields = ('name',)

    def changelist_view(self, request, extra_context=None):
        extra_context = {'title': '选择 产品分类 新增或编辑'}
        return super(GoodsCatalogAdmin, self).changelist_view(request, extra_context=extra_context)

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        if request.FILES:
            print(request.FILES)
            old_img = request.FILES['image']

            path = os.path.join(settings.MEDIA_ROOT + '/goods_c_images')
            path_file = os.path.join(path, str(old_img))
            os.remove(f'{path_file}')


admin_site.register(GoodsCatalog, GoodsCatalogAdmin)


class NewsCatalogAdmin(ViewOnSiteMixin, admin.ModelAdmin):
    list_display = ['id', 'name', 'view_on_site', 'category', 'sort', 'created_time']
    list_display_links = ['id', 'name']
    list_editable = ('sort',)
    list_per_page = 20
    ordering = ('created_time',)
    search_fields = ('name',)

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ['url']
        else:
            return []

    def changelist_view(self, request, extra_context=None):
        extra_context = {'title': '选择 文章分类 新增或编辑'}
        return super(NewsCatalogAdmin, self).changelist_view(request, extra_context=extra_context)


admin_site.register(NewsCatalog, NewsCatalogAdmin)


class GoodsImageAdmin(admin.TabularInline):
    model = GoodsImage
    verbose_name = '产品图片'


class GoodsAdmin(ViewOnSiteMixin, admin.ModelAdmin):
    inlines = [GoodsImageAdmin]
    filter_horizontal = ('goods_tag', 'news_tag', 'tuwen_tag')
    fieldsets = (
        ('基本信息', {
            'fields': ('name', 'url', 'goods_catalog', 'is_topping', 'sort', 'image')
        }),
        ('内容编辑', {
            'classes': ('collapse',),
            'fields': ('summary', 'content')
        }),
        ('SEO相关', {
            'classes': ('collapse',),
            'fields': ('title', 'keywords', 'describe', 'is_sitemap', 'goods_tag', 'news_tag', 'tuwen_tag')
        }),
    )

    list_display = ['id', 'name', 'view_on_site', 'goods_catalog', 'sort', 'created_time', 'updated_time']
    list_display_links = ['id', 'name']
    list_editable = ('sort',)
    list_per_page = 20
    ordering = ('-updated_time',)
    search_fields = ('name',)
    exclude = ('c_url',)

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        goods_obj = Goods.objects.get(id=obj.id)
        c_url = goods_obj.goods_catalog.url
        goods_obj.c_url = c_url

        if MinGan.objects.filter():
            mgc = MinGan.objects.filter()
            for item in mgc:
                if item.name in goods_obj.content:
                    new_content = goods_obj.content.replace(item.name, '*')
                    goods_obj.content = new_content

        goods_obj.save()

    def get_form(self, request, obj=None, **kwargs):
        form = super(GoodsAdmin, self).get_form(request, obj, **kwargs)
        form.base_fields['describe'].widget.attrs['style'] = 'width: 60em; height:6em'
        form.base_fields['title'].widget.attrs['style'] = 'width: 60em;'
        form.base_fields['keywords'].widget.attrs['style'] = 'width: 60em;'
        form.base_fields['summary'].widget.attrs['style'] = 'width: 60em; height:6em'
        form.base_fields['content'].widget.attrs['style'] = 'width: 60em; height:30em'
        return form

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ['url']
        else:
            return []

    def changelist_view(self, request, extra_context=None):
        extra_context = {'title': '选择 产品 新增或编辑'}
        return super(GoodsAdmin, self).changelist_view(request, extra_context=extra_context)

    class Media:
        js = ('/static/kindeditor/kindeditor-all-min.js',
              '/static/kindeditor/lang/zh-CN.js',
              '/static/kindeditor/config.js')

    class Meta:
        model = Goods


admin_site.register(Goods, GoodsAdmin)

admin_site.register(GoodsTag)
admin_site.register(NewsTag)
admin_site.register(TuWenTag)


class NewsAdmin(ViewOnSiteMixin, admin.ModelAdmin):
    filter_horizontal = ('goods_tag', 'news_tag',)
    fieldsets = (
        ('基本信息', {
            'fields': (
                'name', 'url', 'news_catalog', 'is_topping', 'sort', 'small_image', 'source', 'vurl', 'created_time')
        }),
        ('内容编辑', {
            'classes': ('collapse',),
            'fields': ('summary', 'content',)
        }),
        ('SEO相关', {
            'classes': ('collapse',),
            'fields': ('title', 'keywords', 'describe', 'is_sitemap', 'goods_tag', 'news_tag')
        }),
    )

    list_display = ['id', 'name', 'view_on_site', 'news_catalog', 'sort', 'created_time', 'updated_time']
    list_display_links = ['id', 'name']
    list_editable = ('sort',)
    list_per_page = 20
    ordering = ('-updated_time',)
    search_fields = ('name',)
    exclude = ('c_url',)

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        news_obj = News.objects.get(id=obj.id)
        c_url = news_obj.news_catalog.url
        news_obj.c_url = c_url

        if MinGan.objects.filter():
            mgc = MinGan.objects.filter()
            for item in mgc:
                if item.name in news_obj.content:
                    new_content = news_obj.content.replace(item.name, '*')
                    news_obj.content = new_content
        news_obj.save()

        import requests
        home = request.META['HTTP_HOST']
        request_http = 'http://'
        url = request_http + home + '/sitemap.xml'
        num = requests.get(url=url)
        all_url_str = num.text

        host_bad1 = request.get_raw_uri()
        import re
        host_bad2 = re.findall('.*/sxkjcms-admin', host_bad1)
        host = re.sub('sxkjcms-admin', '', host_bad2[0], 1)
        news_url = host + 'a' + '/' + obj.c_url + '/' + obj.url + '.html'

        if obj.url not in all_url_str:
            try:
                site_obj = Site.objects.get(id=1)
                site_url = site_obj.url
                token = site_obj.token
                send_baidu = BaiduTS(site_url, token)
                lists = [news_url]
                result = send_baidu.push(lists)
                success = result['success']
                BaiduFanHuiZhi.objects.create(content=success)

            except Exception as e:
                return HttpResponse('站点网址与token配置信息不存在，请添加后再推送', e)

    def get_form(self, request, obj=None, **kwargs):
        form = super(NewsAdmin, self).get_form(request, obj, **kwargs)
        form.base_fields['describe'].widget.attrs['style'] = 'width: 60em; height:6em'
        form.base_fields['title'].widget.attrs['style'] = 'width: 60em;'
        form.base_fields['keywords'].widget.attrs['style'] = 'width: 60em;'
        form.base_fields['content'].widget.attrs['style'] = 'width: 60em; height:30em'
        return form

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ['url']
        else:
            return []

    def changelist_view(self, request, extra_context=None):
        extra_context = {'title': '选择 文章 新增或编辑'}
        return super(NewsAdmin, self).changelist_view(request, extra_context=extra_context)

    class Media:
        js = ('/static/kindeditor/kindeditor-all-min.js',
              '/static/kindeditor/lang/zh-CN.js',
              '/static/kindeditor/config.js')

    class Meta:
        model = News


admin_site.register(News, NewsAdmin)


class LogEntryAdmin(admin.ModelAdmin):
    list_display = ['action_time', 'user', 'content_type', '__str__']
    list_display_links = ['action_time']
    list_filter = ['action_time', 'content_type', 'user']
    list_per_page = 15
    readonly_fields = ['action_time', 'user', 'content_type',
                       'object_id', 'object_repr', 'action_flag', 'change_message']


admin_site.register(models.LogEntry)
