from django.conf.urls import url
from .feeds import RSSFeed

urlpatterns = [
    url(r'^$', RSSFeed()),
]
