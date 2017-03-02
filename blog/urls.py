from django.conf.urls import url, include
from django.contrib import admin
from blog import views

urlpatterns = [
    url(r'^$', views.blog_index_view, name="blog"),
]
