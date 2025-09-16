
from django.urls import path

from goods import views

urlpatterns = [
    path('<str:goods_c>.html', views.goods_catalog, name='goods_catalog'),
    path('<str:goods_c>/<str:goods_p>.html', views.goods, name='goods'),
]
