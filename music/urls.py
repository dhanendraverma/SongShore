from django.urls import path,re_path
from . import views

urlpatterns = [
	#/music/
    re_path(r'^$', views.index),

    #/music/17/
    re_path(r'^(?P<album_id>[0-9]+)/$',views.detail)
]