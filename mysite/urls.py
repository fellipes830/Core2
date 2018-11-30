
from django.contrib import admin

from django.conf.urls import url
from django.contrib import admin

from core2 import views


urlpatterns = [
    url(r'^$',views.index,name='index'),
    url('^admin/', admin.site.urls),
]
