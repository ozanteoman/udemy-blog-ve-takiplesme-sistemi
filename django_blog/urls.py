"""django_blog URL Configuration

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
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.conf import settings
from blog.views import iletisim, deneme, deneme_ajax, deneme_ajax_2

from django.contrib import admin

urlpatterns = [
    url(r'^deneme/$', deneme, name='deneme'),
    url(r'^deneme/ajax/$', deneme_ajax, name='deneme-ajax'),
    url(r'^deneme/ajax-2/$', deneme_ajax_2, name='deneme-ajax-2'),
    url(r'^admin/', admin.site.urls),
    url(r'^posts/', include('blog.urls')),
    url(r'^auths/', include('auths.urls')),
    url(r'^fallowing/', include('fallowing.urls')),
    url(r'^iletisim/', iletisim, name='iletisim')
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
