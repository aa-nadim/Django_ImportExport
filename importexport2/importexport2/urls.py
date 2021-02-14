"""importexport2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.conf import settings
from main.views import ProfileImageIndexView
from django.contrib import admin
admin.outodiscover()

from main.views import ProfileImageView, ProfileDetailView


urlpatterns = patterns('',
        url(r'^$',ProfileImageIndexView.as_view(),name='home'),
        url(r'^upload/',ProfileImageView.as_view(),name='profile_image_upload'),
        url(r'^uploadad/(?P<pk>\d+)/$',ProfileDetailView.as_view(),name='profile_image'),
        url(r'^admin/', include(admin.site.urls)),
)+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


