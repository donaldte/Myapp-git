from django.urls import path
from videos.views import *

app_name = "videos"
urlpatterns = [
    path('media/videos', videos, name="vid"),
    path('media/videos/categories/',video_list, name="listVid")
]
