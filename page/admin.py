
from django.contrib import admin
from django.utils.safestring import mark_safe

from page.models import Page, Job
from site_set.models import MinGan
from sxkj_admin.admin import admin_site


class ViewOnSiteMixin(object):
    def view_on_site(self, obj):
        return mark_safe("<a href='%s' target='_blank'>现场查看</a>" % obj.get_absolute_url())

    view_on_site.allow_tags = True
    view_on_site.short_description = "前台页面"



class PageAdmin(ViewOnSiteMixin, admin.ModelAdmin):
    list_display = ['id', 'name', 'view_on_site', 'is_bar', 'sort', 'created_time']
    list_display_links = ['id', 'name']
    list_editable = ('sort', 'is_bar')
    list_per_page = 20
    ordering = ('created_time',)
    search_fields = ('name',)

    def get_form(self, request, obj=None, **kwargs):
        form = super(PageAdmin, self).get_form(request, obj, **kwargs)
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

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        page_obj = Page.objects.get(id=obj.id)

        if MinGan.objects.filter():
            mgc = MinGan.objects.filter()
            for item in mgc:
                if item.name in page_obj.content:
                    new_content = page_obj.content.replace(item.name, '*')
                    page_obj.content = new_content
        page_obj.save()

    class Media:
        js = ('/static/kindeditor/kindeditor-all-min.js',
              '/static/kindeditor/lang/zh-CN.js',
              '/static/kindeditor/config.js')


admin_site.register(Page, PageAdmin)


class JobAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'sort', 'created_time']
    list_display_links = ['id', 'name']
    list_editable = ('sort',)
    list_per_page = 20
    ordering = ('created_time',)
    search_fields = ('name',)


admin_site.register(Job, JobAdmin)
