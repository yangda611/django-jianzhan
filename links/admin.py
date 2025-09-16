
from django.contrib import admin
from django.urls import path

from links.models import Links, LinkInner, Mode
from links.views import inner_link
from sxkj_admin.admin import admin_site

admin_site.register(Links)


class ModelinkAdmin(admin.TabularInline):
    model = LinkInner
    readonly_fields = ('name', 'vote_url', 'vote_keyword')
    verbose_name = '内链详情'

    def get_actions(self, request):
        actions = super().get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions

    def has_delete_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request, obj):
        return False


class MyModelAdmin(admin.ModelAdmin):
    inlines = [ModelinkAdmin]

    list_display = ['name', 'url', 'number', 'vote_number']
    list_display_links = ['number', 'vote_number']
    exclude = ('goods', 'news', 'tuwen')
    readonly_fields = ('name', 'url', 'number', 'content', 'vote_number')

    def get_actions(self, request):
        actions = super().get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions

    def has_delete_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request):
        return False

    def render_change_form(self, request, context, add=False, change=False, form_url='', obj=None):
        context.update({
            'show_save': False,
            'show_save_and_continue': False,
            'show_save_and_add_another': False
        })
        return super().render_change_form(request, context, add, change, form_url, obj)

    def get_urls(self):
        urls = super().get_urls()
        my_urls = [
            path('links', self.admin_site.admin_view(inner_link)),
        ]
        return my_urls + urls

    def change_view(self, request, object_id, form_url='', extra_context=None):
        extra_context = {'title': '欢迎查看内链详情'}

        return super(MyModelAdmin, self).change_view(request, object_id,
                                                     form_url, extra_context=extra_context)

    def changelist_view(self, request, extra_context=None):
        extra_context = {'title': '欢迎查看内链列表'}
        return super(MyModelAdmin, self).changelist_view(request, extra_context=extra_context)


admin_site.register(Mode, MyModelAdmin)
