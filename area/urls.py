from django.conf.urls import include, url
from django.contrib import admin
from area import views

urlpatterns = [
    url(r'^show_area$', views.show_area, name='show_area'),  # 显示地区详情
]
