
from django.contrib import admin
from sitemap_set.models import Sitemap
from sxkj_admin.admin import admin_site


class SitemapAdmin(admin.ModelAdmin):
    def get_actions(self, request):
        actions = super().get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions

    def has_delete_permission(self, request, obj=None):
        return False

    readonly_fields = ('newscatalog', 'goodscatalog', 'tuwencatalog', 'page')
    fieldsets = (
        ('sitemap项目', {
            'fields': ('name', 'newscatalog', 'goodscatalog', 'tuwencatalog', 'page')
        }),
        ('权重分配', {
            'fields': ('index_w', 'catalog_w', 'inner_w', 'page_w')
        }),
        ('更新频率', {
            'fields': ('index_f', 'catalog_f', 'inner_f', 'page_f')
        }),
    )

    def render_change_form(self, request, context, add=False, change=False, form_url='', obj=None):
        context.update({
            'show_save': True,
            'show_save_and_continue': False,
            'show_save_and_add_another': False
        })
        return super().render_change_form(request, context, add, change, form_url, obj)

    def changelist_view(self, request, extra_context=None):
        extra_context = {'title': '您的 站点地图 配置文件'}
        return super(SitemapAdmin, self).changelist_view(request, extra_context=extra_context)

    def change_view(self, request, object_id, form_url='', extra_context=None):
        extra_context = {'title': '配置SiteMap'}

        return super(SitemapAdmin, self).change_view(request, object_id, form_url, extra_context=extra_context)

admin_site.register(Sitemap, SitemapAdmin)
