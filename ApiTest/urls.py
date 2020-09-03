"""ApiTest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from MyApp.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    url(r"^child/(?P<eid>.+)/(?P<oid>.*)/$", child),
    path('', home),
    path('home/', home),
    path('login/', login),
    path('login_action/', login_action),
    path('register_action/', register_action),
    path('login_out/', login_out),
    path('case_list/', case_list),
    path('pei/', pei),
    path('api_help/', api_help),
    path('project_list/', project_list),
    path('delete_project/', delete_project),
    path('add_project/', add_project),
    url(r"^apis/(?P<id>.*)/$", open_apis),
    url(r"^cases/(?P<id>.*)/$", cases),
    url(r"^project_set/(?P<id>.*)/$", project_set),
    url(r"^save_project_set/(?P<id>.*)/$", save_project_set),
    url(r"^project_api_add/(?P<Pid>.*)/$", project_api_add),  # Pid project_id，传一个项目id，在该项目下新增一个接口，自动生成接口id
    url(r"^project_api_del/(?P<id>.*)/$", project_api_del),  # id 接口id
    path('save_bz/', save_bz),  # 保存备注
    path('get_bz/', get_bz),  # 获取备注
]
