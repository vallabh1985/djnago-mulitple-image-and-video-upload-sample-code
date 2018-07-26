from django import forms
from django.core.validators import FileExtensionValidator
from .models import Blog, Images, Videos

class BlogForm(forms.ModelForm):
	multipleimages = forms.ImageField(required=False, widget=forms.ClearableFileInput(attrs={'multiple': True}))
	multiplevideos = forms.FileField(required=False, widget=forms.ClearableFileInput(attrs={'multiple': True}),validators=[FileExtensionValidator(allowed_extensions=['mp4','mkv','avi'])])
	
	class Meta:
		model = Blog
		fields = ('title','desc','multipleimages','multiplevideos')