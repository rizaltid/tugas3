from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('about/', inclode ('about.urls')),
    path('contak/', inclode ('contak.urls')),
    path('baru/', inclode ('baru.urls')),
]
