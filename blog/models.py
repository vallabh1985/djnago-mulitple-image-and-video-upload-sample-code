from django.db import models
from django.core.validators import FileExtensionValidator

# Create your models here.
class Blog(models.Model):
	title = models.CharField(max_length=250)
	desc = models.TextField()
	create_date = models.DateTimeField(auto_now_add=True)
	
	def __str__(self):
		return self.title

class Images(models.Model):
	photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
	blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
	
	def __str__(self):
		return self.blog
	
class Videos(models.Model):
	video = models.FileField(upload_to='videos/%Y/%m/%d/',validators=[FileExtensionValidator(allowed_extensions=['mp4','mkv','avi'])])
	blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
	
	def __str__(self):
		return self.blog