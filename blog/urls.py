from django.conf.urls import url, include
from django.views.generic import ListView, DetailView
from blog.models import Post

urlpatterns = [ url(r'^$', ListView.as_view(queryset = Post.object_all().order_by("-date")[:25], templete_name = "blog/blog.html"))]
