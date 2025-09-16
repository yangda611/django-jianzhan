
from django.urls import path

from slide_set import views

urlpatterns = [
    path('<str:slide>', views.slide, name='slide')
]