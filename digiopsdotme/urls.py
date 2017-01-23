from django.conf.urls import url
from django.contrib import admin
from home import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.home_index, name="home"),
    url(r'^about/$', views.about, name="about"),
]
