
from django.urls import path

from site_set import views


urlpatterns = [
    path('<str:site>', views.site_set, name='site_set')
]
