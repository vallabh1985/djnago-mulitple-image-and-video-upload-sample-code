from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import FormView
from django.views.generic import CreateView, FormView, DetailView, View, UpdateView, DeleteView, TemplateView
from .forms import BlogForm

# Create your views here.
class createBlog(CreateView):
	form_class = BlogForm
	template_name = 'blog/index.html'
	success_url = 'success/'
	