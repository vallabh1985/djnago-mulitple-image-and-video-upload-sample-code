from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import CreateView, FormView, DetailView, View, UpdateView, DeleteView, TemplateView
from .models import Images,Videos
from .forms import BlogForm


# Create your views here.
class createBlog(CreateView):
	form_class = BlogForm
	template_name = 'blog/index.html'
	success_url = 'success/'
	
	def post(self, request, *args, **kwargs):
		super(createBlog, self).post(request)
		newblog=self.object
		
		#Get all images and storing
		image_files = request.FILES.getlist('multipleimages', None)
		for p in image_files:
			photo = Images(blog=newblog, photo=p) #calling model here
			photo.save()

		#Get all images and storing
		video_files = request.FILES.getlist('multiplevideos', None)
		for v in video_files:
			video = Videos(blog=newblog, video=v) #calling model here
			video.save()
		
		return HttpResponseRedirect('blog/success')
		

def Success(request):
	return HttpResponse("Succesfully uploaded")