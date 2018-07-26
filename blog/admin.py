from django.contrib import admin
from .models import Blog

# Register your models here.

class blog_Display(admin.ModelAdmin):
	list_display =('title','desc',)
	search_fields = ('title',)
	
	
admin.site.register(Blog,blog_Display)