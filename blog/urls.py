from django.conf.urls import url
from .views import createBlog,Success

urlpatterns = [
    url(r'^$', createBlog.as_view(),name='createBlog'),
	url(r'success/', Success,name='Success'),
]