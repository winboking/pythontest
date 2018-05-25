#coding=utf-8
"""mytestpoj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url

# 登录、退出、主页、欢迎页、个人设置方法引用

from testapp.views import sale_order_list,get_saleorder_list,get_saleorder_list_info,test2,get_treedata

urlpatterns = [
    # 实例1
    url(r'^$', sale_order_list),
    url(r'^get_saleorder_list/$', get_saleorder_list),
    url(r'^get_saleorder_list_info/(?P<order_id>\d{1})/$', get_saleorder_list_info),
    #实例2
    url(r'^html_test2/$', test2),
    url(r'^get_treedata/$', get_treedata),

]
