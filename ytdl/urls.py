from django.urls import path
from ytdl import views


urlpatterns = [
    path('', views.download_video, name = 'index'),
]