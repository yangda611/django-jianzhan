from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.urls import path, include
from django.views.static import serve
from news.uploads import upload_image
from sx_cms import views, settings
from sx_cms.search import search
from sx_cms.settings import admin_address
from django.views.generic.base import TemplateView

from sx_cms.sitemaps import HomeSitemap, GoodsCatalogSitemap, NewsCatalogSitemap, TuWenCatalogSitemap, GoodsSitemap, \
    NewsSitemap, TuWenSitemap, PageSitemap
from sxkj_admin.admin import admin_site

admin.autodiscover()
admin_site.enable_nav_sidebar = False

sitemaps = {
    'home': HomeSitemap,
    'goodscatalog': GoodsCatalogSitemap,
    'newsscatalog': NewsCatalogSitemap,
    'tuwencatalog': TuWenCatalogSitemap,
    'goods': GoodsSitemap,
    'news': NewsSitemap,
    'tuwen': TuWenSitemap,
    'page': PageSitemap,
}

urlpatterns = [
    path(admin_address, admin_site.urls),
    path('', views.home, name='home'),
    path('sitemap.html', views.sitemap, name='sitemap'),
    path('a/', include('news.urls')),
    path('c/', include('tuwen.urls')),
    path('d/', include('page.urls')),
    path('', include('form.urls')),
    path('', include('goods.urls')),
    path('search/', search, name='search'),
    path('robots.txt', TemplateView.as_view(template_name="robots.txt", content_type="text/plain")),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps, 'template_name': 'sitemaps/sitemap.xml'}),
    url(r"^uploads/(?P<path>.*)$", serve, {"document_root": settings.MEDIA_ROOT, }),
    url(r'^admin/upload/(?P<dir_name>[^/]+)$', upload_image, name='upload_image'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])
