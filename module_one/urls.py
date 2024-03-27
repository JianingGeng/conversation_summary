# module_one/urls.py

from django.urls import path
from .views import AudioFileList
from . import views

urlpatterns = [
    path("audiofiles/", AudioFileList.as_view()),
    path("feature1/", views.feature1, name="feature1"),
]
