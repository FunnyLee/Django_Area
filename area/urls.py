from django.conf.urls import include, url
from django.contrib import admin
from area import views

urlpatterns = [
    url(r'^show_area$', views.show_area, name='show_area'),  # 显示地区详情
    url(r'^show_select_area$', views.show_select_area, name='show_select_area'),  # 显示省市县选择页面
    url(r'^get_prov$', views.get_prov, name='get_prov'),  # 获取省级地区
    url(r'^get_city$', views.get_city, name='get_city'),  # 获取市级地区
]
