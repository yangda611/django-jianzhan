
from django.contrib import admin
from django.template.response import TemplateResponse
from django.urls import path

from goods.models import Goods
from slide_set.models import PCSlide, MSlide
from sxkj_admin.admin import admin_site

admin_site.register(PCSlide)
admin_site.register(MSlide)


