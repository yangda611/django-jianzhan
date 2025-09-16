from django.urls import path

from tuwen import views

urlpatterns = [
    path('<str:tuwen_c>.html', views.tuwen_catalog, name='tuwen_catalog'),
    path('<str:tuwen_c>/<slug:tuwen_p>.html', views.tuwen, name='tuwen'),
]