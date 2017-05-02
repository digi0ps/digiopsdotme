from django.conf.urls import url, include
from django.contrib import admin
from home import views
from blog import urls


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.home_index, name="home"),
    url(r'^about/$', views.about, name="about"),
    url(r'^photos/$', views.photos, name="photos"),
    url(r'^college/$', views.college, name="college"),
    url(r'^blog/', include('blog.urls')),
]
