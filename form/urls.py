from django.urls import path

from form import views

urlpatterns = [
    path('message.html', views.message, name='message')
]