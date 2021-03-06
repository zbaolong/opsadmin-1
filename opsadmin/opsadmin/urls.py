"""opsadmin URL Configuration

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
from django.contrib import admin
import asset.api.host
import asset.views.host

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'api/add_host/',asset.api.host.add_host),
    url(r'show_hosts/',asset.views.host.show_hosts,name='show_hosts'),
    url(r'show_detail_host/',asset.views.host.show_detail_host,name='show_detail_host'),
    url(r'del_host/',asset.views.host.del_host,name='del_host'),
    url(r'add_host/',asset.views.host.add_host,name='add_host'),
]
