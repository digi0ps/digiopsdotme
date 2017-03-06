from django.conf.urls import url, include
from django.contrib import admin
from blog import views

urlpatterns = [
    url(r'^$', views.blog_index_view, name="blog"),
    url(r'article/(\d{1,3})$', views.blog_post_view, name="article"),
    url(r'superuser/$', views.super_user_view, name="blog_su")
]
