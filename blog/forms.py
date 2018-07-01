from django import forms
from .models import Blog, Images, Videos

class BlogForm(forms.ModelForm):
	class Meta:
		model = Blog
		fields = ('title','desc')