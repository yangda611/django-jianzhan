from django.contrib import admin
from django.urls import path

from site_set.models import Site, MinGan, BaiduFanHuiZhi
from site_set.views import ban_keyword, all_tui, view_tui, all_tui_view, cache_view_page, cache_set, \
    get_ban_keyword_page
from sxkj_admin.admin import admin_site


class SiteAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        from django.contrib.sites.models import Site as Django_site
        from urllib.parse import urlparse
        site = Django_site.objects.get_current()

        parsed_url = urlparse(form.instance.url)
        cleaned_url = parsed_url.netloc + parsed_url.path

        site.domain = cleaned_url
        site.save()

    def get_actions(self, request):
        actions = super().get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions

    def has_delete_permission(self, request, obj=None):
        return False

    def render_change_form(self, request, context, add=False, change=False, form_url='', obj=None):
        context.update({
            'show_save': True,
            'show_save_and_continue': False,
            'show_save_and_add_another': False
        })
        return super().render_change_form(request, context, add, change, form_url, obj)

    def get_form(self, request, obj=None, **kwargs):
        form = super(SiteAdmin, self).get_form(request, obj, **kwargs)
        form.base_fields['describe'].widget.attrs['style'] = 'width: 60em; height:6em'
        form.base_fields['title'].widget.attrs['style'] = 'width: 60em;'
        form.base_fields['keywords'].widget.attrs['style'] = 'width: 60em;'
        return form

    def change_view(self, request, object_id, form_url='', extra_context=None):
        extra_context = {'title': '以下是您的网站配置信息'}

        return super(SiteAdmin, self).change_view(request, object_id,
                                                  form_url, extra_context=extra_context)

    def changelist_view(self, request, extra_context=None):
        extra_context = {'title': '欢迎查看网站配置'}
        return super(SiteAdmin, self).changelist_view(request, extra_context=extra_context)

    def get_urls(self):
        urls = super().get_urls()
        my_urls = [
            path('cache_set', self.admin_site.admin_view(cache_set)),
            path('cache_view_page', self.admin_site.admin_view(cache_view_page)),
        ]

        return my_urls + urls

    class Meta:
        model = Site


admin_site.register(Site, SiteAdmin)



class MinGanAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_time', 'updated_time']

    def get_urls(self):
        urls = super().get_urls()
        my_urls = [
            path('get_mgc', self.admin_site.admin_view(get_ban_keyword_page)),
            path('mgc', self.admin_site.admin_view(ban_keyword)),
        ]
        return my_urls + urls


admin_site.register(MinGan, MinGanAdmin)


class BaiduFanHuiZhiAdmin(admin.ModelAdmin):
    list_display = ['content']

    def get_urls(self):
        urls = super().get_urls()
        my_urls = [
            path('all_tui', self.admin_site.admin_view(all_tui), name='all_tui'),
            path('all_tui_view', self.admin_site.admin_view(all_tui_view), name='all_tui_view'),
            path('view', self.admin_site.admin_view(view_tui)),
        ]

        return my_urls + urls


admin_site.register(BaiduFanHuiZhi, BaiduFanHuiZhiAdmin)
