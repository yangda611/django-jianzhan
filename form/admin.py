

from django.contrib import admin

from form.models import Message
from sxkj_admin.admin import admin_site


class MessageAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'tel', 'email', 'created_time', 'ipaddress']
    list_display_links = ['id', 'name']
    list_per_page = 20
    search_fields = ('name', 'tel')
    ordering = ['-created_time']

    def change_view(self, request, object_id, form_url='', extra_context=None):
        extra_context = {'title': '留言信息查询'}

        return super(MessageAdmin, self).change_view(request, object_id, form_url, extra_context=extra_context)

    def changelist_view(self, request, extra_context=None):
        extra_context = {'title': '网站留言列表'}
        return super(MessageAdmin, self).changelist_view(request, extra_context=extra_context)


admin_site.register(Message, MessageAdmin)
