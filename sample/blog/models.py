from django.db import models

# Create your models here.
class Blog(models.Model):
	title = models.CharField(max_length=250)
	desc = models.TextField()
	create_date = models.DateTimeField(auto_now_add=True)

class Images(models.Model):
	photo = models.CharField(max_length=250)
	blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
	
class Videos(models.Model):
	vid = models.CharField(max_length=250)
	blog = models.ForeignKey(Blog, on_delete=models.CASCADE)