
from django.urls import path
from page import views

urlpatterns = [
    path('<str:page_item>.html', views.page, name='page'),
]