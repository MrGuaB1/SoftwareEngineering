"""
URL configuration for GroupWork project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from neo.views import *

from neo import views

urlpatterns = [
    path('system/welcome.html', welcome),

    # from this
    path('admin/', admin.site.urls),
    path('system/', system),
    path('system/index/', Index),
    path('system/MainInfo.html', views.MainInfo),
    path('system/Underwater.html', views.Underwater),
    path('system/datacenter.html', views.Datacenter),
    path('system/AIcenter.html', views.AIcenter),
    path('system/admincontrol.html', views.AdminControl),
    path('system/forget.html',views.forget),
    path('system/smart_QA.html', views.smart_qa),

    # 注册登录
    path('',login),
    path('system/register.html',register_page,name ="register"),
    path('system/', system),
    path('backend/backend.html', backend),
    path('backend/table.html', table),
    path('backend/get_data', get_data),
    path('backend/edit_data',edit_data),
    path('backend/edit_check',edit_check),

    # 鱼群
    path('fish/get_fish_statistics', get_fish_statistics),
    path('fish/getTOP5', getTOP5),
    path('fish/get_fish_change', get_fish_change),
    path('fish/get_top_info', get_top_info),
    path('fish/writeDB', writeDB),
    path('fish/predict', fish_predict),
]
