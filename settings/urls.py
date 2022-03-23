from django.contrib import admin
from django.urls import path, include
from django.views.static import serve
from django.conf.urls.static import url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("UserProfile.urls")),
    path('Company/',include('Company.urls')),
    url(r'^media/(?P<path>.*)$', serve,{'document_root':       settings.MEDIA_ROOT}), 
    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}), 
]
