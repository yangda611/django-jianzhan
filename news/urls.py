
from django.urls import path
from news import views

urlpatterns = [
    path('<str:news_c>.html', views.news_catalog, name='news_catalog'),
    path('<str:news_c>/<str:news_p>.html', views.news, name='news'),
]
