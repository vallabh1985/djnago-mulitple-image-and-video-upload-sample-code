from django.conf.urls import url
from .views import createBlog

urlpatterns = [
    url(r'', createBlog.as_view(),name='createBlog'),
]