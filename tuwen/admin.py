import os
from django.conf import settings
from django.contrib import admin
from django.utils.safestring import mark_safe

from site_set.models import MinGan
from sxkj_admin.admin import admin_site
from tuwen.models import TuWenCatalog, TuWenImage, TuWen



class ViewOnSiteMixin(object):
    def view_on_site(self, obj):
        return mark_safe(u"<a href='%s' target='_blank'>现场查看</a>" % obj.get_absolute_url())

    view_on_site.allow_tags = True
    view_on_site.short_description = u"前台页面"


class TuWenCatalogAdmin(ViewOnSiteMixin, admin.ModelAdmin):
    list_display = ['id', 'name', 'view_on_site', 'category', 'sort', 'created_time']
    list_display_links = ['id', 'name']
    list_editable = ('sort',)
    list_per_page = 20
    ordering = ('-created_time',)
    search_fields = ('name',)

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ['url']
        else:
            return []

    def changelist_view(self, request, extra_context=None):
        extra_context = {'title': '选择 图文分类 新增或编辑'}
        return super(TuWenCatalogAdmin, self).changelist_view(request, extra_context=extra_context)


admin_site.register(TuWenCatalog, TuWenCatalogAdmin)


class TuWenImageAdmin(admin.TabularInline):
    model = TuWenImage
    verbose_name = '项目图片'


class TuWenAdmin(ViewOnSiteMixin, admin.ModelAdmin):
    inlines = [TuWenImageAdmin]
    filter_horizontal = ('goods_tag', 'tuwen_tag',)
    fieldsets = (
        ('基本信息', {
            'fields': ('name', 'url', 'tuwen_catalog', 'is_topping', 'sort', 'file_upload')
        }),
        ('内容编辑', {
            'classes': ('collapse',),
            'fields': ('splj', 'summary', 'content')
        }),
        ('SEO相关', {
            'classes': ('collapse',),
            'fields': ('title', 'keywords', 'describe', 'is_sitemap', 'goods_tag', 'tuwen_tag')
        }),
    )

    list_display = ['id', 'name', 'view_on_site', 'tuwen_catalog', 'is_topping', 'sort', 'created_time']
    list_display_links = ['id', 'name']
    list_editable = ('sort', 'is_topping')
    list_per_page = 20
    ordering = ('-created_time',)
    search_fields = ('name',)

    def save_formset(self, request, form, formset, change):
        if request.FILES:
            old_img = request.FILES['tuwenimage_set-0-images']
            formset.save()
            path = os.path.join(settings.MEDIA_ROOT + '/goods_images')
            path_file = os.path.join(path, str(old_img))
            os.remove(f'{path_file}')
        formset.save()

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        tuwen_obj = TuWen.objects.get(id=obj.id)
        c_url = tuwen_obj.tuwen_catalog.url
        tuwen_obj.c_url = c_url

        if MinGan.objects.filter():
            mgc = MinGan.objects.filter()
            for item in mgc:
                if item.name in tuwen_obj.content:
                    new_content = tuwen_obj.content.replace(item.name, '*')
                    tuwen_obj.content = new_content
        tuwen_obj.save()

    def get_form(self, request, obj=None, **kwargs):
        form = super(TuWenAdmin, self).get_form(request, obj, **kwargs)
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
        extra_context = {'title': '选择 图文 新增或编辑'}
        return super(TuWenAdmin, self).changelist_view(request, extra_context=extra_context)

    class Media:
        js = ('/static/kindeditor/kindeditor-all-min.js',
              '/static/kindeditor/lang/zh-CN.js',
              '/static/kindeditor/config.js')

    class Meta:
        model = TuWen


admin_site.register(TuWen, TuWenAdmin)
