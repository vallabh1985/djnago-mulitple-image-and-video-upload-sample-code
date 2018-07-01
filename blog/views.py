from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import FormView
from django.views.generic.base import TemplateView
from .forms import BlogForm

# Create your views here.
class createBlog(TemplateView):
	Form_class = BlogForm
	Template_name = 'blog/index.html'
	