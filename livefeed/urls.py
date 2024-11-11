from django.urls import path
from . import views

urlpatterns = [
    path('video_feed/', views.video_feed, name='video_feed'),
    path('live_preview/',views.live_feed_page,name='live_feed_page'),
]
