from django.urls import path, re_path
from django.conf.urls.static import static
from django.conf import settings

from . import views

urlpatterns = [
    re_path(r'^$', views.ProfileList.as_view()),
    re_path(r'^(?P<id>\d+)$', views.ProfileDetail.as_view()),
]