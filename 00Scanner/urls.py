"""00Scanner URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from . import view

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^$', view.index),

    url(r'^base$', view.base),
    url(r'^baseAction$',view.baseAction),

    url(r'^sqlScan$',view.sqlScan),
    url(r'^sqlScanAction$',view.sqlScanAction),

    url(r'^webManagerScan$',view.webManagerScan),
    url(r'^webManagerScanAction$',view.webManagerScanAction),

    url(r'^weakPassScan$',view.weakPassScan),
    url(r'^weakPassScanAction$',view.weakPassScanAction),

    url(r'^subDomainScan$',view.subDomainScan),
    url(r'^subDomainScanAction$',view.subDomainScanAction),

    url(r'^portScan$',view.portScan),
    url(r'^portScanAction$',view.portScanAction),

    url(r'^findShell$',view.findShell),
    url(r'^findShellAction$',view.findShellAction),

    url(r'^cmsScan$',view.cmsScan),
    url(r'^cmsScanAction$',view.cmsScanAction),

    url(r'^cPartScan$',view.cPartScan),
    url(r'^cPartScanAction$',view.cPartScanAction),

    url(r'^siteMapScan$',view.siteMapScan),
    url(r'^siteMapScanAction$',view.siteMapScanAction),

    url(r'^view$',view.view),

    url(r'^test$',view.test),

]
