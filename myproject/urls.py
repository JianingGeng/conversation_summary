"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path, include  # include 函数用于引入其他 URLconf

urlpatterns = [
    path("admin/", admin.site.urls),  # Django 管理后台的 URL
    path(
        "module_one/",
        include("module_one.urls"),
        "module_two/",
        include("module_two.urls"),
    ),  # 包含 module_one 应用中定义的所有 URL
]
