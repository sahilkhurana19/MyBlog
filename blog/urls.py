from django.conf.urls import url
from . import views

app_name = 'blog'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^posts/(?P<post_id>\d+)/$', views.detail, name='detail'),
    url(r'^category/(?P<tag_id>\d+)/$', views.category, name='category')
]